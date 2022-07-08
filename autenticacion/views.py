from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class LoginView(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'autenticacion/register.html', {'form': form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, 'autenticacion/register.html', {'form': form})

def close_session(request):
    logout(request)
    return redirect('Home')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, "Failed to authenticate.")
                return render(request, 'autenticacion/login.html', {'form': form})
        else:
            messages.error(request, "Failed to authenticate.")
            return render(request, 'autenticacion/login.html', {'form': form})
    form=AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})




