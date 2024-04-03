from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http

class mycustomportal(CustomerPortal):

	def _prepare_home_portal_values(self,counters):
		rtn = super(mycustomportal, self)._prepare_home_portal_values(counters)
		rtn['customers_counts'] = request.env['res.partner'].search_count([])
		return rtn


	@http.route(['/my/customer'], type="http", website=True, auth="public")
	def mycustomerportal(self, **kw):
		customer_obj = request.env['res.partner']
		customer = customer_obj.search([], limit=10)
		vals = {'customers':customer, 'page_name':'customer_list'}
		print(vals)
		return request.render("custom_web_portal.web_customer_portal_list_view", vals)

	@http.route(['/my/customer/<model("res.partner"):id>'], type="http", website=True, auth="public")
	def mycustomerformview(self, id , **kw):
		vals = {'id':id, 'page_name':'customer_form'}
		return request.render("custom_web_portal.web_customer_portal_form_view",vals)
