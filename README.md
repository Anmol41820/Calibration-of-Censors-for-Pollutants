# **Calibration of Censors for Pollutants - Course Group Project**
#### Mentor: Prof. Purushottam Kar, IIT Kanpur
#### Project Duration: Jan '23 - May '23

## Project Overview
In this course group project, we aimed to calibrate sensors for pollutants, specifically focusing on predicting ozone and nitrogen dioxide levels. We employed various regression models to achieve this goal and evaluated their performance based on Mean Absolute Error (MAE). Our project included the use of Ridge, Lasso, ElasticNet, Linear Regression for predicting pollutants based on 4 voltage readings. Additionally, we explored non-linear models, such as K-nearest neighbors (KNN) and Random Forest, using multiple features, including voltages, timestamp, temperature, and humidity.

## Project Objectives
Predict ozone and nitrogen dioxide levels accurately.
Explore the effectiveness of different regression models, both linear and non-linear.
Identify the best-performing model and its hyperparameters.
Calculate and minimize the Mean Absolute Error (MAE) as the evaluation metric.
## Methodology
### - Linear Regression Models
We utilized Ridge, Lasso, ElasticNet, and Linear Regression models to predict pollutant levels based solely on the 4 voltage readings. We experimented with varying regularization coefficients (0.1, 1, 10) to find the best-performing model. Ridge regression with a coefficient of 10 emerged as the best option in the linear models category based on its MAE.

### - Non-Linear Models
For non-linear modeling, we incorporated K-nearest neighbors (KNN) and Random Forest. These models were trained using not only voltage data but also additional features like timestamp, temperature, and humidity. The inclusion of these extra features aimed to capture complex relationships that may not be linear. Among the non-linear models, KNN achieved the best results in terms of MAE.

## Model Selection and Evaluation
### - Linear Regression Models:

Ridge regression with a coefficient of 10 outperformed other linear models in terms of MAE.
It provided the best balance between bias and variance and effectively captured the relationships between voltage readings and pollutant levels.
### - Non-Linear Models:

K-nearest neighbors (KNN) yielded the lowest MAE among the non-linear models.
The inclusion of additional features like timestamp, temperature, and humidity improved the model's ability to predict pollutant levels accurately.
## Conclusion
This project successfully addressed the calibration of sensors for pollutants by implementing a variety of regression models. We found that Ridge regression with a coefficient of 10 was the best-performing model in the linear regression category. In contrast, K-nearest neighbors (KNN) excelled among the non-linear models. The integration of additional environmental variables enhanced the predictive capabilities of the models, leading to more accurate predictions of ozone and nitrogen dioxide levels.

## Future Work
To further improve the calibration of sensors for pollutants, future work may include:

Exploring more complex non-linear models or deep learning techniques.
Collecting additional data and considering more features for model improvement.
Fine-tuning hyperparameters for optimal performance.
This readme file provides an overview of our project's objectives, methodologies, model selection, and outcomes, and it can be used as a reference for your GitHub repository to showcase the work accomplished during this course group project.
