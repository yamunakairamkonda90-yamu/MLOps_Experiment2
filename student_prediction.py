from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4], [5]]
y = [35, 45, 55, 65, 75]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[6]])
print("Study hours: 6")
print("Predicted marks:", prediction[0]) 
