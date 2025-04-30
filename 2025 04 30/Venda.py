valorvenda = float(input('Digite o valor da venda (R$):'))
percentual = float(input('Informe a comissão (%)......:'))

comissão = valorvenda * percentual / 100

print(f'O valor da comissão é R$ {comissão:.2f}')