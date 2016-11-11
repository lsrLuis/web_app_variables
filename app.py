import web

render = web.template.render('views/')

urls = ('/','index',
        '/variables(.*)','variables',
        '/vari(.*)','vari',
        '/bucle(.*)','bucle'
        )

class index:
    def GET(self):
        return render.index()

class variables:
    def GET(self, name):
        name = 'Luis'
        return render.variables(name)

class vari:
    def GET(self, name):
        i = web.input(name = None)
        return render.vari(i.name)

class bucle:
    def GET(self, datos):
        datos = ['lunes','martes','miercoles']
        return render.bucle(datos)

if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
