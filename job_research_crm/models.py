from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from datetime import datetime
from al_db import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    login = Column(String(50), unique=True)
    password = Column(String(120))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.name}'


class EmailCredentials(Base):
    __tablename__ = 'email_credentials'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    login = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    pop_server = Column(String(120), nullable=True)
    imap_server = Column(String(120), nullable=True)
    smtp_server = Column(String(120), nullable=True)
    pop_port = Column(Integer, nullable=True)
    imap_port = Column(Integer, nullable=True)
    smtp_port = Column(Integer, nullable=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'login': self.login,
            'password': self.password,
            'pop_server': self.pop_server,
            'imap_server': self.imap_server,
            'smtp_server': self.smtp_server,
            'pop_port': self.pop_port,
            'imap_port': self.imap_port,
            'smtp_port': self.smtp_port

        }

    def get_mandatory_fields(self):
        return {
            'login': self.login,
            'password': self.password,
            'user_email': self.email,
            'smtp_server': self.smtp_server,
            'smtp_port': self.smtp_port}

    def __init__(self, login, password):
        self.login = login
        self.password = password

    # def __repr__(self):
    #     return f'<EmailCredentials {self.email}>'


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    position_name = Column(String(120), nullable=False)
    company = Column(String(120), nullable=False)
    description = Column(String(200), nullable=False)
    contacts_id = Column(String(120), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    comment = Column(String(120), nullable=True)
    status = Column(Integer, nullable=False)

    def __init__(self, position_name, company, description, contacts_id, comment, status, user_id):
        self.position_name = position_name
        self.company = company
        self.description = description
        self.contacts_id = contacts_id
        self.comment = comment
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return f'<Vacancy {self.position_name}>'


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    event_date = Column(DateTime, default=datetime.utcnow)
    description = Column(String(200), nullable=True)
    title = Column(String(120), nullable=True)
    due_to_date = Column(DateTime, nullable=True)
    status = Column(Integer, nullable=False)

    def __init__(self, title, description, due_to_date, status):
        self.title = title
        self.description = description
        self.due_to_date = due_to_date
        self.status = status

    def __repr__(self):
        return f'<Event {self.title}>'


class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return f'<Template {self.name}>'


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    description = Column(String(200), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name, content, description):
        self.name = name
        self.content = content
        self.description = description

    def __repr__(self):
        return f'<Document {self.name}>'
