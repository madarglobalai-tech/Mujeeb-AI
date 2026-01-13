import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# إعدادات واجهة مدار
st.set_page_config(page_title="Mujeeb AI", page_icon="https://i.ibb.co/s9LHHQs1/Mujeeb-AI-logo-0000-4.png")

# وظيفة الاتصال الثابتة
@st.cache_resource # لضمان عدم تكرار الاتصال وتجنب الأخطاء
def init_firebase():
    if not firebase_admin._apps:
        # بيانات ملفك الأصلي الذي أرفقته
        fb_creds = {
            "type": "service_account",
            "project_id": "mujeeb-ai-by-madar-global",
            "private_key_id": "a23bb14c4762475980f2b16c4a69bb4dc68b9985",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCXriAMlK2dlE0N\nI0OuT01zx3zte7Y/9MNAX23wBZONFKsS+yqgANPNTk4Ow9W9O0GlRHYk2CwkPUAw\nDm+Ax5FVCwl9DWYFtIfLFLC8shgg9JwqsTTXqjOeJ01A+rMtG3J/uKi7pcrKP6O0\n/w8x9zI53FgVzF+SjGoYSSASX0uBT2xUx+rec3dFctZil15ByJa+eEJ3g9b8BlTH\nzm8JuYkKTJeAdenFwX7/vw4vDY/t3rAU5CA7kSvTifhHyV0IK+vm+pO4C24Ix+3O\nZB1kz+VBWuZae8D/UfifO4e8QytOohHUztgBuil5bxWrVG5I6vv3/83z2DI2UzOp\nx4FktbMnAgMBAAECggEAA4VvwV42pCJeRDjYhjjIWQYbQMjM0H7Q/KYnTC7gKGbd\nmS2kQy7aRHDaO6bqrlK1AqoXG+rcaq05NYztkyVGXyYUz/FrYr4N3i3C8/AVj4Pl\nsWrUvOq2gh+UlZR+fNWfUhbfhlLiOo0FdwFykhec/GKNgiVf5fSNzulj8h2CTHVn\nCJ8i3nhymIsujmwdx2NQt9y1T5C4FvwrnLmJq9//o9JqZJ8iKI8qPIH5WKzjEvc7\nlNKLld7XFGwiVjhcc7NPSfk9bwGj8QExmYBiV3TTbW//9mM6UfC56zfIpRCXhMij\najKoZEYxFRZtCwYC2+qDbYH0wmPcmQgDSQ55rwNghQKBgQDPMKkfwPUt1tAeTnWV\nDejFehzDifxNBgswNCh6MdGr1gwFDH8RtIF0aZdYv7OMywgJtXhGGbbnRFGJDUS/\nn37Kj+MTUY0c8TCaa9OYBZ3A23qNwhWe5cAf+I9EKkdIo8QGnt7BPqmbJ40htN/N\nuGmDZhG3wrBoCrClQyG27WdyxQKBgQC7ab25c79WTkKUXIdWc9weyJ+/YeUJ5Upd\n6+BsMgJ5ngvY662v17qA4pyemswEvhZhOAVflBfFPdoee0bmozXC1exRkKzyCHyI\nMqEaudgiv+GDQH6l0i9dE81Fp3WR59YHdTy2NSer2QeSQALBekWOfEhxi4xM7aak\naMNb6fo8+wKBgHr/jkdVi7fswJxdQ5x7J2akeZLzxZ4MKnQxYp44GRsD9RrCMmVW\nXUu4q6p6E6NPnLP20TH8bgKZIjZUdC22B9VE2i9LyJQX8xyZSoIDQ4WMRhMF10P/\nbLEOJC75UlwjLGopwl/CTXnYXwZVlE9SXQEuhPIsWAFL51YUpl0sTq9pAoGBAKbQ\noh1WV7McicrA6X4cNov4C6kwG8xJGX6sG+BySx2xfd4hOUJRhSJ/kuTh6EM4Z3c1\nhCLlEJtySJnlJODZ2VqJS4X2ftoYj7AzUI8XaLjVjodjetdiVOJGY+ph+hZbA3kz\n80xD2AHwdfrJmypYCV2gZmMa0VEQH8orreg8RY7NAoGAbx0o9Tmd/1G4UNEdE+WE\nLJQTwBIL6GCVak20Pjzj/z0yV9bl6QOKUi83/sIaUPQ6/OMPH6sXQUwd2NQkBwWG\nrbVt1MLzHJdlxPELsZ3SS5b+e+si+74UbbmlBjLlOg0Xu6lN2kVPauovFrKnP2k6\nTyNTp15ZudN3vCtY8HtFIMI=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-fbsvc@mujeeb-ai-by-madar-global.iam.gserviceaccount.com",
            "client_id": "101222261744977971324",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40mujeeb-ai-by-madar-global.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }
        cred = credentials.Certificate(fb_creds)
        firebase_admin.initialize_app(cred)
    return firestore.client()

# تشغيل قاعدة البيانات
try:
    db = init_firebase()
    st.success("✅ متصل بقاعدة بيانات مدار")
except Exception as e:
    st.error(f"❌ فشل الاتصال: {e}")
    db = None

st.title("✨ عقل مُجيب")

if db:
    prompt = st.chat_input("تحدث مع مُجيب...")
    if prompt:
        st.chat_message("user").write(prompt)
        # تجربة الحفظ للتأكد من العمل
        db.collection("test_messages").add({"text": prompt})
        st.chat_message("assistant").write("تم استلام رسالتك وحفظها في قاعدة البيانات!")
