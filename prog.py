while True:  """essa linha irá fazer o comando reiniciar sem que precise ficar abrindo e fechando o programa"""

    operacao = input("Qual operação deseja realizar? +, -, *, / \n Para sair precione x")) """pergunta para o usuário qual a operação que deseja fazer"""
    
         if operacao == "x" or operacao == "X" """para fechar o programa utilizar o if para validar a informação e o break para fechar o programa, como tem um while ele irá reiniciar o código"""
            break
            
        elif operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/" """vai validar qual das operações irá realizar e caso não esteja correto irá constar como operação inválida"""
    
         else:
            print("Operação invalida!")
    
    num1 = float(intput("Digite o 1° número: " )) """variável para guardar a informação, poderia ser int ou float, sendo que int e um número inteiro (1 - 2 - 3)e float representa um número fracionado (3,55 - 4,75 - 9,63). Input para que o usuário possa inserir a informação"""
    
    num2 =float(intput("Digite o 1° número: " ))
    
        if operacao == "+" : """ valida se a conta é de soma, se sim irá somar a variável num1 e a num2, senão irá para a próxima e assim por diante """
    
            total = numb1+numb2 
            total"""irá retornar o valor total"""
    
       elif operacao == "-" :
            total = numb1-numb2
            total
    
       elif operacao == "*" :
            total = numb1*numb2
            total
    
       elif operacao == "/" :
            total = numb1/numb2
            total
