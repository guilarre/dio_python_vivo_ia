import re

def validate_numero_telefone(phone_number):
    pattern = r"^[(]\d{2}[)]\s[9]\d{4}-\d{4}$"
    if re.match(pattern, phone_number):
        print("Número de telefone válido.")
    else:
        print("Número de telefone inválido.")

def main():
    phone_number = input()
    validate_numero_telefone(phone_number)

main()