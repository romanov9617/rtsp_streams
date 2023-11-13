
import threading
import time
from typing import Any
import cv2
import redis

from .models import Video
import numpy as np
from numpy import ndarray

class VideoCamera(object):

    def __init__(self, link: str) -> None:
        self.video = cv2.VideoCapture(link)
        self.grabbed, self.frame = self.video.read()
        threading.Thread(target=self.update, args=()).start()


    def __del__(self) -> None:
        self.video.release()

    def get_frame(self) -> ndarray:
        return self.frame

    def update(self) -> None:
        while self.video.isOpened():
            (self.grabbed, self.frame) = self.video.read()

    def gen(self) -> Any:
        while True:
            image = self.get_frame()
            _, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def get_all_frames() -> list[ndarray]:
    """
        Generates a stream of frames from all connected cameras.

        Returns:
            A generator that continuously yields frames from the connected cameras.

        Raises:
            None.
    """
    video_cameras = []
    connected_cameras = []
    while True:
        db_cameras = Video.objects.all()
        if len(db_cameras) != len(video_cameras):
            end_index = len(db_cameras) - len(video_cameras)
            start_index = 0
            video_cameras.extend(db_cameras[start_index:end_index:])
            new_connected_cameras = [VideoCamera(camera.rtsp_link) for camera in video_cameras[start_index:end_index:]]
            connected_cameras.extend(new_connected_cameras)
        with redis.Redis() as r:
            r.set('timer', 1, ex=600)
            while r.exists('timer'):
                yield [camera.get_frame() for camera in connected_cameras]
                time.sleep(5)



