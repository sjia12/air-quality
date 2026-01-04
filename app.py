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
    background-color: #F0FFFF;
}

/* Header */
h1 {
    text-align: center;
    color: #0047AB; /* dark blue */
    margin-top: 30px;
    margin-bottom: 20px;
}

/* Trash icon (top-right, away from header) */
.clear-btn {
    position: fixed;
    top: 80px;
    right: 20px;
    z-index: 2000;
}

/* Bot message (dark blue) */
.bot {
    background-color: #1e3a8a;
    color: #6F8FAF;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    max-width: 90%;
}

/* User message */
.user {
    background-color: #dcfce7;
    color: #ADD8E6;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    margin-left: auto;
    max-width: 90%;
    text-align: right;
}

/* Fixed input area */
.input-box {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #ffffff;
    padding: 14px;
    border-top: 2px solid #38bdf8;
    box-shadow: 0 -4px 10px rgba(0,0,0,0.08);
    z-index: 1000;
}

/* Input field */
.stTextInput input {
    border-radius: 12px;
    padding: 10px;
    border: 2px solid #38bdf8;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ===== Session State =====
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "bot",
            "text": "Hi! I’m AirWise 🌬️. I help explain air quality and its effects on health and daily life. Ask me anything below."
        }
    ]

if "show_confirm" not in st.session_state:
    st.session_state.show_confirm = False

# ===== Clear Chat Button (with confirmation) =====
st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
clear_clicked = st.button("🗑️", key="clear_chat")
st.markdown('</div>', unsafe_allow_html=True)

if clear_clicked:
    st.session_state.show_confirm = True

if st.session_state.show_confirm:
    st.warning("Are you sure you want to clear the chat?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes, clear"):
            st.session_state.messages = [
                {
                    "role": "bot",
                    "text": "Hi! I’m AirWise 🌬️. Ask me anything about air quality and health."
                }
            ]
            st.session_state.show_confirm = False
            st.rerun()

    with col2:
        if st.button("Cancel"):
            st.session_state.show_confirm = False
            st.rerun()

# ===== Header =====
st.title("☁️ AirWise")

# ===== Chat Display =====
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['text']}</div>", unsafe_allow_html=True)

# Space so messages don't hide behind input
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# ===== Bot Logic (Expanded Answers) =====
def get_bot_response(q):
    q = q.lower()

    if "what is air pollution" in q or "define air pollution" in q:
        return (
            "Air pollution is the presence of harmful substances such as smoke, gases, "
            "and fine particles in the air that can harm people, animals, and the environment."
        )

    elif "what is air quality" in q:
        return (
            "Air quality refers to how clean or polluted the air is. "
            "Good air quality means the air is safe to breathe."
        )

    elif "how does air pollution affect our daily life" in q:
        return (
            "Air pollution affects daily life by causing coughing, headaches, and breathing problems. "
            "It can limit outdoor activities, reduce visibility, and affect school and work."
        )

    elif "how does air quality affect our daily life" in q:
        return (
            "Poor air quality can make it unsafe to go outside, especially for exercise. "
            "It can affect sleep, productivity, and overall health."
        )

    elif "health" in q or "lungs" in q or "heart" in q:
        return (
            "Poor air quality harms the lungs and heart. "
            "Long-term exposure can lead to asthma, heart disease, and other serious illnesses."
        )

    elif "children" in q or "elderly" in q:
        return (
            "Children and older adults are more affected by air pollution because "
            "their bodies are more sensitive to polluted air."
        )

    elif "cause" in q or "sources" in q:
        return (
            "Air pollution is caused by vehicle exhaust, factory emissions, burning trash, "
            "forest fires, and natural dust."
        )

    elif "indoor" in q:
        return (
            "Indoor air pollution comes from cooking smoke, chemicals, dust, and mold. "
            "Opening windows and proper ventilation help improve indoor air quality."
        )

    elif "outdoor" in q:
        return (
            "Outdoor air pollution mainly comes from vehicles, factories, and burning activities."
        )

    elif "aqi" in q or "air quality index" in q:
        return (
            "The Air Quality Index (AQI) shows how polluted the air is and what health effects "
            "people may experience."
        )

    elif "protect" in q or "stay safe" in q or "mask" in q:
        return (
            "To stay safe, avoid outdoor activities during poor air quality days, "
            "wear a mask if needed, and keep indoor air clean."
        )

    elif "improve" in q or "reduce pollution" in q:
        return (
            "Air pollution can be reduced by planting trees, using public transportation, "
            "saving energy, and avoiding burning trash."
        )

    elif "environment" in q:
        return (
            "Air pollution damages plants, animals, and ecosystems. "
            "It can reduce crop growth and harm wildlife."
        )

    else:
        return (
            "That’s a great question! Air quality affects our health, daily activities, "
            "and the environment. Clean air helps everyone live better."
        )

# ===== Fixed Input Area =====
st.markdown('<div class="input-box">', unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input("Ask AirWise a question", label_visibility="collapsed")

with col2:
    send = st.button("Ask")

st.markdown('</div>', unsafe_allow_html=True)

# ===== Send Message =====
if send and user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    st.session_state.messages.append(
        {"role": "bot", "text": get_bot_response(user_input)}
    )
    st.rerun()
