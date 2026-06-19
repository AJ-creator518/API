import streamlit as st
import google.generativeai as genai

# Step 1: AI ka Password (API Key)
# Yeh ek secret key hoti hai jo Google tumhe free mein dega")
genai.configure(api_key=" secret api")

# Step 2: Dimaag select karo
model = genai.GenerativeModel('gemini-1.5-flash')

# Step 3: Streamlit App ka Design
st.title("🤖 Mera Pehla AI Chatbot")
st.write("Main Gemini AI hoon. Mujhse kuch bhi pucho!")

user_ki_baat = st.text_input("Tumhara sawal:")
submit_button = st.button("Jawaab Do")

# Step 4: Jaadoo (API Call)
if submit_button:
    if user_ki_baat != "":
        # Waiter (API) order lekar AI ke paas ja raha hai
        response = model.generate_content(user_ki_baat)
        
        # Waiter wapas aa gaya aur jawaab screen par dikha raha hai
        st.success(response.text)
    else:
        st.error("Pehle kuch likho toh sahi!")
