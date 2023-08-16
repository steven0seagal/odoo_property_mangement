from odoo import models, fields, api

class PromasyCleaning(models.Model):
    _name = 'promasy.cleaning'
    _description = 'Rental Property Cleaning Information'

    name = fields.Char(string='Cleaning Task', required=True)
    property_id = fields.Many2many('promasy.property', string='Property', required=True)
    cleaning_type = fields.Selection([
        ('regular', 'Regular'),
        ('deep', 'Deep Cleaning'),
        ('post_rental', 'Post-Rental Cleaning'),
        ('emergency', 'Emergency Cleaning'),
        ('other', 'Other')
    ], string='Cleaning Type', required=True)
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='scheduled')
    schedule_date = fields.Date(string='Scheduled Date')
    completion_date = fields.Date(string='Completion Date')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    notes = fields.Text(string='Notes')
    cost = fields.Float(string='Cost')
    # Other fields and relationships
