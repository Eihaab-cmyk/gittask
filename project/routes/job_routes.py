from flask import Blueprint, request, jsonify
from extensions import db
from models.jobs import Job
from schema.job_schema import job_schema, jobs_schema

job_bp = Blueprint("jobs", __name__, url_prefix="/jobs")

@job_bp.get("/")
def get_jobs():
    query = Job.query
    city = request.args.get("city")
    position = request.args.get("position")

    if city:
        query = query.filter(Job.location.ilike(f"%{city}%"))
    if position:
        query = query.filter(Job.title.ilike(f"%{position}%"))
    
    jobs = query.all()
    return jsonify(jobs_schema.dump(jobs))

@job_bp.get("/<int:job_id>")
def get_job(job_id):
    job = Job.query.get_or_404(job_id)
    return job_schema.jsonify(job)

@job_bp.post("/")
def add_job():
    data = request.json
    required = ["title", "company", "location", "URL"]
    for r in required:
        if r not in data:
            return jsonify({"error": f"{r} is required"}), 400
    new_job = Job(
        title = data["title"],
        company = data["company"],
        location = data["location"],
        URL = data["URL"]
    )

    db.session.add(new_job)
    db.session.commit()
    return job_schema.jsonify(new_job), 201

@job_bp.put("/<int:job_id>")
def update_job(job_id):
    job = Job.query.get_or_404(job_id)
    data = request.json
    job.title = data.get("title", job.title)
    job.company = data.get("company", job.company)
    job.location = data.get("location", job.location)
    job.URL = data.get("URL", job.URL)

    db.session.commit()
    return job_schema.jsonify(job)

@job_bp.delete("/<int:job_id>")
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()

    return jsonify({"message": "Job deleted successfully"})