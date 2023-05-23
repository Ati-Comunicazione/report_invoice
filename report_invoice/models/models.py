

from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Creazione del campo Delivery che mostra i contatti che hanno l'etichetta Delivery impostata
    delivery_contacts = fields.Many2many(
        'res.partner', string='Delivery Contacts', domain="[('category_id', 'ilike', 'Delivery')]")

    # Menu a tendina per la sezione degli aspetti dei prodotti da parte del corriere
    aspetto = fields.Selection([
        ('bancale', 'Bancale'),
        ('cartone', 'Cartone'),
        ('cartone_bancale', 'Cartone / Bancale'),
        ('sfusi', 'Sfusi')
    ], string='Aspetto')

    #Salvataggio dei dati inseriti durante il preventivo nella funzione _prepare_invoice() perchè essa contiene tutti i dati che vengono salvati nel Preventivo 
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['sale_order_id'] = self.aspetto
        invoice_vals['sale_order_delivery_id'] = self.delivery_contacts.name_get()[0][1] if self.delivery_contacts else False
        return invoice_vals
