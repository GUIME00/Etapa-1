import matplotlib.pyplot as plt

desempenho = {}

def registrar_resultado():
    tema = input("Digite o tema (ex: Matemática - Funções): ").strip()
    resultado = input("Você acertou (A) ou errou (E)? ").strip().upper()

    if resultado not in ["A", "E"]:
        print("Entrada inválida. Use 'A' para acerto ou 'E' para erro.")
        return

    if tema not in desempenho:
        desempenho[tema] = {"acertos": 0, "erros": 0}

    if resultado == "A":
        desempenho[tema]["acertos"] += 1
    else:
        desempenho[tema]["erros"] += 1

def mostrar_prioridades():
    print("\n--- Prioridades de Estudo ---")

    # Calcular taxa de acerto
    prioridades = []
    for tema, dados in desempenho.items():
        total = dados["acertos"] + dados["erros"]
        if total == 0:
            taxa = 1.0
        else:
            taxa = dados["acertos"] / total
        prioridades.append((tema, taxa))


    prioridades.sort(key=lambda x: x[1])

    for tema, taxa in prioridades:
        total = desempenho[tema]["acertos"] + desempenho[tema]["erros"]
        porcentagem = round(taxa * 100)
        print(f"{tema} → {porcentagem}% de acerto ({total} tentativas)")

def mostrar_grafico():
    if not desempenho:
        print("Nenhum dado registrado ainda.")
        return

    temas = list(desempenho.keys())
    taxas = []
    for tema in temas:
        acertos = desempenho[tema]["acertos"]
        erros = desempenho[tema]["erros"]
        total = acertos + erros
        taxa = (acertos / total) * 100 if total > 0 else 100
        taxas.append(taxa)

    plt.figure(figsize=(10, len(temas) * 0.6))
    plt.barh(temas, taxas, color='skyblue')
    plt.xlabel("Taxa de Acerto (%)")
    plt.title("Desempenho por Tema")
    plt.xlim(0, 100)
    plt.tight_layout()
    plt.gca().invert_yaxis()  # Tema com menor acerto no topo
    plt.show()

# Loop principal
while True:
    print("\n[1] Registrar resultado\n[2] Ver prioridades\n[3] Ver gráfico\n[4] Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        registrar_resultado()
    elif escolha == "2":
        mostrar_prioridades()
    elif escolha == "3":
        mostrar_grafico()
    elif escolha == "4":
        print("Saindo... Bons estudos!")
        break
    else:
        print("Opção inválida.")



#         esse script faz:
 
# ajuda a organizar os estudos com base no desempenho real;
 
# mostra onde está indo bem e onde precisa melhorar;
 
# pode ser usado qualquer hora após resolver exercícios.