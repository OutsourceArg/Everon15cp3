# -*- coding: utf-8 -*-
{
    'name': "match_invoices_payments",

    'summary': """
        Matchea pagos de clientes con facturas""",

    'description': """
        Matchea pagos de clientes con facturas
    """,

    'author': "Devoogroup",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account',
                'payment'],

    # always loaded
    'data': [
        'data/data_view.xml',
        'views/account_payment_view.xml',
    ],
}
