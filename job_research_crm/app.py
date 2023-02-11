from flask import Flask
from flask import request, render_template
import db_processing

app = Flask(__name__)

vacancies_data = [
    {
     'id': 1,
     'creation_date': '03.02.2023',
     'status': 1,
     'company': 'GPQR',
     'contacts_ids': [1,2],
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
     'contacts_ids': [2,4],
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
     'contacts_ids': [5,6],
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


@app.route('/vacancy', methods=['GET', 'POST'])
def vacancy():
    if request.method == 'POST':
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description =  request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')
        vacancy_data = {'user_id': 1, 'creation_date': '04-02-2023 ', 'position_name': position_name, 'company': company, 'description': description, 'contacts_id': contacts_id, 'comment': comment}
        db_processing.insert_info('vacancy', vacancy_data)
    return render_template('vacancy_add.html')

@app.route('/vacancy/<vacancy_id>', methods=['GET', 'PUT'])
def vacancy_id(vacancy_id):
    for vacancy in vacancies_data:
        if vacancy['id'] == vacancy_id:
            return vacancy # 'vacancy id'


@app.route('/vacancy/<vacancy_id>/events', methods=['GET', 'POST'])
def vacancy_id_events(vacancy_id):
    events_list = []
    for event in events_data:
        if event['vacancy_id'] == vacancy_id:
            events_list.append(event)
    return events_list


@app.route('/vacancy/<vacancy_id>/events/<event_id>', methods=['GET', 'PUT'])
def vacancy_id_events_id(vacancy_id, event_id):
    for event in events_data:
        if event['id'] == event_id:
            return event

@app.route('/vacancy/history', methods=['GET'])
def vacancy_history():
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
