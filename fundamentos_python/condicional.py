MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade"))

if idade >= MAIOR_IDADE:
    print("Maior idade,pode tirar CNH.")
    
if idade < MAIOR_IDADE:
    print("Não pode tirar CNH.")    


if idade >= MAIOR_IDADE:
    print("Maior idade,pode tirar CNH.")
else:
    print("Não pode tirar a CNH")
    
    
if idade >= MAIOR_IDADE:
    print("Maior idade,pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode apenas fazer o curso teorico não pode fazer o pratico")
else:
    print("Não pode tirar a CNH")