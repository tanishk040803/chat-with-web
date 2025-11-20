# src/app.py
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_KEY"

# Helper function 
def get_vectorstore_from_url(url):
    # Load website content
    loader = WebBaseLoader(url)
    docs = loader.load()

    # Split content into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(docs)

    # Use OpenAI embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    # Build FAISS vectorstore
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

# Streamlit Frontend. 
st.set_page_config(page_title="Chat with Website", page_icon="🤖")
st.title("Chat with Website")

# Sidebar for URL input
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL", "https://example.com")  # default small site

# Build vectorstore if URL is provided
if website_url:
    with st.spinner("Processing website..."):
        st.session_state.vectorstore = get_vectorstore_from_url(website_url)
        st.success("Vectorstore built successfully!")

# ---------------------- Chat Functionality ----------------------
if website_url and "vectorstore" in st.session_state:
    # Set up retriever
    retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
    
    # LLM for answering questions
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        retriever=retriever,
        return_source_documents=True
    )

    # User input
    user_query = st.chat_input("Ask something about the website...")
    if user_query:
        with st.spinner("Generating answer..."):
            response = qa_chain.run(user_query)
            st.chat_message("assistant").write(response)