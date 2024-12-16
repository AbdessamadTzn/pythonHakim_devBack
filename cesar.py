import string


# Cesar encrypt

alphabet = string.printable + "éèêàôëùïü"       # For French

def cesar_encrypt(message, n):
    ans = ""

    for char in message:
        if char in alphabet :

            #get index of our char in the alphabet
            idx_of_char = alphabet.index(char)      
            new_idx_of_char = (idx_of_char+n)%len(alphabet)
            ans += alphabet[new_idx_of_char]

    return ans

def cesar_decrypt(message, n):
    return cesar_encrypt(message, -n)

def brute_force_cesar(crypted_message):
    for key in range(len(alphabet)):
        print(cesar_decrypt(crypted_message, key))
        print("_"*16, "\n")

'''

print(cesar_encrypt("Hi encrypt an decrypt me!", 13)) #Output UvïrApELCGïnAïqrpELCGïzr.
encrypted_message = cesar_encrypt("Hi encrypt an decrypt me!", 13)
print(cesar_decrypt(encrypted_message, 13)) #Output Hi encrypt an decrypt me!

'''

brute_force_cesar("UvïrApELCGïnAïqrpELCGïzr.")      #Should find in Output: Hi encrypt an decrypt me!



