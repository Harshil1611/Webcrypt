from django.shortcuts import render,redirect

import string
# manually added content
from django.http import HttpResponse
# from django.template.loader import render_to_string
# import os

# Create your views here.
def home(request):
    if request.method == 'POST':
        input_value = request.POST.get('input_field')
        radio_value = request.POST.get('customKeyOption')
        key_value=request.POST.get('customKey')
        algo_valu=request.POST.get('enc_selectchoice')
# Encryption logic
       
# Encryption logic of CEASER CIPHER
        if algo_valu=='Caeser cipher algo':
            Texttaken=input_value
            if radio_value =='yes':
                key=int(key_value)
            else:
                key=1
            def encrypt(Texttaken, key):
                ciphertext = ""
                for Character in Texttaken:
                    if Character.isalpha():  # Only encrypt alphabetic Characteracters
                        if Character.isupper():
                            ciphertext += chr((ord(Character) + key - 65) % 26 + 65)  # Encrypt uppercase letter
                        else:
                            ciphertext += chr((ord(Character) + key - 97) % 26 + 97)  # Encrypt lowercase letter
                    else:
                        ciphertext += Character  # Leave non-alphabetic Characteracters as they are
                print("Your Excrepted text is as below:-")
                return ciphertext


            def decrypt(ciphertext, key):
                """Decrypts the ciphertext using Caesar cipher algorithm."""
                Texttaken = ""
                for Character in ciphertext:
                    if Character.isalpha():  # Only decrypt alphabetic Characteracters
                        if Character.isupper():
                            Texttaken += chr((ord(Character) - key - 65) % 26 + 65)  # Decrypt uppercase letter
                        else:
                            Texttaken += chr((ord(Character) - key - 97) % 26 + 97)  # Decrypt lowercase letter
                    else:
                        Texttaken += Character
                print("Your Decrepted text is as below:-")
                return Texttaken
            

            
            ciphertext = encrypt(Texttaken, key)
            output_value=ciphertext 
        elif algo_valu == 'Mono alphabetic':
            plain_text = input_value
            if radio_value =='yes':
                key=key_value
            else:
                key=1
            alphabet = string.ascii_lowercase
            cipher_mapping = {}

            if len(key) == len(alphabet):
                for i in range(len(alphabet)):
                    cipher_mapping[alphabet[i]] = key[i]

                def encrypt(plain_text, key):
                    encrypted_text = ''

                    for char in plain_text:
                        if char in cipher_mapping:
                            encrypted_text += cipher_mapping[char]
                        else:
                            encrypted_text += char

                    return encrypted_text

                try:
                    ciphertext = encrypt(plain_text, key)
                    output_value = ciphertext
                except Exception as e:
                    output_value = f"Error: {str(e)}"
            else:
                output_value = "Error: Key length must be the same as the alphabet length"
 
            
# Encryption logic end
        return render(request, 'home.html', {'output': output_value})
    else:
        # Handle GET requests or other cases here
        return render(request, 'home.html')
    

def download(request):
    output = request.GET.get('output', '')

    # Prepare the response to download the file
    response = HttpResponse(content_type="text/plain")
    response["Content-Disposition"] = "attachment; filename=output.txt"
    response.write(output)

    return response


# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email =request.POST.get('email')
#         password =request.POST.get('password')

    
#     return render(request,'login.html')

def decryption(request):
    if request.method == 'POST':
        input_value = request.POST.get('input_field')
        radio_value = request.POST.get('customKeyOption')

        key_value=request.POST.get('customKey')
        algo_valu=request.POST.get('enc_selectchoice')
# Decryption logic
       
# Decryption logic of CEASER CIPHER
        if algo_valu =='Caeser cipher algo':
            ciphertext=input_value
            if radio_value =='yes':
                key=int(key_value)
            else:
                key=1
            def decrypt(ciphertext, key):
                """Decrypts the ciphertext using Caesar cipher algorithm."""
                Texttaken = ""
                for Character in ciphertext:
                    if Character.isalpha():  # Only decrypt alphabetic Characteracters
                        if Character.isupper():
                            Texttaken += chr((ord(Character) - key - 65) % 26 + 65)  # Decrypt uppercase letter
                        else:
                            Texttaken += chr((ord(Character) - key - 97) % 26 + 97)  # Decrypt lowercase letter
                    else:
                        Texttaken += Character
                print("Your Decrepted text is as below:-")
                return Texttaken
            

            
            ciphertext = decrypt(ciphertext, key)
            output_value=ciphertext 
# Decryption logic of MONO ALPHABETIC CIPHER
        elif algo_valu == 'Mono alphabetic':
            ciphertext = input_value
            if radio_value =='yes':
                key=int(key_value)
            else:
                key=1
            def decrypt(ciphertext, key):
                alphabet = string.ascii_lowercase
                cipher_mapping = {}

                if len(key) == len(alphabet):
                    for i in range(len(alphabet)):
                        cipher_mapping[key[i]] = alphabet[i]

                    decrypted_text = ''

                    for char in ciphertext:
                        if char in cipher_mapping:
                            decrypted_text += cipher_mapping[char]
                        else:
                            decrypted_text += char

                    return decrypted_text
                else:
                    return "Error: Key length must be the same as the alphabet length"

            # Example usage:

            output_value = decrypt(ciphertext, key)            
    # Encryption logic end
        return render(request, 'decryption.html', {'output': output_value})
    else:
        # Handle GET requests or other cases here
        return render(request, 'decryption.html')
    