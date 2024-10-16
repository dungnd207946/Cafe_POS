from odoo import models, fields, api
class CafeOrderTakeAway(models.Model):
    _name = 'cafe.order.takeaway'
    _inherit = 'cafe.order'
    _description = 'Cafe Order - Take Away'

    customer_name = fields.Text(string='Tên khách hàng')


