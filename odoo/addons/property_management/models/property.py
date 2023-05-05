from odoo import models, fields, api


class Property(models.Model):

    _name = 'promasy.property'
    _description = 'Property Management System'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image')
    description = fields.Text(string='Description')
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    country = fields.Char(string='Country')
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('other', 'Other'),
    ], string='Property Type', default='house')
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    square_feet = fields.Integer(string='Square Feet')
    rent = fields.Float(string='Rent')
    # photo_ids = fields.Many2many('property.photo', string='Photos')
    # tenant_id = fields.Many2one('res.partner', string='Tenant')
    # tenant_start_date = fields.Date(string='Tenant Start Date')
    # tenant_end_date = fields.Date(string='Tenant End Date')
    # tenant_security_deposit = fields.Float(string='Tenant Security Deposit')
    # tenant_security_deposit_refunded = fields.Boolean(string='Tenant Security Deposit Refunded')
    # tenant_security_deposit_refunded_date = fields.Date(string='Tenant Security Deposit Refunded Date')
    # tenant_security_deposit_refunded_amount = fields.Float(string='Tenant Security Deposit Refunded Amount')
    # tenant_security_deposit_refunded_notes = fields.Text(string='Tenant Security Deposit Refunded Notes')
    # tenant_security_deposit_refunded_by = fields.Many2one('res.partner', string='Tenant Security Deposit Refunded By')
    # tenant_security_deposit_refunded_to = fields.Many2one('res.partner', string='Tenant Security Deposit Refunded To')
    # tenant_security_deposit_refunded_check_number = fields.Char(string='Tenant Security Deposit Refunded Check Number')
    # tenant_security_deposit_refunded_check_date = fields.Date(string='Tenant Security Deposit Refunded Check Date')
    # tenant_security_deposit_refunded_check_amount = fields.Float(string='Tenant Security Deposit Refunded Check Amount')
    # tenant_security_deposit_refunded_check_notes = fields.Text(string='Tenant Security Deposit Refunded Check Notes')
    # tenant_security_deposit_refunded_check_by = fields.Many2one('res.partner', string='Tenant Security Deposit Refunded Check By')
    # tenant_security_deposit_refunded_check_to = fields.Many2one('res.partner', string='Tenant Security Deposit Refunded')

