from odoo import models, fields, api



class WatchVideo(models.TransientModel):
    _name = 'watch.video'
    
    url = fields.Text(string="Video Link")
    