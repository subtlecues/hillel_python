from flask import Flask
from flask import request, render_template
# import db_processing
import al_db, email_lib
from mongo_lib import MongoLibrary
from models import Vacancy, Event, EmailCredentials
from bson.objectid import ObjectId


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world! '


@app.route('/vacancy', methods=['GET', 'POST', 'PUT'])
def vacancy():
    al_db.init_db()

    if request.method == 'POST':
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contact_name = request.form.get('contact_name')
        contact_email = request.form.get('contact_email')
        contact_phone = request.form.get('contact_phone')
        comment = request.form.get('comment')

        contact_id_insert = MongoLibrary.contacts_collection.insert_one(
            {"name": contact_name, "email": contact_email, "phone": contact_phone}
        ).inserted_id

        current_vacancy = Vacancy(position_name, company, description, str(contact_id_insert), comment, 1, 1)
        al_db.db_session.add(current_vacancy)
        al_db.db_session.commit()

    elif request.method == 'PUT':
        pass
    result = al_db.db_session.query(Vacancy.position_name, Vacancy.company, Vacancy.contacts_id).all()
    result_data = []
    for item in result:
        contacts = item[2].split(',')
        contacts_result = []
        for one_contact in contacts:
            data = MongoLibrary.contacts_collection.find_one({'_id': ObjectId(one_contact)})
            contacts_result.append(data)

        result_data.append({'position_name': item[0], 'company': item[1], 'contacts': contacts_result})
    return render_template('vacancy_add.html', vacancies=result_data)


@app.route('/vacancy/<vacancy_id>/', methods=['GET', 'PUT'])
def vacancy_id(vacancy_id):
    al_db.init_db()
    if request.method == 'GET':
        result = al_db.db_session.query(Vacancy).filter_by(id=vacancy_id).all()
        return render_template('vacancy_add.html', vacancies=result)
    else:
        vacancy = al_db.db_session.add(Vacancy).filterby(id=vacancy_id).all()
        return vacancy, al_db.db_session.commit()


@app.route('/vacancy/<vacancy_id>/events', methods=['GET', 'POST'])
def vacancy_id_events(vacancy_id):
    al_db.init_db()
    if request.method == 'POST':
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        title = request.form.get('title')
        due_to_date = request.form.get('due_to_date')

        current_event = Event(title, description, due_to_date, status=1)
        al_db.db_session.add(current_event)
        al_db.db_session.commit()

    else:
        result = al_db.db_session.query(Event).all()
        return render_template('event_add.html', events=result)


@app.route('/vacancy/<vacancy_id>/events/<event_id>', methods=['GET', 'PUT'])
def vacancy_id_events_id(vacancy_id, event_id):
    if request.method == 'GET':
        result = al_db.db_session.query(Event).filter_by(vacancy_id=vacancy_id, id=event_id).all()
        return render_template('event_add.html', events=result)

@app.route('/vacancy/history', methods=['GET'])
def vacancy_history():
    return 'vacancy history'


@app.route('/user', methods=['GET'])
def user_main_page():
    return 'user dashboard'


@app.route('/user/calendar', methods=['GET'])
def user_calendar():
    return 'user calendar'


@app.route('/user/email/', methods=['GET', 'POST'])
def user_email():
    user_settings = al_db.db_session.query(EmailCredentials).filter_by(user_id=1).first()
    email_object = email_lib.EmailWrapper(
        user_settings.login,
        user_settings.password,
        user_settings.email,
        user_settings.smtp_server,
        user_settings.smtp_port,
        user_settings.pop_server,
        user_settings.pop_port,
        user_settings.imap_server,
        user_settings.imap_port
    )
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        email_message = request.form.get('email_message')
        email_object.send_email(recipient, email_message)
        return 'Mail sent'
    emails = email_object.get_emails([1], protocol='pop3')
    return render_template('send_email.html', emails=emails)


@app.route('/user/settings', methods=['GET', 'PUT'])
def show_user_settings():
    return 'user settings'


@app.route('/user/documents', methods=['GET', 'POST'])
def user_docs():
    return 'user documents'


@app.route('/user/templates', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user_templates():
    return 'user templates'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5030)
