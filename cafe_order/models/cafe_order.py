from odoo import models, fields, api

class CafeOrder(models.Model):
    _name = 'cafe.order'
    _description = 'Cafe Order'

    order_number = fields.Char(string='Order Number', required=True)
    order_date = fields.Datetime(string='Thời gian', default=fields.Datetime.now)
    menu_items = fields.One2many('cafe.order.line', 'order_id', string='Order Lines')
    total_amount = fields.Float(string='Tổng tiền', compute='_compute_total')
    table_id = fields.Many2one('cafe.table', string='Số bàn', required=True)
    customer_name = fields.Text(string='Tên khách hàng')
    @api.depends('menu_items.subtotal')
    def _compute_total(self):
        for order in self:
            order.total_amount = sum(line.subtotal for line in order.menu_items)

    def action_save(self):
        # Logic xử lý dữ liệu hoặc tính toán trước khi lưu
        if not self.menu_items:
            raise ValueError("Item is required for orders.")
        self.write({'order_date': fields.Datetime.now()})
        return True