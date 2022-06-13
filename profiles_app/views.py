from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout_app.models import Order
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    '''
    Display user profile
    '''
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated sucessfully')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles_app/profile.html'
    context = {
        'orders': orders,
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout_app/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,   
    }

    return render(request, template, context)
