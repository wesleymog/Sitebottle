% include('header.tpl', title='Page Title')
        <div class="container">
          <form>
            <div class="form-group">
              <label for="titulo">Título</label>
              <input type="text" class="form-control" id="titulo" name="titulo" maxlength="40" placeholder="Insira o Título">
            </div>

            <div class="form-group">
              <label for="autor">Autor</label>
              <input type="text" class="form-control" id="autor" name="autor" maxlength="40" placeholder="Insira um nickname">
            </div>

            <div class="form-group">
              <label for="titulo">Curso</label>
              <input type="text" class="form-control" id="curso" name="curso" maxlength="40" placeholder="Insira seu curso">
            </div>

            <div class="form-group">
              <label for="titulo">Título</label>
              <input type="text" class="form-control" id="titulo" name="titulo" maxlength="40" placeholder="Insira o Título">
            </div>


            <div class="form-group">
              <label for="conteudo">Conteúdo</label>
              <textarea class="form-control" id='conteudo'name="conteudo" rows="4"></textarea>
            </div>


            <button type="submit" name="save" class="btn btn-primary" value="save">Enviar</button>
          </form>
        </div>

% include('footer.tpl')
