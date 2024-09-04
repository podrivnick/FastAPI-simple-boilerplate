from di import (
    bind_by_type,
    Container,
)
from di.api.providers import DependencyProviderType
from di.api.scopes import Scope
from di.dependent import Dependent
from di.executors import AsyncExecutor
from didiator import (
    CommandMediator,
    EventMediator,
    Mediator,
    QueryMediator,
)
from didiator.interface.utils.di_builder import DiBuilder
from didiator.utils.di_builder import DiBuilderImpl


from src.infrastructure.di.const import DiScope
from src.infrastructure.mediator import get_mediator


def init_di_builder() -> DiBuilder:
    di_container = Container()
    di_executor = AsyncExecutor()
    di_scopes = [DiScope.APP, DiScope.REQUEST]
    di_builder = DiBuilderImpl(di_container, di_executor, di_scopes=di_scopes)
    return di_builder


def setup_di_builder(di_builder: DiBuilder) -> None:
    di_builder.bind(
        bind_by_type(Dependent(lambda *args: di_builder, scope=DiScope.APP), DiBuilder),
    )
    setup_mediator_factory(di_builder, get_mediator, DiScope.REQUEST)


def setup_mediator_factory(
    di_builder: DiBuilder,
    mediator_factory: DependencyProviderType,
    scope: Scope,
) -> None:
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), Mediator))
    di_builder.bind(
        bind_by_type(Dependent(mediator_factory, scope=scope), QueryMediator),
    )
    di_builder.bind(
        bind_by_type(Dependent(mediator_factory, scope=scope), CommandMediator),
    )
    di_builder.bind(
        bind_by_type(Dependent(mediator_factory, scope=scope), EventMediator),
    )
