from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from contact.models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def contact(request):
    return render (request,'pages/contact.html')


def inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        

        contact = Contact(
        name=name, company=company, email=email, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        
        # Mail naar Firma
        mail_subject = 'U heeft een nieuw bericht.'
        message = render_to_string('pages/inquiryMailBert.html',{
            'name': name,
            'email': email,
            'phone':phone,
            'message':message
                    })
     
        send_email = EmailMessage(mail_subject,message,to=[admin_email])
        send_email.send()






        # Mail naar klant

        mail_subject = 'Prebert BV Danjewel!'
        message = render_to_string('pages/inquiryMailKlant.html',{
            'name': name,
            'email': email,
            'phone':phone,
            'message':message
                    })
     
        send_email = EmailMessage(mail_subject,message,to=[email])
        send_email.send()

        contact.save()
        return redirect('contact')