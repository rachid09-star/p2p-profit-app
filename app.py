import datetime
import streamlit as st

def حساب_الربح(رأس_المال, سعر_الشراء, سعر_البيع):
    usdt_المشترى = رأس_المال / سعر_الشراء
    العمولة = 0.40
    usdt_صافي = usdt_المشترى - العمولة
    قيمة_usdt_درهم = usdt_صافي * سعر_البيع
    الربح = قيمة_usdt_درهم - رأس_المال
    نسبة_الربح = (الربح / رأس_المال) * 100

    return {
        "USDT بعد العمولة": round(usdt_صافي, 2),
        "قيمة USDT عند البيع (درهم)": round(قيمة_usdt_درهم, 2),
        "الربح الصافي (درهم)": round(الربح, 2),
        "نسبة الربح (%)": round(نسبة_الربح, 2)
    }

st.set_page_config(page_title="حاسبة أرباح P2P", layout="centered")
st.title("حاسبة الربح في تداول P2P")

رأس_المال = st.number_input("رأس المال (درهم)", min_value=100.0, value=1000.0, step=50.0)
سعر_الشراء = st.number_input("سعر الشراء (درهم)", min_value=5.0, value=9.60, step=0.01)
سعر_البيع = st.number_input("سعر البيع (درهم)", min_value=5.0, value=9.85, step=0.01)

if st.button("احسب الربح"):
    نتيجة = حساب_الربح(رأس_المال, سعر_الشراء, سعر_البيع)
    st.subheader("النتائج:")
    for مفتاح, قيمة in نتيجة.items():
        st.write(f"**{مفتاح}:** {قيمة}")
