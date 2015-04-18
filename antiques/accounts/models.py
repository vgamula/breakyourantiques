from antiques import db

from antiques.core.date import utc_now
from antiques.core.mixins import ActiveRecordMixin


class User(ActiveRecordMixin, db.Model):
    """ regular user """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.String(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=utc_now)

    is_active = db.Column(db.Boolean, default=True)
    is_staff = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=True)

    @property
    def full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return u'<User %r>' % self.email

    def __unicode__(self):
        return self.fullname

    # Methods for Flask-Login

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    # End Flask-Login methods
