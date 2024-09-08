# projects/model_loader.py
import torch
from torch import nn
from torchvision import transforms, models
from PIL import Image
import os

# Load the model (update the model path accordingly)
model_path = os.path.join(os.path.dirname(__file__), 'models', 'ct-scan-classifier.pth')


# Initialize the model
def initialize_model(num_classes=4):
    model = models.resnet18(weights='ResNet18_Weights.DEFAULT')
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    return model


# Load the model
model = initialize_model(num_classes=4)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Mapping from index to class names
class_names = [
    "adenocarcinoma_left.lower.lobe",
    "large.cell.carcinoma_left.hilum",
    "normal",
    "squamous.cell.carcinoma_left.hilum"
]


def predict_image(image_path):
    image = Image.open(image_path).convert('RGB')  # RGB format
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    # Convert prediction index to class name
    class_name = class_names[predicted.item()]
    return class_name
