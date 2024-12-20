from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Record
from .forms import RecordForm


# Create your views here.
@csrf_protect
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']

        #Authenticate user
        user = authenticate(request, username=user_name, password=user_password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'home.html')
    else:
        return render(request, 'home.html', {'records': records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')

@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate user
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password1']

            user = authenticate(request, username=user_name, password=user_password)
            login(request, user)

            messages.success(request, 'You have been registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

def view_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': record})
    else:
        messages.error(request, 'You must be logged in to view a record')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to delete a record')
        return redirect('home')

@login_required(login_url='home')
def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST or None)
        if form.is_valid():
            try:
                record = form.save()
                messages.success(request, 'Record added successfully!')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error saving record: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RecordForm()
    
    return render(request, 'add_record.html', {'form': form})

@login_required(login_url='home')
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = RecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('home')
        # messages.error(request, 'Please correct the errors below.')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to update a record')
        return redirect('home')
        

        
    


