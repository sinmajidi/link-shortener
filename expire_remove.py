from database import URLShortener,db,datetime

def delete_expired_entries():
        expired_entries = URLShortener.query.filter(URLShortener.expiry_date < datetime.utcnow()).all()
        print(expired_entries)
        for entry in expired_entries:
            db.session.delete(entry)
        db.session.commit()
delete_expired_entries()
print("Done")