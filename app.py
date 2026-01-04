import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="AirWise – Air Quality & Health Chatbot",
    page_icon="☁️",
    layout="centered"
)

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #f0f9ff;
}

/* Header */
h1 {
    text-align: center;
    color: #0284c7;
    font-weight: 700;
}

/* Intro bubble */
.intro {
    background-color: #bae6fd;
    color: #0f172a;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 16px;
}

/* Bot message */
.bot {
    background-color: #0f172a;
    color: #e5e7eb;
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 10px;
    max-width: 85%;
}

/* User message */
.user {
    background-color: #dbeafe;
    color: #1e3a8a;
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 10px;
    margin-left: auto;
    max-width: 85%;
    text-align: right;
}

/* Fixed chat input bar */
.chat-input {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: linear-gradient(180deg, #0f172a, #020617);
    padding: 14px 16px;
    box-shadow: 0 -6px 20px rgba(0,0,0,0.5);
    z-index: 1000;
}

/* Input field */
.chat-input input {
    background-color: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 999px !important;
    padding: 14px 18px !important;
    border: 1px solid #1e293b !important;
    font-size: 16px !important;
}

/* Placeholder text */
.chat-input input::placeholder {
    color: #9ca3af;
}

/* Send button */
.chat-input button {
    background-color: #22c55e !important;
    color: white !important;
    border-radius: 999px !important;
    height: 48px;
    width: 48px;
    border: none;
    font-size: 20px;
}

/* Trash button (top-right) */
.trash {
    position: fixed;
    top: 12px;
    right: 16px;
    z-index: 1000;
}
</style>
""", unsafe_allow_html=True)

# ================== HEADER ==================
st.title("☁️ AirWise")

# ================== INTRO ==================
st.markdown(
    "<div class='intro'>Hi! I’m <b>AirWise</b> 🌬️. I explain air quality, air pollution, "
    "and how they affect our daily lives and health. Ask me anything below.</div>",
    unsafe_allow_html=True
)

# ================== SESSION STATE ==================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "confirm_clear" not in st.session_state:
    st.session_state.confirm_clear = False

# ================== TRASH BUTTON ==================
st.markdown('<div class="trash">', unsafe_allow_html=True)
if st.button("🗑️"):
    st.session_state.confirm_clear = True
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.confirm_clear:
    st.warning("Clear chat history?")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Yes"):
            st.session_state.messages = []
            st.session_state.confirm_clear = False
            st.experimental_rerun()
    with col_b:
        if st.button("No"):
            st.session_state.confirm_clear = False

# ================== CHAT DISPLAY ==================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['text']}</div>", unsafe_allow_html=True)

# Spacer so messages are not hidden by input
st.markdown("<div style='height:140px'></div>", unsafe_allow_html=True)

# ================== BOT LOGIC ==================
def airwise_response(q):
    q = q.lower()

    if "what is air pollution" in q:
        return "Air pollution is the presence of harmful substances like smoke, gases, and tiny particles in the air that can damage health and the environment."

    elif "effects" in q and "air pollution" in q:
        return "Air pollution can cause coughing, asthma, heart disease, reduced visibility, and damage to plants and animals."

    elif "daily life" in q and "air pollution" in q:
        return "Air pollution affects daily life by limiting outdoor activities, causing health issues, increasing medical costs, and reducing productivity."

    elif "air quality" in q and "daily life" in q:
        return "Poor air quality can make people feel tired, trigger allergies, affect school and work performance, and make outdoor exercise unsafe."

    elif "aqi" in q:
        return "The Air Quality Index (AQI) measures how clean or polluted the air is and shows possible health effects."

    elif "cause" in q:
        return "Common causes of air pollution include vehicle emissions, factory smoke, burning trash, wildfires, and dust."

    elif "health" in q:
        return "Bad air quality affects the lungs and heart and can worsen asthma, allergies, and other respiratory diseases."

    elif "indoor" in q:
        return "Indoor air pollution can come from cooking smoke, dust, mold, and chemicals. Ventilation helps improve it."

    elif "protect" in q or "prevent" in q:
        return "You can protect yourself by wearing masks, checking AQI levels, avoiding polluted areas, and keeping indoor spaces ventilated."

    elif "improve" in q:
        return "Air quality can be improved by planting trees, using public transport, saving energy, and avoiding burning trash."

    else:
        return "That’s a great question! Clean air is essential for health, nature, and a better quality of life."

# ================== INPUT BAR ==================
st.markdown('<div class="chat-input">', unsafe_allow_html=True)

col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "",
        placeholder="Ask something green…",
        label_visibility="collapsed"
    )

with col2:
    send = st.button("➤")

st.markdown('</div>', unsafe_allow_html=True)

# ================== SEND ACTION ==================
if send and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "text": user_input
    })

    response = airwise_response(user_input)

    st.session_state.messages.append({
        "role": "bot",
        "text": response
    })

    st.experimental_rerun()
