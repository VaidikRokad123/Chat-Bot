from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Initialize Google API (Replace with your API key)
genai.configure(api_key="AIzaSyCUv3sCbii6iwEzWNuKhVvX3CPh68zEJOc")

# Load the model (Gemini or any other model you're using)
model = genai.GenerativeModel("gemini-pro")  # Change model name if needed

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        user_message = "Suggest the best products based on the following user preference: " +  user_message

        response = model.generate_content(user_message)  # Correct method
        bot_reply = response.text if response.text else "I didn't understand that."
        #bot_reply = bot_reply.replace('**', '\n\n').replace('* ', '\n')
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
