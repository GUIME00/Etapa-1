# * Coleta informações sobre sua rotina de estudos;
# * Sugere um **cronograma básico personalizado**;
# * Identifica os conteúdos que você mais tem dificuldade;
# * Faz recomendações automáticas de foco de estudo.

### 🧠 Exemplo de Programa: "Assistente de Estudo com IA Simples"
import random

# Simula uma IA simples com base em perguntas e análise de dados do usuário

def recomendar_estudo(topicos_dificeis):
    dicas = {
        "matemática": "Use vídeos do YouTube sobre resolução de problemas e prática com simulados.",
        "física": "Concentre-se em resolver exercícios passo a passo com apoio de simuladores.",
        "história": "Revise com mapas mentais e linha do tempo visual.",
        "biologia": "Use flashcards e resumos com esquemas ilustrativos.",
        "português": "Pratique interpretação de texto e gramática com exercícios diários.",
        "inglês": "Use apps como Duolingo ou leia pequenos textos com tradução."
    }
    print("\n📌 Recomendações baseadas nas suas dificuldades:")
    for topico in topicos_dificeis:
        if topico in dicas:
            print(f"- {topico.capitalize()}: {dicas[topico]}")
        else:
            print(f"- {topico.capitalize()}: Busque materiais complementares e grupos de discussão.")

def gerar_cronograma(dias_disponiveis, tempo_por_dia, topicos):
    cronograma = {}
    dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    dias_escolhidos = dias_semana[:dias_disponiveis]
    
    for i, dia in enumerate(dias_escolhidos):
        cronograma[dia] = {
            "tempo": tempo_por_dia,
            "tema": random.choice(topicos)
        }
    
    return cronograma

# Início da interação
print("📚 Bem-vindo(a) ao Assistente Inteligente de Estudos!\n")

nome = input("Digite seu nome: ")
dias = int(input("Quantos dias por semana você pode estudar? (1 a 7): "))
tempo = int(input("Quantos minutos por dia você pode estudar? "))
materias = input("Quais são suas principais matérias? (separe por vírgula): ").lower().split(',')

topicos_dificeis = input("Quais matérias você tem mais dificuldade? (separe por vírgula): ").lower().split(',')

# Geração do cronograma
cronograma = gerar_cronograma(dias, tempo, materias)

print(f"\n✅ {nome}, aqui está seu cronograma básico de estudos:")
for dia, info in cronograma.items():
    print(f"- {dia.capitalize()}: Estudar {info['tema'].strip()} por {info['tempo']} minutos")

# Recomendações baseadas em dificuldade
recomendar_estudo([topico.strip() for topico in topicos_dificeis])

###  O que esse programa faz:

# * **Recebe dados personalizados do usuário**
# * **Gera um plano de estudo leve, mas direcionado**
# * **Dá recomendações específicas para as matérias mais difíceis**
# * **Simula uma lógica simples de IA baseada em regras**