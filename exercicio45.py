while True:
    num = int(input("Digite um número maior que zero: "))
    if num > 0:
        break
    print("Valor inválido! Tente novamente.")

binario = True
for d in str(num):
    if d != "0" and d != "1":
        binario = False
        break

if binario:
    print("O número é binario")
else:
    print("O número não é binario")
