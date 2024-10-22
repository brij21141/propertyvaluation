from django.dispatch import receiver  
from django.core.mail import send_mail  
from django.conf import settings  
# from api.signals import reset_password_token_created  
# from api.models import ResetPasswordToken  
from django.utils.http import urlsafe_base64_encode  
from django.utils.encoding import force_bytes  
from django.contrib.auth.models import User  

# @receiver(reset_password_token_created)  
# def send_reset_password_email(sender, instance, reset_password_token, **kwargs):  
#     subject = 'Password Reset Requested'  
#     uid = urlsafe_base64_encode(force_bytes(instance.pk))  
#     token = reset_password_token.key  # Assumes you have a 'key' field  
#     reset_link = f'{settings.FRONTEND_URL}/reset-password-confirm/{uid}/{token}/'  

#     message = f'Click the link below to reset your password:\n{reset_link}'  
#     send_mail(  
#         subject,  
#         message,  
#         settings.DEFAULT_FROM_EMAIL,  
#         [instance.email],  
#         fail_silently=False,  
#     )