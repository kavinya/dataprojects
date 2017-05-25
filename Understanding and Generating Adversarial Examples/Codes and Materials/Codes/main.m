
%% Initialization
clear; close all; clc

%% Loading X and Y values (Lables and Images)
data = load('trainImages.csv');
data_labels = load('trainLabels.csv');
X = data(:,:);
y = data_labels(:,1);

%% Logistic Regression

%  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);

% Add x0 of y = wx + bx0 where x0 = 1
X = [ones(m, 1) X];

% Initialize theta (weight - w) to zeros 
initial_theta = zeros(n + 1, 1);

% Compute and display initial cost and gradient
[cost, grad] = costFunction(initial_theta, X, y);

%% Finding optimal w

%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

[theta, cost] = ...
	fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);

%% Store theta
csvwrite('trained_theta.csv',theta)
fprintf('Stored theta data');

%% Store dJ/dtheta
z = transpose(y)*(X*theta);
% Differentiate J w.r.t x to get the noise values
grad_noise = sigmoid(z) * exp(-z) * (-(y)*transpose(theta));
% Write noise values to a file.
csvwrite('image_noise.csv',grad_noise);
fprintf('Stored image noise data');

%% Predict and check accuracy for same data
p = predict(theta, X);
fprintf('\nTraining Accuracy: %f\n', mean(double(p == y)) * 100);
plotData(X,p);
%% Common Metrics for Test Dataset
data_labels = load('testLabels.csv');
y = data_labels(:,1);

%% Predict training dataset and find its accuracy.
data = load('testImages.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Accuracy: %f\n', mean(double(p == y)) * 100);
plotData(X,p);
%% Predict training dataset and find its accuracy.
data = load('adversarial_noise_0.0025.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Adversarial Accuracy - 0.0025 : %f\n', mean(double(p == y)) * 100);
plotData(X,p);
%% Predict training dataset and find its accuracy.
data = load('adversarial_noise_0.025.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Adversarial Accuracy - 0.025 : %f\n', mean(double(p == y)) * 100);
plotData(X,p);
%% Predict training dataset and find its accuracy.
data = load('adversarial_noise_0.5.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Adversarial Accuracy - 0.5 : %f\n', mean(double(p == y)) * 100);
plotData(X,p);