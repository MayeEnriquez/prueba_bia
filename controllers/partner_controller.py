from odoo import http

class PartnerController(http.Controller):

    @http.route('/update_partner', type='http', auth='public',csrf=False)
    def update_partner(self, **post):
        """
        Endpoint to update the partner information
        """

        # parameters
        partner_id = post.get('partner_id', False)
        name = post.get('name', False)

        if not partner_id or not name:
            return "The partner_id and name are require"

        # Checking if the partner exist or no
        partner = http.request.env['res.partner'].browse(int(partner_id))
        if partner:
            # updating the partner
            partner.sudo().write({'name' : name})
        else:
            return "The system can't find the require partner"

        return f"Partner updated successfully: new name {name}"