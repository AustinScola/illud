"""Test illud.repl."""
from typing import Any, List, Optional
from unittest.mock import call, patch

import pytest

from illud.exceptions.break_exception import BreakException
from illud.repl import REPL


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('input_or_exception, result_or_exception, output_or_exception, '
                         'expected_input_call_count, expected_evaluate_call_count, '
                         'expected_print_call_count, expected_inputs, expected_results, expect_catch_called', [
    ([BreakException()], [], [], 1, 0, 0, [], [], False),
    ([Exception], [], [], 1, 0, 0, [], [], True),
    (['foo'], [BreakException], [], 1, 1, 0, ['foo'], [], False),
    (['foo'], [Exception], [], 1, 1, 0, ['foo'], [], True),
    (['foo'], ['bar'], [BreakException], 1, 1, 1, ['foo'], ['bar'], False),
    (['foo'], ['bar'], [Exception], 1, 1, 1, ['foo'], ['bar'], True),
    (['foo', BreakException], ['bar'], [None], 2, 1, 1, ['foo'], ['bar'], False),
    (['foo', Exception], ['bar'], [None], 2, 1, 1, ['foo'], ['bar'], True),
    (['foo', 'bar'], ['baz', BreakException], [None], 2, 2, 1, ['foo', 'bar'], ['baz'], False),
    (['foo', 'bar'], ['baz', Exception], [None], 2, 2, 1, ['foo', 'bar'], ['baz'], True),
    (['foo', 'bar'], ['baz', 'spam'], [None, BreakException], 2, 2, 2, ['foo', 'bar'], ['baz', 'spam'], False),
    (['foo', 'bar'], ['baz', 'spam'], [None, Exception], 2, 2, 2, ['foo', 'bar'], ['baz', 'spam'], True),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_call(input_or_exception: List[Any], result_or_exception: List[Any],
              output_or_exception: List[Optional[BreakException]], expected_input_call_count: int,
              expected_evaluate_call_count: int, expected_print_call_count: int,
              expected_inputs: List[Any], expected_results: List[Any],
              expect_catch_called: bool) -> None:
    """Test illud.repl.REPL.run."""
    repl: REPL = REPL()

    with patch('illud.repl.REPL.startup') as startup_mock, \
        patch('illud.repl.REPL.read', side_effect=input_or_exception) as read_mock, \
        patch('illud.repl.REPL.evaluate', side_effect=result_or_exception) as evaluate_mock, \
        patch('illud.repl.REPL.print', side_effect=output_or_exception) as print_mock, \
        patch('illud.repl.REPL.catch') as catch_mock:

        repl()

        startup_mock.assert_called_once()

        assert read_mock.call_count == expected_input_call_count

        assert evaluate_mock.call_count == expected_evaluate_call_count
        evaluate_mock.assert_has_calls(map(call, expected_inputs))

        assert print_mock.call_count == expected_print_call_count
        print_mock.assert_has_calls(map(call, expected_results))

        if expect_catch_called:
            catch_mock.assert_called_once()
        else:
            catch_mock.assert_not_called()


def test_startup() -> None:
    """Test illud.repl.REPL.startup."""
    repl: REPL = REPL()

    repl.startup()


def test_read() -> None:
    """Test illud.repl.REPL.read."""
    repl: REPL = REPL()

    repl.read()


# yapf: disable
@pytest.mark.parametrize('input_', [
    ('foo'),
    (1),
])
# yapf: enable
def test_evaluate(input_: Any) -> None:
    """Test illud.repl.REPL.evaluate."""
    repl: REPL = REPL()

    repl.evaluate(input_)


# yapf: disable
@pytest.mark.parametrize('result', [
    ('foo'),
    (1),
])
# yapf: enable
def test_print(result: Any) -> None:
    """Test illud.repl.REPL.print."""
    repl: REPL = REPL()

    repl.print(result)


# yapf: disable
@pytest.mark.parametrize('exception', [
    (Exception()),
    (TypeError()),
])
# yapf: enable
def test_catch(exception: Exception) -> None:
    """Test illud.repl.REPL.catch."""
    repl: REPL = REPL()

    with pytest.raises(type(exception)):
        repl.catch(exception)
