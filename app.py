import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# إعدادات الصفحة
st.set_page_config(page_title="Mujeeb AI", page_icon="https://i.ibb.co/s9LHHQs1/Mujeeb-AI-logo-0000-4.png")

# دالة ذكية للاتصال بـ Firebase لمنع الانهيار عند السطر 22
def init_connection():
    if not firebase_admin._apps:
        try:
            # هنا التغيير الجذري: نستخدم القاموس مباشرة دون json.loads
            if "firebase_key" in st.secrets:
                creds_dict = dict(st.secrets.firebase_key)
                creds = credentials.Certificate(creds_dict)
                firebase_admin.initialize_app(creds)
                return firestore.client()
            else:
                st.error("الرجاء إعداد مفاتيح Firebase في Secrets.")
                return None
        except Exception as e:
            st.error(f"خطأ في الاتصال: {e}")
            return None
    return firestore.client()

# تشغيل الاتصال
db = init_connection()

st.title("✨ عقل مُجيب")
st.write("محرك الذكاء الاصطناعي لمجموعة مدار")

# التأكد من وجود الاتصال قبل تفعيل الدردشة
if db:
    if prompt := st.chat_input("تحدث مع مُجيب..."):
        st.chat_message("user").write(prompt)
        
        response = f"أهلاً بك يا مؤسس مدار. أنا عقل مُجيب، استلمت رسالتك: '{prompt}'"
        
        with st.chat_message("assistant"):
            st.write(response)
        
        # الحفظ في Firebase
        db.collection("Madar_Chat_Logs").add({"query": prompt, "answer": response})
else:
    st.warning("تطبيق مُجيب متوقف مؤقتاً لعدم وجود مفاتيح الاتصال.")
