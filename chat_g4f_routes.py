# from flask import Blueprint, render_template, request
# from g4f.client import Client

# chat_bp = Blueprint('chat_bp', __name__)
# client = Client()

# @chat_bp.route("/chat", methods=["GET", "POST"])
# def chat():
#     response = None
#     if request.method == "POST":
#         prompt = request.form.get("prompt", "").strip()
#         if prompt:
#             try:
#                 result = client.chat.completions.create(
#                     model="gpt-4o-mini",
#                     messages=[{"role": "user", "content": prompt}],
#                     web_search=False,
#                 )
#                 response = result.choices[0].message.content
#             except Exception as e:
#                 response = f"Error: {e}"
#     return render_template("chat.html", response=response)
