import streamlit as st
from pathlib import Path
from utils.footer import show_footer

st.set_page_config(page_title="Contact | TRUERIZE",page_icon="📞",layout="wide",initial_sidebar_state="expanded")

BASE_DIR=Path(__file__).resolve().parent.parent
LOGO=BASE_DIR/"assets"/"logo.png"

with st.sidebar:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)
    st.title("📞 Contact")
    st.success("Professional Support")
    st.info("Need assistance? Our team is ready to help.")

left,right=st.columns([3,1])

with left:
    st.title("📞 Contact TRUERIZE")
    st.write("""
Thank you for visiting the TRUERIZE platform. We are available to assist you with technical support, business consultation, training, project guidance and collaboration.
""")

with right:
    if LOGO.exists():
        st.image(str(LOGO),use_container_width=True)

with st.expander("📌 Get In Touch"):
    st.write("We welcome enquiries related to:")
    st.write("• Machine Learning")
    st.write("• Artificial Intelligence")
    st.write("• Technical Support")
    st.write("• Business Collaboration")
    st.write("• Training")
    st.write("• Consulting")
    st.write("• Enterprise Solutions")

with st.expander("☎ Contact Information"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Office")
        st.write("TRUERIZE Strategic Solutions Pvt. Ltd.")
        st.write("AI & Machine Learning Solutions")
        st.write("Monday - Friday")
        st.write("09:00 AM - 06:00 PM")

    with c2:
        st.subheader("Contact")
        st.write("Phone : +91 XXXXXXXXXX")
        st.write("Email : info@yourcompany.com")
        st.write("Technical Support")

    with c3:
        st.subheader("Services")
        st.write("• Technical Support")
        st.write("• Project Consultation")
        st.write("• Training")
        st.write("• Business Collaboration")

with st.expander("🤝 Support Commitment"):

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.success("⚡ Fast Response")

    with c2:
        st.success("🤝 Professional Support")

    with c3:
        st.success("🔒 Reliable Assistance")

    with c4:
        st.success("🌍 Customer Focused")

    st.info("We are committed to providing timely and professional assistance.")

with st.expander("📝 Send an Enquiry"):

    with st.form("contact_form"):

        c1,c2=st.columns(2)

        with c1:
            name=st.text_input("Full Name")
            email=st.text_input("Email Address")

        with c2:
            phone=st.text_input("Phone Number")
            subject=st.selectbox("Subject",["General Enquiry","Technical Support","Business Collaboration","Training","Feedback","Other"])

        message=st.text_area("Message",height=180)

        submit=st.form_submit_button("Submit")

        if submit:
            st.success("Thank you. Your enquiry has been submitted successfully.")

with st.expander("🕒 Business Hours"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Office Hours")
        st.write("Monday - Friday")
        st.write("09:00 AM - 06:00 PM")

    with c2:
        st.subheader("Support Hours")
        st.write("09:30 AM - 05:30 PM")

    with c3:
        st.subheader("Response Time")
        st.write("Within 24 Hours")

with st.expander("⭐ Why Contact TRUERIZE"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Business Consultation")
        st.write("• Enterprise Solutions")
        st.write("• Consulting")
        st.write("• Partnerships")
        st.write("• Project Discussion")

    with c2:
        st.subheader("Technical Support")
        st.write("• Installation")
        st.write("• Configuration")
        st.write("• Troubleshooting")
        st.write("• Platform Guidance")

    with c3:
        st.subheader("Training")
        st.write("• Workshops")
        st.write("• Demonstrations")
        st.write("• Technical Guidance")
        st.write("• Learning Support")

with st.expander("❓ Frequently Asked Questions"):

    with st.expander("How can I request technical support?"):
        st.write("Use the enquiry form or contact the support team through the official communication channels.")

    with st.expander("How quickly will I receive a response?"):
        st.write("Most enquiries receive a response within one business day.")

    with st.expander("Do you provide demonstrations or training?"):
        st.write("Yes. We provide workshops, demonstrations and technical training.")

    with st.expander("Can I discuss collaboration opportunities?"):
        st.write("Yes. We welcome research, consulting and business collaboration enquiries.")

with st.expander("🌐 Connect With Us"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Website")
        st.write("https://yourwebsite.com")

    with c2:
        st.subheader("LinkedIn")
        st.write("linkedin.com/company/yourcompany")

    with c3:
        st.subheader("Email")
        st.write("info@yourcompany.com")

with st.expander("💼 Our Services"):

    c1,c2,c3=st.columns(3)

    with c1:
        st.subheader("Consulting")
        st.write("• AI Consulting")
        st.write("• ML Solutions")
        st.write("• Business Analytics")
        st.write("• Digital Transformation")

    with c2:
        st.subheader("Support")
        st.write("• Technical Support")
        st.write("• System Maintenance")
        st.write("• Platform Updates")
        st.write("• User Assistance")

    with c3:
        st.subheader("Training")
        st.write("• Corporate Training")
        st.write("• Workshops")
        st.write("• Live Demonstrations")
        st.write("• Project Mentoring")

with st.expander("🙏 Thank You"):

    st.write("""
Thank you for choosing TRUERIZE.

We appreciate your interest in our platform and look forward to supporting your Machine Learning journey.

Please feel free to contact us for technical assistance, project guidance, training or collaboration.
""")

    st.success("We look forward to working with you.")

show_footer()