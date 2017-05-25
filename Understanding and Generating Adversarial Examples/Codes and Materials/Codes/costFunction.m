function [J, grad] = costFunction(theta, X, y)
z = transpose(y)*(X*theta);
% Error (J) is given by the soft function
J = softplus(-transpose(y)*(X*theta));
% Differentiate J w.r.t theta to get grad
grad = sigmoid(z) * exp(-z) * (-transpose(X)*y);
end
