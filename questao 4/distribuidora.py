fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

fat_tot = sum(fat.values())

porcent = {}
for e, v in fat.items():
    p = (v / fat_tot) * 100
    porcent[e] = p

for e, p in porcent.items():
    print(f"{e}: {p:.2f}%")
