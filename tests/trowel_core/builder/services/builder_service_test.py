import pytest
import pytest_mock

from src.trowel_core.builder.services import BuilderService

@pytest.fixture
def builder_service(mocker: pytest_mock.MockerFixture):
	return BuilderService(mocker.Mock())


class TestBuilderService:
	def test_build_should_call_strategy(self, builder_service: BuilderService):
		builder_service.run('')
		builder_service._strategy.build.assert_called_once()