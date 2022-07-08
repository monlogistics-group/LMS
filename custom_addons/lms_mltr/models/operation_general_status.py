from odoo import models, fields

class GeneralStatus(models.Model):
    _name = 'lms.general.status'
    _description = 'Status for general status'

    active = fields.Boolean(default=True)
    id = fields.Integer()
    default = fields.Boolean()
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    general_id = fields.One2many('lms.general','state')

    _sql_constraints = [
        ('name_mustbe_uniq',
        "UNIQUE(name)",
        "You already have general with such name")]

    def copy(self,  default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(GeneralStatus, self).copy(default)