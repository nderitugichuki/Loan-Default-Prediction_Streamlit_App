import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('loan_default_model.pkl', 'rb'))

# 🎯 App Title with Emoji Styling
st.title("🔮 Loan Default Prediction App 💰📉")

st.markdown("### **📊 Enter Customer Details Below:**")

# Collect user inputs for all 16 features
age = st.number_input("👤 Age", min_value=18, max_value=100, step=1)
income = st.number_input("💵 Monthly Income ($)", min_value=1000, max_value=100000, step=100)
loan_amount = st.number_input("🏦 Loan Amount ($)", min_value=1000, max_value=500000, step=100)
credit_score = st.number_input("📈 Credit Score", min_value=300, max_value=850, step=1)
months_employed = st.number_input("🧑‍💼 Months Employed", min_value=0, max_value=600, step=1)
num_credit_lines = st.number_input("💳 Number of Credit Lines", min_value=0, max_value=50, step=1)
interest_rate = st.number_input("📉 Interest Rate (%)", min_value=0.0, max_value=30.0, step=0.1)
loan_term = st.number_input("📆 Loan Term (Months)", min_value=6, max_value=360, step=6)
dti_ratio = st.number_input("⚖️ Debt-to-Income Ratio (%)", min_value=0.0, max_value=100.0, step=0.1)

# Categorical features (dropdowns with emojis)
marital_status = st.selectbox("💍 Marital Status", ["Single", "Married", "Divorced"])
education = st.selectbox("🎓 Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
employment_type = st.selectbox("💼 Employment Type", ["Salaried", "Self-Employed", "Unemployed"])
loan_purpose = st.selectbox("🎯 Loan Purpose", ["Home", "Car", "Business", "Personal"])
has_mortgage = st.selectbox("🏠 Has Mortgage?", ["No", "Yes"])
has_dependents = st.selectbox("👶 Has Dependents?", ["No", "Yes"])
has_cosigner = st.selectbox("🤝 Has Co-Signer?", ["No", "Yes"])

# Convert categorical inputs to numbers
marital_mapping = {"Single": 0, "Married": 1, "Divorced": 2}
education_mapping = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
employment_mapping = {"Salaried": 0, "Self-Employed": 1, "Unemployed": 2}
loan_purpose_mapping = {"Home": 0, "Car": 1, "Business": 2, "Personal": 3}
binary_mapping = {"No": 0, "Yes": 1}

marital_status = marital_mapping[marital_status]
education = education_mapping[education]
employment_type = employment_mapping[employment_type]
loan_purpose = loan_purpose_mapping[loan_purpose]
has_mortgage = binary_mapping[has_mortgage]
has_dependents = binary_mapping[has_dependents]
has_cosigner = binary_mapping[has_cosigner]

# Prepare input array (ensure all 16 features are included)
input_data = np.array([[age, income, loan_amount, credit_score, months_employed,
                        num_credit_lines, interest_rate, loan_term, dti_ratio, education,
                        employment_type, marital_status, has_mortgage, has_dependents,
                        loan_purpose, has_cosigner]])

# 🎯 Prediction Button
if st.button("🔍 Predict Loan Default"):
    prediction = model.predict(input_data)
    result = "❌ Default" if prediction[0] == 1 else "✅ No Default"
    st.success(f"**Prediction:** {result}")

    # Add an explanation
    if prediction[0] == 1:
        st.warning("⚠️ This loan is likely to default. Consider reviewing the credit score, income, and DTI ratio.")
    else:
        st.success("🎉 This loan is likely to be repaid! Looks like a safe bet.")

# Footer
st.markdown("---")
st.markdown("🔗 Built with **Streamlit** | Model: **RandomForestClassifier**")
