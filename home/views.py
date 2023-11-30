import random
from django.shortcuts import render,redirect

import string
# manually added content
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import numpy as np


# for the favourite functionlality added 
from .models import FavoriteItem
from users.models import Profile  # Import the Profile model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages


# for login revalidation on going one page back
from django.views.decorators.cache import cache_control

# from django.template.loader import render_to_string
# import os

# Create your views here.
def home(request):
    if request.method == 'POST':
        input_value = request.POST.get('input_field')
        radio_value = request.POST.get('customKeyOption')
        key_value=request.POST.get('customKey')
        algo_valu=request.POST.get('enc_selectchoice')
        # following is for favourite function as it stores the name of algorithm in session 
        request.session['selected_algorithm'] = algo_valu
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
        elif algo_valu == 'Hill cipher':
           # ENCRYPTION:
            import numpy as np
            import string
            import random

            def hill_cipher_encrypt(message, key):
                # Generate the alphabet
                alphabet = string.ascii_uppercase

                # Convert the message to uppercase
                message = message.upper()

                # Remove spaces from the message
                message = ''.join(message.split())

                # Pad the message with random characters if needed
                padding = len(message) % len(key)
                if padding > 0:
                    message += ''.join(random.choice(alphabet) for _ in range(len(key) - padding))

                # Encrypted message
                encrypted_message = ""

                # Group message in vectors and generate crypted message
                for index in range(0, len(message), len(key)):
                    vector = np.array([alphabet.index(char) for char in message[index:index+len(key)]])
                    encrypted_vector = np.dot(key, vector) % 26

                    for value in encrypted_vector:
                        encrypted_message += alphabet[value]

                return encrypted_message

            # Define variables
            key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Your key
            message = input_value  # Your message

            # Encrypt the message
            encrypted_message = hill_cipher_encrypt(message, key)

# Show the result

           # Show the result
            output_value = encrypted_message

        elif algo_valu == 'Railfence cipher':
            
            
            a = input_value
            depth =int(key_value)
            l = len(a)
            c = ""
                # Ciphering
            for i in range(depth):
                j = i
                while j < l:
                    c += a[j]
                    if i != 0 and i != depth - 1 and j + 2*(depth-i-1) < l:
                        c += a[j + 2*(depth-i-1)]
                    j += 2*(depth-1)
            print("\nCipher text after applying rail fence:")
                
            output_value=c
                
            
            


    # Encryption logic end
        return render(request, 'home/home.html', {'output': output_value})
    else:
        # Handle GET requests or other cases here
        return render(request, 'home/home.html')
    


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
        
# Hill Cipher decryption logic
        elif algo_valu == 'Hill cipher' :
                        
            # Decryption:
            import numpy as np
            from sympy import Matrix
            import string

            # Define variables
            dimension = 3 # Your N
            if radio_value=='yes':
                
                key=np.matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]]) # Your key
            else:
                key = np.matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]]) # Your key
            message = input_value # You message

            # Generate the alphabet
            alphabet = string.ascii_uppercase

            # Encrypted message
            decryptedMessage = ""

            # Get the decrypt key
            key = Matrix(key)
            key = key.inv_mod(26)
            key = key.tolist()

            # Group message in vectors and generate crypted message
            for index, i in enumerate(message):
                values = []
                # Create the N blocs
                if index % dimension == 0:
                    for j in range(0, dimension):
                        values.append([alphabet.index(message[index + j])])
                    # Create the vectors and work with them
                    vector = np.matrix(values)
                    vector = key * vector
                    vector %= 26
                    for j in range(0, dimension):
                        decryptedMessage += alphabet[vector.item(j)]


            # Show the result
            print(decryptedMessage)

            output_value = decryptedMessage


        elif algo_valu == 'Railfence cipher':
            c=input_value
            depth = int(key_value)
            l = len(c)

            # Deciphering
            if l % 2 == 0:
                k = l // 2
            else:
                k = (l // 2) + 1
            d = [""] * l
            index = 0
            for i in range(depth):
                j = i
                while j < l:
                    d[j] = c[index]
                    index += 1
                    if i != 0 and i != depth - 1 and j + 2*(depth-i-1) < l:
                        d[j + 2*(depth-i-1)] = c[index]
                        index += 1
                    j += 2*(depth-1)
            print("Text after decryption:")
            print("".join(d))
            output_value=d


    # Encryption logic end
        return render(request, 'home/decryption.html', {'output': output_value})
    else:
        # Handle GET requests or other cases here
        return render(request, 'home/decryption.html')
  


from django.contrib import messages

from django.contrib import messages

@login_required
@cache_control(max_age=0, no_cache=True, must_revalidate=True, no_store=True)
def save_to_favorites(request):
    if request.method == 'POST':
        text_to_save = request.POST.get('text_to_save')
        
        custom_key = request.POST.get('customKeyOption') == 'yes'

        if text_to_save:
            algo_valu=request.session.get('selected_algorithm')
            favorite_item = FavoriteItem(user=request.user, text=text_to_save, algorithm=algo_valu, custom_key=custom_key)
            favorite_item.save()
            
            # Create a message that includes the saved data
            message = f'Message "{text_to_save}" saved to favorites successfully.'

            messages.success(request, message)

    return redirect('home')

