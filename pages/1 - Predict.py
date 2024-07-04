import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.metrics import classification_report
import pickle
import streamlit as st

data = pd.read_csv('data/penguins.csv')
X = data.iloc[:,1:-3]
y = data.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,stratify=y)

# preprocess = make_column_transformer(
#     (StandardScaler(), ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']),
#     (OneHotEncoder(drop='first',handle_unknown='ignore'), ['island','sex']))

# X_train_preprocess = preprocess.fit_transform(X_train)
# # X_test_preprocess = preprocess.transform(X_test)

# # rf = RandomForestClassifier(max_depth=3)
# # rf.fit(X_train_preprocess,y_train)

# # y_pred = rf.predict(X_test_preprocess)
# # print(classification_report(y_test, y_pred, target_names=y_test.unique()))

# # with open("data/model.pkl", "wb") as f:
# #     pickle.dump(rf, f)

# with open("data/model.pkl", "rb") as f:
#     model = pickle.load(f)

# st.write('Now lets predict for a given user input and find out the species of the penguin')

# island = st.selectbox(
#    "Island",
#    X.island.unique(),
#    index=0,
#    placeholder="Choose island where penguin resides",
# )

# bill_length_mm = st.slider("Bill length", 0, 100, 50)

# bill_depth_mm = st.slider("Bill depth", 0, 50, 25)

# flipper_length_mm = st.slider("Flipper length", 100, 250, 125)

# body_mass_g = st.slider("Body Mass", 2000, 7000, 2500)

# sex = st.selectbox(
#    "Flipper length",
#    ['Male', 'Female'],
#    index=0,
#    placeholder="Male or Female",
# )

# st.write(f'You selected that the {sex} penguin in {island} island has {bill_length_mm}mm bill length, {bill_depth_mm}mm bill depth, {flipper_length_mm}mm flipper length with {body_mass_g}g of body mass')


# testing = pd.DataFrame([[island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex]],columns=['island',	'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex'])
# testing_preprocess = preprocess.transform(testing)

# if st.button("Predict"):
#     st.write(f'My model predict that the species of the penguin is {model.predict(testing_preprocess)[0]}')
# else:
#     st.write("Click on Predict to view the species of the penguin")
