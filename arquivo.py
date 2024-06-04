#importar as bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier #modelo de decisão tree
from sklearn.neighbors import KNeighborsClassifier #modelo de kneighbors classifier
from sklearn.metrics import classification_report

# Questão 2 - leitura dos dados com a biblioteca pandas
url = "https://raw.githubusercontent.com/marcelovca90-inatel/AG002/main/palmerpenguins.csv"
data = pd.read_csv(url)
print(data.columns)

# questão 3 - mapeamento da tabela
island_map = {"Biscoe": 0, "Dream": 1, "Torgersen": 2}
sex_map = {"FEMALE": 0, "MALE": 1}
species_map = {"Adelie": 0, "Chinstrap": 1, "Gentoo": 2}

# aplicação do mapeamento
data['island'] = data['island'].replace(island_map)
data['sex'] = data['sex'].replace(sex_map)
data['species'] = data['species'].replace(species_map)

# 4 - reordenação das colunas
data1 = data.reindex(columns=['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species'])
print("Todas as colunas ordenadas:")
print(data1.columns)
print("Resultado das colunas:")
print(data1.species)

# Questão 5 - separação dos dados em duas partes e dividir os dados em conjuntos de treinamento (80%) e teste (20%)
X = data.drop('species', axis=1)
y = data['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""#Resultados com o modelo: **Decision Tree**

"""

# Inicialização do modelo de Árvore de Decisão
dt_model = DecisionTreeClassifier()

# Treinamento do modelo
dt_model.fit(X_train, y_train)

# Previsões nos dados de teste
dt_predictions = dt_model.predict(X_test)


dt_report = classification_report(y_test, dt_predictions, target_names=['Adelie', 'Chinstrap', 'Gentoo'])
print("Decision Tree Classification Report:")
print(dt_report)

"""# Resultado com o modeço: **k-Nearest Neighbors**"""

# Inicialização do modelo de k-Nearest Neighbors com k=5 (por exemplo)
knn_model = KNeighborsClassifier(n_neighbors=5)

# Treinamento do modelo
knn_model.fit(X_train, y_train)

# Previsões do modelo
knn_predictions = knn_model.predict(X_test)

# Métricas da avaliação
knn_report = classification_report(y_test, knn_predictions, target_names=['Adelie', 'Chinstrap', 'Gentoo'])
print("k-Nearest Neighbors Classification Report:")
print(knn_report)

species_map_inverse = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}

# Inserção de dados
user_input = []
user_input.append(float(input("Comprimento do cúlmen (mm): ")))
user_input.append(float(input("Profundidade do cúlmen (mm): ")))
user_input.append(float(input("Comprimento da nadadeira (mm): ")))
user_input.append(float(input("Massa corporal (g): ")))

# Condição na opção ilha para que aceite somente as opções (Ilha (Biscoe, Dream, Torgersen)
while True:
    island_input = input("Ilha (Biscoe, Dream, Torgersen): ")
    if island_input in ["Biscoe", "Dream", "Torgersen"]:
        user_input.append(island_map[island_input])
        break
    else:
        print("Por favor, insira uma ilha válida.")

# Condição na opção sexo para que aceite somente as opções (FEMALE e MALE)
while True:
    sex_input = input("Sexo (FEMALE, MALE): ")
    if sex_input in ["FEMALE", "MALE"]:
        user_input.append(sex_map[sex_input])
        break
    else:
        print("Por favor, insira um sexo válido.")

# Previsão da espécie de pinguim com base nos dados inseridos usando a Árvore de Decisão
dt_prediction = dt_model.predict([user_input])
print("Espécie prevista usando Árvore de Decisão:", species_map_inverse[dt_prediction[0]])

# Previsão da espécie de pinguim com base nos dados inseridos usando k-Nearest Neighbors
knn_prediction = knn_model.predict([user_input])
print("Espécie prevista usando k-Nearest Neighbors:", species_map_inverse[knn_prediction[0]])