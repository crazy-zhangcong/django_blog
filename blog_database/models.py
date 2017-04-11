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
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)

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

