from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/vacancy', methods=['GET', 'POST'])
def vacancy():
    return 'all vacancies'


@app.route('/vacancy/<id>', methods=['GET', 'PUT'])
def vacancy_id():
    return 'vacancy id'


@app.route('/vacancy/<id>/events', methods=['GET', 'POST'])
def vacancy_id_events():
    return 'events of the vacancy'


@app.route('/vacancy/<id>/events/<event id>', methods=['GET', 'PUT'])
def vacancy_id_events_event_id():
    return 'events of the vacancy with event id'


@app.route('/vacancy/<id>/history', methods=['GET'])
def vacancy_id_history():
    return 'vacancy history'


@app.route('/user', methods=['GET'])
def user_main_page():
    return 'user dashboard'


@app.route('/user/calendar', methods=['GET'])
def user_calendar():
    return 'user calendar'


@app.route('/user/email', methods=['GET'])
def user_email():
    return 'user email'


@app.route('/user/settings', methods=['GET', 'PUT'])
def user_settings():
    return 'user settings'


@app.route('/user/documents', methods=['GET', 'POST'])
def user_docs():
    return 'user documents'


@app.route('/user/templates', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user_templates():
    return 'user templates'


if __name__ == '__main__':
    app.run()
