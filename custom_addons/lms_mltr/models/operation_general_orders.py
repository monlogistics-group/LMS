from odoo import models, fields, api, _


class GeneralOrder(models.Model):
    _name = 'lms.general.order'
    _description = 'Order field for general order'

    general_id = fields.Many2one('lms.general',string="Order Ref")
    name = fields.Char(string="ID", required=True,
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