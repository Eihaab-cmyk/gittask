from extensions import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    URL = db.Column(db.String(500), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('title', 'company', name='uq_title_company'),
    )