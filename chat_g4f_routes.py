from g4f.client import Client
import g4f

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    reply = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        try:
            client = Client()
            reply = client.chat.completions.create(
                model=g4f.models.gpt_4o,
                messages=[{"role": "user", "content": prompt}]
            ).choices[0].message.content
        except Exception as e:
            reply = f"Error: {e}"
    
    return render_template('chat.html', reply=reply)
