from odoo import models, fields, api, _


"""
    General Order model
    -------------------------------
    general_id = General order id
    name = REF number
    description = Description
    operation_types = Operation types
    gross_weigth = Gross weigth
    volume = CBM
    quantity = Quantity
    -------------------------------
"""


class GeneralOrder(models.Model):
    _name = 'lms.general.order'
    _description = 'Order field for general order'

    general_id = fields.Many2one('lms.general', string="Order Ref")
    name = fields.Char(string="Ref", required=True,
                       readonly=True, default=lambda self: _('New'))
    description = fields.Text(string="Description")
    operation_types = fields.Many2one(
        'lms.operation.type.datas', string="Operation Types")
    gross_weigth = fields.Float(string="Gross Weight")
    volume = fields.Float(string="CBM")
    quantity = fields.Float(string="Quantity")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'lms.general.order') or _('New')
        res = super(GeneralOrder, self).create(vals)
        return res
