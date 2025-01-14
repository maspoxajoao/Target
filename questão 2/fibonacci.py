# Código da questão 2
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False


n = int(input("Digite um número: "))
print(f"voce digitou o numero: {n}")

if fibonacci(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
