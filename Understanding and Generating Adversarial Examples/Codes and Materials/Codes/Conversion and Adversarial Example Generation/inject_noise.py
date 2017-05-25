import csv

def sign(x):
    if float(x)==float(0): return 1
    else : return float(x)/abs(float(x))

def adv_example(e):
    # Read the test Files
    testImages_file = open('testImages.csv','rb')
    testImages_reader = csv.reader(testImages_file, delimiter=',')
    testImages_data = []
    for x in testImages_reader:
        testImages_data.append(x)

    # Read delta J/ delta x file
    grad_file = open('image_noise.csv', 'rb')
    grad_reader = csv.reader(grad_file, delimiter=',')
    grad_data =[]
    for x in grad_reader:
        grad_data.append(x)

    # Result Noise Data
    result_noisy_data = []
    for i in range(len(testImages_data)):
        result_noisy_data.append([])
        for j in range(len(testImages_data[i])):
            x = testImages_data[i][j]
            dJ_by_dtheta = grad_data[i][j]
            x_cap = float(x) + e * sign(dJ_by_dtheta)
            result_noisy_data[i].append(x_cap)

    print ("Number of rows : " + str(len(result_noisy_data)))
    print ("Number of columns : " + str(len(result_noisy_data[0])))
    with open("adversarial_noise_"+str(e)+".csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(result_noisy_data)

adv_example(0.0025)
adv_example(0.025)
adv_example(0.5)