import pandas as pd
from app import create_app
from extensions import db
from models.jobs import Job

CSV_FILE = "C:/Users/hp/Desktop/Scraping/indeed_results.csv"

def import_job():
    app = create_app()
    with app.app_context():
        try:
            df = pd.read_csv(CSV_FILE)
        except FileNotFoundError:
            print("FIle not found")
            return
        
        print(f"Loaded {len(df)} rows from csv")
        inserted = 0
        skipped = 0

        for _, row in df.iterrows():
            title = row.get("Title", "").strip()
            company = row.get("Company", "").strip()
            location = row.get("Location", "").strip()
            url = row.get("URL", "").strip()

            if not title or not company or not url:
                skipped += 1
                continue

            exists = Job.query.filter_by(title=title, company=company).first()

            if exists:
                skipped += 1
                continue

            new_job = Job(
                title = title,
                company = company,
                location = location,
                URL = url
            )

            db.session.add(new_job)
            inserted += 1

        db.session.commit()

        print("\n✅ Import Completed!")
        print(f"   ➕ Inserted: {inserted}")
        print(f"   🔁 Skipped (duplicates): {skipped}")
        print(f"   🎉 Database is now updated with scraped jobs.")

if __name__ == "__main__":
    import_job()