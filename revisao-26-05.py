# 1. Declare 3 variáveis representando nome, idade e nota de um aluno. Depois, exiba esses dados com print.
# 2. Crie expressões utilizando operadores aritméticos e relacionais.
# 3. Peça uma nota e diga se o aluno foi aprovado (nota ≥ 6).
# 4. Imprima os números de 1 a 10 usando um laço for.
# 5. Crie uma função que receba dois números e retorne a soma.
# 6. Peça ao usuário seu nome e idade e exiba em uma frase formatada.
# 7. Crie uma lista com 5 frutas e imprima a segunda e a última fruta.
# 8. Crie uma matriz 3x3 com números de 1 a 9 e imprima todos os elementos da diagonal principal.
# 9. Peça um número ao usuário e use try/except para impedir erro caso ele digite texto.
# 10. Peça para o usuário inserir uma frase e a modifique com pelo menos 3 métodos de string
# 11. Use um while para pedir um número maior que zero. Se o número for negativo, use continue para pedir de novo.
# 12. Crie um código com dois for que imprimam a tabuada de 1 a 5.
# 13. Use range para imprimir os múltiplos de 3 entre 0 e 30.
# 14. Crie uma tupla com os dias da semana e mostre a terça-feira.
# 15. Peça uma idade e use uma operação ternária para dizer se é maior de idade.
# 16. Crie uma função com dois parâmetros: nome e curso. Ela deve imprimir uma saudação.
# 17. Altere a função anterior para que, ao invés de print, ela retorne a saudação.
# 18. Crie um programa que cadastre nome, idade e curso de um aluno em um dicionário. A chave será o nome do aluno, o valor será outro dicionário com idadae e nota final. Exiba nome, idade e nota de cada aluno


# 1. Declare 3 variáveis representando nome, idade e nota de um aluno. Depois, exiba esses dados com print.
# nome = "João Victor dos Santos Moura"
# idade = 17
# nota = 99
# print (nome, idade, nota)


# 2. Crie expressões utilizando operadores aritméticos e relacionais.
# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Digite o segundo numero: "))
# mult = (num1 * num2)
# print(mult)


# 3. Peça uma nota e diga se o aluno foi aprovado (nota ≥ 6).
# nota = float (input("Digite a nota do aluno: "))
# if nota >= 6:
#     print("Aluno aprovado.")
# else:
#     print("Aluno Reprovado.")


# 4. Imprima os números de 1 a 10 usando um laço for.
# for i in range(1, 11, 1):
#     print(i)


# 5. Crie uma função que receba dois números e retorne a soma.
# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Digite o segundo numero: "))
# soma = (num1 + num2)
# print(soma)


# 6. Peça ao usuário seu nome e idade e exiba em uma frase formatada.
# nome = str(input("Digite seu nome: "))
# idade = int(input("Digite sua idade: "))
# print(f"Parabéns {nome} você tem {idade} anos, e foi cadastrado com sucesso.")


# 7. Crie uma lista com 5 frutas e imprima a segunda e a última fruta.
# frutinhas = ["Pequi", "Kiwi", "Ciriguela", "Bergamota", "Jaca"]
# print(f"{frutinhas[1]}, {frutinhas[-1]}")


# 8. Crie uma matriz 3x3 com números de 1 a 9 e imprima todos os elementos da diagonal principal.
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(f"{matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")


# 9. Peça um número ao usuário e use try/except para impedir erro caso ele digite texto.
# try:
#     num = int(input("Digite um numero: "))
# except ValueError:
#     print("Digite somente numero.")


# 10. Peça para o usuário inserir uma frase e a modifique com pelo menos 3 métodos de string
# frase = input("Digite uma frase motivadora: ")
# print(frase.upper())
# print(frase.lower())
# print(frase.split())


# 11. Use um while para pedir um número maior que zero. Se o número for negativo, use continue para pedir de novo.
# while True:
#     i = int(input("Digite um numero: "))
#     if i < 0:
#         print("Numeros negativos são invalidos, digite um novo numero.")
#         continue
#     else:
#         print("Numero cadastrado com sucesso.")
#         break


# 12. Crie um código com dois for que imprimam a tabuada de 1 a 5.
# for a in range(1,6):
#     for b in range(1, 11):
#         total = a * b
#         print(f"{a} * {b} = {total}")


# 13. Use range para imprimir os múltiplos de 3 entre 0 e 30.
# for i in range(3,31,3):
#     print(i)


# 14. Crie uma tupla com os dias da semana e mostre a terça-feira.
# dias = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado")
# print(dias[2])


# 15. Peça uma idade e use uma operação ternária para dizer se é maior de idade.
# idade = int(input("Digite sua idade: "))
# maior_menor = "Você é maior de idade." if idade > 17 else "Você é menor de idade."
# print(maior_menor)


# 16. Crie uma função com dois parâmetros: nome e curso. Ela deve imprimir uma saudação.
# def cadastro():
#     nome = str(input("Digite seu nome: "))
#     curso = input("Digite o curso que deseja: ")
#     print(f"Tudo certo {nome} ! Cadastrado no curso de {curso} com sucesso.")
# cadastro()


# 17. Altere a função anterior para que, ao invés de print, ela retorne a saudação.
# def cadastro():
#     nome = str(input("Digite seu nome: "))
#     curso = input("Digite o curso que deseja: ")
#     return print(f"Tudo certo {nome} ! Cadastrado no curso de {curso} com sucesso.")
# cadastro() 


# 18. Crie um programa que cadastre nome, idade e curso de um aluno em um dicionário. A chave será o nome do aluno, o valor será outro dicionário com idadae e nota final. Exiba nome, idade e nota de cada aluno
# alunos = {}
# aluno = []
# nome = str(input("Digite seu nome: "))
# alunos[nome] = {}
# alunos[nome]["idade"] = int(input("Digite sua idade: "))
# alunos[nome]["nota"] = input("Digite a nota final: ")
# aluno.append(alunos)
# print(aluno)