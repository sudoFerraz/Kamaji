
'''
    Importa a interface para chamar o método
'''
import interface

import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv('../../datasets/USDBRL/all_normalized.csv')
    df = df.drop('Date', axis=1)

    y = df['close'] - df['close'].shift(1)
    y = y.shift(-1)

    y_regress = y
    y_regress = y_regress.fillna(method='ffill')
    y_regress = np.array(y_regress)
    y_regress = y_regress.reshape(-1, 1)

    y = y.apply(lambda x: 1 if x > 0.0 else 0)

    '''
        Chamando model_and_accuracy e passando o dataframe, APOS O TRATAMENTO QUE QUISER REALIZAR, ou seja,
        após normalização, todos os valores são númericos, etc.
        
        y é o target binário
        
        y_regress é o target para regressão
        
        
        O retorno do método é um dicionario no formato <String, (acuracia, modelo_treinado)>
        sendo as chaves:
        
        'svr' -> SVM em regressao
        'nn' -> Rede neural
        'crf' -> Random Forrest de classificação
        'rrf' -> Random Forrest de regressão
        'svm' -> SVM em classificação
    '''
    dict = interface.model_and_accuracy(df, y, y_regress)

    print(dict)
