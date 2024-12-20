## Hidden Markov Models

A Hidden Markov Model (HMM) is a statistical model used to represent systems that exhibit temporal or sequential characteristics. It is widely applied in fields such as speech recognition, natural language processing, bioinformatics, and pattern recognition.

### Markov Process

To apply Hidden Markov Models, there is a basic requirement that has to be fulfilled, and it's that the modeled process has to be a Markov process. In general, it can be described that every observation (data point) depends only on the previous one. From a formal perspective, such a process can be described by the [@eq:markov]:

$$
P(X_t | X_{t-1}, X_{t-2}, \ldots, X_1) = P(X_t | X_{t-1})
$$ {#eq:markov}

where:

1. $P(X_t | X_{t-1}, X_{t-2}, \ldots, X_1)$:  
   This represents the conditional probability of the state $X_t$ at time $t$, given all previous states $X_1, X_2, \ldots, X_{t-1}$.
2. $P(X_t | X_{t-1})$:  
   This represents the simplified conditional probability of the state $X_t$ at time $t$, depending only on the state at the immediately preceding time step $X_{t-1}$.
3. Markov Property:  
   The key assumption of a Markov process is that the future state $X_t$ is conditionally independent of all past states $X_{t-2}, X_{t-3}, \ldots, X_1$ given the current state $X_{t-1}$. This simplification reduces the complexity of modeling and computations.

This property is fundamental to the application of Hidden Markov Models (HMMs), as it ensures the process follows the Markov assumption, making it tractable for analysis and inference. Hidden Markov Models are based on the idea that every observation can be mapped to its hidden state. It allows for minimizing the dimensionality of the data by converting the feature space into its hidden representation. However, it is very important to carefully set the number of these states to ensure the convergence of the model.

### Text Data

Since text data can be simplified to meet the set requirements for a Markov process, we can successfully apply Hidden Markov Models. Using this model, we can calculate two basic things:

1. Estimation of hidden states for given data sequences.
2. Probability of occurrence of hidden states sequences.

### Proposed Approach 

In the proposed methodology, we applied the first approach. As a basic transformation of text, we applied Bag of Words. Then, from this large amount of feature space, we selected the most relevant features by choosing the top 10 percentile of the most important data. Since HMMs require continuous distributions of data, we had to apply further transformations. After testing different methods, such as PCA, SVD, and others, we ended up with Latent Dirichlet Allocation. We set the `n_components` parameter to 20. Then, we set the number of hidden states to 10 to ensure convergence of our model. In the next step, we trained Gaussian Mixture Models [@https://doi.org/10.1109/PEMC61721.2024.10726395] to calculate initial parameters for the HMM. This allowed for faster and better convergence. Using these parameters, we were able to train the HMM. Finally, we applied the trained model as a feature extractor (converting data to hidden states) for the XGBoost Model.

### Results 

The proposed method resulted in the results shown in [@fig:hmm-xgboost-confusion-matrix] and [@fig:hmm-xgboost-roc].

![The confusion matrix for XGBoost demonstrates that the results are not satisfactory.](images/hmm_xgb_confusion_matrix.png){#fig:hmm-xgboost-confusion-matrix width=100%}

![The receiver operating characteristic (ROC) curve of the XGBoost classifier indicates that it is unable to effectively classify the texts of Reddit posts.](images/roc_hmm_xgboost.png){#fig:hmm-xgboost-roc width=50%}

To achieve such results, we needed to set the model's parameters very carefully. Also, selecting text representation and transformation played a key role in the outcomes. However, we weren't able to achieve better results with the HMM than without it, but this may depend on the quality of the provided data.