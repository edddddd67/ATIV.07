# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
p = float(input('preço'))
v = p*(21/100)
v2 = p+v
print(f'preço com imposto {v2}')
