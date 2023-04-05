'''
Para adaptar o código para o banco de dados Oracle utilizando a biblioteca psycopg2, algumas alterações precisam ser feitas no código. 
Primeiramente, é necessário importar a biblioteca cx_Oracle para fazer a conexão com o banco de dados Oracle. 
Além disso, algumas funções precisam ser adaptadas para o uso do Oracle. Abaixo está o código adaptado:
'''
import cx_Oracle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate

# Configurações do banco de dados
host = "IP_DO_BANCO"
port = 1521 # Porta padrão do Oracle
sid = "NOME_SID"
user = "USUARIO"
password = "SENHA_DO_USUARIO"

# Configurações do e-mail
from_email = "no-reply@email.com"
from_password = "SENHA_DO_EMAIL"
to_email = ["email1@instituicao.com", "email2@instituicao.com","email1@instituicao.com"]
subject = "Relatório de uso de disco"

# Conexão com o banco de dados
dsn_tns = cx_Oracle.makedsn(host, port, sid=sid)
conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)

# Consulta SQL
cursor = conn.cursor()
cursor.execute("""
SELECT DISTINCT(tabela1.coluna1) AS "Modalidade",
        COUNT(DISTINCT(tabela1.coluna2)) AS "Estudos",
        ROUND(SUM(tabela_imagem.coluna3)/1024/1024/1024,1) AS "Tamanho (GB)"
        --ROUND(SUM(tabela3.coluna3)/1024/1024,1) AS "Tamanho (MB)"
    FROM tabela1
    INNER JOIN tabela2 ON tabela1.coluna3 = tabela2.coluna3
    INNER JOIN tabela3 ON tabela2.coluna3 = tabela3.coluna3
    where  to_date(tabela1.coluna1, 'YYYYMMDD') >= SYSDATE - 30
    GROUP BY tabela1.coluna1
    ORDER BY 3 DESC;
""")
results = cursor.fetchall()

# Criação das tabelas com os resultados
headers = ["Modalidade", "Estudos", "Tamanho (GB)"]
rows = []
for result in results:
    row = [result[0], result[1], result[2]]
    rows.append(row)

table_html = tabulate(rows, headers=headers, tablefmt="html")
table_text = tabulate(rows, headers=headers, tablefmt="grid")

# Montagem da mensagem de e-mail em formato HTML
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = ", ".join(to_email)
msg['Subject'] = subject

body = f"""
<html>
    <body>
        <h1>Monitoramento de Volumetria CLIENTE</h1>
        <p>Segue abaixo o relatório de uso de disco nos últimos 30 dias:</p>
        {table_html}
    </body>
</html>"""

msg.attach(MIMEText(body, 'html'))

# Envio do e-mail
with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.starttls() # adiciona criptografia STARTTLS
    smtp.login(from_email, from_password)
    smtp.sendmail(from_email, to_email, msg.as_string())

print("Email enviado com sucesso !")
