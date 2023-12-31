from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages

from .models import (
    About, Summary, Quote,
    Client, FunFact, Education,
    Experience, Sertificate, CodingLanguage,
    Contact, UserLetter
)
from .forms import UserLetterForm

def index(request):
    about = About.objects.last()
    summaries = Summary.objects.all()
    quotes = Quote.objects.filter(is_active=True)
    clients = Client.objects.all()
    fun_facts = FunFact.objects.first()
    context = {
        'section': 'about',
        'about': about,
        'summaries': summaries,
        'quotes': quotes,
        'clients': clients,
        'fun_facts': fun_facts,
        
    }
    return render(request, 'main/index.html', context)

def resume(request):
    education = Education.objects.all()
    experiece = Experience.objects.all()
    sertificates = Sertificate.objects.filter(is_active=True)
    coding_languages = CodingLanguage.objects.filter(is_active=True)
    context = {
        'section': 'resume',
        'education': education,
        'experiece': experiece,
        'sertificates': sertificates,
        'coding_languages': coding_languages
    }
    return render(request, 'main/resume.html', context)


def contact(request):
    contact = Contact.objects.first()
    form = UserLetterForm()
    if request.method == 'POST':
        form = UserLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully. We will contact you soon")
        else:
            messages.error(request, "There was an error sending the message.\nPlease check that all fields are filled in correctly and try again!")
    context = {
        'section': 'contact',
        'contact': contact,
        'form': form

    }
    return render(request, 'main/contact.html', context)


def page_not_found(request, exception):
    return render(request, '404.html', {})