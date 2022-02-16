import json


def load_candidates():
    '''Функция загружает данные из файла'''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_candidates_by_id(uid):
    '''Функция получает данные по ID кандидатов'''
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate

    return None


def get_candidates_by_skills(skill):
    '''Функция получает данные по скиллам кандидатов'''
    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates


def preformatted_list(candidates):
    '''Функция форматирует полученные данные в HTML'''
    page_content = ''

    for candidate in candidates:
        page_content += candidate['name'] + '\n'
        page_content += candidate['position'] + '\n'
        page_content += candidate['skills'] + '\n'
        page_content += '\n'

    return '<pre>' + page_content + '</pre>'
