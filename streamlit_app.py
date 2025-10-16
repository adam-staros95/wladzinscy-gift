import streamlit as st
from collections import Counter

st.set_page_config(page_title="Kalkulator składki na prezent 🎁", page_icon="🎈", layout="centered")

st.title("🎈 Kalkulator składki na prezent")

values = [500, 500, 999, 999]

n = len(values)
total = sum(values)
avg = total / n

counter = Counter(values)
formatted_values = ", ".join(
    [f"{count}x{int(val)}" if count > 1 else f"{int(val)}" for val, count in counter.items()]
)

st.markdown("---")
st.markdown("### 📘 Wzór na średnią arytmetyczną")
st.latex(r"\text{Średnia} = \frac{a_1 + a_2 + \ldots + a_n}{n}")

st.markdown("### 📗 Wzór z podstawionymi wartościami")
st.latex(
    rf"\text{{Średnia}} = \frac{{{ ' + '.join(str(int(v)) for v in values) }}}{{{n}}} = {avg:.2f}"
)

st.markdown("---")
st.markdown(f"### 💰 Kwoty uczestników: {formatted_values}")
st.markdown(f"### 📊 Obecna kwota to: **{avg:.2f} zł**")

thresholds = [500, 800, 999]
closest = min(thresholds, key=lambda x: abs(x - avg))
st.markdown(f"### 🎁 Zatem kupimy voucher za: **{closest} zł**")