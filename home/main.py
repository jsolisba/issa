from flask import Flask, render_template, request, jsonify,redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.utils import secure_filename
import os
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup


app = Flask(__name__)

def send_email(body):

    smtp_server = 'smtp.zoho.com'
    smtp_port = 587
    smtp_user = 'comercial@issacr.net'
    smtp_password = '7cnHvJ0rJwVv'


    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = smtp_user
    msg['Subject'] = 'Solicitud de información'
    msg.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Login to the SMTP server using the application-specific password
            server.login(smtp_user, smtp_password)
            # Send email
            server.sendmail(smtp_user, smtp_user, msg.as_string())
            print('Email sent successfully.')
    except Exception as e:
            print('An error occurred while sending the email:', e)

@app.route("/", methods=["POST", "GET"])
def contactus():
     return "Hola desde Flask!"

@app.route('/email', methods=['POST'])
def post_data():

    name = request.form.get('nombre')
    lastname = request.form.get('apellido')
    email = request.form.get('correo')
    position = request.form.get('puesto')
    company = request.form.get('empresa')
    message = request.form.get('mensaje')
 

    #response = requests.post('http://127.0.0.1:5000/email', data={'name': name, 'apellido': lastname, 'email': email, 'puesto': position, 'empresa': company, 'mensaje$

    #if response.status_code == 200:
     #   return jsonify({'status': 'success', 'message': 'Formulario enviado correctamente'})

    
# Check if the post request has the file part
   # if 'attachment' not in request.files:
    #    return 'No file part'
   # file = request.files['attachment']
   # if file.filename == '':
  #     return 'No selected file'
   # if file:
   #     filename = secure_filename(file.filename)
  #      file.save(os.path.join('C:/email/', filename))

    # Construct the email content
    payload = f"""
    <p>Nombre: {name} </p>
    <p>Apellido: {lastname}</p>
    <p>Puesto: {position}</p>
    <p>Empresa: {company}</p>
    <p>Correo: {email}</p>
    <p>Mensaje: {message}</p>
    """
    #print(payload,"payload")
    soup = BeautifulSoup(payload, 'html.parser')
    #print(soup,"soup")
    body = soup.get_text(separator='\n')
    #print(body,"body")
    send_email(body)
    # Send email logic here
    # Mensaje a mostrar
    mensaje = 'Form submitted successfully!'

    # Renderizar la plantilla y pasar el mensaje
    return render_template('backend.html', mensaje=mensaje)

@app.route('/ruta-en-el-frontend')
def ruta_en_el_frontend():
    # Redirige al frontend
    return redirect("https://jsolisba.github.io/issa/index.html")

    #else:
     #   return jsonify({'status': 'error', 'message': 'Error al enviar el formulario'})


if __name__ == "__main__":
    app.run(debug=True)
