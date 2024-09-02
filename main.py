import json

# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA = SOMA + K

print(SOMA)
# o valor da varivel soma é 91

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
# um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou
# não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente
# definido no código;


def is_fibonacci(num):

    if num < 0: return "O número informado não pertence à sequência"

    a = 0
    b = 1

    if num == a | num == b: return "O número informado pertence à sequência";

    next = a + b

    while next <= num:
        if next == num: return "O número informado pertence à sequência"
        a = b
        b = next
        next = a + b

    return "O número informado não pertence à sequência"


print(is_fibonacci(34))


# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
# na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# > Não encontrei o json disponibilizado. Supus que os dados eram dessa maneira:
# [... {"dia": 18, "valor": 0.0} ...]


def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def calculate_data(data):
    # Filtra apenas os dias com faturamento maior que 0
    valores = [dia['valor'] for dia in data if dia['valor'] > 0]

    # Calcula o menor e o maior valor de faturamento
    menor_valor = min(valores)
    maior_valor = max(valores)

    # Calcula a média mensal considerando apenas dias com faturamento
    media_mensal = sum(valores) / len(valores)

    # Calcula o número de dias com faturamento acima da média mensal
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media


data = load_data('faturamento.json')

menor_valor, maior_valor, dias_acima_da_media = calculate_data(data)

print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
#
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve
# dentro do valor total mensal da distribuidora.  


faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_estados.values())

p_estados = {estado: (faturamento / faturamento_total) * 100 for estado, faturamento in faturamento_estados.items()}

for estado, percentual in p_estados.items():
    print(f"{estado}: {percentual:.2f}%")

#
# 5) Escreva um programa que inverta os caracteres de um string.
#
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser
# previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("String para inverter: ")

inverted_string = ""

for i in range(len(string) - 1, -1, -1):
    inverted_string += string[i]

print(f"String invertida: {inverted_string}")

