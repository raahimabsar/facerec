# Benchmarking the Face Recognition Model
This project focuses on evaluating the accuracy and performance of a cutting-edge face recognition model 
using synthetic face images. By generating synthetic images with varying poses and feeding them into the model,
we aim to assess the model's capability to accurately distinguish between similar and different faces.


# Objective
The primary goal of this project is to benchmark the face recognition model's accuracy by utilizing synthetic face images. 
These synthetic images are designed to mimic real-world scenarios where facial poses and expressions can vary significantly. 
The model's output, which is a metric known as "face distance," indicates the dissimilarity between pairs of compared images. 


# Methodology and Steps 
We use the state of the art eg3d generative model (GAN) to create synthetic faces at variables poses.
Refer to the following repository for more information:

https://github.com/NVlabs/eg3d

Use the above model to generate image strips at desired pose intervals and store in a local directory.
A sample of image strips used in this test is available in test_known folder above.

![synthetic_image](test_known/seed0019.png)

Clone this repository and change the path of the generated faces in 
main.py to reflect the path to your generated faces directory. 
After making the changes, run the main.py file to generate the results.

# Results
The script should generate a graph that compares Face distance to Pose Difference.
Refer to the sample output in Graph2.png:

![Graph2](Graph2.png)


This result was obtained by running the script 
on 150 different synthetic face image strips with a consecutive 0.4 pose difference. 
A higher face distance suggests a greater dissimilarity between the images, suggesting that it 
becomes harder for the model to accurately predict the same person with a different pose.


