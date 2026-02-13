CAR_CLASSES = [436, 511, 609, 656, 661]
TAXI_CLASS = 468
def predict(input_tensor, model):
    import torch
    with torch.no_grad():
        output = model(input_tensor)
    predicted_class = torch.argmax(output, dim=1).item()
    is_taxi = predicted_class == TAXI_CLASS
    is_car = predicted_class in CAR_CLASSES or is_taxi
     return predicted_class, is_car, is_taxi
