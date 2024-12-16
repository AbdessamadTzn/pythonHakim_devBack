import string
import cesar


def convert_password_to_list_of_keys(password):
    list_of_keys = []
    for char in password:
        list_of_keys.append(cesar.alphabet.index(char))
    
    return list_of_keys

def vigenere_encrypt(message, password, reverse=True):
    ans = ""
    list_of_keys = convert_password_to_list_of_keys(password)

    for idx, char in enumerate(list_of_keys):
        current_key = list_of_keys[idx % len(list_of_keys)]

        ans += cesar.cesar_decrypt(char, current_key) if reverse else cesar.cesar_decrypt(char, current_key)


        return ans


print(vigenere_encrypt("UvïrApELCGïnAïqrpELCGïzr.", "13"))

