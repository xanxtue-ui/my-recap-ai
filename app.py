import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# UI ဒီဇိုင်း - နောက်ခံအရောင်ပြေးလေး
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(" Professional Movie Recap AI")

api_key = st.sidebar.text_input("Gemini API Key:", type="password")
movie_name = st.text_input("ဇာတ်ကားနာမည်ကို ရိုက်ထည့်ပါ -")

if st.button("Generate Pro Script"):
    if api_key and movie_name:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = f"Write a professional 20-part TikTok movie recap script for '{movie_name}' in Burmese. Each part < 3 mins. Include strong hooks and cliffhangers. Must be high-quality storytelling."
        
        with st.spinner('Writing Script...'):
            response = model.generate_content(prompt)
            st.text_area("Edit Script Here:", response.text, height=400)
            
            # Audio စနစ်
            tts = gTTS(text=response.text[:500], lang='my')
            tts.save("audio.mp3")
            st.audio("audio.mp3")
    else:
        st.warning("API Key နဲ့ နာမည် ထည့်ပေးပါ။")
