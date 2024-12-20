## Classification

Classification is a supervised learning technique used to predict the category of a given data point based on its features. Categories can be binary (e.g., spam vs. non-spam) or multi-class (e.g., cat, dog, horse). The goal of classification is to develop a model that can accurately predict the category of new data points. There are many classification algorithms, each with its own strengths and weaknesses. Common algorithms include **logistic regression**, **decision trees**, and **support vector machines (SVMs)**.

### Results from Classifiers

The results presented in [@tbl:classification-brown] demonstrate the influence of text representation on the performance of different classifiers. The **SGD classifier** achieved the highest accuracy with *tf-idf* (76.1%), outperforming other models. **Logistic regression** with cross-validation and **SVC** also showed strong performance, with accuracies of 75.74% and 75.68% for *tf-idf*, respectively. These results suggest that *tf-idf* consistently enhances classifier performance across different models. On the other hand, the **decision tree classifier** performed poorly, with accuracies of 57.25% for Bag of Words and 56.19% for *tf-idf*, indicating that decision trees are less effective for text classification in this context. Overall, models such as the SGD classifier and logistic regression with cross-validation performed best with *tf-idf*, highlighting its effectiveness as a text representation method.

|                     | Accuracy for Bag of Words | Accuracy for *tf-idf*  |
| ------------------: | :-----------------------: | :--------------------: |
| Logistic Regression |      70.16% (`saga`)      |    75.46% (`saga`)     |
| Logistic Reg. w/ CV |   **74.79%** (`lbfgs`)    | 75.74% (`sag`/`saga`)  |
|                 SVC |      73.91% (`rbf`)       |     75.68% (`rbf`)     |
|          Linear SVC |  67.43% (`square_hinge`)  |    75.46% (`hinge`)    |
|                 SGD |    68.83% (`log_loss`)    | **76.1%** (`log_loss`) |
|       Decision Tree |      57.25% (`gini`)      |    56.19% (`gini`)     |
|       Random Forest |      72.87% (`gini`)      |    73.03% (`gini`)     |

: **Accuracy of the classifiers for Bag of Words and *tf-idf* representations after reducing the dataset's dictionary with the Brown corpus.** {#tbl:classification-brown}

The classification accuracy of various models is further illustrated in [@tbl:classification-count], which employs both Bag of Words and *tf-idf* representations after reducing the dataset to the first 10,000 words. **Logistic regression with cross-validation** achieved the highest accuracy for Bag of Words (77.3%) and performed similarly with *tf-idf* (78.59%). The **SGD classifier** also performed well, with 78.61% accuracy for *tf-idf*, slightly outperforming all other models. Notably, logistic regression showed the largest improvement when switching from Bag of Words (72.45%) to *tf-idf* (78.71%) using the `newton-cg` solver.

|                     | Accuracy for Bag of Words |  Accuracy for *tf-idf*   |
| ------------------: | :-----------------------: | :----------------------: |
| Logistic Regression |      72.45% (`saga`)      | **78.71%** (`newton-cg`) |
| Logistic Reg. w/ CV |     **77.3%** (`sag`)     |     78.59% (`lbfgs`)     |
|                 SVC |      75.94% (`rbf`)       |    77.24% (`linear`)     |
|          Linear SVC |  68.31% (`square_hinge`)  |     78.19% (`hinge`)     |
|                 SGD |    70.86% (`log_loss`)     |   78.61% (`log_loss`)    |
|       Decision Tree |      58.4% (`gini`)       |     58.24% (`gini`)      |
|       Random Forest |      75.32% (`gini`)      |     74.61% (`gini`)      |

: **Accuracy of the classifiers for Bag of Words and *tf-idf* representations after reducing the dataset to the first 10,000 words.** {#tbl:classification-count}

Other classifiers, such as **SVC** and **Linear SVC**, showed consistent performance. **SVC** achieved 75.94% accuracy for Bag of Words and 77.24% for *tf-idf*, while **Linear SVC** performed similarly, with 68.31% for Bag of Words and 78.19% for *tf-idf*. The **decision tree classifier** and **random forest classifier** showed lower accuracy across both representations. The decision tree achieved 58.4% for Bag of Words and 58.24% for *tf-idf*, while the random forest reached 75.32% for Bag of Words and 74.61% for *tf-idf*. These results indicate that while most models benefit from the *tf-idf* representation, tree-based models continue to underperform relative to other classifiers.

[@tbl:classification-wordnet] illustrates the classification accuracy of various models using Bag of Words and *tf-idf* representations after reducing the dataset’s dictionary with the **WordNet** corpus. **Logistic regression with cross-validation** achieved the highest accuracy for Bag of Words (75.18%) and showed strong performance with *tf-idf* (76.73%). The model demonstrated a notable improvement when switching from Bag of Words to *tf-idf*, achieving 77.61% accuracy.

|                     | Accuracy for Bag of Words |  Accuracy for *tf-idf*   |
| ------------------: | :-----------------------: | :----------------------: |
| Logistic Regression |      70.91% (`sag`)       | **77.61%** (`newton-cg`) |
| Logistic Reg. w/ CV |    **75.18%** (`sag`)     |   76.73% (`newton-cg`)   |
|                 SVC |      74.26% (`rbf`)       |      77.01% (`rbf`)      |
|          Linear SVC |  67.09% (`square_hinge`)  |     75.32% (`hinge`)     |
|                 SGD |    68.96% (`log_loss`)    |     77.09% (`hinge`)     |
|       Decision Tree |      56.66% (`gini`)      |     55.86% (`gini`)      |
|       Random Forest |      73.58% (`gini`)      |     72.97% (`gini`)      |

: **Accuracy of the classifiers for Bag of Words and *tf-idf* representations after reducing the dataset’s dictionary with the WordNet corpus.** {#tbl:classification-wordnet}

The **SVC** also showed strong performance, achieving 74.26% for Bag of Words and 77.01% for *tf-idf*. **Linear SVC** and **SGD classifier** showed moderate results with 67.09% and 68.96% for Bag of Words, respectively, and improved to 75.32% and 77.09% with *tf-idf*. The **decision tree classifier** and **random forest classifier** exhibited the lowest performance, with the decision tree achieving 56.66% for Bag of Words and 55.86% for *tf-idf*, and the random forest reaching 73.58% for Bag of Words and 72.97% for *tf-idf*. These results suggest that most classifiers benefit from the *tf-idf* representation, though tree-based models continue to underperform compared to other algorithms.
