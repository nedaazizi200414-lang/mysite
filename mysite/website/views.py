from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Appointment


# 🏠 HOME PAGE
def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'website/home.html', {'doctors': doctors})


# ℹ️ ABOUT PAGE
def about(request):
    return render(request, 'website/about.html')


# 📞 CONTACT PAGE
def contact(request):
    return render(request, 'website/contact.html')


# 🟢 APPOINTMENT PAGE (CREATE)
def appointment_page(request):
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        Appointment.objects.create(
            patient_name=request.POST.get('patient_name'),
            phone=request.POST.get('phone'),
            doctor_id=request.POST.get('doctor'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            reason=request.POST.get('reason')
        )
        return redirect('table')

    return render(request, 'website/appointment.html', {
        'doctors': doctors,
        'appointment': None
    })


# 📋 MY APPOINTMENTS
def my_appointments(request):
    appointments = Appointment.objects.select_related('doctor').order_by('-created_at')
    return render(request, 'website/my_appointments.html', {
        'appointments': appointments
    })


# ✏️ EDIT APPOINTMENT
def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        appointment.patient_name = request.POST.get('patient_name')
        appointment.phone = request.POST.get('phone')
        appointment.doctor_id = request.POST.get('doctor')
        appointment.date = request.POST.get('date')
        appointment.time = request.POST.get('time')
        appointment.reason = request.POST.get('reason')
        appointment.save()
        return redirect('table')

    return render(request, 'website/appointment.html', {
        'appointment': appointment,
        'doctors': doctors
    })


# ❌ DELETE APPOINTMENT
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('table')
    
def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    return render(
        request,
        'website/doctor_detail.html',
        {'doctor': doctor}
    )