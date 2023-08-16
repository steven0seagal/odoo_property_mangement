from odoo import models, fields, api


class RentalProperty(models.Model):

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
    amenities = fields.Text(string='Amenities')
    deposit = fields.Float(string='Deposit Amount')
    available_from = fields.Date(string='Available From')
    status = fields.Selection([('available', 'Available'), ('rented', 'Rented'), ('maintenance', 'Under Maintenance')],
                              string='Status', default='available')
    image = fields.Binary(string='Property Image')
    landlord_id = fields.Many2one('res.partner', string='Landlord', domain=[('is_landlord', '=', True)])
    tenant_id = fields.Many2one('res.partner', string='Current Tenant', domain=[('is_tenant', '=', True)])
    contract_id = fields.Many2one('promasy.contract', string='Current Contract')
    utility_ids = fields.One2many('promasy.utility_usage', 'property_id', string='Utility Records')
    maintenance_ids = fields.One2many('promasy.maintenance', 'property_id', string='Maintenance Records')
    cleaning_ids = fields.One2many('promasy.cleaning', 'property_id', string='Cleaning Records')
