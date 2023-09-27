from django.shortcuts import render, redirect
from .forms import SignupForm  # Import your SignUpForm or relevant form

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def auth_view(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)

            # Redirect to a different view or URL after successful login
            return redirect('profile')  # Replace 'profile' with your desired view name or URL pattern

        else:
            # Authentication failed, return an error message or handle it as needed
            return render(request, 'login.html', {'error_message': 'Authentication failed'})

    # Handle GET request or other cases
    return render(request, 'login.html')

def login_view(request):
    # Your view logic here
    return render(request, 'authentication/login.html') 