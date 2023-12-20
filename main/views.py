from django.shortcuts import render

def catalog(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User_name: {name}, phone: {phone}, message: {message}')

    return render(request, 'main/contacts.html')

