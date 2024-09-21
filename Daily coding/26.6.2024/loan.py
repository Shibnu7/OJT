import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score

# Load the dataset with the correct delimiter
data = pd.read_csv('loan_data.csv', sep=',', engine='python')

# Print the first few rows of the DataFrame to check the data
print("First few rows of the DataFrame:")
print(data.head())

# Print the columns of the DataFrame to check the column names
print("Columns in the DataFrame:")
print(data.columns)

# Check if the columns are correctly parsed
if 'loan_id' in data.columns[0]:
    # Split the single column into multiple columns
    data = data[data.columns[0]].str.split(',', expand=True)
    data.columns = ['loan_id', 'loan_amount', 'interest_rate', 'term', 'income', 'credit_score', 'age', 'employment_length', 'loan_repaid']

# Print the columns after splitting
print("Columns after splitting:")
print(data.columns)

# Convert the target column to integers
data['loan_repaid'] = data['loan_repaid'].astype(int)

# Select the features which need to be used in the case
x = data[['loan_amount', 'interest_rate', 'term', 'income', 'credit_score', 'age', 'employment_length']]
y = data['loan_repaid']

# Split train_test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initiate a model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(x_train, y_train)

# Make a prediction
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Precision
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# Recall
recall = recall_score(y_test, y_pred)
print("Recall:", recall)

# F1 Score
f1score = f1_score(y_test, y_pred)
print("F1 Score:", f1score)
