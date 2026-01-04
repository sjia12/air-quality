import streamlit as st

# ===== Page Config =====
st.set_page_config(
    page_title="AirWise – Air Quality & Health Chatbot",
    page_icon="☁️",
    layout="centered"
)

# ===== Custom CSS =====
st.markdown("""
<style>
.stApp {
    background-color: #f0f9ff;
}

/* Title */
h1 {
    color: #064e3b;
}

/* Chat bubbles */
.bot {
    background-color: #e6f7f1;
    color: #064e3b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.user {
    background-color: #dbeafe;
    color: #1e3a8a;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    text-align: right;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: #f0fdfa;
    border: 2px solid #10b981;
    color: #064e3b;
}
</style>
""", unsafe_allow_html=True)

# ===== Header =====
st.title("☁️ AirWise")

# ===== Session State (with intro as first message) =====
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "bot",
            "text": "Hi! I’m AirWise 🌬️. I help explain air quality and its effects on health and the environment. Ask me anything below."
        }
    ]

# ===== Clear Chat Button =====
if st.button("🗑️ Clear chat"):
    st.session_state.messages = [
        {
            "role": "bot",
            "text": "Hi! I’m AirWise 🌬️. Ask me anything about air quality and health."
        }
    ]
    st.experimental_rerun()

# ===== Display Chat Messages =====
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['text']}</div>", unsafe_allow_html=True)

# ===== Chat Logic Function =====
def get_bot_response(user_input):
    q = user_input.lower()

    if "what is air pollution" in q or "define air pollution" in q:
        return "Air pollution is the presence of harmful substances like smoke, toxic gases, and dust in the air that can harm health and the environment."

    elif "effects" in q and "pollution" in q:
        return "Air pollution can cause asthma, coughing, breathing problems, and can damage plants, animals, and the climate."

    elif "cause" in q or "burning" in q or "garbage" in q:
        return "Air pollution is caused by burning trash, vehicle exhaust, factory smoke, and forest fires."

    elif "air quality" in q:
        return "Air quality tells us how clean or polluted the air is. Poor air quality makes breathing unsafe."

    elif "health" in q or "asthma" in q or "cough" in q or "breathe" in q:
        return "Poor air quality can cause coughing, asthma attacks, breathing difficulties, and heart problems."

    elif "indoor" in q:
        return "Indoor air pollution can come from cooking smoke, dust, or chemicals. Good ventilation helps improve indoor air quality."

    elif "mask" in q:
        return "Wearing a mask can help reduce the amount of polluted air you breathe, especially on days with poor air quality."

    elif "improve" in q or "tree" in q or "transport" in q:
        return "We can improve air quality by planting trees, using public transport, saving energy, and avoiding burning trash."

    elif "aqi" in q:
        return "The Air Quality Index (AQI) shows how polluted the air is and what health effects may occur."

    else:
        return "That’s a good question! Clean air is important because it keeps our lungs, heart, and environment healthy."

# ===== Input (Bottom like ChatGPT) =====
user_input = st.text_input("Type your question here:")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "text": user_input
    })

    response = get_bot_response(user_input)

    st.session_state.messages.append({
        "role": "bot",
        "text": response
    })

    st.experimental_rerun()
