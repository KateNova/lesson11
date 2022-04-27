from utils import *
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:x>")
def candidate_page(x):
    candidate = get_candidate_info(x)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, count=len(candidates))


@app.route("/skill/<skill_name>")
def skills_page(skill_name):
    candidates = get_candidates_by_skills(skill_name)
    return render_template("skill.html", candidates=candidates, skill=skill_name, count=len(candidates))


app.run()
