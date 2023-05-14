# # -*- coding: utf-8 -*-



from odoo import api, models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    sale_order_id = fields.Char(string='Aspetto')

    sale_order_delivery_id = fields.Char(string='Delivery')

