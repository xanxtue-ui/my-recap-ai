import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# ၁။ API Key သတ်မှတ်ခြင်း (သင့်ရဲ့ Key ကို ထည့်သွင်းပေးထားပါတယ်)
API_KEY = "AIzaSyD1GDQD-0vZG3yMlY6folK5B-jx_7HDjAc"
genai.configure(api_key=API_KEY)

# ၂။ UI ဒီဇိုင်း (Recap by han အတွက် အမိုက်စား ဒီဇိုင်း)
st.set_page_config(page_title="Pro Movie Recap AI", page_icon="")
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #2d2d44;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(" Pro Movie Recap AI Builder")
st.write("ဇာတ်ကားမျိုးစုံကို TikTok Recap Script အပိုင်း ၂၀ ကျော်အထိ မြန်မာလို ရေးပေးပါမည်။")

# ၃။ User Input
movie_name = st.text_input("ဇာတ်ကားနာမည် (သို့မဟုတ်) ဇာတ်လမ်းအကျဉ်းကို ရိုက်ထည့်ပါ -")

if st.button("Generate Pro Script"):
    if movie_name:
        # ၄။ Gemini Model သတ်မှတ်ခြင်း (Error 404 မတက်အောင် models/ ထည့်ထားသည်)
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        # ၅။ AI ကို ခိုင်းမယ့် Prompt
        prompt = f"""
        သင်ဟာ Viral ဖြစ်တဲ့ TikTok Movie Recap ရေးသားသူ ကျွမ်းကျင်ပညာရှင်ပါ။
        '{movie_name}' ဇာတ်ကားအတွက် Recap Script ရေးပေးပါ။
        
        စည်းကမ်းချက်များ:
        1. ဇာတ်လမ်းကို အပိုင်း (၂၀) ကျော် တိကျစွာ ခွဲခြားပါ။
        2. တစ်ပိုင်းလျှင် စကားပြောနှုန်းအရ ၃ မိနစ်စာ (စကားလုံး ၄၀၀-၅၀၀ ဝန်းကျင်) ရှိရမည်။
        3. အပိုင်းတိုင်းတွင် စိတ်ဝင်စားဖွယ် Hook နှင့် နောက်တစ်ပိုင်းကြည့်ချင်အောင် Cliffhanger ပါရမည်။
        4. ဘာသာစကား: မြန်မာလို။
        
        Format:
        Part [နံပါတ်]
        [Hook]
        [ဇာတ်လမ်းအညွှန်း]
        [Cliffhanger]
        ---
        """
        
        with st.spinner('Pro Script များကို ရေးသားနေပါသည်... ခဏစောင့်ပေးပါ...'):
            try:
                response = model.generate_content(prompt)
                
                # ရလာတဲ့ Script ကို ပြသခြင်း
                st.subheader(" Generated Script")
                full_script = st.text_area("Script Details:", response.text, height=500)
                
                # အသံဖိုင် Preview ထုတ်ပေးခြင်း
                st.subheader(" Audio Preview (နမူနာ)")
                tts = gTTS(text=full_script[:400], lang='my')
                tts.save("recap_audio.mp3")
                st.audio("recap_audio.mp3")
                
                st.success("အားလုံးအဆင်ပြေပါတယ်။ Script ကို Copy ကူးပြီး သုံးနိုင်ပါပြီ။")
            except Exception as e:
                st.error(f"Error တက်သွားပါတယ်: {str(e)}")
    else:
        st.warning("ဇာတ်ကားနာမည် အရင်ရိုက်ထည့်ပေးပါ။")
