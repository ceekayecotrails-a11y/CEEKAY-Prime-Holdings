import streamlit as st

st.set_page_config(
    page_title="CEEKAY Prime Holdings",
    page_icon="🏛",
    layout="wide"
)

# ----------------------------------------------------
# GLOBAL STYLING
# ----------------------------------------------------
st.markdown("""
<style>

html, body, .main {
    background-color: #000000 !important;
}

h1, h2, h3, p, span, div {
    color: white !important;
}

/* Center container */
.center {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Logo box */
.logo-box img {
    border-radius: 12px;
    box-shadow: 0 0 25px rgba(255,215,0,0.3);
}

/* Title */
.title {
    font-size: 50px;
    font-weight: 900;
    text-align: center;
    color: #FFD700;
    text-shadow: 0px 0px 30px rgba(255,215,0,0.7);
    margin-top: 20px;
}

.tagline {
    text-align: center;
    color: #D9D9D9;
    font-size: 18px;
    margin-bottom: 40px;
}

/* Gold line */
.gold-line {
    width: 240px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #FFD700, transparent);
    margin: 0 auto 40px auto;
}

/* BUSINESS CARD */
.card {
    background-color: #0D0D0D;
    border: 1px solid #333;
    border-radius: 14px;
    padding: 40px 25px;
    text-align: center;
    transition: 0.3s;
    box-shadow: 0 0 12px rgba(255,215,0,0.12);
}
.card:hover {
    border-color: #FFD700;
    box-shadow: 0 0 20px rgba(255,215,0,0.4);
}

/* Icons */
.icon {
    font-size: 55px;
    color: #FFD700;
    margin-bottom: 14px;
}

/* Buttons */
button[kind="secondary"] {
    background-color: #FFD700 !important;
    color: black !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    height: 48px !important;
    font-size: 16px !important;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER SECTION
# ----------------------------------------------------
st.markdown("<div class='title'>CEEKAY PRIME HOLDINGS</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your Trusted Group of Services</div>", unsafe_allow_html=True)
st.markdown("<div class='gold-line'></div>", unsafe_allow_html=True)

# Centered Logo
st.markdown("<div class='center logo-box'>", unsafe_allow_html=True)
st.image("ceekay_prime_logo.png", width=250)
st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------------------------
# BUSINESS TILES
# ----------------------------------------------------
st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='icon'>🚘</div>", unsafe_allow_html=True)
    st.markdown("<h3>CEEKAY Eco Trails</h3>", unsafe_allow_html=True)
    st.markdown("<p>Transport • Tours • Daily Hire</p>", unsafe_allow_html=True)
    if st.button("Enter Eco Trails System", key="eco"):
        st.switch_page("https://ceekay-eco-trails-ghpv7plux3hj7jze957ugn.streamlit.app/")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='icon'>🏘️</div>", unsafe_allow_html=True)
    st.markdown("<h3>CEEKAY Homes</h3>", unsafe_allow_html=True)
    st.markdown("<p>Girls’ Accommodation & Student Hostel</p>", unsafe_allow_html=True)
    if st.button("Enter CEEKAY Homes System", key="homes"):
        st.info("CEEKAY Homes system coming soon!")
    st.markdown("</div>", unsafe_allow_html=True)
