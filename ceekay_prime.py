import streamlit as st

st.set_page_config(
    page_title="CEEKAY Prime Holdings",
    page_icon="🏛",
    layout="wide",
)

# ---------------------------------------------------
# Custom CSS for Premium Black-Gold Theme
# ---------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #000000;
}

/* Gold Glow Title */
.title-glow {
    font-size: 42px;
    text-align: center;
    font-weight: 700;
    color: #FFD700;
    text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.6);
    margin-top: 10px;
}

.tagline {
    text-align: center;
    color: #cccccc;
    margin-bottom: 40px;
    font-size: 18px;
}

/* Section Containers */
.section {
    background-color: #111111;
    border: 1px solid #333333;
    border-radius: 16px;
    padding: 25px;
    margin: 15px 0px;
    transition: 0.3s;
}
.section:hover {
    background-color: #1a1a1a;
    border-color: #FFD700;
}

/* Icons */
.big-icon {
    font-size: 70px;
    color: #FFD700;
    text-align: center;
}

/* Section Titles */
.section-title {
    text-align: center;
    color: white;
    font-size: 26px;
    font-weight: 600;
    margin-top: 10px;
}

.section-desc {
    text-align: center;
    color: #aaaaaa;
    font-size: 16px;
    margin-bottom: 20px;
}

/* Buttons */
.gold-btn {
    background-color: #FFD700;
    color: black;
    font-weight: 700;
    width: 100%;
    padding: 15px;
    border-radius: 10px;
}
.gold-btn:hover {
    background-color: #ffea77;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("<div class='title-glow'>CEEKAY PRIME HOLDINGS</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your Trusted Group of Services</div>", unsafe_allow_html=True)

# Logo
st.image("ceekay_prime_logo.png", width=200)

st.write("")
st.write("")

# ---------------------------------------------------
# BUSINESS SECTIONS
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<div class='big-icon'>🚗</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>CEEKAY Eco Trails</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-desc'>Your daily travel, hire, and tourism service partner.</div>", unsafe_allow_html=True)

    if st.button("Enter Eco Trails System", key="eco", use_container_width=True):
        st.switch_page("https://ceekay-eco-trails-ghpv7plux3hj7jze957ugn.streamlit.app/")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<div class='big-icon'>🏠</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>CEEKAY Homes</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-desc'>Girls’ accommodation and student hostel service.</div>", unsafe_allow_html=True)

    if st.button("Enter CEEKAY Homes System", key="homes", use_container_width=True):
        st.info("CEEKAY Homes system coming soon!")

    st.markdown("</div>", unsafe_allow_html=True)
