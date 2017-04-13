from django.db import models

# Create your models here.


class UserProfile(models.Model):
    """用户表"""
    username = models.CharField(verbose_name="用户名", max_length=64, unique=True)
    password = models.CharField(verbose_name="密码", max_length=64)

    status_choices = (
        (0, "不启用"),
        (1, "启用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)

    def __str__(self):
        return "%s" % self.username

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"


class Role(models.Model):
    """角色表"""
    name = models.CharField(verbose_name="角色名", max_length=64, unique=True)
    permission = models.ManyToManyField(verbose_name="权限", to='Permissions')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = "角色表"


class Permissions(models.Model):
    """权限表"""
    name = models.CharField(verbose_name="权限名", max_length=64, unique=True)
    path = models.CharField(verbose_name="路径", max_length=64, unique=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "权限表"
        verbose_name_plural = "权限表"


class Tags(models.Model):
    """标签表"""
    tag_name = models.CharField(verbose_name="标签名", max_length=64)
    create_user = models.ForeignKey('UserProfile', verbose_name="创建人", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True, blank=True)
    count = models.PositiveSmallIntegerField(verbose_name="文章数", default=0)


class Articles(models.Model):
    """文章表"""
    title = models.CharField(verbose_name="标题", max_length=128, unique=True)
    article = models.CharField(verbose_name="文章", max_length=102400)
    tags = models.ManyToManyField('Tags', verbose_name="标签")
    column = models.ForeignKey('Columns', verbose_name="栏目")

    latest_time = models.DateTimeField(verbose_name="最后更新时间", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True, blank=True)

    status_choices = (
        (0, '未发布'),
        (1, '已发布'),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    hits = models.PositiveIntegerField(verbose_name="点击数", default=0)


class Columns(models.Model):

    """栏目表"""
    name = models.CharField(verbose_name="栏目名称", max_length=64)
    url = models.CharField(verbose_name="url", max_length=64, null=True, blank=True)
    create_user = models.ForeignKey('UserProfile', verbose_name="创建人", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True, blank=True)
