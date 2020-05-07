from django.shortcuts import render, redirect
from .models import Message
from django.contrib import messages

# Create your views here.
def message_submit(request):
    if request.method == "POST":
        name = request.POST.get("p_name")
        email = request.POST.get("p_email")
        phone = request.POST.get("p_phone")
        subject = request.POST.get("p_subject")
        content = request.POST.get("p_content")

        message = Message(name=name, email=email, phone=phone, subject=subject, content=content)
        message.save()

        messages.success(request, 'Mesajınız başarıyla alınmıştır. Ekibimiz en kısa sürede size dönüş yapacaktır')
        return redirect("index")