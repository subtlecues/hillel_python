from celery import Celery
import os
import al_db
from email_lib import EmailWrapper
from models import EmailCredentials

RABBIT_HOST = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('celery_worker', broker=f'pyamqp://guest@{RABBIT_HOST}//')

@app.task
def send_email(id_email_credentials, recipient, message):
    al_db.init_db()
    email_creds_detail = al_db.db_session.query(EmailCredentials).get(id_email_credentials)
    email_wrapper = EmailWrapper(**email_creds_detail.get_mandatory_fields())
    email_wrapper.send_email(recipient, message)

