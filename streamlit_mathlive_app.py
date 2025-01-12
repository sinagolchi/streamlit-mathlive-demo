import streamlit as st
from st_mathlive import mathfield

Tex, MathML = mathfield(title="Equation 1", value=r"\int_{30}^{100}x^5dx",mathml_preview=True,enable_edit=True)

st.subheader("Tex render via st.latex:")
st.latex(Tex)
st.subheader("MathML code")
st.code(MathML)

