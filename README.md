# Employee Retention Project

## Overview

This project aims to analyze and predict employee retention using various machine learning techniques. The project includes exploratory data analysis (EDA), model selection and building, and the deployment of a REST API with a user-friendly UI.

## Table of Contents
- [Project Structure](#project-structure)
- [Data Description](#data-description)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Selection and Building](#model-selection-and-building)
- [Clustering and Classification](#clustering-and-classification)
- [Deployment](#deployment)
- [How to Run](#how-to-run)
- [Contributors](#contributors)
- [License](#license)

## Project Structure
```
Employee Retention/
├── .idea/
├── Analysis.ipynb
├── EndtoEndML_v11/
├── ModelSelectionandbuilfing.ipynb
├── hr_employee_churn_data.csv
├── readme.md
├── v11/
```


- `.idea/`: IDE specific files
- `Analysis.ipynb`: Notebook for EDA and initial analysis
- `EndtoEndML_v11/`: Directory containing end-to-end ML pipeline scripts
- `ModelSelectionandbuilfing.ipynb`: Notebook for model selection and building
- `hr_employee_churn_data.csv`: Dataset
- `readme.md`: Project README file
- `v11/`: Directory containing version 11 of the project scripts

## Data Description

The dataset `hr_employee_churn_data.csv` contains employee data with various features that help in analyzing and predicting employee retention. The key features include:
- Employee ID
- Age
- Department
- Job Role
- Monthly Income
- Attrition (Yes/No)
- ...and many more.

## Exploratory Data Analysis (EDA)

Initial data exploration and visualization are performed to understand the underlying patterns and relationships in the data. Key steps include:
- Data cleaning and preprocessing
- Statistical summary of features
- Visualizations (e.g., histograms, bar plots, box plots)
- Correlation analysis

## Model Selection and Building

Several machine learning models are evaluated for predicting employee retention. The models include:
- Logistic Regression
- Decision Trees
- Random Forest
- XGBoost

The performance of these models is compared using metrics such as accuracy, precision, recall, and F1-score.

## Clustering and Classification

### K-means Clustering

K-means clustering is employed for employee segmentation. This helps in identifying distinct groups of employees based on their attributes, which can be useful for targeted retention strategies.

### Classification

Random Forest and XGBoost classifiers are used for predicting employee retention. These models are chosen for their robustness and ability to handle complex data structures.

## Deployment

The final model is deployed using a REST API built with Flask. A user-friendly UI is developed using Streamlit, providing an interactive way to predict employee retention.

The application is thoroughly tested and deployed on AWS EC2 with Nginx as the web server. The deployment steps include:
- Setting up an EC2 instance
- Configuring Nginx as a reverse proxy
- Deploying the Flask app and Streamlit UI

## How to Run

### Prerequisites

- Python 3.7+
- Flask
- Streamlit
- Scikit-learn
- XGBoost
- AWS Account (for deployment)

### Local Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/saurin16/Employee_retention_Analysis_and_prediction.git
    cd Repo_name
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Flask API:
    ```sh
    python app.py
    ```

4. Run the Streamlit UI:
    ```sh
    streamlit run ui.py
    ```

5. Open your browser and go to `http://localhost:8501` to interact with the UI.

### Deployment on AWS EC2

1. Launch an EC2 instance and SSH into it.
2. Install necessary packages and clone the repository on the instance.
3. Configure Nginx as a reverse proxy for the Flask app.
4. Run the Flask app and Streamlit UI on the instance.

## Contributors

- [SAURIN PATEL](https://github.com/saurin16)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
