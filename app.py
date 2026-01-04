import streamlit as st

st.set_page_config(
    page_title="Air Quality & Health Chatbot",
    page_icon="☁️",
    layout="centered"
)

# Custom CSS (same design, better readability)
st.markdown("""
<style>
.stApp {
    background-color: #f0f9ff;
}

h1, p, label {
    color: #064e3b !important;
}

.stTextInput > div > div > input {
    border: 2px solid #10b981;
    color: #064e3b;
}
</style>
""", unsafe_allow_html=True)

st.title("☁️ Air Quality & Health Chatbot")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<p>This chatbot explains how air quality affects human health in a clear and simple way.</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

question = st.text_input("💬 Type your question about air quality and health:")

if question:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**Answer:**")
    st.write(
        "Air quality affects our lungs and heart. Poor air quality can lead to breathing problems, asthma, and other health issues."
    )  

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
        
