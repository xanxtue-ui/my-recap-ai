import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# ၁။ API Key ထည့်သွင်းခြင်း
API_KEY = "AIzaSyD1GDQD-0vZG3yMlY6folK5B-jx_7HDjAc"
genai.configure(api_key=API_KEY)

# ၂။ UI ဒီဇိုင်း
st.set_page_config(page_title="Pro Movie Recap AI", page_icon="")
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #1f1c2c, #928dab); color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title(" Pro Movie Recap AI Builder")

movie_name = st.text_input("ဇာတ်ကားနာမည် (သို့မဟုတ်) ဇာတ်လမ်းအကျဉ်းကို ရိုက်ထည့်ပါ -")

if st.button("Generate Pro Script"):
    if movie_name:
        # ဒီနေရာမှာ Error မတက်အောင် တည်ငြိမ်ဆုံး နာမည်ကို သုံးထားပါတယ်
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"Write a viral 20-part TikTok movie recap script for '{movie_name}' in Burmese language. High energy, strong hooks, and cliffhangers for each part."
        
        with st.spinner('Script ရေးနေပါသည်... ခဏစောင့်ပေးပါ...'):
            try:
                response = model.generate_content(prompt)
                
                st.subheader(" Generated Script")
                st.text_area("Full Script:", response.text, height=500)
                
                st.success("အောင်မြင်စွာ ရေးသားပြီးပါပြီ။")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("ဇာတ်ကားနာမည် အရင်ရိုက်ထည့်ပေးပါ။")
