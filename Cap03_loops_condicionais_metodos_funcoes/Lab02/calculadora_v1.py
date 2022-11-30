# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n\n")

print("Selecione o número da operação desejada: \n\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n")

opcao = int(input("Digite sua opção (1/2/3/4): "))

if opcao == 1: #Soma
    primeiro_valor = float(input("Digite o primeiro número: "))
    segundo_valor = float(input("Digite o segundo número: "))
    resultado = primeiro_valor + segundo_valor
    print(str(primeiro_valor) +" + "+ str(segundo_valor) + " = " + str(resultado) )

elif opcao == 2: #Subtração
    primeiro_valor = float(input("Digite o primeiro número: "))
    segundo_valor = float(input("Digite o segundo número: "))
    resultado = primeiro_valor - segundo_valor
    print(str(primeiro_valor) +" - "+ str(segundo_valor) + " = " + str(resultado) )

elif opcao == 3: #Multiplicação
    primeiro_valor = float(input("Digite o primeiro número: "))
    segundo_valor = float(input("Digite o segundo número: "))
    resultado = primeiro_valor * segundo_valor
    print(str(primeiro_valor) +" * "+ str(segundo_valor) + " = " + str(resultado) )

elif opcao == 4: #Divisao
    primeiro_valor = float(input("Digite o primeiro número: "))
    segundo_valor = float(input("Digite o segundo número: "))
    resultado = primeiro_valor / segundo_valor
    print(str(primeiro_valor) +" / "+ str(segundo_valor) + " = " + str(resultado) )

else:
    print("Opção inválida")