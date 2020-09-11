from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from .models import contact


# Create your views here.

def contact(request):
  """
  sends the user to the contact page
  """
  if request.method == 'GET':
      form = ContactForm()
  else:
      form = ContactForm(request.POST)
      if form.is_valid():
          subject = form.cleaned_data['subject']
          print(subject)
          from_email = settings.EMAIL_HOST_USER
          email_address = form.cleaned_data['email_address']
          message = form.cleaned_data['message']
          to_list = [email_address]
          send_mail(
              subject,
              message,
              from_email,
              to_list,
              fail_silently=True)
          messages.success(
              request,
              """We\'ve received your message,
              and shall be back with you shortly""")
          form.save()
          return redirect('products')
          context = {'form': form}


  return render(request, 'contact.html', context)
