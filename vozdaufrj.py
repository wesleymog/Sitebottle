from bottle import route, run, request, template, static_file
import sqlite3

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./imagens/')
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./estilo/')
@route('/java/<filename>')
def server_static(filename):
    return static_file(filename, root='./js/')
@route('/')
def index():
    x=0
    conn = sqlite3.connect('vozdaufrj.db')
    c = conn.cursor()
    c.execute("SELECT * FROM noticias ORDER BY `id`DESC;")
    result = c.fetchall()
    c.close()

    return template('home',result=result, x=x, y=0)
@route('/editar')
def index():
    print 'eta onde to'
    x=0
    conn = sqlite3.connect('vozdaufrj.db')
    c = conn.cursor()
    c.execute("SELECT * FROM noticias;")
    result = c.fetchall()
    c.close()
    if request.GET.editar:
        print 'Olalalalao!'
        indice= request.GET.id.strip()
        titulo = request.GET.titulo.strip()
        conteudo=request.GET.conteudo.strip()
        imagem=request.GET.imagem.strip()
        conexao = sqlite3.connect('vozdaufrj.db')
        curso = conexao.cursor()
        print (titulo)


        curso.execute("UPDATE noticias SET titulo=?,conteudo=?,imagem=? WHERE ID=?", (titulo, conteudo, imagem, indice))
        new_id = c.lastrowid
        conn.commit()
        c.close()



    return template('editar',result=result, x=x, y=0)
@route('/add', method="GET")
def index():
    if request.GET.save:
        print 'Eis me aqui'
        titulo = request.GET.titulo.strip()
        conteudo=request.GET.conteudo.strip()
        imagem=request.GET.imagem.strip()
        conn = sqlite3.connect('vozdaufrj.db')
        c = conn.cursor()
        print (titulo)

        c.execute("INSERT INTO noticias (titulo,conteudo,imagem) VALUES (?,?,?)", (titulo,conteudo, imagem))


        conn.commit()
        c.close()

        return template('add')
    else:
        return template('add')


    return template('add')
@route ('/admin')
def index():
    return template('admin')

run(host='localhost', port=8081)
