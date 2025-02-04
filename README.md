# AI-Powered-Chatbot-
Here's a **beautifully formatted README.md** file for your **GitHub repository** showcasing your **therapeutic chatbot "Dizzy"**:

---

🧘‍♀️ Dizzy - Your Virtual Therapeutic Assistant 🤖❤️  

Welcome to **Dizzy**, a compassionate **AI-powered therapeutic assistant** designed to provide **empathetic and supportive conversations** to users experiencing distress, trauma, or anxiety.  

Dizzy listens, responds with validation, and gently guides users through their thoughts without **judgment or unsolicited advice**.  

---

🌟 Features  

🎙️ Voice Interaction  
- Uses **speech recognition** (Google Speech API) to allow users to **speak** instead of typing.  
- Responds with **text-to-speech (TTS)** using `pyttsx3`.  

🧠 AI-Powered Conversations  
- Built with **Google Gemini AI (LangChain)** to ensure **context-aware and emotionally intelligent** responses.  
- Uses **memory buffer** to maintain the flow of conversation.  

### 🔍 Smart Web Search  
- Uses **DuckDuckGo Search API** to fetch **helpful mental health resources** upon request.  

### 📜 Ethical Guidelines  
- **Validates emotions** (e.g., “It’s okay to feel this way.”).  
- **Offers gentle encouragement** (e.g., “Take your time.”).  
- **Provides resources upon request.**  
- 🚫 **Avoids medical diagnoses, assumptions, and triggering topics**.  

---

## 🛠️ Tech Stack  

| Technology  | Purpose  |
|-------------|----------|
| **Python** | Core backend logic  |
| **Flask** | API Framework  |
| **LangChain** | AI conversation handling  |
| **Google Gemini AI** | AI-powered responses  |
| **SpeechRecognition** | Converts speech to text  |
| **pyttsx3** | Converts AI responses to speech  |
| **DuckDuckGo API** | Fetches external mental health resources  |
| **BeautifulSoup** | Web scraping for search results  |

---

## 🚀 Installation & Setup  

1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/dizzy-therapeutic-chatbot.git
cd dizzy-therapeutic-chatbot
```

2️⃣ Install Dependencies  
Ensure you have **Python 3.8+** installed.  
```bash
pip install -r requirements.txt
```

3️⃣ Set Up Environment Variables  
Create a `.env` file and add your **Google API Key**:  
```
GOOGLE_API_KEY=your_api_key_here
```

 4️⃣ Run the Application  
```bash
python app.py
```

---

🎤 How to Use  

1️⃣ Start the chatbot - it will **greet you and ask how you’re feeling**.  
2️⃣ **Speak** or **type** your thoughts.  
3️⃣ Dizzy will **listen**, respond **empathetically**, and offer **gentle support**.  
4️⃣ If needed, ask Dizzy to **search** for resources online.  
5️⃣ **Exit anytime** by saying `"quit"` or `"exit"`.  

---

💡 Example Conversation  

```
👤 User: I'm feeling overwhelmed.  
🤖 Dizzy: It's okay to feel this way. I'm here for you. Want to talk about it?  

👤 User: I just feel like I can't do anything right.  
🤖 Dizzy: That sounds really tough. But I want you to know that you're doing your best, and that counts.  

👤 User: Can you find resources on dealing with anxiety?  
🤖 Dizzy: Of course! Let me look that up for you...  
    📌 [Title: Managing Anxiety - Mental Health Guide](https://example.com)  
```

---

## Why Dizzy?  
Dizzy was built to provide **a safe, warm, and non-judgmental space** for users to express themselves. Whether you need a **gentle reminder** or a **mental health resource**, Dizzy is here for you.  

> _“Your feelings are valid. You are not alone.”_ 💙  

---

## 🏗️ Future Enhancements  
✅ Integrate **OpenAI GPT for enhanced responses**.  
✅ Add **multi-language support**.  
✅ Develop a **mobile-friendly UI**.  

---

## 📜 License  
This project is licensed under the **MIT License**. 

---

👩‍💻 **Developed by**:Kolluri Sruthi (https://github.com/your-username)  
🌐 **GitHub Repo**: AI Powered Bot ()

🚀 _Let's build **AI with empathy**!
