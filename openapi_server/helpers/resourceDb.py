from .. import db
import json

class ResourceDb(db.Model):

    __tablename__ = 'resource_db'
    id = db.Column(db.String, primary_key=True)
    object_class = db.Column(db.String)
    data = db.Column(db.Text)

    def save(self):
        if self.id:
            db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    @staticmethod
    def get_by_id(id):
        return ResourceDb.query.filter_by(id=id).first()


