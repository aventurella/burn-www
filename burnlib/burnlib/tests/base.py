import unittest
from .ioc import build_container
from .ioc import sqlalchemy_session


class SqlAlchemyTest(unittest.TestCase):

    def setUp(self):
        # http://sontek.net/blog/detail/writing-tests-for-pyramid-and-sqlalchemy
        # See base testing class
        session_factory = sqlalchemy_session()

        connection = session_factory.kw['bind'].connect()

        self.trans = connection.begin()

        session_factory.configure(bind=connection)

        self.session = session_factory()
        self.ioc = build_container(self.session)

    def tearDown(self):
        self.trans.rollback()
        self.session.close()
