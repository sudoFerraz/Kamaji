#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import genetic_algorithm as ga
import numpy as np
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if __name__ == '__main__':
    pd.set_option('use_inf_as_na', True)
    df = pd.read_csv('../../datasets/USDBRL/all_normalized.csv')
    df = df.drop('Date', axis=1)
    labels = pd.read_csv('../../datasets/labels.csv')
    y1 = labels['y1']
    df = df[15:-15]
    y = df['close'] - df['close'].shift(-15)
    #y = y.shift(-1)

    y_regress = y
    y_regress = y_regress.fillna(method='ffill')
    y_regress = np.array(y_regress)
    y_regress = y_regress.reshape(-1, 1)

    y = y.apply(lambda x: 1 if x > 0.0 else 0)

    '''
        Chamando initialize e passando o dataframe, APOS O TRATAMENTO QUE QUISER REALIZAR, ou seja,
        após normalização, todos os valores são númericos, etc.

        y é o target para o modelo.
        Se for classificacao, deixar o target em classes, notei agora que por enquanto tá funcionando só quando é
            binário, vou arrumar pra poder suportar mais classes depois


        O retorno do método é a populacao que foi gerada, com todos os individuos, e um dicionario que contem a acuracia
        no decorrer da evolucao.


        A assinatura do método é a seguinte
        initialize(df, y, nb_generations=10, nb_population=20, model='svm', accuracy=0.6)

        Então passar o datafram e o target sao parametros obrigatorios.
        nb_generation -> numeros de geracoes
        nb_population -> numero de individuos em cada populacao
        model -> qual modelo usar, podend ser ['svm', 'crf', 'svr', 'rrf', 'nn'] que são svm classificacao,
        random forrest classificacao, svm de regressao e random forrest regressao e rede neural, nessa ordem.

        O ultimo parametro é a accuracia para ficar no loop, cuidado pra nao colocar um valor que nao da pra alcançar.
    '''
    population, accuracies = ga.initialize(df, y, model='svm')

    '''
        Para acessar a média da acurácia na geracao 3:
    '''
    print('Media de acuracia na 3 geracao:')
    print(np.mean(accuracies[3]))


    '''
        Selecionando os 5 melhores da populacao
    '''
    print('\n\nMelhores 5 acuracias encontradas')
    first_five = population[:5]


    '''
        Imprimindo a acuracia dos 5 primeiros
    '''
    for individual in first_five:
        print(individual.accuracy)

    '''
        Selecionando o melhor modelo, já treinado, e pronto para utilizar. Também pode utilizar para retirar as métricas
        que precisar.
    '''
    best_model = first_five[0].model
    print(best_model)
