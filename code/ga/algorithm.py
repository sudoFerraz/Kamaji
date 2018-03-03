import random
from operator import add
from functools import reduce

import model as mdl


class GA:
    def __init__(self, features, retain=0.25, random_select=0.1, mutation=0.2):
        self.features = features
        self.retain = retain
        self.random_select = random_select
        self.mutation = mutation

    def create_population(self, count, model_name):
        pop = []
        for _ in range(count):
            model = mdl.Model(self.features[_], model_name)
            pop.append(model)

        return pop

    @staticmethod
    def fitness(model):
        return model.accuracy

    def grade(self, pop):
        all = reduce(add, (self.fitness(model) for model in pop))
        return all / len(pop)

    def breed(self, individual_a, individual_b):
        individual = {1: individual_a, 2: individual_b}
        children = []

        for _ in range(2):
            features = ''
            feature = 0
            while len(features) < len(individual_a.features):
                features += individual[random.randint(1, 2)].features[feature]

            if self.mutation > random.random():
                features = self.mutate(features)

            model = mdl.Model(features, individual_a.model_name)
            model.define_features(features)

            children.append(model)

        return children

    def mutate(self, features):
        index = random.randint(0, len(features) - 1)
        h = features[:index]
        t = features[index+1:]
        features = h + str(1 - int(features[index])) + t
        return features

    def evolve(self, pop):
        graded = [(self.fitness(model), model) for model in pop]
        graded = [x[1] for x in sorted(graded, key=lambda k: k[0], reverse=True)]
        retain_length = int(len(graded) * self.retain)

        parents = graded[:retain_length]

        for individual in graded[retain_length:]:
            if self.random_select > random.random():
                parents.append(individual)

        nb_parents = len(parents)
        length = len(pop) - nb_parents
        children = []

        while len(children) < length:
            individual_a = random.randint(0, nb_parents - 1)
            individual_b = random.randint(0, nb_parents - 1)

            if individual_a != individual_b:
                individual_a = parents[individual_a]
                individual_b = parents[individual_b]

                babies = self.breed(individual_a, individual_b)

                for baby in babies:
                    if len(children) < length:
                        children.append(baby)

        parents.extend(children)
        return parents
