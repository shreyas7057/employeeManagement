from django.db import models
from accounts.models import User
# Create your models here.

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
)


LEAVE_CHOICES = (
    ('Accepted','Accepted'),
    ('Rejected','Rejected'),
    ('Pending','Pending'),
)


SALARY_STATUS = (
    ('Pending','Pending'),
    ('Done','Done'),
    ('50%','50%')
)

SALARY_MONTH = (
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December')
)



class Department(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='profile/',default='/profile/my.jpg')
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    employee_code = models.CharField(max_length=10,null=True,blank=True)
    aadhar_card_no = models.CharField(max_length=15)

    def __str__(self):
        return f"Email: {self.user.email}...Name: {self.name}"


class Salary(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary_month = models.CharField(max_length=20,choices=SALARY_MONTH)
    salary_description = models.CharField(max_length=255)
    salary_amount = models.IntegerField()
    salary_given = models.CharField(max_length=20,choices=SALARY_STATUS)
    bonus = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"Employee: {self.employee.name}...Salary Amount: {str(self.salary_amount)}"

    
    def bonusandsalary(self):

        if self.bonus:
            total_salary = self.salary_amount+self.bonus
            return total_salary



class Leave(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    leave_from = models.DateField(auto_now_add=False)
    leave_till = models.DateField(auto_now_add=False)
    leave_reason = models.CharField(max_length=255)
    leave_status = models.CharField(max_length=20,choices=LEAVE_CHOICES)

    def __str__(self):
        return self.employee.name+" "+self.leave_status



class Job(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    exp_in_company = models.CharField(max_length=10)
    

    def __str__(self):
        return self.employee.name+" "+self.position