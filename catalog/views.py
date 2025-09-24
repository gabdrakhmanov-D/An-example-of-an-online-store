from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        user_text = request.POST.get('user_text')
        print(name,user_text)
        return render(request, 'catalog/thanks.html')
    return render(request, 'catalog/contacts.html')