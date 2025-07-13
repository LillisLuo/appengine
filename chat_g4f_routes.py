from g4f.client import Client
import g4f

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    replies = {}
    if request.method == 'POST':
        prompt = request.form['prompt']
        models = {
            'gpt-4o': g4f.models.gpt_4o,
            'claude-3.5-sonnet': g4f.models.claude_3_5_sonnet,
            'llama-3': g4f.models.llama_3,
        }
        for name, model in models.items():
            try:
                response = g4f.ChatCompletion.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}]
                )
                replies[name] = response
            except Exception as e:
                replies[name] = f"Error: {e}"
    return render_template('chat.html', replies=replies)
