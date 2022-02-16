from flask import Flask

import utils

app = Flask(__name__)


@app.route('/', )
def page_index():
    candidates = utils.load_candidates()
    page_content = utils.preformatted_list(candidates)
    return page_content


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    candidate = utils.get_candidates_by_id(uid)
    if not candidate:
        return '<pre><b>' + 'Кандидат по данному ID не найден!' + '</b></pre>'

    candidates = [candidate]
    page_content = utils.preformatted_list(candidates)
    return page_content


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skills(skill_name)
    page_content = utils.preformatted_list(candidates)
    return page_content


app.run()
