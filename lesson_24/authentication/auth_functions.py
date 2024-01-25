from .models import Users


def hide_mail():
    users = Users.objects.all()
    private_mail = []
    for user in users:
        mail_mod = str(user).split('@')
        modded_mail = mail_mod[0][:3] + '***' + '@' + mail_mod[1]
        private_mail.append(modded_mail)
    return private_mail[-10:]
