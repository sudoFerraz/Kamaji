import auxiliary
import model
import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np

session = auxiliary.ostools().db_connection()
invoice_df = pd.DataFrame(columns=['nro_invoice', 'dt_vencimento', 'dt_pagamento', 'valor_invoice', 'dolar_vencimento', 'dolar_provisao', 'dolar_pagamento', 'valor_pago', 'saving provisao', 'saving vencimento', 'total vencimento', 'total provisao'])
invoices = session.query(model.Invoice).all()
i = 0
data = pd.read_csv('datasets/USDBRL/all_indicators.csv')
total_vencimento = 0
total_provisao = 0

for invoice in invoices:
    if invoice.status == 'encerrada':
        vencimento = datetime.strptime(invoice.dt_vencimento, "%Y-%m-%d")
        if vencimento < datetime.today():
            while data.loc[data['Date'] == datetime.strftime(vencimento, "%Y-%m-%d")].empty == True:
                vencimento = vencimento - timedelta(days=1)
            vencimento = datetime.strftime(vencimento, "%Y-%m-%d")
            dolar_vencimento = data.loc[data['Date'] == vencimento]['close'].values[0]
            savings_vencimento = dolar_vencimento * invoice.valor_invoice
            savings_vencimento = savings_vencimento - invoice.valor_pago
            savings_provisao = (invoice.valor_invoice * invoice.dolar_provisao) - invoice.valor_pago
            total_vencimento = total_vencimento + savings_vencimento
            total_provisao = total_provisao + savings_provisao
            invoice_df.loc[i] = invoice.nro_invoice, invoice.dt_vencimento, invoice.dt_pagamento, invoice.valor_invoice, dolar_vencimento, invoice.dolar_provisao, invoice.dolar_pagamento, invoice.valor_pago, savings_provisao, savings_vencimento, total_vencimento, total_provisao
            i = i + 1

invoice_df.to_csv('../kamaji-front-end/results.csv', mode='w', header=True)
