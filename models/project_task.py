#!/usr/bin/env python
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class ProjectTask(models.Model):
	_inherit = "project.task"

	service_id = fields.Integer('Service ID')

	def get_service_task(self):
		self.service_id = self.get_service()

	def get_service(self):
		"""
		Allow to get the service ID
		"""
		# Mock endpoint for the technical challenge, I created this endpoint
		res = requests.get('https://servicebia.free.beeceptor.com')
		if res.status_code == 200:
			return res.json().get('service_id')
		return False

	@api.model
	def create(self, vals):
		"""
		Allow to call the get service when the new record is created
		"""
		service = self.get_service()
		if service:
			# Allow update the vals before to save the task in the db
			vals.update({'service_id' : service})

		res = super(ProjectTask, self).create(vals)
		return res
	