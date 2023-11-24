from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
# Import the libraries
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import matplotlib.patches as patches
def object_detection(url): 
    results = None
    image = Image.open(url)
    plt.imshow(image)
    ax = plt.gca()
    # you can specify the revision tag if you don't want the timm dependency
    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to COCO API
    # let's only keep detections with score > 0.9
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.5)[0]

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        # Extract the score, label, and box coordinates
        xmin = box[0]
        ymin = box[1]
        xmax = box[2]
        ymax = box[3]
        # Calculate the width and height of the box
        width = xmax - xmin
        height = ymax - ymin
        # Create a rectangle patch with the box coordinates, edge color, and face color
        rect = patches.Rectangle((xmin, ymin), width, height, linewidth=2, edgecolor='r', facecolor='none')
        # Add the rectangle patch to the axes
        ax.add_patch(rect)
        # Add the label text to the axes
        plt.text(xmin, ymin-10, f'{model.config.id2label[label.item()]}: {score:.2f}', color='r', fontsize=12)
        plt.savefig('static/plot.png')
    plt.cla()
    return "plot.png"
