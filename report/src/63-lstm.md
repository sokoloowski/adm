## LSTM Model

| Layer (type)             | Output Shape      | Param #    |
| :----------------------- | :---------------- | :--------- |
| Embedding                | (None, 1463, 300) | 24,379,800 |
| SpatialDropout1D         | (None, 1463, 300) | 0          |
| Bidirectional            | (None, 1463, 64)  | 85,248     |
| Dropout                  | (None, 1463, 64)  | 0          |
| Bidirectional            | (None, 1463, 64)  | 24,832     |
| Dropout                  | (None, 1463, 64)  | 0          |
| Bidirectional            | (None, 64)        | 24,832     |
| Dropout                  | (None, 64)        | 0          |
| Dense                    | (None, 5)         | 325        |
| **Total params**         | **24,515,037**    |            |
| **Trainable params**     | **135,237**       |            |
| **Non-trainable params** | **24,379,800**    |            |

: LSTM model summary {#tbl:lstm-model-summary}

![While the learning curve is not as elegant as that observed in [@fig:dense-learning-curve], it nevertheless demonstrates potential.](images/lstm_accuracy.png){#fig:lstm-learning-curve widh=80%}

![The `technology` class is still the most commonly confused. However, there has been a noticeable improvement in classification.](images/lstm_confusion_matrix.png){#fig:lstm-confusion-matrix widh=80%}

![Using the LSTM model, the `technology` class eventually achieved 90% of the AUC.](images/roc_lstm.png){#fig:lstm-roc widh=80%}
