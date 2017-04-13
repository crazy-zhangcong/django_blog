from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from blog_admin.views_dir.authentication import is_login
from blog_admin.views_dir import forms

from blog_database import models
from django.http import JsonResponse


class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.message = None
        self.data = None
        self.error = None


@is_login
def index(request):
    return render(request, 'blog_admin/index.html')


@is_login
def article(request):
    return render(request, 'blog_admin/article.html')


@is_login
def column(request):
    return render(request, 'blog_admin/column.html')


@is_login
def tags(request):
    print(request.method)
    response = BaseResponse()
    if request.method == "GET":
        tags_obj = models.Tags.objects.filter(create_user__username=request.session['username'])

        return render(request, 'blog_admin/tags.html', locals())

    elif request.method == "POST":

        type_ = request.POST.get('type_')

        if type_ == "PUT":
            tag_name = request.POST.get('v')
            tag_id = request.POST.get('tag_id')

            tags_count = models.Tags.objects.filter(create_user__username=request.session['username'], tag_name=tag_name).count()
            if tags_count > 0:
                response.status = False
                response.message = "标签 %s 已存在" % tag_name

            models.Tags.objects.filter(create_user__username=request.session['username'], id=tag_id).update(
                tag_name=tag_name)
            response.status = True
        elif type_ == "DELETE":
            tag_id = request.POST.get('tag_id')
            models.Tags.objects.filter(create_user__username=request.session['username'], id=tag_id).delete()
            response.status = True

    return JsonResponse(response.__dict__)


@is_login
def tags_add(request):

    if request.method == "POST":

        form_obj = forms.TagsForm(request.POST)

        if form_obj.is_valid():

            tag_name = form_obj.cleaned_data['tag_name']

            tags_obj = models.Tags.objects.filter(tag_name=tag_name, create_user__username=request.session['username'])
            if tags_obj:
                form_obj.errors['tag_name'] = ["该标签已存在",]
            else:
                userprofile_obj = models.UserProfile.objects.get(username=request.session['username'])
                models.Tags.objects.create(tag_name=tag_name, create_user=userprofile_obj)

                return redirect('/blog_admin/tags/')

            return render(request, 'blog_admin/tags_add.html', locals())

    form_obj = forms.TagsForm()
    return render(request, 'blog_admin/tags_add.html', locals())
