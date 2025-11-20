Chat With Website

Short Description: A simple Streamlit app that lets you chat with any website by scraping its content, generating OpenAI embeddings, storing them in FAISS, and answering questions using GPT models. (Streamlit + OpenAI + FAISS)

This project allows you to chat with any website using OpenAI embeddings, FAISS vector search, and a Streamlit UI.

You simply:
	1.	Enter any website URL
	2.	Enter your OpenAI API key
	3.	Ask questions about the website

The app automatically:
	•	Scrapes the website
	•	Splits the text into chunks
	•	Generates embeddings using OpenAI
	•	Stores vectors in FAISS
	•	Uses a RetrievalQA chain to answer your questions

⸻

🚀 Features
	•	Chat with any website
	•	Automatic web scraping
	•	OpenAI embeddings (text-embedding-3-large)
	•	Fast semantic search using FAISS
	•	Chat-based question answering using gpt-3.5-turbo
	•	Streamlit-based clean UI
	•	Simple to deploy
	•	Only requirement for user: Enter their OpenAI API key

⸻

📁 Project Structure

CHAT-WITH-WEBSITE/
│
├── src/
│   └── app.py            # Main Streamlit application
│
├── .venv/                # Virtual environment
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


⸻

🔧 Setup Instructions

1. Clone the repository

git clone https://github.com/your-username/CHAT-WITH-WEBSITE.git
cd CHAT-WITH-WEBSITE

2. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
# OR
.venv\\Scripts\\activate   # Windows

3. Install dependencies

pip install -r requirements.txt

4. Add OpenAI API key (User Input)

Users don’t need to edit the code — they’ll simply enter their API key inside the app.

But if you want to set it manually:

export OPENAI_API_KEY="your_key_here"

5. Run the app

streamlit run src/app.py


⸻

🔐 How API Key Handling Works

Users only need to enter their API key inside the app UI.

No purchase required.
No code changes required.
No .env file required.

This makes the GitHub version 100% safe to publish.

⸻

📦 Deployment

You can deploy this on:
	•	Streamlit Cloud (recommended)
	•	Render.com
	•	Railway
	•	Heroku

Deploy on Streamlit Cloud
	1.	Push repo to GitHub
	2.	Go to: https://share.streamlit.io
	3.	Connect your repo
	4.	Add OPENAI_API_KEY in Secrets
	5.	Deploy!

⸻

📘 Example Usage
	1.	Open the app
	2.	Paste a website URL (e.g., https://example.com)
	3.	Enter your OpenAI API key
	4.	Ask questions like:
	•	“What is this website about?”
	•	“Summarize the main content.”

⸻

📝 Requirements

streamlit
langchain
openai
faiss-cpu
beautifulsoup4
requests


⸻

🤝 Contributing

Pull requests are welcome.

⸻

📄 License

MIT License

⸻

⭐ If you like this project

Give the repo a star on GitHub!

⸻

📬 Support

If you need help, open an issue on GitHub or message me.
