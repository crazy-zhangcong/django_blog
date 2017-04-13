from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


from django.forms import Form
from django.forms import fields
from django.forms import widgets
import hashlib

from blog_database import models


# 装饰器 判断是否登录
def is_login(func):
    """判断是否登录"""

    def inner(request, *args, **kwargs):
        username = request.session.get("username")  # 从session中获取用户的username对应的值
        if not username:
            return redirect("/blog_admin/auth_login/?next=%s" % request.path)
        return func(request, *args, **kwargs)
    return inner


# 给密码加密
def str_encrypt(pwd):
    """
    用户输入的密码加密
    :param pwd: 密码
    :return:
    """
    hash = hashlib.md5()
    hash.update(pwd.encode())
    return hash.hexdigest()


class UserProfileForm(Form):
    """用户认证Form"""
    username = fields.CharField(
        error_messages={
            "required": "用户名不能为空",
        },

        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "name": "username",
            }
        )
    )

    password = fields.CharField(
        error_messages={
            "required": "密码不能为空",
        },

        widget=widgets.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
            }
        )
    )

    def clean_password(self):
        """对密码进行加密"""
        encrypt_password = str_encrypt(self.cleaned_data['password'])
        return encrypt_password


def auth_login(request):

    if request.method == "POST":
        form_obj = UserProfileForm(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data['username']
            password = form_obj.cleaned_data['password']
            model_obj = models.UserProfile.objects.filter(**form_obj.cleaned_data)
            if model_obj:
                request.session['username'] = form_obj.cleaned_data['username']
                request.session['user_id'] = model_obj.first().id
                request.session['is_login'] = True

                if request.GET.get('next'):
                    next_url = request.GET.get('next')
                else:
                    next_url = "/blog_admin/"
                return redirect(next_url)
            else:
                form_obj.errors["password"] = ["用户名或密码错误"]

    else:
        form_obj = UserProfileForm()

    return render(request, 'blog_admin/auth_login.html', locals())


def auth_logout(request):
    request.session.clear()

    return redirect('/blog_admin/auth_login/')

