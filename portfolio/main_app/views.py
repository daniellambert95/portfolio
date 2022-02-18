from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
# from django.core.mail import EmailMessage


# Create your views here.

def index(request):
    
    contact_form = ContactForm
    if request.method == 'POST':
        print("Hello")
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            from_email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            message = f'''{message}\n\n
{name} sent you this email via your portfolio contact form, respond to them via - {from_email}
            '''

            send_mail( subject, message, from_email, ['danjlambert95@gmail.com'], fail_silently=False)


            # Redirect success message
            # messages.success(request, f'Your message has successfully been sent!')
            
            return redirect('home_page')
    else:
        form = ContactForm()
        
    return render(request, 'main_app/index.html', {'form': form})
