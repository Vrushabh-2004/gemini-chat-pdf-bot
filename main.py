import streamlit as st
import os
from utils.gemini_chain import get_gemini_answer
from dotenv import load_dotenv

st.set_page_config(page_title="Chat with Your Notes", page_icon="📄")

st.title("📄 Chat with Your Notes (Gemini PDF Q&A Bot)")

load_dotenv()


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "query" not in st.session_state:
    st.session_state.query = ""
if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""

uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")
st.divider()

query = st.text_input("💬 Ask a question:", value=st.session_state.query)


detail = st.radio("🎯 How detailed should the answer be?", ["Brief", "Balanced", "Detailed"], index=1)


max_pages = st.slider("📄 Number of pages to analyze", 1, 100, 5)

if uploaded_file and query:
    pdf_path = os.path.join("data", uploaded_file.name)
    os.makedirs("data", exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🤖 Thinking..."):
        answer = get_gemini_answer(pdf_path, query, detail_level=detail, max_pages=max_pages)

    st.markdown("### 🧠 Gemini Answer:")
    st.success(answer)

    st.session_state.chat_history.append((query, answer))
    st.session_state.last_answer = answer
    st.session_state.query = ""

    # Save Q&A log
    log_path = f"data/chatlog_{uploaded_file.name}.txt"
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"Q: {query}\nA: {answer}\n\n")

    with open(log_path, "rb") as f:
        st.download_button("📥 Download Q&A Log", f, file_name="chat_history.txt")

    # Follow-up input
    follow_up = st.text_input("🔁 Not satisfied or want to ask a follow-up question?", key="followup_input")
    if follow_up:
        with st.spinner("🧠 Thinking deeper..."):
            refined_answer = get_gemini_answer(
                pdf_path,
                query=follow_up,
                detail_level=detail,
                max_pages=max_pages,
                context=st.session_state.last_answer
            )

        st.markdown("### 🔄 Follow-Up Answer:")
        st.success(refined_answer)
        st.session_state.chat_history.append((follow_up, refined_answer))
        st.session_state.last_answer = refined_answer


if uploaded_file and st.button("📌 Summarize the PDF"):
    with st.spinner("📝 Summarizing PDF..."):
        summary = get_gemini_answer(pdf_path, "Summarize this PDF in simple bullet points.", max_pages=max_pages)
    st.markdown("### 📌 Summary:")
    st.info(summary)

