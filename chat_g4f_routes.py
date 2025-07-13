from flask import Blueprint, request, render_template
from g4f.client import Client
import g4f

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    reply = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        model_name = "gpt-4o"
        model_ref = g4f.models.gpt_4o
        try:
            client = Client()
            response = client.chat.completions.create(
                model=model_ref,
                messages=[{"role": "user", "content": prompt}]
            )
            reply = f"[{model_name} 回复]: {response.choices[0].message.content}"
        except Exception as e:
            reply = f"[{model_name} 错误]: {e}"
    return render_template('chat.html', reply=reply)
