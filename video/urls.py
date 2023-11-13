from django.urls import path
from video import views


urlpatterns = [
        path('', views.PublicCameraListView.as_view(), name='public_cameras'),
        path('my_cameras', views.MyCameraListView.as_view(), name='my_cameras'),
        path('add', views.VideoAddView.as_view(), name="add_camera"),
        path('video/<int:video_id>', views.video_stream, name="video_stream"),
    ]


