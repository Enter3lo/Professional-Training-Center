import sqlite3


from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired
from wtforms import Form, DateField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.secret_key = 'Djkf22113jsd2'


def load_curses():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT curses.title, requirements.title,' \
            ' price, form_education.title, date_start, date_finish,' \
            ' count_hours, count_months ' \
            'FROM curses INNER JOIN requirements ' \
            'ON curses.id = requirements.id ' \
            'INNER JOIN form_education' \
            ' ON form_education.id = curses.form_education'
    result = connection.cursor().execute(query).fetchall()
    curses = ''
    for i in range(len(result)):
        curses += '<tr>'
        for j in range(len(result[i])):
            curses += f'<td>{result[i][j]}</td>'
        curses += '</tr>'
    return curses


def load_listener():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT snf, job_title.title, place_of_work.title,' \
            ' gender, date_of_birth ' \
            'FROM listener_curses ' \
            'INNER JOIN job_title ' \
            'ON listener_curses.id = job_title.id ' \
            'INNER JOIN place_of_work ' \
            'ON listener_curses.place_of_work = place_of_work.id'
    result = connection.cursor().execute(query).fetchall()
    listener = ''
    for i in range(len(result)):
        listener += '<tr>'
        for j in range(len(result[i])):
            listener += f'<td>{result[i][j]}</td>'
        listener += '</tr>'
    return listener


@app.route('/')
@app.route('/main')
def main():
    curses_table = load_curses()
    listener_table = load_listener()
    return render_template('index.html',
                           title='Центр обучения профессионалов',
                           style_main='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_main.html',
                           report='reports/report_main.html',
                           view='view/main/view_main.html',
                           curses=curses_table,
                           listener=listener_table)


def load_agreement():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT agreement.date, curses.title, listener_curses.snf, curses.date_start, curses.date_finish, ' \
            'agreement.status_education' \
            ' FROM agreement' \
            ' INNER JOIN curses ON agreement.id = curses.id' \
            ' INNER JOIN listener_curses ON agreement.id = listener_curses.id'
    result = connection.cursor().execute(query).fetchall()
    agreement = ''
    for i in range(len(result)):
        agreement += '<tr>'
        for j in range(len(result[i])):
            agreement += f'<td>{result[i][j]}</td>'
        agreement += '</tr>'
    return agreement


@app.route('/main/agreement')
def agreement():
    agreement_table = load_agreement()
    return render_template('index.html',
                           title='Договоры',
                           style_main='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_main.html',
                           style_agreement='style=background-color:#EAAC25;border-radius:5px;',
                           report='reports/report_main.html',
                           view='view/view_table.html',
                           action='action=/',
                           title_view='Договоры',
                           table='view/main/agreement.html',
                           agreement=agreement_table)


@app.route('/curses')
def curses():
    return render_template('index.html',
                           title='Курсы',
                           style_curses='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_curses.html',
                           report='reports/report_curses.html')


@app.route('/curses/curses_table')
def curses_table():
    curses_table = load_curses()
    return render_template('index.html',
                           title='Курсы',
                           style_curses='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_curses.html',
                           create='/curses/create_curse?query=/curses',
                           style_curses_tabel='style=background-color:#EAAC25;border-radius:5px;',
                           report='reports/report_curses.html',
                           view='view/view_table.html',
                           action='action=/curses',
                           title_view='Курсы',
                           table='view/curses/curses.html',
                           curses=curses_table)


def load_requirements():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT title FROM requirements'
    result = connection.cursor().execute(query).fetchall()
    requirements = ''
    for i in range(len(result)):
        requirements += f'<tr><td>{result[i][0]}</td><tr>'
    return requirements


@app.route('/curses/requirements_tabel')
def requirements_tabel():
    requirements_tabel = load_requirements()
    return render_template('index.html',
                           title='Требования',
                           style_curses='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_curses.html',
                           style_requirements_tabel='style=background-color:#EAAC25;border-radius:5px;',
                           report='reports/report_curses.html',
                           view='view/view_table.html',
                           action='action=/curses',
                           title_view='Требования',
                           table='view/curses/requirements.html',
                           requirements=requirements_tabel)


@app.route('/listener')
def listener():
    return render_template('index.html',
                           title='Слушатели',
                           style_listener='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_listener.html',
                           report='reports/report_listener.html')


@app.route('/listener/agreement')
def agreement_listener():
    agreement_table = load_agreement()
    return render_template('index.html',
                           title='Договоры',
                           style_listener='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_listener.html',
                           style_agreement_tabel='style=background-color:#EAAC25;border-radius:5px;',
                           report='reports/report_listener.html',
                           view='view/view_table.html',
                           action='action=/listener',
                           title_view='Договоры',
                           table='view/listener/agreement_table.html',
                           agreement=agreement_table)


@app.route('/listener/listener_table')
def listener_table():
    listener_table = load_listener()
    return render_template('index.html',
                           title='Слушатели курсов',
                           style_listener='style=background-color:#EAAC25;',
                           list='navigation_tables/nav_listener.html',
                           style_listener_tabel='style=background-color:#EAAC25;border-radius:5px;',
                           report='reports/report_listener.html',
                           view='view/view_table.html',
                           action='action=/listener',
                           title_view='Слушатели крусов',
                           table='view/listener/listener_table.html',
                           listener=listener_table)


def load_requiraments():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT title FROM requirements ORDER BY title'
    result = connection.cursor().execute(query).fetchall()
    requiraments = ''
    for i in range(len(result)):
        requiraments += f'<option value=\'{result[i][0]}\'>{result[i][0]}</option>'
    return requiraments


def load_form_education():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT title FROM form_education ORDER BY title DESC'
    result = connection.cursor().execute(query).fetchall()
    requiraments = ''
    for i in range(len(result)):
        requiraments += f'<option value=\'{result[i][0]}\'>{result[i][0]}</option>'
    return requiraments


class FromCurses(FlaskForm):
    title = StringField('Наименование')
    price = StringField('Стоимость', default='00,00р')
    date_start = DateField('Дата начала')
    date_finish = DateField('Дата окончания')


def create_value_for_curses(title, requirament, price, form_education, date_start, date_finish, count_hundred, count_month):
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = f'INSERT INTO curses (title, requirements, price, form_education, date_start, date_finish, count_hours, ' \
            f'count_months)' \
            f' VALUES (\"{title}\", {requirament}, \"{price}\", {form_education}, \"{date_start}\", \"{date_finish}\", {count_hundred}, {count_month})'
    connection.cursor().execute(query)
    connection.commit()


def get_id_requirament(title):
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = f'SELECT id FROM requirements WHERE title = \"{title}\"'
    result = connection.cursor().execute(query).fetchall()
    return result


def get_id_form_education(title):
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = f'SELECT id FROM form_education WHERE title = \"{title}\"'
    result = connection.cursor().execute(query).fetchall()
    return result


@app.route('/curses/create_curse', methods=['GET', 'POST'])
@app.route('/main/create_curse', methods=['GET', 'POST'])
def create_curse():
    query_requirements = load_requiraments()
    query_form_education = load_form_education()
    form = FromCurses()
    if form.validate_on_submit():
        title = form.title.data
        price = form.price.data

        date_start = form.date_start.data
        date_finish = form.date_finish.data
        formatted_date_start = date_start.strftime('%d.%m.%Y')
        formatted_date_finish = date_finish.strftime('%d.%m.%Y')

        requirement = request.form.get('requirements')
        id_req = get_id_requirament(requirement)
        form_education = request.form.get('education')
        id_form_education = get_id_form_education(form_education)
        count_hundred = request.form.get('count_hundred')
        count_month = request.form.get('count_month')
        create_value_for_curses(title, id_req[0][0], price, id_form_education[0][0], formatted_date_start, formatted_date_finish, count_hundred, count_month)
        return redirect(url_for('curses_table'))
    else:
        query = request.args.get('query')
        nav = 'navigation_tables/nav_'+query[1:]+'.html'
        report = 'reports/report_'+query[1:]+'.html'
        st_main = '#3078FF'
        st_curses = '#3078FF'
        if query == '/main':
            st_main = '#EAAC25;'
        elif query == '/curses':
            st_curses = '#EAAC25;'
        return render_template('index.html',
                               title='Добавление нового курса',
                               style_main=f'style=background-color:{st_main}',
                               style_curses=f'style=background-color:{st_curses}',
                               list=nav,
                               report=report,
                               view='buttons_actions/create_or_edit.html',
                               title_view='Добавление нового курса',
                               action='action=/main',
                               cancel=query,
                               action_create=query+"/create_curse?query="+query,
                               input_field='buttons_actions/curses/curses.html',
                               requirements=query_requirements,
                               form_education=query_form_education,
                               form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
