from django.shortcuts import render, redirect
from .models import Message
from attorney.models import Attorney
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def message_submit(request):
    if request.method == "POST":
        name = request.POST.get("p_name")
        email = request.POST.get("p_email")
        phone = request.POST.get("p_phone")
        subject = request.POST.get("p_subject")
        content = request.POST.get("p_content")

        message = Message(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            content=content
        )
        message.save()

        mail = f" İsim: {name} \n Email: {email} \n Telefon: {phone} \n Konu: {subject} \n Mesaj:{content}"
        to = Attorney.objects.exclude(email=None).values('email')
        
        to_list = []
        for item in to:
            to_list.append(item.get('email'))
        
        print(to_list)
        

        send_mail(
            'Web Site Bildirimleri',
            mail,
            settings.EMAIL_HOST_USER,
            to_list,
            fail_silently=False,
        )
        messages.success(request,'Mesajınız başarıyla alınmıştır.\
            Ekibimiz en kısa sürede sizinle iletişime geçecektir.')
        return redirect("contact")
