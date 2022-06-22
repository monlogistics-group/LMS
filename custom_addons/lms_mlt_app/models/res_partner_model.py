from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    lms_ids = fields.Many2many('lms.task', string='Teams')
