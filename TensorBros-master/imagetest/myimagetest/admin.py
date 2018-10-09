from django.contrib import admin

from .models import VideoModel

# Register your models here.
class VideoModelAdmin(admin.ModelAdmin):
	
	list_display = ["primary_key", "video",]
	list_display_links = ["primary_key"]


admin.site.register(VideoModel, VideoModelAdmin)