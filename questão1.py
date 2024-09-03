def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def check_fibonacci(n):
    sequence = fibonacci_sequence(n)
    if n in sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
resultado = check_fibonacci(numero)
print(resultado)