##Надо написать функцию choose_coffee

resept = {
    "Эспрессо": [1, 0, 0],
    "Капучино": [1, 3, 0],
    "Маккиато": [2, 1, 0],
    "Кофе по-венски": [1, 0, 2],
    "Латте Маккиато": [1, 2, 1],
    "Кон Панна": [1, 0, 1],
}

def choose_coffee(*args):
    global ingredients
    for x in args:
        need = resept[x]
        if ingredients[0] - need[0] >= 0 and ingredients[1] - need[1] >= 0 and ingredients[2] - need[2] >= 0:
            ingredients[0] -= need[0]
            ingredients[1] -= need[1]
            ingredients[2] -= need[2]
            return x
    else:
        return "К сожалению, не можем предложить Вам напиток"


def encrypt_caesar(msg, shift):
    a = shift
    b = msg
    result = ''
    for i in b:
        if i == ' ' or i == '–' or i == '!' or i == ',' or i == '.' or i == '_' or i == '—':
            result += i
    else:
        c = ord('А') if i.isupper() else ord('а')
    result += chr((ord(i) + a - c) % 32 + c)
    return result


def decrypt_caesar(msg, shift):
    a = shift
    b = msg
    result = ''
    for i in b:
        if i == ' ' or i == '–' or i == '!' or i == ',' or i == '.' or i == '_' or i == '—':
            result += i
    else:
        c = ord('А') if i.isupper() else ord('а')
    result += chr((ord(i) - a - c) % 32 + c)
    return result

msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)


