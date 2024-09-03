def verificar_letra_a(string):
    # Converte a string para minúscula para contar 'a' e 'A' igualmente
    string_min = string.lower()
    
    # Conta quantas vezes a letra 'a' aparece
    quantidade_a = string_min.count('a')
    
    # Verifica se a letra 'a' aparece na string
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")
        
# Exemplo de uso
string_teste = "Aprender a programar é essencial!"
verificar_letra_a(string_teste)
