from odoo import models, fields

"""
    Freight Type model
    -------------------------------
    active = Active
    id = For moving
    name = Name
    description = Description
    -------------------------------
"""
class FreightTypes(models.Model):
    _name = "lms.freight.type.datas"
    _description = " LMS - Freight Type (master data)"

    active = fields.Boolean(default=True)
    id = fields.Integer()
    name = fields.Char(string="Freight Type Full name", required=True)
    description = fields.Char(string="Freight Type description")
    _sql_constraints = [
        ('name_mustbe_uniq',
         "UNIQUE(name)",
         "You already have general with such name")]

    def copy(self,  default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(FreightTypes, self).copy(default)

"""
    Operation Type model
    -------------------------------
    active = Active
    id = For moving
    name = Name
    description = Description
    -------------------------------
"""
class OperationTypes(models.Model):
    _name = "lms.operation.type.datas"
    _description = "LMS - Operation Types (master data)"

    active = fields.Boolean(default=True)
    id = fields.Integer()
    name = fields.Char(string="Operation Full Name", required=True)
    description = fields.Char(string="Operation Description")
    _sql_constraints = [
        ('name_mustbe_uniq',
         "UNIQUE(name)",
         "You already have general with such name")]

    def copy(self,  default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(OperationTypes, self).copy(default)