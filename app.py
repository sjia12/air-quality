import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Air Quality & Health Chatbot",
    page_icon="🌱",
    layout="centered"
)

st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #f0f9ff;
}

/* Main text */
h1, h2, h3, p, label, span {
    color: #064e3b !important;
}

/* Subtitle / smaller text */
small {
    color: #065f46 !important;
}

/* Text input box */
.stTextInput > div > div > input {
    border: 2px solid #10b981;
    color: #064e3b;
    background-color: #ffffff;
}

/* Placeholder text */
::placeholder {
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🌱 Air Quality & Health Chatbot")
st.markdown("""
Welcome to the **Air Quality & Health Chatbot**! I'm here to help you learn about the air we breathe and how to stay healthy. 
Our mission is to promote **cleaner air for a healthier future**.
""")

# Chat Logic Function
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "what is air pollution" in user_input or "define air pollution" in user_input:
        return "Air pollution is the presence of harmful substances in the atmosphere, such as toxic gases, smoke, and dust, that can damage human health and the environment."
    
    elif "effects" in user_input and "pollution" in user_input:
        return "Air pollution has serious effects: it causes breathing problems like asthma, harms plants and animals, and even contributes to climate change by trapping heat in the sky."
    
    elif "cause" in user_input or "garbage" in user_input or "burning" in user_input:
        return "A major cause of air pollution is households burning garbage, which releases toxic chemicals. Other causes include smoke from factories, car exhaust, and forest fires."
    
    elif "how" in user_input and "quality" in user_input:
        return "Air pollution directly lowers air quality by adding 'smog' and tiny particles (PM2.5) that make the air hazy and dangerous to breathe. High pollution means low air quality!"
    
    elif "quality" in user_input:
        return "Air quality tells us how clean or polluted the air is. Clean air is essential for our health, as it helps our lungs and heart work properly!"
    
    elif "pollution" in user_input:
        if "cause" in user_input or "why" in user_input:
            return "Air pollution is caused by many things, including smoke from factories, exhaust from cars, burning trash, and even natural dust."
        elif "harm" in user_input or "affect" in user_input or "bad" in user_input:
            return "Air pollution harms you by entering your lungs and bloodstream. it can lead to immediate problems like stinging eyes and coughing, and long-term issues like asthma or heart disease."
        return "Air pollution happens when harmful substances like smoke, chemicals, or dust get into the air, making it unsafe for people and nature."
    
    elif "cause" in user_input or "vehicle" in user_input or "factory" in user_input or "trash" in user_input or "dust" in user_input:
        return "Common causes of air pollution include vehicle emissions, factory smoke, burning trash, and dust. These all release harmful particles into the sky."
    
    elif "health" in user_input or "cough" in user_input or "asthma" in user_input or "breathe" in user_input or "allergy" in user_input:
        return "Dirty air can cause coughing, asthma attacks, breathing problems, and allergies. Long-term exposure can lead to serious health risks for our hearts and lungs."
    
    elif "daily" in user_input or "activity" in user_input or "outdoor" in user_input:
        return "Poor air quality can limit outdoor activities like sports and play. It's important to check the air quality before spending a lot of time outside."
    
    elif "indoor" in user_input or "outdoor" in user_input:
        return "Outdoor pollution comes from cars and factories, while indoor pollution can come from cooking smoke, dust, or pet dander. Both are important to watch!"
    
    elif "aqi" in user_input or "index" in user_input:
        return "The Air Quality Index (AQI) is a scale used to report daily air quality. It tells you how clean or polluted your air is and what associated health effects might be a concern."
    
    elif "protect" in user_input or "mask" in user_input or "ventilate" in user_input:
        return "To stay safe, you can wear a mask outside on smoggy days, avoid heavy exercise outdoors when the AQI is high, and keep your rooms well-ventilated."
    
    elif "improve" in user_input or "tree" in user_input or "transport" in user_input or "energy" in user_input:
        return "We can help by planting trees, using public transport like buses or trains, saving energy at home, and never burning trash."
        
