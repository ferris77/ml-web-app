#Description: this program detects if someone has diabetes using machine learning and python!

#Import the libraries
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#Get the data for the model
df = pd.read_csv('C:/Users/lucas/OneDrive/Documentos/venv/diabetes.csv')

#Split the data into independentent 'X' and dependente 'Y' variables
X = df.iloc[:, 0:8].values #we want the array, not the df
Y = df.iloc[:, -1].values

#Split the data into 75% training and 25% testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

#Get the feature input from the user
"""
def get_user_input():
    pregnancies = st.sidebar.slider('pregnancies', 0, 17, 3)
    glucose = st.sidebar.slider('glucose', 0, 199, 117)
    blood_pressure = st.sidebar.slider('blood_pressure', 0, 122, 72)
    skin_thickness = st.sidebar.slider('skin_thickness', 0, 99, 23)
    insulin = st.sidebar.slider('insulin', 0.0, 846.0, 30.0)
    BMI = st.sidebar.slider('BMI', 0.0, 67.1, 32.0)
    DPF = st.sidebar.slider('DPF', 0.078, 2.42, 0.3725)
    age = st.sidebar.slider('age', 21, 81, 29)

    #Store a dictionary into a variable
    
    user_data = {'pregnancies': pregnancies,
                 'glucose': glucose,
                 'blood_pressure': blood_pressure,
                 'skin_thickness': skin_thickness,
                 'insulin': insulin,
                 'BMI': BMI,
                 'DPF': DPF,
                 'age': age
                 }
    
    #Transform the data into a dataframe
    features = pd.DataFrame(user_data, index = [0])

    return features
    """

#Store the users input into a variable
#user_input = get_user_input()

#Create and train the model
RFC = RandomForestClassifier()
RFC.fit(X_train, Y_train)

#Store the models predictions in a variable
#prediction = RFC.predict(user_input)

#Saving serialized model to disk
joblib.dump(RFC, 'model.pkl')

#Loading model o compare the results
#loaded_model = joblib.load('model.py')