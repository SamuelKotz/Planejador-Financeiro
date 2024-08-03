#Obtendo o valor do salário
salario = float(input("Qual o valor do seu salário? "))

#Dividindo o salário com base na regra dos 50% 30% 20%

porcentagem50 = (salario / 100) * 50
porcentagem30 = (salario / 100) * 30
porcentagem20 = (salario / 100) * 20

#Printando o salário de forma dividida

print("========================================\nSeus números de 50% e 30% e 20%\n=========================")
print(f"Necessidades: R$ {porcentagem50:.2f}")
print(f"Investimento: R$ {porcentagem30:.2f}")
print(f"Lazer/Utilizável: R$ {porcentagem20:.2f}")
