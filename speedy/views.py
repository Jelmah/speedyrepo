from django.shortcuts import render, redirect
from .models import Contactinfo, RegisterationForm
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index (request):
    return render(request, 'speedy/index.html')


@csrf_exempt
def contact (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contactinfo = Contactinfo(name=name,email=email,phone=phone,subject=subject,message=message)
        contactinfo.save()

    else:
        print('am gettin bored')
    return render(request, 'speedy/contact.html')

@csrf_exempt
def signin (request):
    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        phonenum = request.POST['phonenum']
        state = request.POST['state']
        dob = request.POST['dob']
        password = request.POST['password']

        registerationform = RegisterationForm(username=username,useremail=useremail,phonenum=phonenum,state=state,dob=dob,password=password)
        registerationform.save()
        return redirect('dashboard')
    else:
        print('am getting bored')
    
    return render(request, 'speedy/signin.html')

def dashboard(request):
    greet = RegisterationForm.objects.order_by('username')

    context = {
        'greet' : greet
    }
    return render (request, 'speedy/dashboard.html', context)


