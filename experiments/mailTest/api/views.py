from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

# Create your views here.
@api_view(['POST'])
def sendMail(request): 
    body = request.data.get('body', None)
    
    if body: 
        subject = "test"
        message = body
        from_email = "otakugod000@outlook.com"
        recipient_list = ['otakugod0000@gmail.com',]
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
        return Response("Email Sent Successfully", status=status.HTTP_200_OK)
    
    else: 
        return Response("No body attribute recieved in request.data", status=status.HTTP_400_BAD_REQUEST)