import account.views
from .forms import AppForm
from .forms import SignupForm
from .models import UserProfile
from django.views.generic.edit import FormView

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

class LoginView(FormView):

    form_class = account.forms.LoginEmailForm

    def generate_username(self, form):
        username = "<magic>"
        return username

class ApplicationView(FormView):
    template_name = 'application.html'
    form_class = AppForm
    success_url = '/thanks/'
    def form_valid(self, form):
        return super().form_valid(form)
