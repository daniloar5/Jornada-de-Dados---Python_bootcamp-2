import traceback
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_1 = float(input("Por favor insira o primeiro número para soma: "))
# numero_2 = float(input("Por favor insira o segundo número para a soma: "))
# resultado = numero_1 + numero_2

# if resultado.is_integer():
#     print(f"A soma dos dois números é {int(resultado)}")
# else:
#     print(f"A soma dos dois números é {resultado}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.



# while True:
#     try:
#         resto_1 = float(input("Por favor insira um número para o cálculo de resto 5: "))
#         resultado_resto_1 = resto_1 % 5

#         if resultado_resto_1.is_integer():
#             print(f"O resto da conta é: {int(resultado_resto_1)}")
#             break
#         else:
#             print(f"{resultado_resto_1:.2f}")
#             break

#     except Exception as e:
#         print("Ocorreu um erro:")
#         traceback.print_exc()

#         resposta= input("\nDeseja tentar novamente? (s/n): ").strip().lower()

#         if resposta != "s":
#             print("Programa encerrado. Até mais!")
#             break
#         else:
#             print("\nReiniciando programa")



# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.



while True:
    try:
        multi_1 = float(input("Digite o primeiro número da multplicação: "))
        multi_2 = float(input("Digite o segundo número da multplicação: "))
        resultado_multi = multi_1 * multi_2

        if resultado_multi.is_integer():
            print(f"O resultado da multiplicação é: {int(resultado_multi)}")
            break
        else:
            print(f"O resultado da multiplicação é: {resultado_multi}")
            break
    except:
        print("Aconteceu um erro: ")
        traceback.print_exc()

        resposta_multi= input("\nDeseja tentar novamente? (s/n): ").strip().lower()

        if resposta_multi != "s":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("\nReiniciando programa")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação