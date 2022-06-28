from odoo import models, fields


class FreightTypes(models.Model):
    _name = "lms.freight.type.datas"
    _description = " LMS - Freight Type (master data)"

    name = fields.Char(string="Freight Type name", required=True)
    description = fields.Char(string="Freight Type description")
