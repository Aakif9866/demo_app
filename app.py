import streamlit as st
import json

st.set_page_config(page_title="Email Productivity Agent", layout="wide")

st.title("📧 Email Productivity Agent (Demo Mode)")
st.write("This is a demo-ready version of the Email Agent frontend. It runs without a backend and always generates clean, positive outputs.")


st.sidebar.header("Prompt Brain")

categorization_prompt = st.sidebar.text_area(
    "Categorization Prompt",
    value="Categorize the email into Important, To-Do, Newsletter, Spam, or Social."
)

action_prompt = st.sidebar.text_area(
    "Action Item Prompt",
    value="Extract important tasks from the email and return them as a JSON list."
)

reply_prompt = st.sidebar.text_area(
    "Auto-Reply Prompt",
    value="Write a polite, professional reply to the email."
)

if st.sidebar.button("💾 Save Prompts"):
    st.sidebar.success("Prompts saved successfully (demo mode).")



st.subheader("📬 Emails (Demo Mock Inbox)")

emails = {
    "Urgent Bug Report": "Hi team,\nWe found a critical bug in the login page. Please fix ASAP.\nThanks.",
    "Meeting Request": "Hello,\nCan we schedule a meeting tomorrow to discuss the project timeline?\nRegards.",
    "Newsletter": "Top tech stories of the week: AI breakthroughs, cloud updates..."
}

selected_email = st.selectbox("Select an email:", list(emails.keys()))

st.write("### Email Content:")
st.code(emails[selected_email])



st.subheader("⚡ Process Email")

if st.button("Run Processing"):
    st.success("Email processed successfully (demo mode).")


    st.json({
        "category": "Important",
        "reason": "Contains key information that needs attention."
    })

   
    st.json({
        "tasks": [
            {"task": "Review the email", "deadline": None},
            {"task": "Take required action", "deadline": None}
        ]
    })



st.subheader("💬 Email Agent")

query = st.text_input("Ask something about this email:")

if st.button("Ask Agent"):
    st.success("Agent response generated successfully (demo mode).")

    st.json({
        "summary": "This email contains important information requiring your attention.",
        "action_required": "yes",
        "reply": "Hi, thanks for the update. I'll take care of it immediately."
    })



st.subheader("📝 Drafts")

if st.button("Save Draft"):
    st.success("Draft saved successfully (demo mode).")

