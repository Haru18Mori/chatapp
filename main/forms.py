from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.mail import send_mail
from .models import User,Talk
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

TABOO_WORDS = [
    "ばか",
    "バカ",
    "あほ",
    "アホ",
    "クソ",
    "くそ",
]
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

class LoginForm(AuthenticationForm):
    pass

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)
    
    def clean_message(self):
        message = self.cleaned_data["message"]
        matched = [w for w in TABOO_WORDS if w in message]
        # print(matched)
        
        if matched:
            logger.info(
                # "%sという禁止語が入力されてしまいました",matched
                "%sという禁止語が入力されてしまいました",', '.join(matched)
            )
            bad_text = message
            email = "receiver@example.com"

            subject = "禁止ワードが含まれた文章が送信されました"
            message = "%sという禁止な文が送信されました。" % (message)
            from_email = "sender@example.com"
            recipient_list = [email]
            send_mail(subject,message,from_email,recipient_list)


            raise ValidationError(f"禁止ワード {', '.join(matched)} が含まれていますぅwダメねェ")
          
        
        return message

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザー名"}
        help_texts = {"username": ""}

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {"email": "新しいメールアドレス"}
