from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#pip install chatterbot==1.0.4
# Cria o chatbot
chatbot = ChatBot('MeuBot')

# Treina o chatbot com dados de exemplo
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")

# Função de interação com o chatbot
def conversar():
    print("Digite 'sair' para encerrar a conversa.")
    while True:
        entrada_usuario = input("Você: ")
        if entrada_usuario.lower() == 'sair':
            break
        resposta = chatbot.get_response(entrada_usuario)
        print(f"Bot: {resposta}")

# Inicia a interação com o chatbot
conversar()