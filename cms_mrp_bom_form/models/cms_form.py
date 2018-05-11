# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MrpBomFormSearch(models.AbstractModel):

    _name = 'cms.form.search.mrp.bom'
    _inherit = 'cms.form.search'
    _form_model = 'mrp.bom'
    _form_model_fields = ('name', 'code', )
    _form_required_fields = ('name', 'code', )

    name = fields.Char()

    def form_search_domain(self, search_values):
        domain = super().form_search_domain(search_values)
        is_website_publisher = self.env['res.users'].has_group(
            'website.group_website_publisher')
        if not is_website_publisher:
            default_domain = [
                ('website_published', '=', True),
            ]
            domain.extend(default_domain)
        return domain
