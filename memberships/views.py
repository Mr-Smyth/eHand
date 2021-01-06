from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Packages, Memberships, Subscriptions

import stripe

# Create your views here.


def get_current_package(request):
    """ A helper funtion that retrieves the membership package that the user
    is currently subscribed to.
    """

    current = get_object_or_404(Memberships, user=request.user)
    if current:
        return current
    return None


def get_user_subscription(request):
    """ A helper funtion that retrieves the users current subscription
    """

    # look in subscriptions for the current user
    query_subscription = Subscriptions.objects.filter(
        user_membership=get_current_package(request))
    if query_subscription.exists():
        user_subscription = query_subscription.first()
        return user_subscription


def get_selected_package(request):
    """ A helper funtion that gets the selected package from session storage
    """
    package_type = request.session['selected_package_type']
    # convert it to an object

    selected_package_query = get_object_or_404(
            Packages, package_type=package_type)
    if selected_package_query:
        return selected_package_query
    return None



def select_package(request):
    """ A view that returns the membership selection page """

    packages = Packages.objects.all()
    # Get the users current package - we want to compare this in the template
    # Also needed in post section
    current_package = get_current_package(request)

    if request.method == 'POST':
        # Get the posted info - then gets it in object form
        selected_package_type = request.POST.get('package_type')
        selected_package_query = get_object_or_404(
            Packages, package_type=selected_package_type)
        if selected_package_query:
            selected_package = selected_package_query

        # Get the current users subscription
        user_subscription = get_user_subscription(request)

        # Validate

        # check if current = selected - this should not be possible
        # but need to let them know they already have this package
        if current_package.membership_type == selected_package:
            if user_subscription is not None:
                messages.info(request, "This is your existing membership package. \
                    Your next payment is due on: {}".format(
                        'need to get this from stripe'))
                # send user back to the page they came -  packages
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # Now we can save the selected_package into session storage
        # because we want to pass it to the next view
        request.session[
            'selected_package_type'] = selected_package.package_type
        return HttpResponseRedirect(reverse('packages/payment'))

    context = {
        'packages': packages,
        'current_package': str(current_package.membership_type)
    }
    return render(request, 'memberships/select_package.html', context)


def payment(request):
    """ Get the stripe payment form for the user
        Also handle the payment
    """
    # get some required variables
    current_package = get_current_package(request)
    selected_package = get_selected_package(request)
    publicKey = settings.STRIPE_PUBLIC_KEY
