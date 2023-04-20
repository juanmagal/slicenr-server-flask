from .. import db
import json

class SliceProfileDb(db.Model):

    __tablename__ = 'slice_profile_db'
    id = db.Column(db.String, primary_key=True)
    data = db.Column(db.Text)

    def save(self):
        if self.id:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return SliceProfileDb.query.filter_by(id=id).first()


