from ultralytics import YOLO

model = YOLO("AI/models/best.pt")


def analyze_image(image_path):

    results = model(image_path)

    if len(results[0].boxes) == 0:

        return {
            "prediction": "No Damage",
            "confidence": 0,
            "severity": "Low",
            "support": "No maintenance required."
        }

    box = results[0].boxes[0]

    prediction = model.names[int(box.cls)]

    confidence = float(box.conf)

    if confidence > 0.9:
        severity = "Critical"
    elif confidence > 0.7:
        severity = "High"
    elif confidence > 0.5:
        severity = "Medium"
    else:
        severity = "Low"

    return {
        "prediction": prediction,
        "confidence": round(confidence * 100, 2),
        "severity": severity,
        "support": f"{prediction} detected. Send maintenance team."
    }