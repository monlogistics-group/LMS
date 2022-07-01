from odoo import models, fields


class FreightTypes(models.Model):
    _name = "lms.freight.type.datas"
    _description = " LMS - Freight Type (master data)"

    freight_id = fields.Char(string="Freight Type Name", required=True)
    name = fields.Char(string="Freight Type Full name")
    description = fields.Char(string="Freight Type description")

class OperationTypes(models.Model):
    _name = "lms.operation.type.datas"
    _description = "LMS - Operation Types (master data)"

    operation_id = fields.Char(string="Operation Name", required=True)
    name = fields.Char(string="Operation Full Name")
    description = fields.Char(string="Operation Description")
