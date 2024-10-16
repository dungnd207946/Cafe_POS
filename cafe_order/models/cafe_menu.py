from odoo import models, fields, api

class CafeMenu(models.Model):
    _name = 'cafe.menu'
    _description = 'Cafe Menu'

    name = fields.Char(string='Tên món', required=True)
    price = fields.Float(string='Giá tiền', required=True)