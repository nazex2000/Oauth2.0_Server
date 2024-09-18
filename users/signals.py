from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def populate_user_data(request, user, **kwargs):
    extra_data = user.socialaccount_set.filter(provider='google')[0].extra_data
    user.profile_picture = extra_data['picture']
    user.phone_number = extra_data.get('phoneNumber', None)
    user.save()


