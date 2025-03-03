import click
import pytest
import subprocess
import unittest.mock

from src.trowel_core.builder.strategies import BuilderStrategyMake

@pytest.fixture
def make_strategy():
	return BuilderStrategyMake()


class TestBuilderStrategyMake:
	def test_build_should_be_successful(self, make_strategy: BuilderStrategyMake):
		with unittest.mock.patch('subprocess.run') as mock_run:
			mock_run.return_value = unittest.mock.MagicMock(returncode=0)
			with unittest.mock.patch('sys.stdout') as mock_stdout:
				make_strategy.build('')

			args, kwargs = mock_run.call_args
			mock_run.assert_called_once()
			assert args[0][0] == 'make'
			assert args[0][1] == '-f'

	def test_build_error(self, make_strategy: BuilderStrategyMake):
		with pytest.raises(click.Abort):
			with unittest.mock.patch('subprocess.run') as mock_run:
				mock_run.side_effect = subprocess.CalledProcessError(1, ['make'])
				with unittest.mock.patch('sys.stdout') as mock_stdout:
					make_strategy.build('')

				mock_run.assert_called_once()
				mock_stdout.write.assert_any_call("Build error: Command '['make']' returned non-zero exit status 1.\n")
