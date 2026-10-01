from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse

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
        email_message = EmailMessage(
            subject=f"New Dental Appointment - {name}",

            body=f"""
NEW APPOINTMENT RECEIVED

Patient Name: {name}
Patient Email: {email}
Phone Number: {phone}
Service: {service}
Preferred Date: {date}

Message:
{message}

--------------------------------
City Dental Hospital
Website Appointment System
""",

            # EMAIL_HOST_USER se sender automatically liya jayega
            from_email=None,

            # Doctor ka Gmail
            to=["citydentalhospital425@gmail.com"],

            # Patient ke Gmail par Reply jayega
            reply_to=[email],
        )

        email_message.send()

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


def robots_txt(request):

    content = """User-agent: *
Allow: /

Sitemap: https://citydentalhospitalbawal.com/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )