## Classification

Classification is a supervised learning technique that is used to predict the category of a given data point. The categories are often binary (e.g., spam/not spam), but can also be multi-class (e.g., cat, dog, horse). The objective of classification is to develop a model that can accurately predict the category of a new data point based on its features. There are many different classification algorithms, each with its own strengths and weaknesses. Some of the most popular classification algorithms include logistic regression, decision trees, and support vector machines.

The results presented in [@tbl:classification-brown] highlight the impact of text representation on the performance of various classifiers. SGD classifier achieved the highest accuracy with *tf-idf* (76.1%), outperforming other models, while logistic regression with cross-validation and SVC also demonstrated strong performance with accuracies of 75.74% and 75.68% for *tf-idf*, respectively. These results suggest that *tf-idf* consistently improves classifier performance across different models. On the other hand, Decision Tree classifier performed poorly, with accuracies of 57.25% for bag of words and 56.19% for *tf-idf*, indicating that decision trees are less effective for text classification tasks in this context. Overall, models such as SGD classifier and logistic regression with cross-validation performed best with *tf-idf*, highlighting its superiority as a text representation method.

|                          | Accuracy for bag of words | Accuracy for *tf-idf*  |
| -----------------------: | :-----------------------: | :--------------------: |
|     `LogisticRegression` |      70.16% (`saga`)      |    75.46% (`saga`)     |
|   `LogisticRegressionCV` |   **74.79%** (`lbfgs`)    | 75.74% (`sag`/`saga`)  |
|                    `SVC` |      73.91% (`rbf`)       |     75.68% (`rbf`)     |
|              `LinearSVC` | 67.43% (`squared_hinge`)  |    75.46% (`hinge`)    |
|          `SGDClassifier` |    68.83% (`log_loss`)    | **76.1%** (`log_loss`) |
| `DecisionTreeClassifier` |      57.25% (`gini`)      |    56.19% (`gini`)     |
| `RandomForestClassifier` |      72.87% (`gini`)      |    73.03% (`gini`)     |

: Accuracy of the classifiers for the bag of words and *tf-idf* representations after reducing dataset's dictionary with Brown corpus. {#tbl:classification-brown}

The classification accuracy of various models is presented in [@tbl:classification-count], which employs bag of words and *tf-idf* representations after the dataset has been reduced to the first 10,000 words. Logistic regression with cross-validation achieved the highest accuracy for bag of words (77.3%) and performed similarly with *tf-idf* (78.59%). SGD classifier also performed well, with 78.61% accuracy for *tf-idf*, slightly outperforming all other models. Notably, logistic regression demonstrated the largest improvement when switching from bag of words (72.45%) to *tf-idf* (78.71%) using the `newton-cg` solver.

|                          | Accuracy for bag of words |  Accuracy for *tf-idf*   |
| -----------------------: | :-----------------------: | :----------------------: |
|     `LogisticRegression` |      72.45% (`saga`)      | **78.71%** (`newton-cg`) |
|   `LogisticRegressionCV` |     **77.3%** (`sag`)     |     78.59% (`lbfgs`)     |
|                    `SVC` |      75.94% (`rbf`)       |    77.24% (`linear`)     |
|              `LinearSVC` | 68.31% (`squared_hinge`)  |     78.19% (`hinge`)     |
|          `SGDClassifier` |    70.86 (`log_loss`)     |   78.61% (`log_loss`)    |
| `DecisionTreeClassifier` |      58.4% (`gini`)       |     58.24% (`gini`)      |
| `RandomForestClassifier` |      75.32% (`gini`)      |     74.61% (`gini`)      |

: Accuracy of the classifiers for the bag of words and *tf-idf* representations after reducing dataset to first 10,000 words. {#tbl:classification-count}

Other classifiers like SVC and Linear SVC showed consistent performance, with SVC reaching 75.94% for bag of words and 77.24% for *tf-idf*, while Linear SVC performed similarly (68.31% for bag of words and 78.19% for *tf-idf*). The Decision Tree classifier and Random Forest classifier exhibited lower accuracy across both representations, with Decision Tree classifier achieving 58.4% for bag of words and 58.24% for *tf-idf*, and Random Forest classifier reaching 75.32% for bag of words and 74.61% for *tf-idf*. These results suggest that while most models benefit from *tf-idf*, Decision Tree classifier and Random Forest classifier continue to underperform relative to other classifiers.

[@tbl:classification-wordnet] illustrates the classification accuracy of diverse models utilising bag of words and *tf-idf* representations, subsequent to the reduction of the dataset's dictionary with the WordNet corpus. Logistic Regression with cross-validation achieved the highest accuracy for bag of words (75.18%) and performed similarly with *tf-idf* (76.73%), indicating a strong overall performance across both representations. Logistic Regression showed notable improvement with *tf-idf*, reaching 77.61%, compared to 70.91% for bag of words.

|                          | Accuracy for bag of words |  Accuracy for *tf-idf*   |
| -----------------------: | :-----------------------: | :----------------------: |
|     `LogisticRegression` |      70.91% (`sag`)       | **77.61%** (`newton-cg`) |
|   `LogisticRegressionCV` |    **75.18%** (`sag`)     |   76.73% (`newton-cg`)   |
|                    `SVC` |      74.26% (`rbf`)       |      77.01% (`rbf`)      |
|              `LinearSVC` | 67.09% (`squared_hinge`)  |     75.32% (`hinge`)     |
|          `SGDClassifier` |    68.96% (`log_loss`)    |     77.09% (`hinge`)     |
| `DecisionTreeClassifier` |      56.66% (`gini`)      |     55.86% (`gini`)      |
| `RandomForestClassifier` |      73.58% (`gini`)      |     72.97% (`gini`)      |

: Accuracy of the classifiers for the bag of words and *tf-idf* representations after reducing dataset's dictionary with WordNet. {#tbl:classification-wordnet}

SVC also performed well, achieving 74.26% for bag of words and 77.01% for *tf-idf*, while Linear SVC and SGD classifier showed moderate results with 67.09% and 68.96% for bag of words, respectively, and improved to 75.32% and 77.09% with *tf-idf*. Decision Tree classifier and Random Forest classifier exhibited the lowest performance, with Decision Tree classifier achieving 56.66% for bag of words and 55.86% for *tf-idf*, and Random Forest classifier showing 73.58% for bag of words and 72.97% for *tf-idf*. These results suggest that most classifiers benefit from the *tf-idf* representation, but tree-based models continue to underperform compared to others.
