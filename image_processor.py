import cv2


class ImageProcessor(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.matcher = lambda x: NotImplemented()

    def set_matcher(self, matcher):
        self.matcher = matcher


if __name__ == '__main__':
    pass
