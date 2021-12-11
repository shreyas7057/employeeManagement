from django.urls import path
from .views import create_employee,emp_profile_info,user_apply_for_leave,display_job,add_job,update_job,delete_job


urlpatterns = [


    path('create/',create_employee,name='create_employee'),
    path('show/',emp_profile_info,name='emp_profile_info'),

    path('leave/apply/',user_apply_for_leave,name='user_apply_for_leave'),

    path('jobs/',display_job,name='display_job'),
    path('jobs/add/',add_job,name='add_job'),
    path('jobs/update/<int:id>/',update_job,name='update_job'),
    path('jobs/delete/<int:id>/',delete_job,name='delete_job'),
]