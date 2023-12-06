import streamlit as st
import base64
from PIL import Image
import plotly.express as px
import cv2


st.set_page_config(
    page_icon='/Users/renadamer/Downloads/stream/mainpage_app/logo1.png',
)


df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()




img = get_img_as_base64("/Users/renadamer/Downloads/stream/logos.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://www.raed.net/img?id=504776");
background-size:100% 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
#background-image: url("data:/Users/renadamer/Downloads/stream/logos.png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



import streamlit as st

st.sidebar.markdown("قصص الحروف الهجائية")

# قائمة بالأحرف الهجائية العربية
arabic_letters = ['أ', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']

# قاموس يحتوي على روابط الصور وملفات الصوت لكل حرف
letters_data = {
    'أ': {'image': '/Users/renadamer/Downloads/stream/mainpage_app/حرف الألف.png', 'audio': '/Users/renadamer/Downloads/stream/mainpage_app/alifalphabet.ogg'},
    'ب': {'image': 'https://example.com/ba.png', 'audio': 'https://example.com/ba.mp3'},
    # ... وهكذا لباقي الأحرف
}

# تخطيط الصفحة باستخدام Streamlit
st.title(': إضغط على الحرف لتستمع إلى الحرف وقصته ')

# عدد الأعمدة لعرض الحروف
num_cols = 6

selected_letter = None  # تهيئة المتغير مسبقًا

# تقسيم الحروف إلى صفوف وأعمدة
for i in range(0, len(arabic_letters), num_cols):
    cols = st.columns(num_cols)
    for j in range(num_cols):
        index = i + j
        if index < len(arabic_letters):
            letter = arabic_letters[index]

            # عرض زر لكل حرف
            if cols[j].button(letter):
                selected_letter = letter

# عرض الصورة والصوت في العمود الأخير عند النقر على حرف
if selected_letter:
    st.image(letters_data[selected_letter]['image'], width=200)
    st.audio(letters_data[selected_letter]['audio'], format='audio/mp3')

st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: space-between;
        margin-top: 190px;
    }
    .custom-button {
        padding: 10px 20px;
        background-color: #EBA1A6;
        color: white; 
        border-radius: 20px;
        border: none;
        text-decoration: none;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div class="button-container">
        <a href="http://localhost:8501/page_3" class="custom-button">التالي</a>
        <a href="http://localhost:8501/" class="custom-button">السابق</a>
    </div>
    """
    , unsafe_allow_html=True
)


