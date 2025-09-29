# e (and)=>somente é verdadeiro se ambos forem verdadeiros
# ou (or) => somente é falso quando ambos forem falsos
# se então => somente é falso se a primeira opção for verdadeira e a segunda for falso caso isso não ocorrer é verdadeiro
# se e somente se =>somente é verdadeiro se ambas forem iguais


saldo =1000
saque = 250
limite = 200
conta_especial = True

expre=saldo>=saque and saque<=limite or conta_especial and saldo>=saque
print(expre)

expre_2=(saldo>=saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expre_2)