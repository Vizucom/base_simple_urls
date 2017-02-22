# -*- coding: utf-8 -*-
from openerp import models, fields, _


class RedirectRule(models.Model):

    _name = 'base_simple_urls.redirect_rule'
    _description = 'Redirect Rule'

    get_variable = fields.Char('GET Variable', required=True)
    model_id = fields.Many2one('ir.model', 'Target model', required=True)
    field_id = fields.Many2one('ir.model.fields', 'Target field', required=True)
    action_id = fields.Many2one('ir.actions.act_window', 'Target action', required=True)
    description = fields.Char('Description')

    _sql_constraints = [
        ('get_variable', 'unique(get_variable)', 'Please use a unique GET variable'),
    ]
