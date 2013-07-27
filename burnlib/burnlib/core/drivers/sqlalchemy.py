from .base import Driver


class SqlAlchemyDriver(Driver):
    ''' Our SQLAlchemy based resources will be working with sessions.
    Typically, this is easy to reason about in a web request:

    #. Web Request starts and the session is created.
    #. All of the work is done.
    #. When the request ends, the session is then committed.

    However, we may be using SqlAlchemyResource based objects in a non-web
    context. So the question becomes how to handle the SQLAlchemy Session?

    Given the Service + Resource pattern we have established, it does not
    make sense to expose any of the SQLAlchemy based operations outside of
    the SqlAlchemyResource itself. There would be no point in abstracting
    away the Service/Resource idea, as we would leak the underlying
    SQLAlchemy handling.

    To that end, all of the session control should be contained within
    child resource implementations. In most cases, we are just doing something
    simple like createing a user. No other DB manipulation would need to
    happen. Thinking about this in web terms: we are submitting a user form,
    creating the user, and redirecting the client to some other location after
    the POST. The only DB manipulation is the user related work.

    However, there may be cases where a more complex transaction is required.
    In those cases that work should be encapsulated in the SqlAlchemyResource
    implementation, retaning full control over the session until the complex
    transaction is ready to be committed. Under this methodology, the
    underlying SQLAlchemy mehcnaics should never need to leak out of the
    SqlAlchemyResource object.

    Reference:
    http://docs.sqlalchemy.org/en/rel_0_8/orm/session.html#unitofwork-contextual

    This also means, that once the required work is complete, and the session
    has been terminated, you may not want to expire ORM based objects you wish
    to return or use after the action.

    By default, a SQLAlchemy ``commit()``
    will expire all of the objects in the transaction::

        Note that expire_all() is called automatically whenever commit()
        or rollback() are called.

    See: http://docs.sqlalchemy.org/en/rel_0_8/orm/session.html#refreshing-expiring
    for more information.

    Once expired, the next attribute access on the object
    will attempt to use it's session to update the object if needed. If the
    session has been destroyed, however, you will get a
    ``DetachedInstanceError`` when attempting attribute access on these
    returned/used objects.

    We can prevent this exception if we instruct the session not to expire
    objects on commit.

    When a session is created, pass expire_on_commit=False as a kwarg:
        .. code:: python
          session = self.session(expire_on_commit=False)
          session.add(user)
          session.commit()
          self.session.remove()

    After the commit, the object will not be expired, aka will not try to
    fetch values from the DB on attribute access if something changed.

    Because we are closing the session with self.session.remove, the object
    will become detached from a session. If we were to expire it, the next
    attribute access will attempt communication to a DB with no session to
    help it find its way. Hence ``DetachedInstanceError``. The arg
    expire_on_commit=False instructs SQLAlchemy not to expire the objects.

    **IMPORTANT** because the object is not expired and it is detached you
    are accepting that there is no more communication to the DB for that
    object. Unless, of course, you merge it into another session.

    Note that we are calling ``self.session.remove`` **NOT**
    ``session.remove``. The latter is used to perform a DELETE operation,
    the former is used to dispose of the session: return connections
    to the pool, etc:

    http://docs.sqlalchemy.org/en/rel_0_8/orm/session.html#sqlalchemy.orm.scoping.scoped_session.remove

    '''

    def __init__(self, session_factory):
        '''
        See bigmethod.persistence.sqlalchemy.utils.sqlalchemy_session_factory
        for creating the appropriate session_factory
        '''
        self.session = session_factory
