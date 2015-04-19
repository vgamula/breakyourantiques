from antiques import db


class ActiveRecordMixin():
    def save(self, commit=True):
        db.session.add(self)
        if commit:
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
