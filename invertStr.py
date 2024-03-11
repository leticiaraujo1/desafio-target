# Escreva um programa que inverta os caracteres de um string.

my_str = input('digite a string a ser invertida:')

def inverter(str):
    new_str = []
    for i in str:
        new_str.insert(0,i)
    
    return ''.join(new_str)
    
print(inverter(my_str))