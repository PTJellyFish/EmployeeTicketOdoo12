# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ticket_odoo(models.Model):
#     _name = 'ticket_odoo.ticket_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Ticket(models.Model):
    _name = 'ticket.ticket'
 
    name = fields.Char(string="Subject", required=True)
    category = fields.Selection([('Bullying','Bullying'),
                                ('Commit terror', 'Commit terror'), 
                                ('Defamation', 'Defamation'), 
                                ('Destruction of company property', 'Destruction of company property'), 
                                ('Disturbing', 'Disturbing'), 
                                ('Hate speech', 'Hate speech'), 
                                ('Physical abuse', 'Physical abuse'), 
                                ('Sexual violence', 'Sexual violence'),
                                ('Theft', 'Theft'),
                                ('Threatening', 'Threatening')],
                                string="Category", required=True)

    description = fields.Text(help="Describe your problem with the employee in question here.")
    reporter_id = fields.Many2one('res.users', ondelete='set null', readonly=True, string="Reporter", index=True, default=lambda self: self.env.user)
    reported_id = fields.Many2one('hr.employee', string='Reported Employee', required=True, help="Employee that has problem with you.")
    date = fields.Date(string="Date", required=True, help="Date of the problem occurred.")