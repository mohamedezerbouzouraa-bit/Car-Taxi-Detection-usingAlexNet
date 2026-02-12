import torch
from torchvision import models
def load_model():
    model = models.alexnet(pretrained=True)
    model.eval()
    return model
