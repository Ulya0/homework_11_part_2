import json


def load_candidates_from_json():
    """Возвращает список всех кандидатов"""

    with open('candidates.json', 'r') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    """Возвращаяет одного кандидата по id"""

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if int(candidate_id) == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""

    candidates = load_candidates_from_json()
    list_candidates = []
    counter = 0
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            list_candidates.append(candidate)
            counter += 1
    return list_candidates, counter


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""

    candidates = load_candidates_from_json()
    list_candidates = []
    counter = 0
    for candidate in candidates:
        for skill in candidate['skills'].split(', '):
            if skill_name.lower() == skill.lower() and candidate not in list_candidates:
                list_candidates.append(candidate)
                counter += 1
    return list_candidates, counter
