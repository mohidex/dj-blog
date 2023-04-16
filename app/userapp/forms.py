from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class BlogUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "username")


class BlogUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email", "username")
