# chat_g4f_routes.py
from flask import Blueprint, render_template, request
import g4f

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    reply = ''
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        try:
            reply = g4f.ChatCompletion.create(
                model=g4f.models.default,
                provider=g4f.Provider.You,
                messages=[{"role": "user", "content": prompt}]
            )
        except Exception as e:
            reply = f"Error: {str(e)}"
    return render_template('chat.html', reply=reply)
