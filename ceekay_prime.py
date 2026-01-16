import streamlit as st

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="CEEKAY Prime Holdings",
    page_icon="🏛",
    layout="centered",
)

# ------------------------------
# CUSTOM CSS (Black & Gold Theme)
# ------------------------------
st.markdown("""
<style>
body {
    background-color: #000000;
}
.big-tile {
    width: 160px;
    height: 160px;
    background-color: #111111;
    border: 2px solid #FFD700;
    border-radius: 16px;
    padding: 20px;
    cursor: pointer;
    text-align: center;
}
.big-tile:hover {
    background-color: #1a1a1a;
}
.tile-icon {
    font-size: 55px;
    margin-bottom: 10px;
}
.logo {
    text-align: center;
    margin-bottom: 30px;
}
.title-text {
    font-size: 32px;
    font-weight: bold;
    color: #FFD700;
    text-align: center;
    margin-bottom: 10px;
}
.sub-text {
    color: #cccccc;
    text-align: center;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# HEADER
# ------------------------------
st.markdown("<div class='title-text'>CEEKAY PRIME HOLDINGS</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Your Trusted Group of Services</div>", unsafe_allow_html=True)

# ------------------------------
# LOGO PLACEHOLDER (Your Black-Gold Logo)
# ------------------------------
st.image("ceekay_prime_logo.png", width=180)  # replace when you upload actual logo


st.write("")
st.write("")

# ------------------------------
# TWO BIG TILES
# ------------------------------
col1, col2 = st.columns(2, gap="large")

with col1:
    if st.button("🚗\nCEEKAY Eco Trails", use_container_width=True):
        st.switch_page("https://ceekay-eco-trails-ghpv7plux3hj7jze957ugn.streamlit.app/")

with col2:
    if st.button("🏠\nCEEKAY Homes", use_container_width=True):
        st.info("CEEKAY Homes system is coming soon!")
