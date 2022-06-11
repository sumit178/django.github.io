from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from proj.models import contact
# Create your views here.

def aboutme(request):
    return render(request, 'about.html')



def writeups(request):
    return render(request, 'writeups.html')
        
def spacehero(request):
    return render(request, 'ctf/spacehero.html')

def jersey(request):
    return render(request, 'ctf/jersey.html')

def feedback(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        country=request.POST.get('country')
        feedback=request.POST.get('feedback')
        feedback=contact(firstname=firstname, lastname=lastname, country=country, feedback=feedback, date = datetime.today())
        feedback.save()
    return render(request, 'feedback.html')