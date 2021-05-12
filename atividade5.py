dia = int(input("Que dia é hoje ?"))
mes = int(input("De que mês ? Use apenas números"))
ano = int(input("De qual ano ?"))
print("Tudo bem, agoras vamos escolher a data futura")
diaf = int(input("Qual o dia ?"))
mesf = int(input("De que mês ?"))
anof = int(input("De qual ano ?"))

anoV = anof-ano
# if mes>mesf: mesV= mes-mesf
mesV = mesf-mes

if dia > diaf : diaV = dia-diaf
else: diaV = diaf-dia



DiasFaltam = anoV*365 + mesV*30 + diaV

print("Faltam",DiasFaltam,"dias")
