import streamlit as st
st.markdown("---")
st.header("CV App: Build Your Profile")

name2    = st.text_input("Your name")
age2     = st.slider("Your age", 15, 80, 20)
subject2 = st.selectbox("Your major", ["AI", "Computer Science", "Engineering", "Medicine"])
shortbio   = st.text_area("Your Short Bio")
gpa  = st.radio("Your GPA",["A","B","C","D","F"])

if st.button("Generate Profile Card"):
    st.success("✅ Thank you for filling your information!")
    st.markdown("---")
    st.subheader("📋 Your Profile Card")
    st.write(f"*Name:*    {name2}")
    st.write(f"*Age:*     {age2}")
    st.write(f"*Major:*   {subject2}")
    st.write(f"*Your Short Bio:*   {shortbio}")
    st.write(f"*Your GPA:* {gpa}")
else:
    st.warning("⚠️ Please fill in your information")
