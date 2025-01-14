import json

with open('C:/Users/João Victor/Documents/Target/questão 3/vet.json', 'r') as f:
    dados_faturamento = json.load(f)

fat_valido = [d["valor"]
              for d in dados_faturamento["faturamento"] if d["valor"] > 0]

fat_min = min(fat_valido)
fat_max = max(fat_valido)

fat_media = sum(fat_valido) / len(fat_valido)

fat_acima_media = len([valor for valor in fat_valido if valor > fat_media])

print(f"Faturamento minimo: {fat_min}")
print(f"Faturamento maximo: {fat_max}")
print(f"Faturamento media: {fat_media:.2f}")
print(f"Faturamento acima da media: {fat_acima_media}")
