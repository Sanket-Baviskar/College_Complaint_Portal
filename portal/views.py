from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from .forms import ComplaintForm, StatusUpdateForm
from .models import Complaint, Department
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from .models import Profile
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'portal/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-create student profile
            Profile.objects.create(user=user, role='student')
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'portal/signup.html', {'form': form})

@login_required
def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('my_complaints')
    else:
        form = ComplaintForm()  # ← this ensures form is passed in GET request

    return render(request, 'portal/submit_complaint.html', {'form': form})


@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'portal/my_complaints.html', {'complaints': complaints})

@login_required
def complaint_detail(request, pk):from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # show all complaints
    return render(request, 'portal/home.html')



@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'portal/my_complaints.html', {
        'complaints': complaints
    })

@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)

    # allow only owner or staff
    if complaint.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to view this complaint.')
        return redirect('home')

    form = None
    if request.user.is_staff and request.method == 'POST':
        form = StatusUpdateForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status updated successfully.')
            return redirect('complaint_detail', pk=complaint.pk)
    elif request.user.is_staff:
        form = StatusUpdateForm(instance=complaint)

    return render(request, 'portal/complaint_detail.html', {
        'complaint': complaint,
        'form': form
    })

@login_required
def department_dashboard(request):
    # dashboard for departments
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('home')

    dept_name = request.GET.get('dept')
    complaints = Complaint.objects.all().order_by('-updated_at')

    if dept_name:
        complaints = complaints.filter(department__name=dept_name)

    departments = Department.objects.all()

    return render(request, 'portal/department_dashboard.html', {
        'complaints': complaints,
        'departments': departments,
        'dept_name': dept_name,
    })

def staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(staff_check)
def department_dashboard(request):
    # Filter by department via staff user's first_name OR a query param
    dept_name = request.GET.get('dept') or request.user.first_name
    complaints = Complaint.objects.all()
    if dept_name:
        complaints = complaints.filter(department__name=dept_name)
    complaints = complaints.order_by('-created_at')
    departments = Department.objects.order_by('name')
    return render(request, 'portal/department_dashboard.html', {'complaints': complaints, 'departments': departments, 'dept_name': dept_name})

@login_required
def logout_view(request):
    logout(request)   # clears session
    return redirect('login')