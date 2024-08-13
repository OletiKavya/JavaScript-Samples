from flask import Flask, request, jsonify
import sendgrid
from flask_cors import CORS
from sendgrid.helpers.mail import Mail, Email, To, Content

app = Flask(__name__)
CORS(app)

# Replace with your SendGrid API key
SENDGRID_API_KEY = 'Enter Secure API Key'

@app.route('/send', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email("oletiramanjulukavya@gmail.com")  # Replace with your SendGrid verified email
    to_email = To("oletiramanjulukavya@gmail.com")  # Replace with the recipient's email
    subject = "Hi Kavya!! New Contact Form Message"
    content = Content("text/plain", f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.send(mail)
        return jsonify({"message": "Message sent successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send message."}), 500

if __name__ == '__main__':
    app.run(debug=True)
