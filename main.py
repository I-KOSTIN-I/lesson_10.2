from flask import Flask
import utils

app = Flask(__name__)


@app.route('/', )
def page_index():
    candidates = utils.get_candidates_all()
    page_content = utils.preformatted_list(candidates)

    return page_content


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    candidate = utils.get_candidates_by_id(uid)
    page_content = utils.preformatted_list(candidate)
    return page_content


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skills(skill_name)
    page_content = ''

    for candidate in candidates:
        page_content += candidate['name'] + '\n'
        page_content += candidate['position'] + '\n'
        page_content += candidate['skills'] + '\n'
        page_content += '\n'

        return '<pre>' + page_content + '</pre>'


app.run()
