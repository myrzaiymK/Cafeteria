from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Category


def get_home(request):
    return render(request, 'index.html')


def get_about(request):
    return render(request, 'about.html')


def get_service(request):
    return render(request, 'service.html')


def get_menu(request):
    category = Category.objects.all()
    return render(request, 'menu.html', {'categories': category})


def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, template_name='contact.html', context=context)
