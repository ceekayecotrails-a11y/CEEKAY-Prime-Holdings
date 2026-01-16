import streamlit as st

st.set_page_config(
    page_title="CEEKAY Prime Holdings",
    page_icon="🏛",
    layout="wide",
)

# ---------------------------------------------------
# FORCE DARK BACKGROUND (WORKS IN STREAMLIT CLOUD)
# ---------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #000000 !important;
    color: white !important;
}

.main {
    background-color: #000000 !important;
}

/* Center everything */
.center {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Title */
.title {
    font-size: 42px;
    text-align: center;
    font-weight: 900;
    color: #FFD700;
    text-shadow: 0 0 20px rgba(255,200,0,0.6);
}

.tagline {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
    color: #cccccc;
}

/* Section card */
.box {
    background-color: #111111;
    padding: 30px;
    border-radius: 14px;
    border: 1px solid #222222;
    transition: 0.3s ease;
}

.box:hover {
    border: 1px solid #FFD700;
    background-color: #1a1a1a;
}

/* Icons */
.bigicon {
    font-size: 60px;
    text-align: center;
    color: #FFD700;
}

/* Buttons */
button[kind="secondary"] {
    background-color: #FFD700 !important;
    color: black !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------
st.markdown("<div class='title'>CEEKAY PRIME HOLDINGS</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your Trusted Group of Services</div>", unsafe_allow_html=True)

# Center Logo
st.markdown("<div class='center'>", unsafe_allow_html=True)
st.image("ceekay_prime_logo.png", width=220)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------
# BUSINESS CARDS
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='bigicon'>🚗</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>CEEKAY Eco Trails</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#bbbbbb;'>Daily travel & tourism solutions</p>", unsafe_allow_html=True)

    if st.button("Enter Eco Trails System", key="eco"):
        st.switch_page("https://ceekay-eco-trails-ghpv7plux3hj7jze957ugn.streamlit.app/")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='bigicon'>🏠</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>CEEKAY Homes</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#bbbbbb;'>Girls’ accommodation & student hostel</p>", unsafe_allow_html=True)

    if st.button("Enter CEEKAY Homes System", key="homes"):
        st.info("CEEKAY Homes system coming soon!")

    st.markdown("</div>", unsafe_allow_html=True)
