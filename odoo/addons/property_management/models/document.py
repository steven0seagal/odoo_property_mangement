from odoo import models, fields, api


class Document(models.Model):

    _name = 'promasy.document'
    _description = 'Document'

    name = fields.Char(string='File name', required=True)
    file = fields.Binary(string='File')
    description = fields.Text(string='Description')
    property_id = fields.Many2one('promasy.property', string='Property')
    document_type = fields.Selection([
        ('lease', 'Lease'),
        ('rental_application', 'Rental Application'),
        ('rental_annex', 'Rental Annex'),
        ('other', 'Other'),
    ], string='Document Type', default='lease')
