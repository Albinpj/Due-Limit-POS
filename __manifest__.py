{
    'name': 'Due Limit',
    'version': '15.0.1.0',
    'category': 'Due Limit',
    'sequence': -1501,
    'summary': 'Due Limit For Customer',
    'application': True,
    'depends': [
        'base',
        'contacts',
        'point_of_sale',

    ],
    'data': [
        'views/res_partner.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'due_limit/static/src/js/pos_due_limit.js',
        ],
    },

}
