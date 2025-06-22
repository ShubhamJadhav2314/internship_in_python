from joblib import load

area = int(input("Enter area: "))
rooms = int(input("Enter rooms: "))
age = int(input("Enter age: "))

model = load('model')       # Calling Linear Regression Model
prediction = model.predict([[area,rooms,age]])
print(f"The price will be ₹{prediction[0]}")