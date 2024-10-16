from odoo import models, fields, api

class CafeOrderDineIn(models.Model):
    _name = 'cafe.order.dinein'
    _inherit = 'cafe.order'
    _description = 'Cafe Order - Dine In'

    table_id = fields.Many2one('cafe.table', string='Số bàn', required=True)
