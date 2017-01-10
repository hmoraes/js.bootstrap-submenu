from fanstatic import Library, Resource, Group
from js.bootstrap import bootstrap
from js.jquery import jquery

library = Library('bootstrap_submenu', 'resources')

bootstrap_submenu_css = Resource(library, 'css/bootstrap-submenu.css',
                        minified='css/bootstrap-submenu.min.css',
                        depends=[])

bootstrap_submenu_js = Resource(library, 'js/bootstrap-submenu.js',
                        minified='js/bootstrap-submenu.min.js',
                        bottom=True,
                        depends=[bootstrap, jquery,])

bootstrap_submenu = Group([bootstrap_submenu_css, bootstrap_submenu_js,])
