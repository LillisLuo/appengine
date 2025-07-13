from flask import Blueprint, render_template, request
from g4f import ChatCompletion, Provider  # 更明确导入

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    reply = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        try:
            response = ChatCompletion.create(
                model="gpt-3.5-turbo",
                provider=Provider.You,  # ✅ 指定 Provider，避免被 Cloudflare 拦截
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response
        except Exception as e:
            reply = f"Error: {e}"
    return render_template('chat.html', reply=reply)
