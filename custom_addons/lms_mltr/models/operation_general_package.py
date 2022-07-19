from odoo import models, fields, api, _ 

class GeneralPackage(models.Model):
    _name = 'lms.general.package'
    _description = 'LMS general package'

    general_id = fields.Many2one('lms.general', string="Order Ref")
    name = fields.Char(string='Ref', required=True,
                       readonly=True, default=lambda self: _('New'))
    description = fields.Text(string="Name")
    package = fields.Char(string="Package")
    operation_types = fields.Many2one(
        'lms.operation.type.datas', string="Operation Types")
    gross_weigth = fields.Float(string="Gross Weight")
    volume = fields.Float(string="CBM")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'lms.general.package') or _('New')
        res = super(GeneralPackage, self).create(vals)
        return res