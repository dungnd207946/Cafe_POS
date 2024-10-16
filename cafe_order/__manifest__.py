{
    'name': 'Cafe Order Management',
    'version': '1.0',
    'author': "<DUNG>",
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/cafe_menu_views.xml",
        'views/cafe_order.xml',
        'views/cafe_table_views.xml',
        'views/menu_item_views.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
