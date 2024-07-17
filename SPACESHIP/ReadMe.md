Spaceship Titanic: Predicting Alternate Dimension Transportation 🚀
Welcome to my Data Science and Machine Learning portfolio! This repository houses my work on the Kaggle Spaceship Titanic competition.
In this cosmic mystery, we aim to predict which passengers were transported to an alternate dimension during the Spaceship Titanic’s collision with a spacetime anomaly.
Key Insights & Results
One of the most critical factors in predicting passenger transportation was the “CryoSleep” feature, showing a strong correlation of over 0.4. Passengers who opted for cryosleep were more likely to be transported to an alternate dimension.
Through rigorous analysis and modeling, I achieved a commendable score of 0.80, securing a top 28% ranking among 2062 teams.
My model’s predictions played a vital role in the rescue mission’s success.
About the Challenge 🌟
The Spaceship Titanic competition tasks us with solving a cosmic mystery. By leveraging data science skills, we aim to predict the fate of passengers who encountered a spacetime anomaly during their voyage.

Goal: Classify passengers as transported or not transported to an alternate dimension.
Datasets:
train.csv: Training dataset with personal records and ground truth labels.
test.csv: Test dataset for predictions.
sample_submission.csv: Sample submission file with the required format.
My Approach 🚀
Reading Datasets: I began by loading the provided datasets, both the training and test data.
Checking Class Distribution: To understand the balance between transported and non-transported passengers, I examined the distribution of classes in the training dataset.
Handling Missing Values: I addressed missing data in the dataset, ensuring that no valuable information was lost.
Making the Correlation Heatmap: I created a correlation heatmap to visualize relationships between different features, highlighting the strong correlation between “CryoSleep” and passenger transportation.
Feature Engineering: To improve model performance, I engineered new features. For example, I extracted additional information from the “Cabin” column, breaking it down into “Deck,” “Num,” and “Side” components.
One-Hot Encoding: I prepared the data for modeling by performing one-hot encoding, a necessary step for many machine learning models.
Acknowledgments 🙌
I’d like to express my gratitude to the Kaggle community, fellow competitors, and the organizers of the Spaceship Titanic challenge. Your insights and support were invaluable!

Feel free to explore the code and analysis in my Kaggle Notebook.
