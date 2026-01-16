import streamlit as st

st.set_page_config(
    page_title="CEEKAY Prime Holdings",
    page_icon="🏛",
    layout="wide",
)

# ---------------------------------------------------
# FULL BLACK GOLD PREMIUM STYLING
# ---------------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #000 !important;
    color: #ffffff !important;
}

/* Main container */
.main {
    background-color: #000 !important;
    padding-top: 20px;
}

/* Center everything */
.center {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Premium gold title */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    color: #FFD700;
    text-shadow: 0 0 25px rgba(255, 215, 0, 0.8);
    font-family: 'Arial Black', sans-serif;
}

/* Tagline */
.tagline {
    text-align: center;
    color: #bbbbbb;
    font-size: 18px;
    margin-top: -10px;
}

/* Gold line */
.goldline {
    width: 180px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #FFD700, transparent);
    margin: 20px auto 40px auto;
    border-radius: 10px;
}

/* Premium card box */
.box {
    background: linear-gradient(180deg, #111, #000);
    border: 1px solid #222;
    border-radius: 16px;
    padding: 30px;
    transition: 0.25s;
    box-shadow: 0px 0px 12px rgba(255, 215, 0, 0.08);
}

.box:hover {
    border: 1px solid #FFD700;
    box-shadow: 0px 0px 18px rgba(255, 215, 0, 0.3);
}

/* Icons */
.bigicon {
    font-size: 65px;
    color: #FFD700;
    text-align: center;
    margin-bottom: 10px;
}

/* Business titles */
.btitle {
    text-align: center;
    color: #ffffff;
    font-size: 24px;
    font-weight: 600;
}

/* Description */
.desc {
    text-align: center;
    color: #aaaaaa;
    margin-bottom: 25px;
    font-size: 15px;
}

/* Gold button */
button[kind="secondary"] {
    background-color: #FFD700 !important;
    color: black !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    height: 45px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("<div class='title'>CEEKAY PRIME HOLDINGS</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your Trusted Group of Services</div>", unsafe_allow_html=True)

# Gold divider line
st.markdown("<div class='goldline'></div>", unsafe_allow_html=True)

# Centered Logo
st.markdown("<div class='center'>", unsafe_allow_html=True)
st.image("ceekay_prime_logo.png", width=230)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------
# TWO GOLD PREMIUM TILES
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='bigicon'>🚗</div>", unsafe_allow_html=True)
    st.markdown("<div class='btitle'>CEEKAY Eco Trails</div>", unsafe_allow_html=True)
    st.markdown("<div class='desc'>Transport • Tours • Daily Hire</div>", unsafe_allow_html=True)

    if st.button("Enter Eco Trails System", key="eco"):
        st.switch_page("https://ceekay-eco-trails-ghpv7plux3hj7jze957ugn.streamlit.app/")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<div class='bigicon'>🏠</div>", unsafe_allow_html=True)
    st.markdown("<div class='btitle'>CEEKAY Homes</div>", unsafe_allow_html=True)
    st.markdown("<div class='desc'>Girls’ Accommodation & Student Hostel</div>", unsafe_allow_html=True)

    if st.button("Enter CEEKAY Homes System", key="homes"):
        st.info("CEEKAY Homes system coming soon!")

    st.markdown("</div>", unsafe_allow_html=True)
