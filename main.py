from car_taxi_classifier.model import load_model
from car_taxi_classifier.preprocess import preprocess_image
from car_taxi_classifier.predict import predict
from car_taxi_classifier.utils import print_result

image_path = "ezertrial.jpg"
model = load_model()
input_tensor = preprocess_image(image_path)
predicted_class, is_car, is_taxi = predict(input_tensor, model)
print_result(predicted_class, is_car, is_taxi)
