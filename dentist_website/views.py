from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':  # fill and send the form via email
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send mail
        send_mail(
            "Mail From Customer - " + message_name,  # subject
            'Name - ' + message_name + '\n' + 'Mail ID: ' + message_email + '\n\n' + 'Content:\n' + message,  # content
            message_email,  # from email
            ['naveen.m1616@gmail.com'],  # To email
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def about(request):
    return render(request, 'about.html', {})


def health_blog(request):
    return render(request, 'health_blog.html', {})


def corona_blog(request):
    return render(request, 'corona_blog.html', {})


def appointment(request):
    if request.method == 'POST':  # fill and send the form via email
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_date = request.POST['your-date']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        # send mail
        appointment = 'Name: ' + your_name + '\nPhone: '+your_phone + '\nEmail: '+your_email+'\nMessage: '+your_message
        send_mail(
            "Appointment From - " + your_name,  # subject
            appointment,  # content
            your_email,  # from email
            ['naveen.m1616@gmail.com'],  # To email
        ) 

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_date': your_date,
            'your_time': your_time,
            'your_message': your_message
        })
    else:
        return render(request, 'home.html', {})



