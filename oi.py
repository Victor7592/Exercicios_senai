from colorama import init,Fore

init(autoreset=True)

nome = input ('nome do aluno: ')
nota_1 = float(input ('digite a primeira nota: ' ) ) 
nota_2 = float(input ('digite a segunda nota: ' ) ) 
nota_3 = float(input ('digite a terceira nota: ' ) )
media = (nota_1+nota_2+nota_3) / 3 
media = round ((nota_1+nota_2+nota_3) /3, 2)
print ('aluno', nome,'\nMédia: ', media)
if media >=5:
    print(Fore.GREEN + 'aluno aprovado')
else:
    print(Fore.RED + 'aluno reprovado')