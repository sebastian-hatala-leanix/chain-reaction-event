import cv2
import numpy as np
from numpy.linalg import norm
import requests

def _get_image_frame(camera) -> np.ndarray:
    _, frame = camera.read()
    return frame

def _convert_frame_to_hsv(frame: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

def _post_to_michi() -> None:
    try:
        requests.post("https://tbaum.duckdns.org/api/webhook/awesome-leanix")
    except Exception:
        _post_to_michi()

def main() -> None:
    camera = cv2.VideoCapture(0)

    while True:
        frame = _get_image_frame(camera)
        hsv_img = _convert_frame_to_hsv(frame)

        if np.average(norm(hsv_img, axis=2)) / np.sqrt(3) > 110:
            _post_to_michi()
            break

    print("Success!")


if __name__ == "__main__":
    main()