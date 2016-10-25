% include('header.tpl', title='Page Title')
        <div class="container">
           <div class="row">
               <div class="col-md-8 col-md-offset-2">
                   <div class="panel panel-default">
                       <div class="panel-heading">Notícias</div>
                       <div class="panel-body">
                          %for linha in result:
                          <div class="noticias">
                          <form method="get">
                                %for obj in linha:

                                    %if x==0:
                                        <input class="escondidinho" type="text" name="id" value="{{obj}}">
                                        %x=x+1
                                    %elif x==1:
                                        <div class="form-group">
                                        <label for="titulo">Título</label>
                                        <input type="text" class="form-control" name="titulo" value="{{obj}}" size="35">
                                        </div>
                                        %x=x+1
                                    %elif x==2:
                                        <div class="form-group">
                                        <label for="conteudo">Conteudo</label>
                                        <textarea type="text" class="form-control" name="conteudo" >{{obj}}</textarea>
                                        </div>
                                        %x=x+1
                                    %elif x==3:
                                        <div class="form-group">
                                        <label for="imagem">Imagem</label>
                                        <input type="file" name="imagem" value="{{obj}}" class="form-control-file">
                                        </div>
                                        <button class="btn btn-warning" value="editar" name="editar">Editar</button>
                                        <button class="btn btn-danger" name="deletar">Deletar</button>
                                      </div>
                                        %x=x-3
                                        %y=y+1
                                        %if len(result)==y:




                      </div>
                   </div>
               </div>
           </div>
       </div>

   </div>

% include('footer.tpl')
