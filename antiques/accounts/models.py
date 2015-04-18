from antiques import db

from antiques.core.date import utc_now


class User(db.Model):
    """ regular user """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), null=False)
    first_name = db.Column(db.String(255))
    last_name = db.String(db.String(255))
    created_at = db.Column(db.DataTime(timezone=True), default=utc_now)

    is_active = db.Column(db.Boolean, default=True)
    is_staff = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=True)
