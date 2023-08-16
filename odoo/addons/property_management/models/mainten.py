from odoo import models, fields, api

class PromasyMaintenance(models.Model):
    _name = 'promasy.maintenance'
    _description = 'Rental Property Maintenance Information'

    name = fields.Char(string='Maintenance Title', required=True)
    property_id = fields.Many2many('promasy.property', string='Property', required=True)
    description = fields.Text(string='Description')
    maintenance_type = fields.Selection([
        ('repair', 'Repair'),
        ('inspection', 'Inspection'),
        ('cleaning', 'Cleaning'),
        ('upgrade', 'Upgrade'),
        ('other', 'Other')
    ], string='Maintenance Type', required=True)
    status = fields.Selection([
        ('requested', 'Requested'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='requested')
    request_date = fields.Date(string='Request Date', default=fields.Date.context_today)
    completion_date = fields.Date(string='Completion Date')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    cost = fields.Float(string='Cost')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    notes = fields.Text(string='Notes')
    # Other fields and relationships
