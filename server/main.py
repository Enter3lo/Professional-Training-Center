import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


def load_curses():
    connection = sqlite3.connect('databases/Professional-Training-Center.db')
    query = 'SELECT curses.title, requirements.title, type,' \
            ' price, form_education, date_start, date_finish,' \
            ' count_hours, count_months ' \
            'FROM curses INNER JOIN requirements ' \
            'ON curses.id = requirements.id '
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
            'ON listener_curses.id = place_of_work.id'
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
