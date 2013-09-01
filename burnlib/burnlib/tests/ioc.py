from pydi import Container
from pydi.utils import Resolve
from bigmethod.core.configuration import settings
from bigmethod.sqlalchemy.utils import sqlalchemy_session_factory
from bigmethod.users.services import UserService
from bigmethod.channels.services import ChannelService
from bigmethod.clients.services import ClientService
from bigmethod.projects.services import ProjectService
from bigmethod.collectors.services import CollectorService
from bigmethod.accounts.services import ChannelAccountService
from bigmethod.jobs.services import JobService
from bigmethod.sqlalchemy.resources.users import SqlAlchemyUserResource
from bigmethod.sqlalchemy.resources.channels import SqlAlchemyChannelResource
from bigmethod.sqlalchemy.resources.clients import SqlAlchemyClientResource
from bigmethod.sqlalchemy.resources.projects import SqlAlchemyProjectResource
from bigmethod.sqlalchemy.resources.collectors import SqlAlchemyCollectorResource
from bigmethod.sqlalchemy.resources.accounts import SqlAlchemyChannelAccountResource
from bigmethod.sqlalchemy.resources.jobs import SqlAlchemyJobResource

from burnlib.users.services import GameCenterService
from burnlib.users.services import UserService


def sqlalchemy_session():
    session_factory = sqlalchemy_session_factory(
        settings.data['bigmethod:sqlalchemy:test'],
        echo=False)

    return session_factory


def build_container(session):

    container = Container()

    container.register(UserService) \
    .depends(SqlAlchemyUserResource, session_factory=session)

    container.register(ChannelService) \
    .depends(SqlAlchemyChannelResource, session_factory=session)

    container.register(ClientService) \
    .depends(SqlAlchemyClientResource, session_factory=session)

    container.register(ProjectService) \
    .depends(SqlAlchemyProjectResource, session_factory=session)

    container.register(CollectorService) \
    .depends(SqlAlchemyCollectorResource, session_factory=session)

    container.register(ChannelAccountService) \
    .depends(SqlAlchemyChannelAccountResource, session_factory=session)

    container.register(JobService) \
    .depends(SqlAlchemyJobResource, session_factory=session)

    return container
