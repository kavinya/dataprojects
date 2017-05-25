adversarial = load('adversarial_noise_0.5.csv');
for i = 1:13007
m = adversarial(i,:);
B = reshape(m,[28,28]);
d = strcat('5_7_',num2str(i));
d = strcat(d,'.jpg');
imwrite(mat2gray(B),d);
end