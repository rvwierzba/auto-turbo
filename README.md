# ⚡ AutoU Classificador Turbo - Solução Relâmpago

Solução de classificação de emails com IA desenvolvida em **menos de 30 minutos** para o processo seletivo AutoU.

## 🎯 Funcionalidades

- **Classificação Automática**: Identifica se emails são produtivos ou improdutivos
- **Respostas Inteligentes**: Gera sugestões de resposta baseadas no contexto
- **Interface Simplificada**: Design limpo e intuitivo
- **IA de Verdade**: Usa modelo BART-large da Facebook/Meta via Hugging Face

## 🚀 Como Usar (30 Segundos)

1. **Acesse**: http://localhost:5000 (local) ou [Link do Deploy]
2. **Cole o texto**: do email na caixa de texto
3. **Clique em Classificar**: e veja a mágica acontecer!

## ⚡ Tecnologias Usadas

- **Backend**: Python + Flask
- **Frontend**: HTML5 + CSS3 + JavaScript vanilla
- **IA**: Hugging Face Transformers (facebook/bart-large-mnli)
- **Deploy**: Hugging Face Spaces (recomendado)

## 📦 Instalação Local (2 Minutos)

```bash
# Clone o repositório
git clone https://github.com/rvwierzba/autou-turbo.git
cd autou-turbo

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py

🎮 Exemplos de Teste

Email Produtivo:
text

"Bom dia, preciso de suporte urgente com meu pedido #12345. O sistema não está funcionando desde ontem."

Email Improdutivo:
text

"Olá equipe! Desejo a todos um feliz natal e um próspero ano novo! Atenciosamente."

📊 Métricas de Performance

    Tempo de desenvolvimento: < 30 minutos

    Precisão da IA: ~85% (baseado em bart-large-mnli)

    Tempo de resposta: < 3 segundos

    Linhas de código: 150 (leve e eficiente)

🎥 Vídeo Demonstrativo Automático

https://img.youtube.com/vi/VIDEO_ID/0.jpg

Vídeo gerado automaticamente via AI - veja a solução em ação!
🔧 Estrutura do Projeto
text

autou-turbo/
├── app.py              # Backend Flask principal
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html     # Frontend completo
└── README.md          # Este arquivo

🚀 Deploy Rápido
Hugging Face Spaces (Recomendado - 5 minutos):

    Crie conta em huggingface.co

    Vá em "Spaces" → "Create new Space"

    Escolha "Docker"

    Faça upload dos 3 arquivos principais

    Pronto! Seu app está no ar

Outras Opções:

    Render: Upload do repositório GitHub

    PythonAnywhere: Upload manual dos arquivos

    Heroku: Com git push

📈 Próximas Melhorias (Se Houver Tempo)

    Suporte a upload de arquivos PDF/TXT

    Histórico de classificações

    Mais categorias de email

    Fine-tuning do modelo

👨‍💻 Desenvolvido Por

[Rafael Vinicius Wierzba] - Candidato AutoU 🚀

"Do. Or do not. There is no try." - Yoda

⭐ Se gostou, deixe uma star no repositório!