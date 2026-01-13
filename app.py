import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# إعدادات الصفحة
st.set_page_config(page_title="Mujeeb AI - Madar", page_icon="✨")

# الربط الآمن مع Firebase باستخدام Secrets
if not firebase_admin._apps:
    try:
        # سنضع بيانات الـ JSON في 'Secrets' داخل Streamlit Cloud لاحقاً
        if "firebase_key" in st.secrets:
            key_dict = json.loads(st.secrets["firebase_key"])
            creds = credentials.Certificate(key_dict)
            firebase_admin.initialize_app(creds)
        else:
            st.error("الرجاء إعداد مفاتيح Firebase في الإعدادات المتقدمة.")
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")

db = firestore.client()

st.title("✨ عقل مُجيب")
st.write("محرك الذكاء الاصطناعي لمجموعة مدار")

# نظام الدردشة
if prompt := st.chat_input("تحدث مع مُجيب..."):
    st.chat_message("user").write(prompt)
    
    # استجابة تجريبية (يمكنك ربطها بـ Llama 3 API لاحقاً)
    response = f"أهلاً بك يا مؤسس مدار. أنا عقل مُجيب، استلمت رسالتك: '{prompt}'"
    
    with st.chat_message("assistant"):
        st.write(response)
    
    # حفظ في Firebase (مجموعة Madar_Chat_Logs)
    db.collection("Madar_Chat_Logs").add({"query": prompt, "answer": response})
