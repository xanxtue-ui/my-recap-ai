import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# API Key ကို ဒီမှာ တစ်ခါတည်း ထည့်သွင်းပေးထားပါတယ်
API_KEY = "AIzaSyD1GDQD-0vZG3yMlY6folK5B-jx_7HDjAc"
genai.configure(api_key=API_KEY)

# UI ဒီဇိုင်း - နောက်ခံအရောင်ပြေးလေး
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(" Pro Movie Recap AI Builder")

movie_name = st.text_input("ဇာတ်ကားနာမည်ကို ဒီမှာ ရိုက်ထည့်ပါ -")

if st.button("Generate Pro Script"):
    if movie_name:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Write a professional 20-part TikTok movie recap script for '{movie_name}' in Burmese. Each part < 3 mins. Include strong hooks and cliffhangers. Must be high-quality storytelling."
        
        with st.spinner('Pro Script များကို ရေးသားနေပါသည်...'):
            try:
                response = model.generate_content(prompt)
                st.subheader(" Generated Script")
                full_script = st.text_area("Script Details:", response.text, height=500)
                
                tts = gTTS(text=full_script[:500], lang='my')
                tts.save("audio.mp3")
                st.audio("audio.mp3")
                st.success("အားလုံးအဆင်ပြေပါတယ်။")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("ဇာတ်ကားနာမည် အရင်ရိုက်ထည့်ပေးပါ။")
