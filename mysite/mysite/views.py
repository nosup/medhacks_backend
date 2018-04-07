import account.views

from .forms import SignupForm
from .models import UserProfile

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
