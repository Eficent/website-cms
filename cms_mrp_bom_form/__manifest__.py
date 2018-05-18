# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'CMS Form MRP Boms',
    'summary': """
        Search forms for MRP Boms""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Eficent, '
              'Odoo Community Association (OCA)',
    'depends': [
        'website_mrp_bom',
        'cms_form',
    ],
    "data": [
        "data/product_category_demo.xml",
        "data/product_product_demo.xml",
        "data/mrp_bom_demo.xml",
        'security/ir.model.access.csv'
    ],
    'installable': True,
}
