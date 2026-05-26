nome_missao = "Titan Research Mission"
nome_equipe = "Equipe Titan"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

def analisar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", 1

    elif valor <= 30:
        return "NORMAL", 0

    elif valor <= 35:
        return "ATENÇÃO", 1

    else:
        return "CRÍTICO", 2

def analisar_comunicacao(valor):

    if valor < 30:
        return "CRÍTICO", 2

    elif valor <= 59:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0

def analisar_bateria(valor):

    if valor < 20:
        return "CRÍTICO", 2

    elif valor <= 49:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0

def analisar_oxigenio(valor):

    if valor < 80:
        return "CRÍTICO", 2

    elif valor <= 89:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0

def analisar_estabilidade(valor):

    if valor < 40:
        return "CRÍTICO", 2

    elif valor <= 69:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0

def classificar_ciclo(risco):

    if risco <= 2:
        return "MISSÃO ESTÁVEL"

    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"

def analisar_tendencia(primeiro, ultimo):

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."

    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável."

def gerar_recomendacao(risco):

    if risco <= 2:
        return "Manter operação normal e continuar monitoramento."

    elif risco <= 5:
        return "Monitorar sistemas em atenção."

    else:
        return "Ativar plano de contingência imediatamente."

riscos_ciclos = []

pontuacao_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print("Missão:", nome_missao)
print("Equipe:", nome_equipe)
print("Quantidade de ciclos:", len(dados_missao))

print("=" * 60)

for i in range(len(dados_missao)):

    ciclo = dados_missao[i]

    print("\nCICLO", i + 1)
    print("-" * 60)

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    status_temp, risco_temp = analisar_temperatura(temperatura)

    status_com, risco_com = analisar_comunicacao(comunicacao)

    status_bat, risco_bat = analisar_bateria(bateria)

    status_oxi, risco_oxi = analisar_oxigenio(oxigenio)

    status_est, risco_est = analisar_estabilidade(estabilidade)

    risco_total = risco_temp + risco_com + risco_bat + risco_oxi + risco_est

    riscos_ciclos.append(risco_total)

    pontuacao_areas[0] += risco_temp
    pontuacao_areas[1] += risco_com
    pontuacao_areas[2] += risco_bat
    pontuacao_areas[3] += risco_oxi
    pontuacao_areas[4] += risco_est

    classificacao = classificar_ciclo(risco_total)

    print("Temperatura:", temperatura, "°C |", status_temp)

    print("Comunicação:", comunicacao, "% |", status_com)

    print("Bateria:", bateria, "% |", status_bat)

    print("Oxigênio:", oxigenio, "% |", status_oxi)

    print("Estabilidade:", estabilidade, "% |", status_est)

    print("\nPontuação de risco:", risco_total)

    print("Classificação:", classificacao)

    recomendacao = gerar_recomendacao(risco_total)

    print("Recomendação:", recomendacao)

print("\n" + "=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

for ciclo in dados_missao:

    soma_temp += ciclo[0]
    soma_com += ciclo[1]
    soma_bat += ciclo[2]
    soma_oxi += ciclo[3]
    soma_est += ciclo[4]

media_temp = soma_temp / len(dados_missao)
media_com = soma_com / len(dados_missao)
media_bat = soma_bat / len(dados_missao)
media_oxi = soma_oxi / len(dados_missao)
media_est = soma_est / len(dados_missao)

print("Média temperatura:", round(media_temp, 2), "°C")
print("Média comunicação:", round(media_com, 2), "%")
print("Média bateria:", round(media_bat, 2), "%")
print("Média oxigênio:", round(media_oxi, 2), "%")
print("Média estabilidade:", round(media_est, 2), "%")

maior_risco = max(riscos_ciclos)

ciclo_critico = riscos_ciclos.index(maior_risco) + 1

print("\nCiclo mais crítico: Ciclo", ciclo_critico)

print("Maior pontuação de risco:", maior_risco)

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

print("Risco médio da missão:", round(risco_medio, 2))

quantidade_criticos = 0

for risco in riscos_ciclos:

    if risco >= 6:
        quantidade_criticos += 1

print("Quantidade de ciclos críticos:", quantidade_criticos)

tendencia = analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
)

print("\nTendência da missão:")

print(tendencia)

maior_pontuacao = max(pontuacao_areas)

indice_area = pontuacao_areas.index(maior_pontuacao)

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):

    print(
        areas_monitoradas[i],
        "-",
        pontuacao_areas[i],
        "pontos"
    )

print("\nÁrea mais afetada:")

print(areas_monitoradas[indice_area])

classificacao_final = classificar_ciclo(round(risco_medio))

print("\nClassificação final:")

print(classificacao_final)

print("\nConclusão:")

print(
    "A missão apresentou instabilidades durante a operação."
)