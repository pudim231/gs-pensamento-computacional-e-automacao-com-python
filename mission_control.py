nome_missao = "Osiris Test omega"
nome_equipe = "Equipe Osiris"

dados_missao = [
    [21, 98, 95, 97, 94],
    [24, 89, 90, 95, 88],
    [32, 74, 81, 93, 79],
    [35, 60, 47, 89, 67],
    [40, 27, 15, 77, 34],
    [31, 66, 54, 86, 73]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


# FUNÇÕES DE ANÁLISE

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
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
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


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def gerar_recomendacao(temp, com, bat, oxi, est):
    recomendacoes = []

    if temp == "CRÍTICO":
        recomendacoes.append(
            "Verificar controle térmico da missão"
        )

    if com == "CRÍTICO":
        recomendacoes.append(
            "Restabelecer comunicação com a base"
        )

    if bat == "CRÍTICO":
        recomendacoes.append(
            "Ativar modo de economia de energia"
        )

    if oxi == "CRÍTICO":
        recomendacoes.append(
            "Acionar protocolo de suporte à vida"
        )

    if est == "CRÍTICO":
        recomendacoes.append(
            "Reduzir operações não essenciais"
        )

    if not recomendacoes:
        return "Manter operação normal e continuar monitoramento."

    return "; ".join(recomendacoes)


def identificar_area_mais_afetada(pontos_areas):
    maior = max(pontos_areas)
    indice = pontos_areas.index(maior)

    return areas_monitoradas[indice], maior


# PROCESSAMENTO DA MISSÃO

riscos_ciclos = []
pontos_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao):

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    status_temp, pontos_temp = analisar_temperatura(temperatura)
    status_com, pontos_com = analisar_comunicacao(comunicacao)
    status_bat, pontos_bat = analisar_bateria(bateria)
    status_oxi, pontos_oxi = analisar_oxigenio(oxigenio)
    status_est, pontos_est = analisar_estabilidade(estabilidade)

    risco_total = (
        pontos_temp +
        pontos_com +
        pontos_bat +
        pontos_oxi +
        pontos_est
    )

    riscos_ciclos.append(risco_total)

    pontos_areas[0] += pontos_temp
    pontos_areas[1] += pontos_com
    pontos_areas[2] += pontos_bat
    pontos_areas[3] += pontos_oxi
    pontos_areas[4] += pontos_est

    classificacao = classificar_ciclo(risco_total)

    recomendacao = gerar_recomendacao(
        status_temp,
        status_com,
        status_bat,
        status_oxi,
        status_est
    )

    print(f"\nCICLO {i+1}")
    print("-" * 60)

    print(f"Temperatura: {temperatura}°C | {status_temp}")
    print(f"Comunicação: {comunicacao}% | {status_com}")
    print(f"Bateria: {bateria}% | {status_bat}")
    print(f"Oxigênio: {oxigenio}% | {status_oxi}")
    print(f"Estabilidade: {estabilidade}% | {status_est}")

    print(f"Pontuação de risco: {risco_total}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")


# Relatório final


media_temp = sum(linha[0] for linha in dados_missao) / len(dados_missao)
media_com = sum(linha[1] for linha in dados_missao) / len(dados_missao)
media_bat = sum(linha[2] for linha in dados_missao) / len(dados_missao)
media_oxi = sum(linha[3] for linha in dados_missao) / len(dados_missao)
media_est = sum(linha[4] for linha in dados_missao) / len(dados_missao)

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

ciclos_criticos = 0

for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

tendencia = analisar_tendencia(riscos_ciclos)

area_mais_afetada, pontos = identificar_area_mais_afetada(
    pontos_areas
)

print("\n")
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print(f"Média de temperatura: {media_temp:.2f} °C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")

print(f"Ciclo mais crítico: {ciclo_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")

print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

print("\nTendência da missão:")
print(tendencia)

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontos_areas[i]} pontos")

print(f"\nÁrea mais afetada: {area_mais_afetada}")

classificacao_final = classificar_ciclo(round(risco_medio))

print(f"\nClassificação final da missão:")
print(classificacao_final)

print("\nConclusão:")

if risco_medio <= 2:
    print("A missão permaneceu estável durante toda a operação.")
elif risco_medio <= 5:
    print("A missão apresentou situações de atenção que exigem monitoramento.")
else:
    print("A missão apresentou falhas críticas e requer ações corretivas imediatas.")

print("=" * 60)