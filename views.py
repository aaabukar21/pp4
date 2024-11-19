from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation

def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the reservation to the database
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = ReservationForm()

    return render(request, 'reservations/book_table.html', {'form': form})

def booking_success(request):
    return render(request, 'reservations/booking_success.html')
