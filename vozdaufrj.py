from bottle import route, run, request, template, static_file
import sqlite3

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./imagens/')
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./estilo/')
@route('/java/<filename>')
@route('/')
def index():
    x=0
    conn = sqlite3.connect('vozdaufrj.db')
    c = conn.cursor()
    c.execute("SELECT * FROM noticias ORDER BY `id`DESC limit 10;")
    result = c.fetchall()
    c.close()

    return template('home',result=result, x=x, y=0)
@route('/criar', method="GET")
def index():
    if request.GET.save:

        titulo = request.GET.titulo.strip()
        conteudo=request.GET.conteudo.strip()
        autor=request.GET.autor.strip()
        curso=request.GET.curso.strip()
        conn = sqlite3.connect('vozdaufrj.db')
        c = conn.cursor()


        c.execute("INSERT INTO noticias (titulo,autor,curso,conteudo) VALUES (?,?,?,?)", (titulo,autor,curso,conteudo))


        conn.commit()
        c.close()

        return template('add')
    else:
        return template('add')


    return template('add')
run(host='localhost', port=8080)
