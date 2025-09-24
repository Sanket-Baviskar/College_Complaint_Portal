from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

class CustomLoginView(auth_views.LoginView):
    template_name = 'portal/login.html'
    redirect_authenticated_user = False   # 🚨 forces showing login always

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),

    # Auth
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Complaints
    path('home/', views.home, name='home'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('my/', views.my_complaints, name='my_complaints'),
    path('complaint/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('dashboard/', views.department_dashboard, name='department_dashboard'),
]
