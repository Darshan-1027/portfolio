from django.shortcuts import render,redirect
from .models import *
from .forms import Contactform
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    
    Profile = PhotoModel.objects.first()
    Details = NameModel.objects.first()
    Resume = ResumeModel.objects.first()
    Skills = skillmodel.objects.all()
    Filters = filter.objects.all()
    projects = projectmodel.objects.all()

    form = Contactform()
    if request.method=="POST":
        form = Contactform(request.POST)
        if form.is_valid():
            contact = form.save()  # Save to DB and store object

        subject = f"New Contact from {contact.name}"
        message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

        auto_reply_subject = "Thanks for contacting Darshan 👋"
        auto_reply_message = (
                f"Hi {contact.name},\n\n"
                "Thank you for reaching out! I’ve received your message and will get back to you soon.\n\n"
                "Regards,\n"
                "Darshan Prajapati"
            )
        send_mail(
                auto_reply_subject,
                auto_reply_message,
                settings.DEFAULT_FROM_EMAIL,
                [contact.email]
            )
        form = Contactform()
        return redirect('home')

        

    return render(request,"home.html",{ "Image":Profile , "Details" :Details , "Resume":Resume ,"skills":Skills,"filters":Filters,"projects":projects,'form': form})
