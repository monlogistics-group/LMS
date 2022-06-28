from odoo import models, fields, api, _


class OperationTypes(models.Model):
    _name = "lms.operation.type.datas"
    _description = "LMS - Operation Types (master data)"

    id = fields.Char(string="ID", required=True, readonly=True,
                     default=lambda self: _('New'))
    name = fields.Char(string="Operation Name")
    description = fields.Char(string="Operation Description")

    @api.model
    def create(self, vals):
        if vals.get('id', _('New')) == _('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code(
                'lms.operation') or _('New')
        res = super(OperationTypes, self).create(vals)
        return res
