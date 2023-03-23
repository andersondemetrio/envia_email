
  <h1>Automatização Python</h1>
  <p>Nesse exemplo, é enviado um e-mail via <a href="https://pt.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol" target="_blank">SMTP</a> ao usuário com um relatório mensal de armazenamento de exames, é feito um agendamento via <a href="https://pt.wikipedia.org/wiki/Crontab" target="_blank">Crontab</a> + integração com <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a> e <a href="https://www.python.org/" target="_blank">Python</a>. Como resultado, o usuário final terá um relatório mensal da quantidade de exames armazenados, bem como a volumetria e modalidade dos mesmos.</p>

<h1> Configuração Crontab no Linux </h1>

<p>Neste cenário, o cliente final possui sistema operacional Linux, logo para o programa seja exexutado mensalmente segue as configuração abaixo </p>

# Configure o script em uma pasta do sistema operacional, de preferência a pasta /opt
# crie uma pasta com o comando mkdir scripts
#edite via editor de texto do linux o vi ou vim arquivo.py
# identifique se o python está instalado, recomendo usar versões maiores que o python 3.6
# identifique se todas as libs estão instaladas, acaso não exexcute o comando pip install pip install psycopg2,  tabulate
#valide se a máquina possui conexão com o banco de dados postgres
