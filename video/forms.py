from django import forms
from .models import Video


VideoFormSet = forms.modelformset_factory(Video, fields=['rtsp_link', 'camera_name', 'address', 'is_public'], extra=1, can_delete=True)
