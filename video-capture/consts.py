import os
from dotenv import load_dotenv

CAMERA_SERVICE_URL = os.environ.get("CAMERA_SERVICE_URL")
YOLO_URL = os.environ.get("YOLO_URL")
DATA_COLLECTOR_URL = os.environ.get("DATA_COLLECTOR_URL")