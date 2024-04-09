from django.shortcuts import render, redirect
from .models import Booking, Period, Teacher
from .forms import BookingForm
from datetime import date, timedelta
from django.db.models import Sum


def book_ipad(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            teacher_name = form.cleaned_data['teacher_name']
            teacher, created = Teacher.objects.get_or_create(name=teacher_name)

            booking = form.save(commit=False)
            booking.teacher = teacher
            booking.num_ipads = form.cleaned_data['num_ipads']
            booking.save()  # Save the booking instance to generate an id

            if check_availability(booking.date, booking.periods.all(), booking.num_ipads):
                form.save_m2m()  # Save the many-to-many relationship for periods
                return redirect('booking_success')
            else:
                booking.delete()  # Delete the booking if it's not available
                return render(request, 'booking/booking_failed.html')
    else:
        form = BookingForm()
    return render(request, 'booking/book_ipad.html', {'form': form})

def check_availability(date, periods, num_ipads):
    for period in periods:
        booked_ipads = Booking.objects.filter(date=date, periods=period).aggregate(Sum('num_ipads'))['num_ipads__sum'] or 0
        if booked_ipads + num_ipads > 40:
            return False
    return True

def booking_success(request):
    return render(request, 'booking/booking_success.html')


def availability(request):
    # Get the dates for the next week
    dates = [date.today() + timedelta(days=i) for i in range(7)]

    # Get all periods
    periods = Period.objects.all()

    # Create a dictionary mapping dates to another dictionary mapping periods to availability
    availability = {
        date: {
            period: {
                'bookings': Booking.objects.filter(date=date, periods=period).select_related('teacher'),
                'available': 40 - (Booking.objects.filter(date=date, periods=period).aggregate(Sum('num_ipads'))['num_ipads__sum'] or 0)
            }
            for period in periods
        }
        for date in dates
    }

    return render(request, 'booking/availability.html', {'availability': availability})
from django.shortcuts import render

