import streamlit as st

st.set_page_config(
    page_title="Kalp Hastalığı Risk Tahmini",
    page_icon="❤️",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #f8f7fc;
    --card: #ffffff;
    --border: #e0d9f0;
    --purple-dark: #4a2880;
    --purple: #7c3aed;
    --purple-light: #ede9ff;
    --gray: #6b7280;
    --gray-light: #f3f0fa;
    --text: #1a1a2e;
    --white: #ffffff;
}

* { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
}

/* HERO */
.hero {
    text-align: center;
    padding: 3rem 0 2rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    color: var(--purple-dark);
    margin: 0;
    letter-spacing: -1px;
}
.hero p {
    color: var(--gray);
    font-size: 0.85rem;
    font-weight: 400;
    margin-top: 0.5rem;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.accent-line {
    width: 60px;
    height: 4px;
    background: linear-gradient(90deg, var(--purple), #a78bfa);
    margin: 1rem auto;
    border-radius: 99px;
}

/* KARTLAR */
.card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 20px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 24px rgba(124,58,237,0.06);
}
.card-title {
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--purple);
    margin-bottom: 1.2rem;
    font-weight: 600;
}

/* SONUÇ KUTULARI */
.result-box {
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    margin: 1.5rem 0;
    border: 1.5px solid var(--border);
}
.result-safe {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    border-color: #86efac;
}
.result-warning {
    background: linear-gradient(135deg, #fffbeb, #fef3c7);
    border-color: #fcd34d;
}
.result-danger {
    background: linear-gradient(135deg, #fdf4ff, #ede9ff);
    border-color: var(--purple);
}
.result-icon { font-size: 3.5rem; margin-bottom: 0.5rem; }
.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    margin: 0.5rem 0;
    font-weight: 700;
}
.result-desc {
    color: var(--gray);
    font-size: 0.95rem;
    font-weight: 300;
    line-height: 1.6;
}

/* DETAY SATIRLARI */
.detail-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.7rem 0;
    border-bottom: 1px solid var(--border);
    font-size: 0.9rem;
}
.detail-label { color: var(--gray); }
.detail-value {
    color: var(--purple-dark);
    font-weight: 600;
    background: var(--purple-light);
    padding: 2px 12px;
    border-radius: 99px;
    font-size: 0.85rem;
}

/* BUTON */
div.stButton > button {
    background: linear-gradient(135deg, var(--purple), #9333ea) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.85rem 2rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(124,58,237,0.3) !important;
    transition: all 0.2s !important;
}
div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(124,58,237,0.4) !important;
}

/* SELECT & INPUT */
div[data-baseweb="select"] > div {
    background: var(--gray-light) !important;
    border-color: var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
}
div[data-baseweb="input"] > div {
    background: var(--gray-light) !important;
    border-color: var(--border) !important;
    border-radius: 12px !important;
}
label {
    color: var(--gray) !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}

/* BADGE */
.badge {
    display: inline-block;
    background: var(--purple-light);
    color: var(--purple);
    border-radius: 99px;
    padding: 4px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 1rem;
}

/* FOOTER */
.footer {
    text-align: center;
    color: var(--gray);
    font-size: 0.78rem;
    letter-spacing: 1px;
    padding: 2rem 0 1rem;
    border-top: 1.5px solid var(--border);
    margin-top: 2rem;
}

/* EXPANDER */
div[data-testid="stExpander"] {
    background: var(--white) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# BAŞLIK
# ==========================================
st.markdown("""
<div class="hero">
    <div class="badge">AI Destekli Analiz</div>
    <h1>Kalp Risk Analizi</h1>
    <div class="accent-line"></div>
    <p>Fuzzy Three-Valued Logic Sistemi</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# GİRİŞ KARTLARI
# ==========================================
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><div class="card-title">👤 Kişisel Bilgiler</div>', unsafe_allow_html=True)
    gender = st.selectbox("Cinsiyet", ["Kadın", "Erkek"])
    age    = st.number_input("Yaş", min_value=1, max_value=100, value=40)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><div class="card-title">🚬 Yaşam Tarzı</div>', unsafe_allow_html=True)
    smoke    = st.selectbox("Sigara", ["Hayır", "Evet"])
    alco     = st.selectbox("Alkol",  ["Hayır", "Evet"])
    physical = st.selectbox("Fiziksel Aktivite", ["Evet", "Hayır"])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# TAHMİN BUTONU
# ==========================================
if st.button("🔍  ANALİZ ET", use_container_width=True):

    g = 1 if gender   == "Kadın" else 2
    x = 1 if smoke    == "Evet"  else 0
    y = 1 if alco     == "Evet"  else 0
    z = 0 if physical == "Evet"  else 1

    # Fuzzification
    if x == y == z == 0:
        other_factors = 0
    elif x == y == z == 1:
        other_factors = 1
    else:
        other_factors = 0.5

    # Yaş Kategorisi
    age_cat = 0 if (g == 1 and age < 55) or (g == 2 and age < 45) else 1

    # 12 Kural
    if g == 1:
        if   age_cat == 0 and other_factors == 0:   risk = 0
        elif age_cat == 0 and other_factors == 0.5: risk = 0.5
        elif age_cat == 0 and other_factors == 1:   risk = 1
        elif age_cat == 1 and other_factors == 0:   risk = 0.5
        elif age_cat == 1 and other_factors == 0.5: risk = 0.5
        else:                                        risk = 1
    else:
        if   age_cat == 0 and other_factors == 0:   risk = 0
        elif age_cat == 0 and other_factors == 0.5: risk = 0.5
        elif age_cat == 0 and other_factors == 1:   risk = 1
        elif age_cat == 1 and other_factors == 0:   risk = 0.5
        elif age_cat == 1 and other_factors == 0.5: risk = 0.5
        else:                                        risk = 1

    # SONUÇ
    if risk == 0:
        st.markdown("""
        <div class="result-box result-safe">
            <div class="result-icon">✅</div>
            <div class="result-title" style="color:#16a34a">RİSK YOK</div>
            <div class="result-desc">Kalp hastalığı riski tespit edilmedi.<br>Sağlıklı yaşam tarzınızı sürdürmeye devam edin.</div>
        </div>
        """, unsafe_allow_html=True)

    elif risk == 0.5:
        st.markdown("""
        <div class="result-box result-warning">
            <div class="result-icon">⚠️</div>
            <div class="result-title" style="color:#d97706">RİSK OLABİLİR</div>
            <div class="result-desc">Kalp hastalığı riski belirsiz.<br>Eksik sağlıklı alışkanlıkları hayatınıza ekleyin.</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="result-box result-danger">
            <div class="result-icon">🔴</div>
            <div class="result-title" style="color:#7c3aed">RİSK VAR</div>
            <div class="result-desc">Kalp hastalığı riski yüksek!<br>Lütfen en kısa sürede bir doktora başvurun.</div>
        </div>
        """, unsafe_allow_html=True)

    # DETAYLAR
    with st.expander("🔎 Hesaplama Detayları"):
        st.markdown(f"""
        <div class="detail-row">
            <span class="detail-label">Cinsiyet</span>
            <span class="detail-value">{gender}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Yaş Kategorisi</span>
            <span class="detail-value">{'≥ Eşik' if age_cat == 1 else '< Eşik'}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Sigara (x)</span>
            <span class="detail-value">{x}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Alkol (y)</span>
            <span class="detail-value">{y}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Hareketsizlik (¬z)</span>
            <span class="detail-value">{z}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Other Factors (θ)</span>
            <span class="detail-value">{other_factors}</span>
        </div>
        <div class="detail-row" style="border:none">
            <span class="detail-label">Risk Skoru</span>
            <span class="detail-value">{risk}</span>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    📖 Khushal & Fatima — Fuzzy Three-Valued Logic in Machine Learning · 2025
</div>
""", unsafe_allow_html=True)