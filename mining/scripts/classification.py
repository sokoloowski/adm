import gc
import time

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, auc, classification_report, confusion_matrix, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, LabelBinarizer


def _get_clf_param(classifier) -> str:
    """
    Get param value, defaults for "unknown"
    """
    param = getattr(classifier, 'kernel', 'unknown')
    param = getattr(classifier, 'criterion', param)
    param = getattr(classifier, 'solver', param)
    return getattr(classifier, 'loss', param)


def train_analyze(classifier, vectorizer, dataframe, random_state=None) -> None:
    le = LabelEncoder()
    y = le.fit_transform(dataframe['subreddit'])
    X = vectorizer.fit_transform(dataframe['body'])

    classifier_name = classifier.__class__.__name__
    vectorizer_name = vectorizer.__class__.__name__
    labels = le.classes_

    param = _get_clf_param(classifier)
    
    start_time = time.time()

    # Train
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state)
    try:
        y_score = classifier.fit(X_train, y_train).predict_proba(X_test)

        # Plot ROC curve
        lb = LabelBinarizer()
        lb.fit(y_train)
        y_onehot_test = lb.transform(y_test)
        limits = [-0.02, 1.02]
        plt.figure(figsize=(6, 6))
        for i, label in enumerate(labels):
            fpr, tpr, _ = roc_curve(y_onehot_test[:, i], y_score[:, i])
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, label=f'{label} (area = {roc_auc:.2f})')
        plt.plot(limits, limits, 'k--')
        plt.xlim(limits)
        plt.ylim(limits)
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.legend()
        plt.title(f'ROC curve for {classifier.__class__.__name__} with {param} on {vectorizer_name}')
        plt.gca().set_aspect('equal')
        plt.savefig(f'images/roc_{classifier_name}_{param}_{vectorizer_name}.png', bbox_inches='tight')
        plt.show()
    except:
        classifier.fit(X_train, y_train)

    print("Training took", round(time.time() - start_time, 2), "seconds")
    
    y_pred = classifier.predict(X_test)

    # Analyze
    print(f'First 10 predictions for {classifier_name} with {param} on {vectorizer_name}:')
    for i in range(10):
        print("\t", labels[y_test[i]], '->', labels[y_pred[i]])
    print()

    print(f'Classification report for {classifier_name} with {param} on {vectorizer_name}:')
    print(classification_report(y_test, y_pred, target_names=labels))
    with open(f'results/{classifier_name}_{param}_{vectorizer_name}.txt', 'w') as f:
        f.write(classification_report(y_test, y_pred, target_names=labels))
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(16, 9))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    acc = round(accuracy_score(y_test, y_pred) * 100, 2)
    plt.title(f'Confusion matrix for {classifier_name} with {param} on {vectorizer_name} with {acc}% accuracy')
    plt.savefig(f'images/confusion_matrix_{classifier_name}_{param}_{vectorizer_name}.png', bbox_inches='tight')
    plt.show()

    # Collect garbage
    gc.collect()
