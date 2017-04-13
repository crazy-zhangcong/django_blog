#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:zhangcong
# Email:zc_92@sina.com


from django.forms import Form
from django.forms import widgets
from django.forms import MultipleChoiceField
from django.forms import fields


class TagsForm(Form):
    """标签 Form表单"""

    tag_name = fields.CharField(
        error_messages={
            "required": "标签不能为空",
        },
        widget=widgets.Input(
            attrs={"class": "form-control", "name": "hostname", "type": "text"})
    )