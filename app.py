
import streamlit as st
from gtts import gTTS
import os
from datetime import datetime

rashis = {
    "मेष": "आज का दिन आपके लिए ऊर्जावान रहेगा।",
    "वृषभ": "धैर्य और समझदारी से काम लें।",
    "मिथुन": "सकारात्मक सोच से कार्य सिद्ध होंगे।",
    "कर्क": "परिवार के साथ समय बिताएं।",
    "सिंह": "नेतृत्व क्षमता बढ़ेगी।",
    "कन्या": "वित्तीय लाभ के योग हैं।",
    "तुला": "नए अवसर मिल सकते हैं।",
    "वृश्चिक": "मनोबल ऊँचा रहेगा।",
    "धनु": "धार्मिक कार्यों में मन लगेगा।",
    "मकर": "नई ज़िम्मेदारियाँ मिलेंगी।",
    "कुंभ": "दोस्तों का सहयोग मिलेगा।",
    "मीन": "संतुलन बनाए रखें।"
}

st.set_page_config(page_title='जय ज्योतिष - Sanatan AI')
st.title('🙏 जय ज्योतिष - Sanatan AI')
st.markdown('''### 🚩 Sanatan AI: Horoscope • Mantras • Shloka
''')

option = st.selectbox("सेवा चुनें:", ["🔮 राशिफल देखें", "🕉️ मंत्र सुनें (11 बार)"])

if option == "🔮 राशिफल देखें":
    rashi = st.selectbox("अपनी राशि चुनें:", list(rashis.keys()))
    today = datetime.now().strftime("%d-%m-%Y")
    st.image(f"images/{rashi}.png", width=150)
    st.subheader(f"📅 {today} का राशिफल")
    st.success(rashis[rashi])
    
elif option == "🕉️ मंत्र सुनें (11 बार)"):
    mantra = st.selectbox("मंत्र चुनें:", ["गायत्री मंत्र", "महामृत्युंजय मंत्र", "हनुमान चालीसा"])
    if st.button("🔊 11 बार सुनाएं"):
        with open(f"mantras/{mantra}.txt", "r", encoding="utf-8") as f:
            text = f.read()
        repeated = (text + "\n") * 11
        tts = gTTS(repeated, lang='hi')
        tts.save("output.mp3")
        audio_file = open("output.mp3", "rb")
        st.audio(audio_file.read(), format='audio/mp3')
        audio_file.close()
