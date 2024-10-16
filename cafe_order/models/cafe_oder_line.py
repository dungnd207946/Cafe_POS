from odoo import models, fields, api

class CafeOrderLine(models.Model):
    _name        = 'cafe.order.line'
    _description = 'Cafe Order Line'
    order_id     = fields.Many2one('cafe.order', string='Order Id', required=True, ondelete='cascade', onupdate='cascade')
    menu_item_id = fields.Many2one('cafe.menu', string='Tên món', required=True)
    quantity     = fields.Integer(string='Số lượng', default=1)
    subtotal     = fields.Float(string='Thành tiền', compute='_compute_subtotal', store=True)

    @api.depends('menu_item_id.price', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.menu_item_id.price * line.quantity