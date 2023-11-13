# from typing import Any
from typing import Any
from django import http
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import VideoFormSet
from .models import Video
from django.views.generic import ListView, TemplateView
from .video_camera import *
from django.contrib.auth.mixins import LoginRequiredMixin

class PublicCameraListView(ListView):
    model = Video
    template_name = "video/public_cameras.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        videos = Video.objects.filter(is_public=True).all()
        return render(request, self.template_name, {'videos': videos})


class MyCameraListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = "video/my_cameras.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        videos = Video.objects.filter(author=request.user).all()
        return render(request, self.template_name, {'videos': videos})

class VideoAddView(LoginRequiredMixin, TemplateView):
    template_name = "video/add_video.html"

    def get(self, *args, **kwargs):
        formset = VideoFormSet(queryset=Video.objects.none())
        return self.render_to_response({'video_formset': formset})

    def post(self, *args, **kwargs):
        formset = VideoFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            for form in formset:
                video = form.save(commit=False)
                video.author = self.request.user
                video.save()
            return redirect(reverse_lazy("my_cameras"))

        return self.render_to_response({'video_formset': formset})

def video_stream(request, video_id):
    camera_link = Video.objects.filter(id=video_id).first().rtsp_link
    camera = VideoCamera(camera_link)
    try:
        return StreamingHttpResponse(camera.gen(), content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        return render(request, 'video/not_available.html')
