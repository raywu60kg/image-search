from dependency_injector import containers, providers

from src.adapter.outward.persistence.database import Database
from src.adapter.outward.persistence.feedback.feedback_mapper import FeedbackMapper
from src.adapter.outward.persistence.feedback.feedback_persistence_adapter import (
    FeedbackPersistenceAdapter,
)
from src.adapter.outward.persistence.feedback.feedback_repository import (
    FeedbackRepository,
)
from src.adapter.outward.persistence.image.image_mapper import ImageMapper
from src.adapter.outward.persistence.image.image_persistence_adapter import (
    ImagePersistenceAdapter,
)
from src.adapter.outward.persistence.image.image_repository import ImageRepository
from src.adapter.outward.persistence.search_image_record.search_image_record_mapper import (
    SearchImageRecordMapper,
)
from src.adapter.outward.persistence.search_image_record.search_image_record_persistence_adapter import (
    SearchImageRecordPersistenceAdapter,
)
from src.adapter.outward.persistence.search_image_record.search_image_record_repository import (
    SearchImageRecordRepository,
)
from src.app.domain.service.feedback.give_feedback_service import GiveFeedbackService
from src.app.domain.service.image.search_image_service import SearchImageService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.db_uri.from_env(
        "DB_URI",
        "postgresql+psycopg2://image_search:image_search@localhost:5432/image_search",
    )
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.adapter.inward.web.feedback.router",
            "src.adapter.inward.web.image.router",
        ]
    )
    database = providers.Singleton(Database, db_uri=config.db_uri)

    image_repository = providers.Factory(
        ImageRepository,
        session_factory=database.provided.session,
    )
    feedback_repository = providers.Factory(
        FeedbackRepository,
        session_factory=database.provided.session,
    )
    search_image_record_repository = providers.Factory(
        SearchImageRecordRepository, session_factory=database.provided.session
    )

    image_mapper = providers.Factory(ImageMapper)
    feedback_mapper = providers.Factory(FeedbackMapper)
    search_image_record_mapper = providers.Factory(SearchImageRecordMapper)

    image_persistence_adapter = providers.Factory(
        ImagePersistenceAdapter,
        image_mapper=image_mapper,
        image_repository=image_repository,
    )
    feedback_persistence_adapter = providers.Factory(
        FeedbackPersistenceAdapter,
        feedback_mapper=feedback_mapper,
        feedback_repository=feedback_repository,
    )

    search_image_record_persistence_adapter = providers.Factory(
        SearchImageRecordPersistenceAdapter,
        search_image_mapper=search_image_record_mapper,
        search_image_record_repository=search_image_record_repository,
    )

    give_feedback_service = providers.Factory(
        GiveFeedbackService,
        load_search_image_record_port=search_image_record_persistence_adapter,
        save_feedback_port=feedback_persistence_adapter,
    )
    search_image_service = providers.Factory(
        SearchImageService,
        search_image_port=image_persistence_adapter,
        save_search_image_record_port=search_image_record_persistence_adapter,
    )
