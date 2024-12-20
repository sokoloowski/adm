## LSTM Model

### Utilizing Sequential Nature of Data

The biggest drawback of the dense model is that it is not the best solution for utilizing sequentiality. To address this challenge, we applied recurrent layers—more specifically, LSTM. Since text data often contains two-way word dependencies, we applied Bidirectional LSTM. This type of layer provides the capability to take into account both local and more global (learned in the past) patterns in the data.

### Model Architecture

However, the computational requirements of such models are high and require significant resources. Because of that, we needed to use a more powerful machine with GPU acceleration. We trained and evaluated the model using an NVIDIA GeForce RTX 3090 with 24GB of GPU memory. This setup allowed for training the model 30x faster (from 30 minutes per epoch to 1 minute).

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

The achieved results were better than all previous ones, but only by a few percent. However, this issue can depend on the quality of the data and will be further discussed in the summarization chapter. The learning curve wasn't as smooth this time, and the model showed signs of overfitting after the first 30 epochs.

![While the learning curve is not as elegant as that observed in [@fig:dense-learning-curve], it nevertheless demonstrates potential.](images/lstm_accuracy.png){#fig:lstm-learning-curve width=60%}

![The `technology` class is still the most commonly confused. However, there has been a noticeable improvement in classification.](images/lstm_confusion_matrix.png){#fig:lstm-confusion-matrix width=100%}

![Using the LSTM model, the `technology` class eventually achieved 90% of the AUC.](images/roc_lstm.png){#fig:lstm-roc width=50%}
