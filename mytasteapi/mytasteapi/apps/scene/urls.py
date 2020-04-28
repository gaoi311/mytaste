# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/27/20 9:20 PM
# software: PyCharm

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('scene/(?P<pk>\d+)/', views.SceneAPIView.as_view()),
    re_path('city/(?P<pk>\d+)/', views.CityAPIView.as_view()),
    re_path('scenes/(?P<pk>\d+)', views.CityScenesAPIView.as_view()),
    re_path('scene_comments/(?P<pk>\d+)', views.SceneCommentAPIView.as_view()),
    path('scene_comment/', views.SceneCommentCreateAPIView.as_view()),
    path('scenes/', views.ScenesSummaryAPIView.as_view()),
]
