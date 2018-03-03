import methods


def initialize(df, y, nb_generations=10, nb_population=20, model='svm', accuracy=0.6):
    return methods.generate(df, y, nb_generations, nb_population, model, accuracy)
