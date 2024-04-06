class NaiveBayesClassifier:
    def __init__(self):
        self.prior = {}
        self.likelihood = {}
    
    def fit(self, X, y):
        total_samples = len(y)
        self.prior['0'] = sum(1 for label in y if label == '0') / total_samples
        self.prior['1'] = sum(1 for label in y if label == '1') / total_samples
        for feature in X.columns:
            self.likelihood[feature] = {
                '0': X[y == '0'][feature].mean(),
                '1': X[y == '1'][feature].mean()
            }
    
    def predict(self, X):
        predictions = []
        for idx, sample in X.iterrows():
            p_0 = self.prior['0']
            p_1 = self.prior['1']
            for feature, value in sample.items():
                p_0 *= self.likelihood[feature]['0'] if value == 1 else (1 - self.likelihood[feature]['0'])
                p_1 *= self.likelihood[feature]['1'] if value == 1 else (1 - self.likelihood[feature]['1'])
            predictions.append('1' if p_1 > p_0 else '0')
        return predictions

# Example usage
import pandas as pd
X_train = pd.DataFrame({'Feature1': [1, 0, 1, 0], 'Feature2': [0, 1, 1, 0]})
y_train = pd.Series(['0', '1', '1', '0'])
clf = NaiveBayesClassifier()
clf.fit(X_train, y_train)
X_test = pd.DataFrame({'Feature1': [1, 0], 'Feature2': [1, 0]})
print(clf.predict(X_test))
