%% Initialization
clear; close all; clc

%% Common Metrics
data_theta = load('trained_theta.csv');
theta = data_theta(:,1);
data_labels = load('testLabels.csv');
y = data_labels(:,1);

%% Predict training dataset and find its accuracy.
data = load('testImages.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Accuracy: %f\n', mean(double(p == y)) * 100);

%% Predict training dataset and find its accuracy.
data = load('adversarial_noise_0.0025.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Adversarial Accuracy - 0.0025 : %f\n', mean(double(p == y)) * 100);

%% Predict training dataset and find its accuracy.
data = load('adversarial_noise_0.025.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Adversarial Accuracy - 0.025 : %f\n', mean(double(p == y)) * 100);

%% Predict training dataset and find its accuracy.
data = load('adversarial_noise_0.5.csv');
X = data(:,:);
[m, n] = size(X);
X = [ones(m, 1) X];
p = predict(theta, X);
fprintf('Testing Adversarial Accuracy - 0.5 : %f\n', mean(double(p == y)) * 100);