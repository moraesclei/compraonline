num = int(input("Digite o grau esférico do olho esquerdo: "))
num2 = int(input("Digite o grau esférico do olho direito: "))

nmPrime = "lente Prime"
primeEsf = -3
primeEsf1 = 0
primeEsf2 = -2
primeCilin = -12


nmVision = "lente Vision"
visionEsf = -15
visionCilindr = -5


if visionEsf < primeEsf:
    print("A lente que atenda o cliente é: ", nmVision)

if primeCilin > visionCilindr:
    print("A lente que atenda o cliente é: ", nmPrime)

if primeEsf1 > visionCilindr:
    print("A lente que atenda o cliente é: ", nmPrime)

if visionEsf > primeEsf:
    print("A lente que atenda o cliente é: ", nmVision)

if visionCilindr > primeEsf:
    print("A lente que atenda o cliente é: ", nmVision)
