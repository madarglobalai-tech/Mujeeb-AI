import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# إعدادات الصفحة
st.set_page_config(page_title="Mujeeb AI", page_icon="✨")

@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        # هنا نقرأ البيانات من Secrets بأمان دون كتابة المفاتيح في الكود
        fb_dict = dict(st.secrets["firebase_key"])
        
        # تصحيح الـ \n برمجياً لضمان عدم حدوث خطأ التشفير
        fb_dict["private_key"] = fb_dict["private_key"].replace("\\n", "\n")
        
        cred = credentials.Certificate(fb_dict)
        firebase_admin.initialize_app(cred)
    return firestore.client()

try:
    db = init_firebase()
    st.success("✅ متصل بقاعدة بيانات مدار بأمان")
except Exception as e:
    st.error(f"❌ خطأ: {e}")
