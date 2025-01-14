def reverse(s):
    ent = ''
    for i in range(len(s)-1, -1, -1):
        ent += s[i]
    return ent


ent_string = input("Digite a string: ")


result = reverse(ent_string)
print(f"Você escreveu: {ent_string}\nQue invertido fica: {result}")
