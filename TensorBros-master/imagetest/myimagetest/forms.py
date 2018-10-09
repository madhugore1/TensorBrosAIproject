from django import forms

from .models import VideoModel

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ["video"]

