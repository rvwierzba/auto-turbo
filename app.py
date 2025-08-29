from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Configuração RÁPIDA da IA - já treinada, só usar!
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_email():
    try:
        data = request.json
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Digite algum texto primeiro!'})
        
        if len(text) < 10:
            return jsonify({'error': 'Texto muito curto! Mínimo 10 caracteres.'})
        
        # CLASSIFICAÇÃO RÁPIDA com IA
        result = classifier(text, candidate_labels=["produtivo", "improdutivo"])
        
        # RESPOSTAS AUTOMÁTicas inteligentes
        category = result['labels'][0]
        confidence = round(result['scores'][0] * 100, 1)
        
        if category == 'produtivo':
            response = "✅ Agradecemos seu contato. Nossa equipe já está analisando sua solicitação e retornará em breve. Caso número: #AUTO" + str(hash(text) % 1000)
        else:
            response = "🙏 Obrigado pelo seu email! Desejamos um ótimo dia e estamos à disposição para qualquer necessidade."
        
        return jsonify({
            'category': category,
            'confidence': confidence,
            'response': response
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro no processamento: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)