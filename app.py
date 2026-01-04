import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AirWise – Air Quality & Health Chatbot",
    page_icon="☁️",
    layout="centered"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.stApp {
    background-color: #f0f9ff;
}

/* Header */
h1 {
    text-align: center;
    color: #0284c7;
    font-weight: 800;
    margin-top: 10px;
}

/* Intro box */
.intro {
    background-color: #bae6fd;
    color: #0f172a;
    padding: 16px;
    border-radius: 16px;
    margin-bottom: 18px;
}

/* Bot message */
.bot {
    background-color: #0f172a;
    color: #e5e7eb;
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 12px;
    max-width: 85%;
}

/* User message */
.user {
    background-color: #dbeafe;
    color: #1e3a8a;
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 12px;
    margin-left: auto;
    max-width: 85%;
    text-align: right;
}

/* Trash icon */
.trash {
    position: fixed;
    top: 16px;
    right: 16px;
    z-index: 2000;
}

/* Input styling */
.stTextInput input {
    background-color: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 999px !important;
    padding: 14px 18px !important;
    border: 1px solid #1e293b !important;
    font-size: 16px !important;
}

.stTextInput input::placeholder {
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.title("☁️ AirWise")

# ================= INTRO =================
st.markdown(
    "<div class='intro'>Hi! I’m <b>AirWise</b> 🌬️. I explain air quality, air pollution, "
    "and how they affect our daily lives and health. Ask me anything below.</div>",
    unsafe_allow_html=True
)

# ================= SESSION STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "confirm_clear" not in st.session_state:
    st.session_state.confirm_clear = False

# ================= TRASH BUTTON =================
st.markdown('<div class="trash">', unsafe_allow_html=True)
if st.button("🗑️", key="trash"):
    st.session_state.confirm_clear = True
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.confirm_clear:
    st.warning("Clear chat history?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            st.session_state.messages = []
            st.session_state.confirm_clear = False
            st.experimental_rerun()
    with col2:
        if st.button("No"):
            st.session_state.confirm_clear = False

# ================= CHAT DISPLAY =================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['text']}</div>", unsafe_allow_html=True)

# Space so input isn't covered
st.markdown("<div style='height:160px'></div>", unsafe_allow_html=True)

# ================= BOT LOGIC =================
def airwise_response(q):
    q = q.lower()

    if "what is air pollution" in q:
        return "Air pollution is the presence of harmful substances such as smoke, gases, and tiny particles in the air that can damage health and the environment."

    if "effects" in q and "air pollution" in q:
        return "Air pollution causes breathing problems, asthma, heart disease, eye irritation, and can damage plants, animals, and buildings."

    if "daily life" in q and "air pollution" in q:
        return "Air pollution affects daily life by limiting outdoor activities, increasing illness, reducing productivity, and making the air unsafe to breathe."

    if "air quality" in q and "daily life" in q:
        return "Poor air quality can cause tiredness, headaches, allergies, and makes outdoor exercise unsafe, especially for children and elders."

    if "aqi" in q:
        return "The Air Quality Index (AQI) shows how clean or polluted the air is and what health effects may occur."

    if "cause" in q:
        return "Air pollution is caused by vehicle emissions, factory smoke, burning trash, wildfires, and dust."

    if "health" in q:
        return "Bad air quality affects the lungs and heart and can worsen asthma, allergies, and other respiratory diseases."

    if "indoor" in q:
        return "Indoor air pollution comes from cooking smoke, dust, mold, and chemicals. Proper ventilation helps improve it."

    if "protect" in q or "prevent" in q:
        return "You can protect yourself by wearing masks, checking AQI levels, avoiding polluted areas, and keeping indoor spaces well ventilated."

    if "improve" in q:
        return "Air quality can be improved by planting trees, using public transport, saving energy, and avoiding burning trash."

    return "That’s a great question! Clean air is essential for health, nature, and a better quality of life."

# ================= INPUT =================
user_input = st.text_input(
    "",
    placeholder="Ask something green…",
    label_visibility="collapsed"
)

send = st.button("➤")

# ================= SEND ACTION =================
if send and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "text": user_input
    })

    reply = airwise_response(user_input)

    st.session_state.messages.append({
        "role": "bot",
        "text": reply
    })

    st.experimental_rerun()
