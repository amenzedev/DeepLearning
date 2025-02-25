from ultralytics import YOLO
import cv2

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Define path to video file
source = "../data/video.mp4"

# Define video parameters
output_file = '../data/output.mp4'  # Output file name
frame_width = 1280
frame_height = 720
fps = 30  # Frames per second
codec = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI format

# Initialize VideoWriter
output= cv2.VideoWriter(output_file, codec, fps, (frame_width, frame_height))


# Run inference on the source
results = model(source, stream=True)  # generator of Results objects

# Process results list
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()  # Bounding boxes
    scores = result.boxes.conf.cpu().numpy()  # Confidence scores
    class_ids = result.boxes.cls.cpu().numpy()  # Class IDs
    frame = result.orig_img

    for box, score, class_id in zip(boxes, scores, class_ids):
        if(score < 0.65):
            continue
        x1, y1, x2, y2 = map(int, box)
        label = f"{model.names[int(class_id)]}: {score:.2f}"

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    output.write(cv2.resize(frame, (frame_width, frame_height)))

output.release()
cv2.destroyAllWindows()