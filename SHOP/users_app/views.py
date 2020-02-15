from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

from .models import Profile


def get_profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist as exception_alias:
        response = JsonResponse({'error': f'{exception_alias}'})
        response.status_code = 200
        return response
    json_data = {
        'id': profile.id,
        'user': user.id,
        'address': profile.address,
        'phone_number': profile.phone_number
    }
    return JsonResponse({'profile': json_data})



# def sign_up(request):
#     form_data = request.POST
#     firstname_and_lastname = form_data.get('name', '')
#     email = form_data.get('username', False)
#     phone = form_data.get('phone', '')
#     password = form_data.get('password', False)
#     if email and password:
#         firstname, lastname = split_full_name(firstname_and_lastname)
#         try:
#             User.objects.get(username=email)
#         except ObjectDoesNotExist:
#             new_user = User()
#             new_user.username = email
#             new_user.email = email.lower()
#             new_user.first_name = firstname
#             new_user.last_name = lastname
#             new_user.set_password(password)
#             new_user.is_active = False
#             new_user.save()
#
#             new_user_extend_obj = UserExtend()
#             new_user_extend_obj.user = new_user
#             new_user_extend_obj.phone = phone
#             new_user_extend_obj.save()
#             activation_link = new_user_extend_obj.get_activation_link()
#             send_mail(
#                 subject='Ссылка для активации аккаунта на сайте blablabla.com',
#                 message_text=request.build_absolute_uri(activation_link),
#                 address=email
#             )
#     return render(request, template_name='users_app/login_template.html')