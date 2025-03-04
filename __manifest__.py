{
    'name': 'Odoo Pandas XLSX Generator',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Generates an XLSX file on module installation',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
}
