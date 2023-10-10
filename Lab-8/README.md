# Question-1  
## Consider the 128- dimensional feature vectors (d=128) given in the “gender.csv” file. (2 classes, male and female)
a) Use PCA to reduce the dimension from d to d‟. (Here d=128).   
b) Display the eigenvalue based on increasing order, select the d‟ of the corresponding eigenvector which is the appropriate dimension d‟ ( select d‟ S.T first 95% of λ values of the covariance matrix are considered).   
c) Use d‟ features to classify the test cases (use any classification algorithm taught in class like Bayes classifier, minimum distance classifier, and so on).

### Dataset Specifications:
Total number of samples = 800   
Number of classes = 2 (labeled as “male” and “female”)  
Samples from “1 to 400” belongs to class “male”   
Samples from “401 to 800” belongs to class “female”   
Number of samples per class = 400   
Number of dimensions = 128   
Use the following information to design classifier:  
Number of test cases (first 10 in each class) = 20   
Number of training feature vectors ( remaining 390 in each class) = 390   
Number of reduced dimensions = d‟ (map 128 to d‟ features vector)

# Question-2
## Eigenfaces-Face classification using PCA (40 classes)
a) Use the following “face.csv” file to classify the faces of 40 different people using PCA.   
b) Do not use the in-built function for implementing PCA.   
c) Use appropriate classifier taught in class (use any classification algorithm taught in class like Bayes classifier, minimum distance classifier, and so on)  
d) Refer to the following link for a description of the dataset: https://towardsdatascience.com/eigenfaces-face-classification-in-python-7b8d2af3d3ea
