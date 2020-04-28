# TODO buscar comandos de git en consola de visual, git con linea de comandos 
# TODO ingresar el metodo para que salga el error

import web

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant') 

urls = (
	'/alumnos?', 'application.controllers.alumnos.Alumnos' 
)
app = web.application(urls, globals())

#render = web.template.render('templates/') 

if __name__ == "__main__":
	web.config.debug = False
	app.run()