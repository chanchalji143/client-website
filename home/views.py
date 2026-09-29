from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .models import Appointment, Gallery, ClinicSettings


def home(request):

    # Gallery images
    galleries = Gallery.objects.all()

    # Clinic logo
    clinic = ClinicSettings.objects.first()

    if request.method == "POST":

        # Form se data lena
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        date = request.POST.get("date")
        message = request.POST.get("message")
        email = request.POST.get("email")

        # Database me Appointment save karna
        appointment = Appointment.objects.create(
            name=name,
            phone=phone,
            service=service,
            date=date,
            message=message,
            email=email
        )

        # Doctor ko Email Notification
        send_mail(
            subject="New Dental Appointment",
            message=f"""
New Appointment Received

Patient Name: {name}
Phone Number: {phone}
Visitor Email: {email}
Service: {service}
Preferred Date: {date}

Message:
{message}
""",
            from_email=None,
            recipient_list=["pkundu52@gmail.com"],
        )

        # Success message
        messages.success(
            request,
            "Your appointment has been booked successfully!"
        )

        print("Appointment Saved:", appointment)

        # POST ke baad redirect
        return redirect("home")

    return render(
        request,
        "home/index.html",
        {
            "galleries": galleries,
            "clinic": clinic,
        }
    )

from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://citydentalhospitalbawal.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")