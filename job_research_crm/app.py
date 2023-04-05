from flask import Flask
from flask import request, render_template
# import db_processing
import al_db
import email_lib
from models import Vacancy, Event, EmailCredentials


app = Flask(__name__)

vacancies_data = [
    {
     'id': 1,
     'creation_date': '03.02.2023',
     'status': 1,
     'company': 'GPQR',
     'contacts_ids': [1, 2],
     'description': 'Vaca desc',
     'position_name': 'Junior Py dev',
     'comment': 'mild reqs and cool salary',
     'user_id': 1
    },
    {
     'id': 2,
     'creation_date': '04.02.2023',
     'status': 2,
     'company': 'Balance',
     'contacts_ids': [2, 4],
     'description': 'Vaca desc',
     'position_name': 'Trainee Py dev',
     'comment': 'mild reqs and cool salary',
     'user_id': 1
    },
    {
     'id': 3,
     'creation_date': '05.02.2023',
     'status': 1,
     'company': 'Future',
     'contacts_ids': [5, 6],
     'description': 'Vaca desc',
     'position_name': 'Junior Py dev',
     'comment': 'mild reqs and cool salary',
     'user_id': 1
    }
]

events_data = [
    {
        'id': 1,
        'vacancy_id': 1,
        'description': 'blablabla',
        'event_date': '10.02.2023',
        'title': ' Event title',
        'due_to_date': '15.02.2023',
        'status': 1
    },
    {
        'id': 2,
        'vacancy_id': 2,
        'description': 'blablabla2',
        'event_date': '12.02.2023',
        'title': ' Event title',
        'due_to_date': '16.02.2023',
        'status': 1
    },
    {
        'id': 3,
        'vacancy_id': 3,
        'description': 'blablabla3',
        'event_date': '13.02.2023',
        'title': ' Event title',
        'due_to_date': '17.02.2023',
        'status': 1
    },

]


@app.route('/')
def hello():
    return 'Hello world! '


@app.route('/vacancy', methods=['GET', 'POST', 'PUT'])
def vacancy():
    al_db.init_db()

    # with db_processing.DB() as db:
    if request.method == 'POST':
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')

        current_vacancy = Vacancy(position_name, company, description, contacts_id, comment, 1, 1)
        al_db.db_session.add(current_vacancy)
        al_db.db_session.commit()
    elif request.method == 'PUT':
        pass
    result = al_db.db_session.query(Vacancy).all()
    return render_template('vacancy_add.html', vacancies=result)


@app.route('/vacancy/<vacancy_id>', methods=['GET', 'PUT'])
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
