#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:zhangcong
# Email:zc_92@sina.com


from django import template

register = template.Library()


@register.simple_tag
def get_path(path):
    return path.strip('/').split('/')[-1]