def print_result(predicted_class, is_car, is_taxi):
    print("Predicted class index:", predicted_class)
    if is_car:
        print("Object: CAR 🚗")
        if is_taxi:
            print("Type: TAXI 🚕")
        else:
            print("Type: NOT a taxi")
    else:
        print("Object: NOT a car ❌")
