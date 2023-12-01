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

# stagno imports

import mimetypes
import os

import cv2
from django.conf import settings as django_settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.defaults import page_not_found, server_error

from FSSApp.LSBSteg import LSBSteg






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

        elif algo_valu == 'Vigenère cipher':

            if radio_value=='yes':
                key=key_value
            else:
                key=123
            decryption_key = key
            def generate_repeated_key(plaintext, key):
                key = list(key)
                if len(plaintext) == len(key):
                    return key
                else:
                    for i in range(len(plaintext) - len(key)):
                        key.append(key[i % len(key)])
                    return key

            def encryption_algo(plaintext, key):
                ciphertext = []
                for i in range(len(plaintext)):
                    if plaintext[i].isalpha():
                        encrypted_char = (ord(plaintext[i].upper()) + ord(key[i].upper())) % 26 + ord('A')
                        ciphertext.append(chr(encrypted_char))
                    else:
                        ciphertext.append(plaintext[i])
                return "".join(ciphertext)

            

            print("20012021049_harshil Raval")
            plain_input = input_value

            key = generate_repeated_key(plain_input, key)
            enc_text = encryption_algo(plain_input, key)

            decryption_key = generate_repeated_key(enc_text, decryption_key)
            print("Encrypted text ->", enc_text)
            output_value=enc_text

            print("Enter key to decrypt")

            print("------------------------------------------------------------------")

                
            
            


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
        
        elif algo_valu == 'Vigenère cipher':
            # plain_input = input("Enter text to Encryption: ") 
            # k = input("Enter Private Key`  : ")   
            print("20012021049_harshil Raval")
            def generateKey(string, key):  
                key = list(key)     
                if len(string) == len(key):          
                    return(key)     
                else:  
                    for i in range(len(string) -len(key)):  
                        key.append(key[i % len(key)])     
                return("" . join(key))  
            
            # k= generateKey(plain_input,k)  
            
            
            def decryption_algo(cipher, key):
                plaintext = [] 
                for i in range(len(cipher)): 
                    if cipher[i].isalpha():
                        plain_input = (ord(cipher[i].upper()) - ord(key[i].upper()) + 26)%26 
                        plain_input += ord('a') 
                        plaintext.append(chr(plain_input))
                    else:
                        plaintext.append(cipher[i])
                return("" . join(plaintext))
            
            enc_text = input_value
            print("Encrypted text -> ", enc_text)
            
            print("Enter key to decrypt") 
            
            print("------------------------------------------------------------------")
            
            key=  key_value
            key = generateKey(enc_text,key)
            if key == k:
                dec_text= decryption_algo(enc_text,key)
                print("Decrypted text: ", dec_text) 
                output_value=dec_text
            else:
                print("Incorrect key...Try again")


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




def stagno(request):
    # encoding part
    if request.method == 'POST' and 'enc_apply' in request.POST:
        content = request.FILES['enc_c_file'].read()
        file = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'encryptsourceimage.png'), 'wb+')
        file.write(content)
        # text encoding
        if request.POST['enc_selectchoice'] == 'enc_text':
            steg = LSBSteg(cv2.imread(file.name))
            processed_text = request.POST['enc_steg_text']
            processed_text = processed_text.replace(' ', '_')
            img_encoded = steg.encode_text(processed_text)
            # path = str('../media/' + {user.username} + '_steg.png')
            BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = 'steg_image.png'
            filepath = BASEDIR + '/media/' + filename
            cv2.imwrite(filepath, img_encoded)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            # Return the response value
            return response

        # image encoding
        if request.POST['enc_selectchoice'] == 'enc_image':
            content = request.FILES['enc_c_img'].read()
            imgfile = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'encryptstegimage.png'), 'wb+')
            imgfile.write(content)
            steg = LSBSteg(cv2.imread(file.name))
            # instead of encode image using encode binary
            data = open(imgfile.name, "rb").read()
            new_im = steg.encode_binary(data)
            # new_im = steg.encode_image(cv2.imread(imgfile.name))
            BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = 'steg_image.png'
            filepath = BASEDIR + '/media/' + filename
            cv2.imwrite(filepath, new_im)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        # binary encoding
        if request.POST['enc_selectchoice'] == 'enc_binary':
            content = request.FILES['enc_c_bfile'].read()
            binfile = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'encryptstegbinary.bin'), 'wb+')
            binfile.write(content)
            steg = LSBSteg(cv2.imread(file.name))
            # instead of encode image using encode binary
            data = open(binfile.name, "rb").read()
            new_bin = steg.encode_binary(data)
            # new_im = steg.encode_image(cv2.imread(imgfile.name))
            BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = 'steg_image.png'
            filepath = BASEDIR + '/media/' + filename
            cv2.imwrite(filepath, new_bin)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        return render(request, 'home/stagno.html')

    if request.method == 'POST' and 'dec_retrieve' in request.POST:
        print('dec')
        content = request.FILES['dec_c_file'].read()
        file = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'decryptsourceimage.png'), 'wb+')
        file.write(content)
        file.close()
        BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = f'decryptsourceimage.png'
        filepath = BASEDIR + '\\media\\' + filename
        print(filepath)
        # text decoding
        if request.POST['dec_selectchoice'] == 'dec_text':
            im = cv2.imread(filepath)
            steg = LSBSteg(im)
            dec_text = steg.decode_text()
            print(dec_text)
            dec_text = dec_text.replace('_', ' ')
            print(dec_text)
            return render(request, 'home/stagno.html', context={'dec_text': dec_text})

        # image decoding
        if request.POST['dec_selectchoice'] == 'dec_image':
            steg = LSBSteg(cv2.imread(filepath))
            binary = steg.decode_binary()
            filename = 'newimage.png'
            filepath = BASEDIR + '/media/' + filename
            with open(filepath, "wb+") as f:
                f.write(binary)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response

        # binary decoding
        if request.POST['dec_selectchoice'] == 'dec_binary':
            steg = LSBSteg(cv2.imread(filepath))
            binary = steg.decode_binary()
            filename = 'newbinary.bin'
            filepath = BASEDIR + '/media/' + filename
            with open(filepath, "wb+") as f:
                f.write(binary)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response

        return render(request, 'home/stagno.html')
    return render(request, 'home/stagno.html')
    