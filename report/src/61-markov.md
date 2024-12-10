### Hidden Markov Models

A Hidden Markov Model (HMM) is a statistical model used to represent systems that exhibit temporal or sequential characteristics. It is widely applied in fields such as speech recognition, natural language processing, bioinformatics, and pattern recognition.
We decided to apply them as feature extractor for text classification task. We fited model with TF-IDF vectors and then compute hidden states. Then we passed this hidden states as input to XGBoost classifier. The proposed method resulted with below results.

![](images/hmm_xgb_confusion_matrix.png){#fig:hmm-xgboost-confusion-matrix widh=80%}

![](images/roc_hmm_xgboost.png){#fig:hmm-xgboost-roc widh=80%}