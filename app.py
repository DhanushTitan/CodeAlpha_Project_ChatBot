from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you! How can I assist you today?",]
    ],
    [
        r"what is your name?",
        ["I am a Dhanush's chatbot.",]
    ],
    [
        r"how are you?",
        ["I am doing well, thank you!", "I'm fine, how can I assist you?",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you. What do you need assistance with?",]
    ],
    [
        r"quit",
        ["Goodbye, have a great day!",]
    ],
    [
        r"where are you from?",
        ["I am a virtual assistant, so I don't have a physical location.",]
    ],
    [
        r"what can you do?",
        ["I can help answer questions, provide information, or just chat with you.",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"how can I contact support?",
        ["You can contact support by emailing support@example.com.",]
    ],

]



chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["user_message"]
    bot_response = chatbot.respond(user_message)
    return {"user_message": user_message, "bot_response": bot_response}

if __name__ == "__main__":
    nltk.download("punkt")  
    app.run(debug=True)
