import streamlit as st
import google.generativeai as genai

# API Key
genai.configure(api_key="AIzaSyD1GDQD-0vZG3yMlY6folK5B-jx_7HDjAc")

st.title(" Pro Movie Recap AI Builder")

movie_name = st.text_input("ဇာတ်ကားနာမည် ရိုက်ထည့်ပါ -")

if st.button("Generate Pro Script"):
    if movie_name:
        # models/ မပါဘဲ နာမည်အမှန်အတိုင်းပဲ သုံးထားပါတယ်
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Write a viral 20-part TikTok movie recap script for '{movie_name}' in Burmese. Professional storytelling."
        
        with st.spinner('Script ရေးနေပါသည်...'):
            try:
                response = model.generate_content(prompt)
                st.subheader(" Generated Script")
                st.write(response.text)
                st.success("အောင်မြင်စွာ ရေးသားပြီးပါပြီ။")
            except Exception as e:
                # အကယ်၍ flash နဲ့ အဆင်မပြေရင် gemini-pro နဲ့ ပြန်စမ်းခိုင်းပါမယ်
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(prompt)
                    st.write(response.text)
                    st.success("အောင်မြင်စွာ ရေးသားပြီးပါပြီ။")
                except Exception as e2:
                    st.error(f"Error: {str(e2)}")
    else:
        st.warning("ဇာတ်ကားနာမည် အရင်ရိုက်ထည့်ပေးပါ။")
