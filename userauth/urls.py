from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


    

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('add-employee/', views.add_employee_view, name='add_employee'),
    path('choose-mode/', views.choose_mode_view, name='choose-mode'),
    path('choose-role/', views.choose_role_view, name='choose-role'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Dashboard URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    
    # Ticket management
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/status/<str:new_status>/', views.update_ticket_status, name='update_ticket_status'),
]






