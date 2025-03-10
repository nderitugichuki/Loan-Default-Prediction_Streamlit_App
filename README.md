# Loan-Default-Prediction_App  

This project is a machine learning-powered web application designed to predict the likelihood of a loan applicant defaulting on their loan. It uses a trained **Random Forest Classifier** to analyze various financial and personal attributes and provide an estimated risk assessment. The application is built with **Streamlit** for an interactive web interface and can be deployed using **Docker** for scalability.  

## Project Overview  

The goal of this project is to assist financial institutions and lenders in evaluating loan applicants by predicting whether they are likely to default based on historical data. The model considers multiple factors such as income, credit score, loan amount, employment status, and debt-to-income ratio to make informed predictions.  

## Key Features  

- User-friendly web interface built with **Streamlit**  
- Accepts both numerical and categorical inputs  
- Predicts loan default probability using **machine learning**  
- Deployable as a **Docker container** for scalability  
- Provides a detailed prediction based on user input  

## Technologies Used  

- **Python** (Pandas, NumPy, Scikit-learn)  
- **Machine Learning** (Random Forest Classifier)  
- **Streamlit** (Web-based user interface)  
- **Docker** (Containerized deployment)  
- **GitHub** (Version control and collaboration)  

## Dataset and Features  

The model is trained on a dataset containing financial and demographic data, with key features including:  

- **Age** – Borrower’s age  
- **Income** – Monthly income of the borrower  
- **Loan Amount** – Total loan amount requested  
- **Credit Score** – Borrower’s credit rating  
- **Months Employed** – Duration of employment  
- **Debt-to-Income Ratio (DTI Ratio)** – Ratio of debt to income  
- **Employment Type** – Type of employment (e.g., salaried, self-employed)  
- **Marital Status** – Marital status of the applicant  
- **Loan Purpose** – The purpose for which the loan is being taken  
- **Has Co-Signer** – Indicates whether the borrower has a co-signer  
- **Default** – Target variable (0 = No Default, 1 = Default)  

## Model Performance  

- **Accuracy:** 88.7%  
- **Precision (Default Class):** 61%  
- **Recall (Default Class):** 5%  
- **Confusion Matrix:** Shows correct vs. incorrect classifications  

## How to Run the Application  

### 1. Clone the Repository  

```bash
git clone https://github.com/nderitugichuki/Loan-Default-Prediction_App.git
cd Loan-Default-Prediction_App
```

### 2. Install Dependencies  

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App  

```bash
streamlit run app.py
```

## Deploying with Docker  

To build and run the application inside a container, use the following commands:  

```bash
docker build -t loan-default-app .
docker run -p 8501:8501 loan-default-app
```

## Future Improvements  

- Enhance feature engineering and data preprocessing  
- Improve model performance with hyperparameter tuning  
- Integrate real-time model retraining with **MLflow** or **BentoML**  
- Deploy to cloud platforms for broader accessibility  

## Contributing  

Contributions are welcome. If you’d like to improve this project, feel free to fork the repository, create a new branch, and submit a pull request.  

## License  

This project is licensed under the MIT License.  

