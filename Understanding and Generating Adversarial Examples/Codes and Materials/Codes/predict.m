function p = predict(theta, X)
p = round(sigmoid(X * theta));
end
