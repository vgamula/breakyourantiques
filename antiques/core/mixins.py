from antiques import db


class ActiveRecordMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_one(cls, **params):
        return cls.query.filter_by(**params).first()

    @classmethod
    def find(cls, **params):
        return cls.query.filter_by(**params).all()
