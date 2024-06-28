from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route('/candidate/<int:uid>')
def page_candidate_id(uid):
    candidate = get_candidate(uid)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def page_candidates_by_name(candidate_name):
    candidates, counter = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, counter=counter)


@app.route('/skill/<skill_name>')
def pege_candidates_by_skill(skill_name):
    candidates, counter = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, counter=counter, skill_name=skill_name)


app.run()
