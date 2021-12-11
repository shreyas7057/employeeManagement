from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
from .forms import RegisterForm,AuthenticationForm
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import login, authenticate

User = get_user_model()


def registerEmployeeView(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'Employee Register Successfully')
            return redirect('login-employee')
    
    else:
        form = RegisterForm()

    context = {
        'form':form,
    }

    return render(request,'accounts/register.html',context)



def loginEmployeeView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            print("1")
            email = request.POST.get('email')
            password = request.POST.get('password')
            print("2")
            user = authenticate(email=email, password=password)
            print("3")
            if user is not None:
                if user.is_active:
                    print("4")
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return redirect('emp_profile_info') 

                else:
                    messages.error(request,'user is not active')
                    return redirect('login-employee')
            
            else:
                messages.error(request,'invalid credentials')
                return redirect('login-employee')

    else:
        print("5")
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form,})



def logout_view(request):
    logout(request)
    return redirect('index')