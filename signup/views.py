from django.shortcuts import render,redirect ,render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from signup.forms import UserForm, UserProfileForm, OrderForm, ContactForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail ,BadHeaderError
from django.conf import settings
# Create your views here.


def user_login(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args.update(csrf(request))
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect('/')
            else:
                # An inactive account was used - no logging in!
                return render_to_response("Your  account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            args['error'] = "Invalid login details"
            return render_to_response("login.html", args)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', args)
    
    
    
def logout(request):
    auth.logout(request)
    return redirect("/")

def order(request):
    args = {}
    args['username'] = auth.get_user(request).username
    if request.method == 'POST':
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid():
            user = order_form.save()
            user.save()
        else:
            print order_form.errors
    else:
        order_form = OrderForm()
    args['order_form'] = order_form
    return render(request,
            'order.html',args)

def order1(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args.update(csrf(request))
    if request.method == 'POST':
        text = request.POST.get('text')
        phone = request.POST.get('phone')
        subject = {}
        subject = text
        send_mail('HookahOrder', subject, settings.EMAIL_HOST_USER, ['timofeimelnyk@gmail.com'])
        return render(request, 'order1.html')
    else:
        return render_to_response('order1.html', args)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    args = {}
    args['username'] = auth.get_user(request).username
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    args['user_form'] = user_form
    args['profile_form'] = profile_form
    args['registered_form'] = registered
    return render(request,
            'register.html',args )