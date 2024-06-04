![Avaliação Global](img/avaliação.jpg)


## Integrantes: 
- Joyce da Costa Dias
- Vitor Oliveira

Este script Python utiliza dados sobre pinguins do Arquipélago Palmer para treinar modelos de classificação e permitir a classificação de dados inseridos pelo usuário.


## Resumo do código: 
1. **Importação de Bibliotecas:**
   - **pandas:** Para manipulação de dados.
   - **train_test_split:** Para dividir os dados em conjuntos de treinamento e teste.
   - **DecisionTreeClassifier:** Para o modelo de Árvore de Decisão.
   - **KNeighborsClassifier:** Para o modelo k-Nearest Neighbors.
   - **classification_report:** Para avaliar o desempenho dos modelos.

2. **Leitura dos Dados:**
   - Os dados são lidos de um arquivo CSV hospedado online.

3. **Mapeamento dos Dados:**
   - Os valores categóricos para ilha, sexo e espécie são mapeados para valores numéricos.

4. **Reordenação das Colunas:**
   - As colunas do DataFrame são reordenadas para seguir uma ordem específica.

5. **Separação dos Dados:**
   - Os dados são divididos em conjuntos de treinamento (80%) e teste (20%).

6. **Treinamento dos Modelos:**
   - Modelos de Árvore de Decisão e k-Nearest Neighbors são treinados, mas foram usados dois para comparar quais são os melhores resultados.

7. **Avaliação dos Modelos:**
   - As métricas de avaliação (precisão, recall, etc.) são calculadas para ambos os modelos.

8. **Classificação de Dados do Usuário:**
   - O usuário pode inserir dados arbitrários para prever a espécie de pinguim usando os modelos treinados.

---

### Executando no Terminal:

1. Certifique-se de ter o Python instalado em seu sistema.
2. Abra um terminal e navegue até o diretório onde o script Python está localizado.
3. Execute o script usando o seguinte comando:
   ```
   python arquivo.py
   ```
4. Siga as instruções apresentadas no terminal para inserir os dados do pinguim quando solicitado.

### Executando no Google Colab:

1. Abra o Google Colab em seu navegador.
2. Crie um novo notebook Python.
3. Copie e cole o código fornecido em uma célula do notebook ou exporte o arquivo.
4. Execute a célula.
5. Siga as instruções apresentadas na saída para inserir os dados do pinguim quando solicitado.

---