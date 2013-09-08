from pydi import Container
from burnlib.core.configuration import settings
from burnlib.sqlalchemy.utils import sqlalchemy_session_factory
from burnlib.users.services import GameCenterUserService
from burnlib.users.services import UserService

from burnlib.sqlalchemy.drivers.users import UserDriver
from burnlib.sqlalchemy.drivers.users import GameCenterUserDriver


def sqlalchemy_session():
    session_factory = sqlalchemy_session_factory(
        settings.data['burn:sqlalchemy:test'],
        echo=False)

    return session_factory


def build_container(session):

    container = Container()

    container.register(GameCenterUserService) \
    .depends(GameCenterUserDriver, session_factory=session)

    container.register(UserService) \
    .depends(UserDriver, session_factory=session)

    # container.register(UserService) \
    # .depends(SqlAlchemyUserResource, session_factory=session)

    # container.register(ChannelService) \
    # .depends(SqlAlchemyChannelResource, session_factory=session)

    # container.register(ClientService) \
    # .depends(SqlAlchemyClientResource, session_factory=session)

    # container.register(ProjectService) \
    # .depends(SqlAlchemyProjectResource, session_factory=session)

    # container.register(CollectorService) \
    # .depends(SqlAlchemyCollectorResource, session_factory=session)

    # container.register(ChannelAccountService) \
    # .depends(SqlAlchemyChannelAccountResource, session_factory=session)

    # container.register(JobService) \
    # .depends(SqlAlchemyJobResource, session_factory=session)

    return container
