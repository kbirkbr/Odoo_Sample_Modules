from odoo import models, api, fields




class VideoLinks(models.Model):
    _name = 'video.links'
    
    name = fields.Char(string="Video Name")
    url = fields.Char(string="URL")
    
    
    @api.multi
    def watch_this_video(self):
        
        iframe = "<iframe width='560' height='315' src='%s' frameborder='0' allowfullscreen></iframe>"%(self.url)
        
        return {
                'name' : "Watch Video",
                 'type': 'ir.actions.act_window',
                 'res_model': 'watch.video',
                 'view_type': 'form',
                 'view_mode': 'form',
                 'context': {'default_url': iframe},
                 'target': 'new',
                }