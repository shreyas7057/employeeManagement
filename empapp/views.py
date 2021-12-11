from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from .models import Employee,Department, Job,Salary,Leave
from .forms import EmployeeForm,LeaveUserApply,JobAddForm,JobUpdateForm
from django.utils.crypto import get_random_string

User = get_user_model()


def index(request):
    if request.user.is_authenticated:
        return redirect('emp_profile_info')

    else:
        return render(request,'index.html')


# this will display logged in info means there name and other details
def emp_profile_info(request):
    if not request.user.is_authenticated:
        return redirect('login-employee')
    

    employee = Employee.objects.filter(user=request.user)

    # salary
    employees = get_object_or_404(Employee,user=request.user)
    salaries = Salary.objects.filter(employee=employees)


    # leaves
    employee_leave = get_object_or_404(Employee,user=request.user)
    leaves = Leave.objects.filter(employee=employee_leave)


    context = {
        'employees':employee,
        'salaries':salaries,
        'leaves':leaves,
    }
    return render(request,'employee_profile.html',context)


# logged in user can fill Employee information
def create_employee(request):

    if not request.user.is_authenticated:
        return redirect('login-employee')

    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)

        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.employee_code = get_random_string(8)
            employee.save()
            return redirect('emp_profile_info')

    else:
        form = EmployeeForm()

    context = {

        'form':form

    }

    return render(request,'employee_create.html',context)



# user will apply for leave
def user_apply_for_leave(request):
    
    if request.method == "POST":

        form = LeaveUserApply(request.POST)

        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user.employee
            leave.leave_status = "Pending"
            leave.save()
            return redirect('emp_profile_info')

    else:
        form = LeaveUserApply()

    context = {
        'form':form
    }

    return render(request,'leave_apply.html',context)


def display_job(request):
    employee = get_object_or_404(Employee,user=request.user)
    jobs = Job.objects.filter(employee=employee)
    context = {
        'jobs':jobs
    }

    return render(request,'job_display.html',context)



def add_job(request):
    
    if request.method == "POST":

        form = JobAddForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.employee = request.user.employee
            job.save()
            return redirect('display_job')
    
    else:
        form = JobAddForm()

    context = {
        'form':form
    }

    return render(request,'add_job.html',context)


def update_job(request,id):

    job = Job.objects.get(id=id)

    if request.method == "POST":
        position = request.POST.get('position')
        company_name = request.POST.get('company_name')
        exp_in_company = request.POST.get('exp_in_company')


        job.employee = request.user.employee
        job.postion = position
        job.company_name = company_name
        job.exp_in_company = exp_in_company
        job.save()

        return redirect('display_job')

    else:
        print("GET request")

    context = {
        'job':job,
    }

    return render(request,'update_job.html',context)


def delete_job(request,id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('display_job')