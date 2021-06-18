from apps.users_app.models import UserType


def make_user_type():
    all_users_type = UserType.objects.all()
    all_users_type.delete()
    secretaria = UserType.objects.create(type_name = "secretaria")
    procuradora = UserType.objects.create(type_name = "procuradora")
