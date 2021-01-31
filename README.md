# PHISHCOOP phishing website detection
Detection of phishing websites is a really important safety measure for most of the online platforms. So, as to save a platform with malicious requests from such websites, it is important to have a robust phishing detection system in place.

## DATA SELECTION

The dataset is downloaded from UCI machine learning repository. The dataset contains 31 columns, with 30 features and 1 target. The dataset has 2456 observations.

## MODELS

To fit the models over the dataset the dataset is split into training and testing sets. The split ratio is 75-25.  Where in 75% accounts to training set. 

Now the training set is used to train the classifier. The classifiers chosen is:  
### Support Vector Machine

Support vector machine with a rbf kernel and using gridsearchcv to predict best parameters for svm was a really good choice, and fitting the model with predicted best parameters I was able to get 96.47 accuracy which is pretty good.

## Variable Importance

![alt text](https://github.com/mayursaparia/detection_of_phishing_url_using_svm/blob/master/variable_Importances.png?raw=true)

#### NOTE

Logistic Regression and Random Forest Classification models are in process.

