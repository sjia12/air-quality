import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AirWise",
    page_icon="☁️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #f0f9ff;
}

/* FORCE HEADER COLOR (LIGHT + DARK MODE FIX) */
[data-testid="stAppViewContainer"] h1,
[data-testid="stAppViewContainer"] h1 span,
[data-testid="stHeader"] h1,
[data-testid="stHeader"] h1 span {
    color: #0284c7 !important; /* sapphire blue */
    font-weight: 800 !important;
    text-align: center;
}

/* Intro box */
.intro-box {
    background-color: #bae6fd;
    color: #0f172a;
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 20px;
    font-size: 16px;
}

/* Bot message */
.bot-msg {
    background-color: #0f172a;
    color: #e0f2fe;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
}

/* User message */
.user-msg {
    background-color: #e0f2fe;
    color: #0f172a;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
}

/* Fixed input area */
.input-area {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    background-color: #020617;
    padding: 12px;
    border-radius: 16px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

/* Text input */
.stTextInput > div > div > input {
    background-color: #020617;
    color: white;
    border-radius: 12px;
    border: 1px solid #38bdf8;
}

/* Send button */
.stButton button {
    background-color: #38bdf8;
    color: black;
    border-radius: 12px;
    font-weight: bold;
}

/* Trash button color */
.trash button {
    color: #0284c7 !important;   /* blue */
    font-size: 22px;
}
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1>☁️ AirWise</h1>", unsafe_allow_html=True)

# ---------------- CLEAR CHAT ----------------
if "confirm_clear" not in st.session_state:
    st.session_state.confirm_clear = False

col1, col2 = st.columns([8, 1])

with col2:
    if st.button("🗑️", key="trash"):
        st.session_state.confirm_clear = True

if st.session_state.confirm_clear:
    st.warning("Clear all chat messages?")

    c1, c2 = st.columns(2)

    if c1.button("Yes"):
        st.session_state.messages = []
        st.session_state.confirm_clear = False
        st.rerun()

    if c2.button("No"):
        st.session_state.confirm_clear = False
        st.rerun()

# ---------------- INTRO ----------------
st.markdown("""
<div class="intro-box">
Hi! I’m <b>AirWise ☁️</b>.  
Ask me about air quality, air pollution, and how they affect our daily lives!
</div>
""", unsafe_allow_html=True)

# ---------------- CHAT MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- KNOWLEDGE BASE ----------------
def airwise_response(question):
    q = question.lower().strip()

    # ---------------- GREETINGS ----------------
    if q in ["hi", "hello", "hey", "yo", "wassup"]:
        return "Hello! 👋 I'm AirWise ☁️ How can I help you today?"

    # ---------------- BOT INFO ----------------
    if q in ["who are you", "what is this bot", "bot description"]:
        return (
            "I am AirWise ☁️, an air quality chatbot designed to help students "
            "understand air pollution, air quality, and their effects on daily life."
        )

    # ---------------- BASIC CONCEPTS ----------------
    if "what is air pollution" in q:
        return (
            "Air pollution is the presence of harmful substances like smoke, gases, "
            "and tiny particles in the air that can harm humans, animals, and the environment."
        )

    if "what is air quality" in q:
        return (
            "Air quality refers to how clean or polluted the air is. "
            "Good air quality means safe air to breathe, while poor air quality can be harmful."
        )

    if "aqi" in q:
        return (
            "AQI stands for Air Quality Index. It tells us how clean or polluted the air is "
            "and what health effects may happen."
        )

    # ---------------- GOOD vs BAD AIR QUALITY ----------------
    if "good air quality" in q:
        return (
            "Good air quality means the air is clean and safe to breathe. "
            "It helps people stay healthy and enjoy outdoor activities."
        )

    if "bad air quality" in q:
        return (
            "Bad air quality means the air contains many pollutants that can cause "
            "breathing problems, coughing, and illness."
        )

    if "difference between good and bad air quality" in q or "compare good and bad air quality" in q:
        return (
            "Good air quality is clean and safe for health, while bad air quality is polluted "
            "and can cause sickness and discomfort."
        )

    # ---------------- EFFECTS ----------------
    if "how does good air quality affect us" in q or "effects of good air quality" in q:
        return (
            "Good air quality helps us breathe easily, stay active, focus better in school, "
            "sleep well, and reduces the risk of diseases."
        )

    if "how does bad air quality affect us" in q or "effects of bad air quality" in q:
        return (
            "Bad air quality can cause coughing, headaches, difficulty breathing, asthma, "
            "lung disease, and heart problems, especially in children and the elderly."
        )

    if "air quality affect our daily life" in q:
        return (
            "Air quality affects our daily activities such as going outside, exercising, "
            "traveling, and even our mood and productivity."
        )

    if "air pollution affect our daily life" in q:
        return (
            "Air pollution can cause health problems, reduce visibility, damage crops, "
            "and limit outdoor activities."
        )

    if "health" in q:
        return (
            "Poor air quality can cause asthma, lung infections, heart disease, "
            "and other serious health problems."
        )

    # ---------------- PREVENTION ----------------
    if "prevent" in q or "reduce" in q:
        return (
            "We can reduce air pollution by using public transport, saving electricity, "
            "avoiding burning trash, and planting trees."
        )

    # ---------------- DEFAULT ----------------
    return (
        "I'm still learning 🌱 Try asking about air pollution, AQI, "
        "good or bad air quality, health effects, or prevention tips."
        )
# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)

# ---------------- INPUT AREA ----------------
st.divider()

user_input = st.text_input(
    "Ask AirWise",
    placeholder="Type your question here..."
)

send = st.button("➤ Ask")

if send and user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = airwise_response(user_input)

    st.session_state.messages.append(
        {"role": "bot", "content": reply}
    )

    st.rerun()
