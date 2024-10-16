from odoo import models, fields

class CafeTable(models.Model):
    _name = 'cafe.table'
    _description = 'Cafe Table'

    name = fields.Char(string='Table Name', required=True)
    capacity = fields.Integer(string='Capacity')
    is_available = fields.Boolean(string='Available', default=True)
