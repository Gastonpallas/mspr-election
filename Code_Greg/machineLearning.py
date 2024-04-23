import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Charger les données Excel
data = pd.read_excel('finalExcel/donneesPropres.xlsx')

# Diviser les données en attributs et étiquettes
X = data.drop(['Code région', 'Code département', 'Département'], axis=1) # Attributs
y = data['Département'] # Étiquettes

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le classificateur RandomForest
clf = RandomForestClassifier()

# Entraîner le modèle
clf.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = clf.predict(X_test)

# Calculer l'exactitude des prédictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
