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
    q = question.lower()
    
    if st.button("Ask"):
       q = question.lower().strip()

    if q in ["hi", "hello", "hey", "wassup", "yo"]:
        return "Hello! 👋 I'm AirWise. How can I help you today?"
  
    elif q == "what is air pollution":
        st.success(
            "Air pollution is the presence of harmful substances in the air "
            "such as smoke, dust, and gases that can harm people and the environment."
        )

    elif q in ["who are you", "what is this bot", "bot description"]:
        st.success(
            "I am an Air Quality Chatbot created to help students understand "
            "air pollution and air quality."
        )

    else:
       st.warning("Sorry, I don't understand that yet.")
  
    if "what is air pollution" in q:
        return "Air pollution is the presence of harmful substances like smoke, chemicals, and tiny particles in the air that can harm humans, animals, and the environment."

    if "good air quality" in q:
        return "Good air quality means the air is clean and safe to breathe, with very low levels of pollutants. It supports good health and outdoor activities."

    if "bad air quality" in q:
        return "Bad air quality means the air contains high levels of pollutants that can cause breathing problems, eye irritation, and other health issues."

    if "air quality affect our daily life" in q:
        return "Air quality affects how safe it is to go outside, exercise, travel, and even how productive we feel. Poor air quality can limit outdoor activities."

    if "air pollution affect our daily life" in q:
        return "Air pollution can cause coughing, headaches, fatigue, and can worsen asthma. It can also reduce visibility and damage buildings and crops."

    if "health" in q:
        return "Poor air quality can cause asthma, lung disease, heart problems, and can be especially dangerous for children and the elderly."

    if "aqi" in q:
        return "AQI stands for Air Quality Index. It tells us how clean or polluted the air is and what health effects may occur."

    if "prevent" in q or "reduce" in q:
        return "We can reduce air pollution by using public transport, saving electricity, avoiding burning trash, and planting trees."

    return "That’s a great question! Air quality affects our health, environment, and daily activities. Try asking about pollution, AQI, health effects, or prevention tips."
    if "how does good air quality affect us" in q or "effects of good air quality" in q:
        return (
            "Good air quality helps us breathe easily, stay active, and feel healthier. "
            "It reduces the risk of asthma, allergies, and heart problems, improves sleep, "
            "boosts concentration in school and work, and allows people to enjoy outdoor activities safely."
        )

    if "how does bad air quality affect us" in q or "effects of bad air quality" in q:
        return (
            "Bad air quality can cause coughing, difficulty breathing, eye irritation, "
            "headaches, and fatigue. Over time, it can lead to serious health problems such as "
            "asthma, lung disease, heart conditions, and can be especially harmful to children and the elderly."
        )

    if "why is good air quality important" in q:
        return (
            "Good air quality is important because clean air is essential for life. "
            "It protects our lungs and heart, supports mental well-being, helps ecosystems thrive, "
            "and improves overall quality of life."
        )

    if "compare good and bad air quality" in q or "difference between good and bad air quality" in q:
        return (
            "Good air quality means clean, safe air that supports health and outdoor activities. "
            "Bad air quality means polluted air that can cause illness, discomfort, and long-term health risks."
    )
def ask_airwise():
    user_input = entry.get().lower().strip()

    if user_input in knowledge_base:
        result_label.config(text=knowledge_base[user_input])

    else:
        result_label.config(
            text="Hmm… that doesn’t seem related to air quality. Try keywords like AQI, pollution, or PM2.5!"
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
