divida = int(input())
aluguel = int(input())
pagamento = 0

while divida > 0:
    pagamento += 1
    print(f'pagamento: {pagamento}')
    print(f'antes = {divida}')
    if aluguel < divida:
        divida -= aluguel
    else:
        divida = 0 
    print(f'depois = {divida}')   
    print('-' * 5)  
