# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def _compute_website_url(self):
        super(ProductTemplate, self)._compute_website_url()
        for product in self:
            # If the product cannot be sold, then use the new form view.
            # Otherwise, use the defult URL from website_sale, which will
            # redirect the user to the shop.
            if not product.sale_ok:
                product.website_url = "/product/%s" % slug(product)


class ProductsFormSearch(models.AbstractModel):

    _name = 'cms.form.search.product.template'
    _inherit = 'cms.form.search'
    _form_model = 'product.template'
    _form_model_fields = ('name', )
    _form_required_fields = ('name', )

    default_code = fields.Char()

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


class ProductsForm(models.AbstractModel):

    _name = 'cms.form.product.template'
    _inherit = 'cms.form'
    _form_model = 'product.template'
    _form_model_fields = ('name', )
    _form_required_fields = ('name', )
