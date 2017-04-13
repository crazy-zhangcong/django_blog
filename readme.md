# 使用 django 搭建一个博客系统

## 运行环境: 
```
    python  -->  python 3.x
    django  -->  django 1.10
```


## 开发进度

| 时间      |    更新内容 |
| :--------: | :--------:|
| 2017-04-12  | 后台大概框架已经弄好,准备开始做功能 <br> 功能主要分为: 标签管理、栏目管理、文章管理、权限管理 |
| 2017-04-13  | 1、标签管理的增、删、改、查已经完成,还差分页和搜索功能 <br> |


## 目录结构
```
django_blog/            # 程序主目录
├── blog_admin              ## 后台管理app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templatetags
│   │   ├── base_active.py
│   │   └── __init__.py
│   ├── tests.py
│   ├── urls.py                 ### 路由
│   ├── views_dir
│   │   ├── authentication.py   ### 登录认证模块
│   │   ├── forms.py            ### forms 表单验证模块
│   │   └── __init__.py
│   └── views.py                ### 视图
├── blog_database           ## 该 app 主要存放数据库表结构
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── blog_web                ## 前端页面展示
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── django_blog             ## 默认app
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── readme.md
├── templates
│   ├── blog_admin              ### 后台 html 模板
│   └── blog_web                ### 前台 html 模板
└── static                  ## 静态文件存放目录
    ├── css
    ├── font
    └── js
```
