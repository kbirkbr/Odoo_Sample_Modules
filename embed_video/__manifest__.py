# -*- coding: utf-8 -*-
{
    'name': 'Embed Videos',
    'version': '1.0',
    'website': 'https://www.sorrysemicolon.com',
    'author': 'Alpesh Valaki (alpeshvalaki@gmail.com)',
    
    'category': 'Other',
    'summary': 'Embed Videos',
    'description': """this module embed video in form with given video url
""",
    'depends': ['base'],
    'data': [
	    'data/data.xml',
            'views/video_links.xml',
            'wizard/watch_video_view.xml',
        
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
