# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class General(models.Model):
    _name = 'lms.general'
    _description = 'LMS general information'

    customer_id = fields.Many2one('res.partner', string='Customer')
    general_ref = fields.Char(
        string='General REF', required=True, readonly=True, default=lambda self: _('New'))
    gross_weigth = fields.Float(string="Gross Weight (kg)")
    volume = fields.Float(string="CBM (㎥)")
    package_qty = fields.Float(string="Package Quantity")
    package_img = fields.Image(string="Package Images")
    freigth_types = fields.Many2one('lms.freight.type.datas',string="Freigth Types")
    package_name = fields.Char(string="Package Name")
    origin_country = fields.Many2one('res.country', string='Origin Country')
    origin_address = fields.Text(string="Origin Address")
    destination_country = fields.Many2one(
        'res.country', string='Destination Country')
    destination_delivery = fields.Text(string="Destination Address")
    pickup_date = fields.Date(string="Pickup Date")
    delivery_date = fields.Date(string="Delivery Date")
    estimated_cost = fields.Float(string="Estimated Cost")
    mltr_cost = fields.Float(string="MLTr Cost")
    contact_name = fields.Char(string="Contact Name")
    contact_details = fields.Text(string="Contact Details")
    temprature = fields.Float(string="Package Temprature")
    fleet_id = fields.Many2one('fleet.vehicle', string="Trucks")
    notice = fields.Text(string="Notice")

    @api.model
    def create(self, vals):
        if vals.get('general_ref', _('New')) == _('New'):
            vals['general_ref'] = self.env['ir.sequence'].next_by_code('lms.general') or _('New')
        res = super(General, self).create(vals)
        return res
