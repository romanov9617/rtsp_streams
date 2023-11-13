from video.utils import menu

def get_video_context(request):
    return {
        'menu': menu
    }

