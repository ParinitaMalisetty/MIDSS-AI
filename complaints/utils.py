import os
import uuid


def complaint_image_path(instance, filename):
    ext = filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join(
        "complaints",
        filename
    )