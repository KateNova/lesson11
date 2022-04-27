import json


def load_candidates_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        info = json.load(f)
    return info


def get_candidate_info(candidate_id):
    info = load_candidates_from_json("candidates.json")
    for candidate in info:
        if candidate_id == int(candidate["id"]):
            return candidate
    return None


def get_candidates_by_name(candidate_name):
    info = load_candidates_from_json("candidates.json")
    cand_list = []
    for candidate in info:
        if candidate_name.lower() in candidate["name"].lower():
            cand_list.append(candidate)
    return cand_list


def get_candidates_by_skills(candidate_skill):
    info = load_candidates_from_json("candidates.json")
    candidate_list = []
    for candidate in info:
        if candidate_skill.lower() in candidate["skills"].lower():
            candidate_list.append(candidate)
    return candidate_list
