# 1. Olá, Mundo!
print("Olá, mundo!")

# 2. Entrada de Nome
nome = input("Qual seu nome? ")
print(f"Seja bem-vindo(a), {nome}!")

# 3. Soma de dois números
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
print(f"A soma desses dois números é {soma}.")

# 4. Maior de dois números
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 > n2:
    print(f"{n1} é o maior.")
elif n2 > n1:
    print(f"{n2} é o maior.")
else:
    print("Os números digitados são iguais.")

# 5. Conversor de Temperatura
celsius = float(input("Digite a temperatura atual em Celsius (°C): "))
fahrenheit = (celsius * 9/5) + 32
print(f"Sua temperatura em Fahrenheit é {fahrenheit}°F.")

# 6. Calculadora de Média (3 notas)
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
nota3 = float(input("Digite sua nota 3: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")

# 7. Verificador de idade
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

# 8. Mensagem Personalizada
nome = input("Qual seu nome? ")
cor = input("Qual sua cor favorita? ")
print(f"Olá {nome}, sua cor favorita é {cor}!")

# 8 (parte 2). Dobro e Triplo
numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
print(f"Dobro: {dobro}\nTriplo: {triplo}")

# 9. Conversor de Metros para Centímetros e Milímetros
metro = float(input("Digite uma quantidade em metros: "))
centimetros = metro * 100
milimetros = metro * 1000
print(f"Centímetros: {centimetros}\nMilímetros: {milimetros}")

# 10. Conversor de Moeda
real = float(input("Digite um valor em reais para converter para dólar: "))
dolar = real / 5.0
print(f"Você tem {dolar:.2f} dólares.")

# 11. Ano de Nascimento
idade = int(input("Digite sua idade: "))
ano_nascimento = 2025 - idade
print(f"Você nasceu em {ano_nascimento}.")

# 13. Verificador de Nota
nota = float(input("Digite sua nota de 0 a 10: "))
if nota >= 7:
    print("Boa.")
elif nota < 5:
    print("Insuficiente.")

# 14. Soma de 3 números
soma3 = 0
for i in range(3):
    num3 = int(input("Digite um número: "))
    soma3 += num3
print(f"A soma dos números: {soma3}.")

# 15. Saudação Simples
nome = input("Qual seu nome: ")
cidade = input("Onde você mora: ")
print(f"Olá {nome}, você mora em {cidade}!")

# 16. Quadrado e Raiz
numeroR = float(input("Digite um número: "))
quadrado = numeroR ** 2
raiz = numeroR ** 0.5
print(f"O quadrado é {quadrado} e a raiz quadrada é {raiz}.")

# 17. Cálculo de Idade (2030)
ano_nascimento = int(input("Digite seu ano de nascimento: "))
anos = 2030 - ano_nascimento
print(f"Você terá {anos} anos em 2030.")

# 18. Classificação de Idade
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade incorreta")

# 19. Produto de 3 números
multiplicacao = 1
for i in range(3):
    numero = int(input("Digite um número: "))
    multiplicacao *= numero
print(f"A multiplicação dos números: {multiplicacao}.")

# 20. Calculadora de Média (2 notas)
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aprovado.")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Reprovado.")

# 21. Par ou Ímpar
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("Ele é par")
else:
    print("Ele é ímpar")

# 22. Cálculo de Desconto
preco = float(input("Preço original do produto: R$ "))
desconto_pct = float(input("Percentual de desconto (%): "))
valor_desconto = preco * (desconto_pct / 100)
preco_final = preco - valor_desconto
print(f"Desconto: R$ {valor_desconto:.2f} | Preço final: R$ {preco_final:.2f}")

# 23. Calculadora de Área de Retângulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
print(f"A área do retângulo é {area}.")

# 24. Contador de Caracteres
texto = input("Digite uma palavra ou frase: ")
print(f"O texto possui {len(texto)} caracteres.")

# 25. Tabuada Simples
num_tab = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num_tab} x {i} = {num_tab * i}")

# 26. Conversor de Tempo
minutos_totais = int(input("Digite o tempo em minutos: "))
horas = minutos_totais // 60
minutos = minutos_totais % 60
print(f"{horas} horas e {minutos} minutos")

# 27. Verificador de Número Positivo/Negativo
n = float(input("Digite um número: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Zero")

# 28. Cálculo de IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura * altura)
print(f"Seu IMC é {imc:.2f}")

# 29. Repetidor de Palavras
palavra = input("Digite uma palavra: ")
vezes = int(input("Quantas vezes deseja repetir? "))
for i in range(vezes):
    print(palavra)

# 30. Verificador de Triângulo
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo.")

