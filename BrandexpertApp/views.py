from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from .gspread import G_sheet
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        new_contact = Contact(name=name, email=email, phone=phone, source="Main_page")
        new_contact.save()
        # Add to sheet
        G_sheet(name,email,phone,"Main Page")
        # send an email
        send_mail(
            subject=f'new submit - brandexpert',
            message=f'Name: {name}\nemail:{email}\nphone: {phone}\nsource: Main-Page',
            from_email=email,
            recipient_list=['sales@brandexpertlojistik.com'],
            fail_silently = False  
        )
        return redirect(success)  
    else:
        new_contact = ContactForm()
    template = "main/index.html"
    return render(request, template)

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        new_contact = Contact(name=name, email=email, phone=phone ,source="Form_page")
        new_contact.save()
        # Add to sheet
        G_sheet(name,email,phone,"Form Page")
        # send an email
        send_mail(
            subject=f'new submit - brandexpert',
            message=f'Name: {name}\nemail: {email}\nphone: {phone}\nsource: Form-Page',
            from_email=email,
            recipient_list=['sales@brandexpertlojistik.com'],  
        )
        return redirect(success)  
    else:
        new_contact = ContactForm()
    template = "main/form.html"
    return render(request, template)
    
def success(request):
    template = "main/success.html"
    return render(request, template)

