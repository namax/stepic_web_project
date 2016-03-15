"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

    /
/login/
/signup/
/question/<123>/    # вместо <123> - произвольный ID
/ask/
/popular/
/new/
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.last_questions_list, name='last_questions_list'),
    url(r'^login', views.test, name='login'),
    url(r'^signup', views.test, name='signup'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question_details, name='question_details'),
    url(r'^ask', views.question_add, name='ask'),
    url(r'^popular', views.popular_questions_list, name='popular_questions_list'),
    url(r'^new', views.test, name='new'),
    url(r'^answer', views.save_answer, name='save_answer'),
]
