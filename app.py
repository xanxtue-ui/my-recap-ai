
import streamlit as st
import google.generativeai as genai

# ၁။ API Key ထည့်သွင်းခြင်း
try:
    genai.configure(api_key="AIzaSyD1GDQD-0vZG3yMlY6folK5B-jx_7HDjAc")
except:
    st.error("API Key ချိတ်ဆက်မှု အဆင်မပြေပါ။")

st.title("🎬 Pro Movie Recap AI Builder")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ထည့်ပါ -")

if st.button("Generate Pro Script"):
    if movie_name:
        with st.spinner('Script ရေးနေပါသည်...'):
            try:
                # ၂။ ရနိုင်တဲ့ Model ကို အလိုအလျောက်ရွေးချယ်တဲ့စနစ် (Error 404 ကို ကျိန်းသေဖြေရှင်းပေးမည်)
                # flash version ကို အရင်စမ်းမည်၊ အဆင်မပြေပါက pro version ကို သုံးမည်
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(f"Write a 20-part TikTok movie recap script for '{movie_name}' in Burmese.")
                except:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(f"Write a 20-part TikTok movie recap script for '{movie_name}' in Burmese.")
                
                st.subheader("📝 Generated Script")
                st.write(response.text)
                st.success("အောင်မြင်စွာ ရေးသားပြီးပါပြီ။")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("ဇာတ်ကားနာမည် အရင်ရိုက်ထည့်ပေးပါ။")
