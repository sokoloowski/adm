## LSTM Model

### Utilizing sequentail nature of data

The biggest drawback of dense model is that it is not the best solution to utilize sequentiality. To adress this challenge we applied recurrent layers, more accurately speaking LSTM. Since in text there are some so called two ways words dependencies we applied Biderectional-LSTM. This type of layer provide capability of taking into account as well local and more global (learned in the past) patterns in data.

### Model architecture

However computational requirements of such models require a lot of resources. Because of that we needed to use more powerful machine and GPU acceleration. We trained and evaluted the model using NVIDIA GeForce RTX 3090 with 24GB GPU memory. It allowed for training such model 30x faster (from 30 minutes per epoch to 1 minute).

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

### Results

Achieved results were better than all previous ones, but only by few percent. However this problem can depend on the quality of the data and will be further and wider discussed on the summarization chapter. Learning curve was't so smooth this time, and model showed signs of overfitting after first 30 epochs.

![While the learning curve is not as elegant as that observed in [@fig:dense-learning-curve], it nevertheless demonstrates potential.](images/lstm_accuracy.png){#fig:lstm-learning-curve width=60%}

![The `technology` class is still the most commonly confused. However, there has been a noticeable improvement in classification.](images/lstm_confusion_matrix.png){#fig:lstm-confusion-matrix width=100%}

![Using the LSTM model, the `technology` class eventually achieved 90% of the AUC.](images/roc_lstm.png){#fig:lstm-roc width=50%}
