from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUptadeForm, UserDeleteForm
from django.contrib.auth import login, authenticate, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from .tokens import account_activation_token
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


def registration_view(request):

    if request.method == 'GET':
        return render(request, "register.html")

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            if user.email.__contains__("edu.tr"):
                user.is_active = False

                user.save()
                current_site = get_current_site(request)

                mail_subject = 'Activate your account.'
                message = render_to_string('acc_activate.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return render(request, "registerINFO.html")
            else:
                messages.info(
                    request, 'Lütfen edu.tr uzantılı bir e-posta giriniz.')
        else:
            messages.info(
                request, 'Kayıt işlemi başarısız oldu, lütfen bilgilerinizi kontrol ediniz.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "registerOK.html")
    else:
        return render(request, "registerFAIL.html")


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("index")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "login.html", context)


def account_view(request):

    if not request.user.is_authenticated:
        return redirect("account:login")

    context = {}

    if request.POST or request.FILES:

        form = AccountUptadeForm(request.POST or None,
                                 request.FILES or None, instance=request.user)

        if form.is_valid():

            form.initial = {
                "email": request.POST.get("email"),
                "fullName": request.POST.get("fullName"),
                "universty": request.POST.get("universty"),
                "department": request.POST.get("department"),
                "account_type": request.POST.get("account_type"),
                "account_avatar": request.FILES.get("account_avatar")

            }

            context['succes_message'] = "Başarıyla Güncellendi."

            form.save()

    else:
        form = AccountUptadeForm(
            initial={
                "email": request.user.email,
                "fullName": request.user.fullName,
                "universty": request.user.universty,
                "department": request.user.department,
                "account_type": request.user.account_type,
                "account_avatar": request.user.account_avatar
            }
        )

    context['account_form'] = form
    return render(request, "accountUptade.html", context)


@login_required(login_url="account:login")
def delete_user(request):

    if request.method == 'POST':

        delete_form = UserDeleteForm(request.POST, instance=request.user)

        user = request.user

        # user.delete()

        password = request.user.password

        deletePassword = request.POST.get("password")

        if check_password(deletePassword, password) == True:

            user.delete()
            messages.success(request, 'Hesabınız Başarıyla Silinmiştir.')
            return redirect("index")
        else:

            messages.info(request, 'Lütfen Şifrenizi Doğru Giriniz.')

    else:

        delete_form = UserDeleteForm(instance=request.user)

    context = {

        'delete_form': delete_form
    }

    return render(request, 'delete_user.html', context)
