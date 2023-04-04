#!/usr/bin/env python
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class CrmLead(models.Model):
	_inherit = "crm.lead"
	
	task_ids = fields.One2many('project.task', 'partner_id', 'Tareas relacionadas', compute = 'comp_related_task')

	def comp_related_task(self):
		"""
		Allow to get the related task of the partner
		"""
		related_task_ids = False
		if self.partner_id:
			# Getting all the related task assigned to the specific partner
			related_task_ids = self.env['project.task'].search([('partner_id', '=', self.partner_id.id)])

		self.task_ids = related_task_ids.ids if related_task_ids else False