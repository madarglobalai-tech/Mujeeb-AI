import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# إعدادات الصفحة بشعار مدار
st.set_page_config(page_title="Mujeeb AI", page_icon="https://i.ibb.co/s9LHHQs1/Mujeeb-AI-logo-0000-4.png")

# وظيفة الاتصال بـ Firebase - النسخة المتوافقة مع AttrDict
if not firebase_admin._apps:
    try:
        # هنا السر: st.secrets["firebase_key"] تعيد AttrDict تلقائياً
        # ونحن نحولها لقاموس عادي ليقبلها Firebase
        secret_info = dict(st.secrets["firebase_key"])
        creds = credentials.Certificate(secret_info)
        firebase_admin.initialize_app(creds)
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")

# التأكد من تشغيل قاعدة البيانات
try:
    db = firestore.client()
except Exception as e:
    st.error("قاعدة البيانات غير متصلة. تأكد من إعدادات Secrets.")
    db = None

st.title("✨ عقل مُجيب")
st.write("محرك الذكاء الاصطناعي لمجموعة مدار")

# نظام الدردشة
if db:
    if prompt := st.chat_input("تحدث مع مُجيب..."):
        st.chat_message("user").write(prompt)
        
        # استجابة ذكاء مدار
        response = f"مرحباً بك في مدار. أنا عقل مُجيب، استقبلت رسالتك: '{prompt}'"
        
        with st.chat_message("assistant"):
            st.write(response)
        
        # حفظ في Firebase
        db.collection("Madar_Chat_Logs").add({
            "query": prompt, 
            "answer": response
        })
