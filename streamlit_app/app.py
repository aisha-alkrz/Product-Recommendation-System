import streamlit as st
import pandas as pd

# تحميل الملفات اللازمة
clustered_with_price = pd.read_csv("data/products_names_with_clusters_with_price.csv")
clustered_without_price = pd.read_csv("data/products_names_with_clusters_without_price.csv")
apriori_rules = pd.read_csv("data/apriori_rules.csv")

# واجهة المستخدم
st.title("🛒 نظام توصية المنتجات")

# اختيار المنتج
all_products = clustered_with_price['productname'].unique()
selected_product = st.selectbox("اختر منتجًا:", all_products)

# اختيار نوع التجميع
mode = st.radio("اختر طريقة العنقدة:", ["📊 مع السعر", "🔍 بدون السعر"])

# تحديد مصدر البيانات
df = clustered_with_price if mode == "📊 مع السعر" else clustered_without_price

# تحديد رقم العنقود للمنتج المحدد
product_cluster = df[df['productname'] == selected_product]['cluster'].values[0]

# عرض منتجات من نفس العنقود
st.subheader("🔗 منتجات من نفس العنقود:")
similar_products = df[(df['cluster'] == product_cluster) & (df['productname'] != selected_product)]
st.write(similar_products[['productname']].reset_index(drop=True))

# عرض توصيات من قواعد Apriori
st.subheader("🧠 منتجات مقترحة من قواعد Apriori:")
related_rules = apriori_rules[apriori_rules['antecedents'].str.contains(selected_product)]
if not related_rules.empty:
    for _, row in related_rules.iterrows():
        st.markdown(f"- **{list(eval(row['consequents']))[0]}** (ثقة: {row['confidence']:.2f})")
else:
    st.info("لا توجد قاعدة ارتباط مباشرة لهذا المنتج.")
