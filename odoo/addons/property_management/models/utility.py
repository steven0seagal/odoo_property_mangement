from odoo import models, fields, api


class RentalUtilityUsage(models.Model):
    _name = 'promasy.utility_usage'
    _description = 'Rental Property Utility Usage Information'

    property_id = fields.Many2many('promasy.property', string='Property', required=True)
    tenant_id = fields.Many2one('promasy.tenant', string='Tenant')
    utility_type = fields.Selection([
        ('power', 'Power'),
        ('water', 'Water'),
        ('gas', 'Gas'),
        ('internet', 'Internet'),
        ('other', 'Other')
    ], string='Utility Type', required=True)
    usage = fields.Float(string='Usage')  # Depending on the utility type, could be in kWh, gallons, cubic meters, etc.
    billing_period_start = fields.Date(string='Billing Period Start')
    billing_period_end = fields.Date(string='Billing Period End')
    rate = fields.Float(string='Rate')  # Price per unit of the utility
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost') # Calculated based on rate and usage
    invoice_id = fields.Many2one('account.move', string='Invoice')
    notes = fields.Text(string='Notes')
    # Other fields and relationships

    @api.depends('usage', 'rate')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.usage * record.rate
