from apps.users_app.models import UserTyp


def make_user_type():
    all_users_type = UserTyp.objects.all()
    all_users_type.delete()
    secretaria = UserTyp.objects.create(type_name = "secretaria")
    procuradora = UserTyp.objects.create(type_name = "procuradora")
