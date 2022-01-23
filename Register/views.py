#Importaciones para creación de formulario y visualización
from django.shortcuts import render
from Register.forms import UserRegisterForm #Formulario creado
from django.contrib import messages

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'registrar/registro.html', context)