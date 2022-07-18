# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', string='Responsible', ondelete='set null', index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]

    class Session(models.Model):
        _name = 'openacademy.session'
        _description = "OpenAcademy Sessions"

        name = fields.Char(required=True)
        start_date = fields.Date(default=fields.Date.today())
        duration = fields.Float(digits=(6, 2), help="Duration in days")
        seats = fields.Integer(string="Number of seats")