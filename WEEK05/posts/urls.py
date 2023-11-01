from django.urls import path

from .views import post_diary_view
from .views import post_sns_view, post_song_view, post_photo_view

app_name='posts'

urlpatterns=[
    path('', post_diary_view, name='post-diary'),
    path('<int:id>/', post_song_view),
    path('<int:id>/photo', post_photo_view),
    path('<int:id>/sns', post_sns_view),
]