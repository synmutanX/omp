from transformers import pipeline
from PIL import Image
import torch
from torchvision import models, transforms

# Text-based NSFW classification (Hugging Face)
text_classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_text(text):
    result = text_classifier(text)
    return result[0]["label"] == "NSFW"

# Image-based NSFW classification (ResNet Pretrained Model)
image_classifier = models.resnet50(pretrained=True)
image_classifier.eval()

def classify_image(image_path):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    image = Image.open(image_path)
    input_tensor = preprocess(image).unsqueeze(0)

    with torch.no_grad():
        output = image_classifier(input_tensor)
        _, predicted = torch.max(output, 1)
    
    # Example: Define 1 as NSFW (you can fine-tune this logic)
    return predicted.item() == 1
