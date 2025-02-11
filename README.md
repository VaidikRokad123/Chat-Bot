# 🛍️ Personalized Shopping Suggester Chatbot

## 🚀 Overview
The **Personalized Shopping Suggester Chatbot** is an AI-powered recommendation system that provides tailored product suggestions based on user preferences. It uses **Flask** for the backend, **Google's Generative AI (Gemini-Pro)** for content generation, and **HTML, CSS, and JavaScript** for the frontend, ensuring an interactive and user-friendly experience.

## ✨ Features
- 🤖 **AI-Powered Recommendations** – Utilizes Google's AI API to generate personalized shopping suggestions.
- 📝 **Structured Response Formatting** – Formats chatbot replies into readable paragraphs.
- 💬 **Interactive UI** – Real-time message display with a typing indicator.
- ⚡ **Efficient Backend API** – Flask handles user requests and response formatting.
- 🛑 **Error Handling** – Provides fallback messages for failed API responses.
- 🔗 **Scalability** – Can be integrated with e-commerce platforms or expanded for multiple product categories.

## 🛠️ Technologies Used
- **Backend:** Flask, Google Generative AI API
- **Frontend:** HTML, CSS, JavaScript
- **API Handling:** Flask with JSON-based requests and responses

## 🏗️ Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/VaidikRokad123/Chat-Bot.git
   cd Chat-Bot
   ```
2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **🔑 Configure Google API Key:**
   - Replace `YOUR_GOOGLE_API_KEY` in `app.py` with your actual Google Generative AI API key.

## ▶️ Usage
1. **Run the Flask App:**
   ```bash
   python app.py
   ```
2. **🌍 Open the Web Interface:**
   - Visit `http://127.0.0.1:5000/` in your browser.
3. **💡 Chat with the Bot:**
   - Enter your shopping preferences and receive AI-generated recommendations.

## 📁 Project Structure
```
shopping-suggester-chatbot/
│── app.py  # Flask backend
│── templates/
│   └── index.html  # Frontend UI
│── static/
│   └── styles.css  # Styling
│── requirements.txt  # Project dependencies
│── README.md  # Project documentation
```

## 🔮 Future Enhancements
- 🎙️ Add **voice-based input** for user interaction.
- 🛒 Integrate **real-time e-commerce data** for product recommendations.
- 🌎 Expand support for **multiple languages**.
  
---
### 👥 Contributors
- **[Vaidk Rokad]** – Developer
- 💡 Open for contributions! Feel free to submit pull requests.
