import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.title("Equity Research Tool")

st.sidebar.title("New Article URLs")
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)
process_url_clicked= st.sidebar.button("Process URLs")

main_placeholder = st.empty()
#Streamlit → /process_urls → FastAPI builds index
if process_url_clicked:
    urls = [url.strip() for url in urls if url and url.strip()]
    with st.spinner("Building index (loading URLs -> Splitting -> Embedding)..."):
        response = requests.post(
            f"{API_BASE}/process_urls",
            json={"urls":urls},
        )
        st.write(response.json())

query = main_placeholder.text_input("Question:")
if query:
    with st.spinner("Answering (retrieving context -> calling LLM)..."):
        response = requests.post(
            f"{API_BASE}/ask",
            json={"query":query}
        )
        st.write(response.json())