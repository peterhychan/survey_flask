import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(client, employee, rating, comments):
	message = Mail(
		from_email='peterhoychan@outlook.com',
		to_email='pchandemo@gmail.com',
		subject='New Customer Response Received',
		html_content=f"<h3>New Response Received</h3><ul><li>Client: {client}</li><li>Employee: {employee}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
	)
	sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
	response= sg.send(message)
	print(response.status_code, response.body, response.headers)
