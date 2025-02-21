from flask import Flask, render_template, request, redirect, url_for, session
from modules.model_interface import query_model
from modules.response_generator import generate_response
from modules.memory_manager import MemoryManager
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session security
 
# Initialize Memory Manager
memory = MemoryManager()
 
@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []
 
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            # Query the AI model and get a response
            model_response = query_model(user_input)
            bot_response = generate_response(user_input, model_response)
            
            # Update session chat history
            chat_history = session["chat_history"]
            chat_history.append(("You", user_input))
            chat_history.append(("Bot", model_response))
            session["chat_history"] = chat_history
 
            # Optionally store in memory
            memory.add_to_memory(user_input, model_response)
            
        return redirect(url_for("index"))
 
    return render_template("index.html", chat_history=session["chat_history"])
 
if __name__ == '__main__':
 app.run(debug=True)
 