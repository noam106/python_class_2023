from flask import Flask, jsonify, request
import datetime
import calendar
import spacy

# app = Flask("example app")
#
# @app.route('/')
# def greeting():
#     return 'hello'
#
# if __name__=='__main__':
#     app.run(debug=True)

# app = Flask('W0')
# @app.route('/api/names/<name>/length')
# def len_name(name: str):
#     num = len(name)
#     data = {'name len': num}
#     return jsonify(data)
#
# @app.route('/api/dates/<date>?season=true&is_leap=true&days_in_month=true')
# def date_analsys(date: str):
#     datetime_object = datetime.datetime.strptime(date, '%d-%m-%Y')
#     is_leap = None
#     season = None
#     day_in_month = None
#     if 'is_leap' in request.args:
#         if request.args['is_leap'] is True:
#             is_leap = calendar.isleap(datetime_object.year)
#
#     if 'season' in request.args:
#         if request.args['season'] is True:
#             if datetime_object.month in (1,2,3):
#                 season = 'winter'
#             elif datetime_object.month in (4,5,6):
#                 season = 'spring'
#             elif datetime_object.month in (7,8,9):
#                 season = 'summer'
#             else:
#                 season = 'fall'
#
#     if 'days_in_month' in request.args:
#         if request.args['days_in_month'] is True:
#             day_in_month = calendar.monthrange(datetime_object.year, datetime_object.month)[1]
#
#
#
#     data = {'date': datetime_object,
#             'is_leap': is_leap,
#             'Season': season,
#             'Day_in_month': day_in_month}
#     return jsonify(data)


app = Flask('w6')


@app.route('/api/v1/sentences', methods =['POST'])
def sentences_divide():
    text = request.form['text']
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    data = {}

    for i, sentence in enumerate(doc.sents):
       data[i] = sentence.text
    return jsonify(data)

@app.route('/api/v1/pos/<text>')
def pos_analesys(text):
    data = {}
    for i, sentence in enumerate(text):
        for

if __name__ == '__main__':
    app.run(debug=True)


