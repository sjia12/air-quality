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
    background-color: #eef6ff;
}

/* Center title */
h1 {
    text-align: center;
    color: #0f172a;
}

/* Clear chat button (top right) */
.clear-btn {
    position: fixed;
    top: 15px;
    right: 20px;
    z-index: 1000;
}

/* Bot message */
.bot {
    background-color: #bae6fd;
    color: #0f172a;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    max-width: 90%;
}

/* User message */
.user {
    background-color: #dcfce7;
    color: #064e3b;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    text-align: right;
    margin-left: auto;
    max-width: 90%;
}

/* Fixed input area */
.input-box {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #e0f2fe;
    padding: 12px;
    border-top: 2px solid #38bdf8;
    z-index: 1000;
}
</style>
""", unsafe_allow_html=True)

# ===== Session State =====
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "bot",
            "text": "Hi! I’m AirWise 🌬️. I help explain air quality and its effects on health and the environment. Ask me anything below."
        }
    ]

# ===== Clear Chat Button (Icon Only) =====
with st.container():
    st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
    if st.button("🗑️"):
        st.session_state.messages = [
            {
                "role": "bot",
                "text": "Hi! I’m AirWise 🌬️. Ask me anything about air quality and health."
            }
        ]
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ===== Header =====
st.title("☁️ AirWise")

# ===== Chat Display =====
st.markdown("<br><br>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{msg['text']}</div>", unsafe_allow_html=True)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# ===== Bot Logic =====
def get_bot_response(q):
    q = q.lower()

    if "what is air pollution" in q:
        return "Air pollution is the presence of harmful substances like smoke, gases, and dust in the air that can harm people and the environment."

    elif "effects" in q:
        return "Air pollution can cause asthma, coughing, breathing problems, and can damage plants, animals, and climate."

    elif "cause" in q or "burning" in q:
        return "Common causes include burning trash, vehicle exhaust, factory smoke, and forest fires."

    elif "health" in q:
        return "Poor air quality affects the lungs and heart, especially in children and the elderly."

    elif "aqi" in q:
        return "The Air Quality Index (AQI) shows how polluted the air is and what health effects may occur."

    elif "improve" in q:
        return "We can improve air quality by planting trees, using public transport, and saving energy."

    else:
        return "That’s a great question! Clean air helps keep people healthy and protects the environment."

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
