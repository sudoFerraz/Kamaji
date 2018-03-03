import methods as methods


class Model:
    def __init__(self, features, model_name):
        self.accuracy = 0.0
        self.features = features
        self.model_name = model_name
        self.model = None

    def define_features(self, features):
        self.features = features

    def train(self, df, y):
        if not self.accuracy:
            self.accuracy, self.model = methods.train_and_score(self.features, df, y, self.model_name)
