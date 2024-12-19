## LSTM with attention Model

### Enhancing LSTM with Attention

While LSTMs are powerful in capturing dependencies over sequences, they may struggle to effectively focus on the most relevant parts of the input, particularly for longer sequences. To overcome this limitation, attention mechanisms are integrated with LSTMs. The attention mechanism allows the model to dynamically assign importance (weights) to different parts of the input sequence based on their relevance to the task at hand. 

#### Key Features of LSTM with Attention:

1. Selective Focus:  
   Attention enables the model to "attend" to specific parts of the input sequence rather than treating all parts equally. This is particularly useful in cases where certain parts of the input carry more significance than others.

2. Contextual Representation:  
   By computing a weighted sum of the hidden states of the LSTM, the attention mechanism provides a richer, context-aware representation of the input.

3. Scalability to Longer Sequences:  
   Attention mitigates the challenge of forgetting or diluting information in longer sequences, a common issue in vanilla LSTM models.

4. Learned Relevance:  
   The attention weights are learned during training, allowing the model to automatically determine which parts of the sequence are most important for a given task.

### Model architecture


| Layer (type)             | Output Shape       | Param #    |
| :----------------------- | :----------------- | :--------- |
| Embedding                | (None, 1072, 300) | 7,788,900  |
| SpatialDropout1D         | (None, 1072, 300) | 0          |
| Bidirectional            | (None, 1072, 256) | 439,296    |
| Dropout                  | (None, 1072, 256) | 0          |
| Bidirectional            | (None, 1072, 128) | 164,352    |
| Dropout                  | (None, 1072, 128) | 0          |
| AttentionLayer           | (None, 128)       | 129        |
| Dense                    | (None, 128)       | 16,512     |
| Dropout                  | (None, 128)       | 0          |
| Dense                    | (None, 64)        | 8,256      |
| Dropout                  | (None, 64)        | 0          |
| Dense                    | (None, 32)        | 2,080      |
| Dropout                  | (None, 32)        | 0          |
| Dense                    | (None, 5)         | 165        |
| **Total params**         | **8,419,690**     |            |
| **Trainable params**     | **630,790**       |            |
| **Non-trainable params** | **7,788,900**     |            |

: LSTM with attention model summary {#tbl:lstm-attention-model-summary}

## Results

Applying attention mechanism improved results but it wasn't significant improvement.

![While the learning curve is not as elegant as that observed in [@fig:dense-learning-curve], it nevertheless demonstrates potential.](images/lstm_accuracy.png){#fig:lstm-learning-curve widh=80%}

![The `technology` class is still the most commonly confused. However, there has been a noticeable improvement in classification.](images/lstm_confusion_matrix.png){#fig:lstm-confusion-matrix widh=80%}

![Using the LSTM model, the `technology` class eventually achieved 90% of the AUC.](images/roc_lstm.png){#fig:lstm-roc widh=80%}
