# -*- coding: utf-8 -*-
{
    'name': "Sales Import Order-lines",
    'version': '15.0.2.0.1',
    'summary': """
            Allows to import bulk sales order lines using CSV file.
        """,
    'description': """
            Allows to import bulk sales order lines using excel/csv sheet.
            CSV file attached in docs folder with sample data.
        """,
    'category': 'Sales',
    'author': 'Teapot Techies Private Limited',
    'support': 'teapottechies@gmail.com',
    'website': 'http://teapottechies.com/',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_inherit.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'currency': 'EUR',
    'price': '10',
}
