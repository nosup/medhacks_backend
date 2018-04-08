import account.views
from .forms import AppForm
from .forms import SignupForm
from .models import UserProfile
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse

# for LoginView
import account.forms
import account.views

class SignupView(account.views.SignupView):

    form_class = SignupForm

    def update_profile(self, form):
        UserProfile.objects.create(
            user=self.created_user,
            birthdate=form.cleaned_data["birthdate"]
        )
        # UserProfile.objects.create(
        #     user=self.created_user,
        #     birthdate=form.cleaned_data["birthdate"],
        # )

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm

    def generate_username(self, form):
        username = "<magic>"
        return username

def application(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            #form.save()
            return redirect('/account/login/')
    else:
        form = AppForm()
        args = {'form': form}
        return render(request, 'application.html', args)
