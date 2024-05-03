from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Doctor, Patient, Nurse, Pharmacist, Laboratory, Accountant, Receptionist, Department

def admin_dashboard(request):
    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_nurses = Nurse.objects.count()
    total_pharmacists = Pharmacist.objects.count()
    total_laboratories = Laboratory.objects.count()
    total_accountants = Accountant.objects.count()
    total_receptionists = Receptionist.objects.count()
    total_departments = Department.objects.count()
    return render(request, 'hospital_management/admin_dashboard.html', {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_nurses': total_nurses,
        'total_pharmacists': total_pharmacists,
        'total_laboratories': total_laboratories,
        'total_accountants': total_accountants,
        'total_receptionists': total_receptionists,
        'total_departments': total_departments,
    })

def manage_users(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    nurses = Nurse.objects.all()
    pharmacists = Pharmacist.objects.all()
    laboratories = Laboratory.objects.all()
    accountants = Accountant.objects.all()
    receptionists = Receptionist.objects.all()
    return render(request, 'hospital_management/manage_users.html', {
        'doctors': doctors,
        'patients': patients,
        'nurses': nurses,
        'pharmacists': pharmacists,
        'laboratories': laboratories,
        'accountants': accountants,
        'receptionists': receptionists,
    })

def manage_departments(request):
    departments = Department.objects.all()
    return render(request, 'hospital_management/manage_departments.html', {
        'departments': departments,
    })

# Add other views as needed
