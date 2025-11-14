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




import re

def parse_num(s):

    if s is None:
        raise ValueError("Entrada vazia")

    s = s.strip()
    if s == "":
        raise ValueError("Entrada vazia")
    # remove espaços dentro (ex: "1 000,50")
    s = s.replace(" ", "")

    # aceita sinal
    sign = ""
    if s.startswith(("+", "-")):
        sign = s[0]
        s = s[1:]

    # só caracteres esperados
    if not re.match(r'^[0-9\.,]+$', s):
        raise ValueError(f"Formato inválido: {s}")

    has_comma = "," in s
    has_dot = "." in s

    if has_comma and has_dot:
        # ex: 1.234.567,89  -> remove pontos, troca vírgula por ponto
        s = s.replace(".", "")
        s = s.replace(",", ".")
    elif has_comma:
        # ex: 1500,6 -> 1500.6
        s = s.replace(",", ".")
    elif has_dot:
        # somente pontos
        parts = s.split(".")
        if len(parts) > 2:
            # muitos pontos: tratar como milhares exceto, possivelmente, o último
            # verificar última parte: se tem 3 dígitos -> provavelmente milhares
            if len(parts[-1]) == 3:
                # todos pontos são separadores de milhar -> remover todos
                s = "".join(parts)
            else:
                # tratar último como decimal, juntar os anteriores como milhares
                s = "".join(parts[:-1]) + "." + parts[-1]
        else:
            # exatamente um ponto
            left, right = parts[0], parts[1]
            if len(right) == 3 and len(left) <= 3:
                # ex: 5.444 -> muito provavelmente 5444 (ponto de milhar)
                s = left + right
            else:
                # ex: 5.44 -> decimal
                s = left + "." + right

    # recoloca sinal e converte
    s = sign + s
    return float(s)


def format_result(x):
    # se for inteiro dentro de uma tolerância, mostra sem casas
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    # remove zeros desnecessários
    text = f"{x:.10f}".rstrip("0").rstrip(".")
    return text


if __name__ == "__main__":
    while True:
        try:
            a_raw = input("Digite o primeiro número da multiplicação: ")
            b_raw = input("Digite o segundo número da multiplicação: ")

            a = parse_num(a_raw)
            b = parse_num(b_raw)

            resultado_multi = a * b

            print("Valores interpretados: ", a, "x", b)
            print("O resultado da multiplicação é:", format_result(resultado_multi))
            break

        except Exception as e:
            print("Aconteceu um erro:", e)
            traceback.print_exc()
            resposta_multi = input("\nDeseja tentar novamente? (s/n): ").strip().lower()
            if resposta_multi != "s":
                print("Programa encerrado. Até mais!")
                break
            else:
                print("\nReiniciando programa...")


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