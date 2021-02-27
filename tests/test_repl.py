"""Test illud.repl."""
from typing import Any, List, Optional
from unittest.mock import call, patch

import pytest

from illud.exceptions.break_exception import BreakException
from illud.repl import REPL


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('input_or_exception, result_or_exception, output_or_exception, '
                         'expected_input_call_count, expected_evaluate_call_count, '
                         'expected_print_call_count, expected_inputs, expected_results', [
    ([BreakException()], [], [], 1, 0, 0, [], []),
    (['foo'], [BreakException], [], 1, 1, 0, ['foo'], []),
    (['foo'], ['bar'], [BreakException], 1, 1, 1, ['foo'], ['bar']),
    (['foo', BreakException], ['bar'], [None], 2, 1, 1, ['foo'], ['bar']),
    (['foo', 'bar'], ['baz', BreakException], [None], 2, 2, 1, ['foo', 'bar'], ['baz']),
    (['foo', 'bar'], ['baz', 'spam'], [None, BreakException], 2, 2, 2, ['foo', 'bar'], ['baz', 'spam']),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_call(input_or_exception: List[Any], result_or_exception: List[Any],
              output_or_exception: List[Optional[BreakException]], expected_input_call_count: int,
              expected_evaluate_call_count: int, expected_print_call_count: int,
              expected_inputs: List[Any], expected_results: List[Any]) -> None:
    """Test illud.repl.REPL.run."""
    repl: REPL = REPL()

    with patch('illud.repl.REPL.read', side_effect=input_or_exception) as read_mock, \
        patch('illud.repl.REPL.evaluate', side_effect=result_or_exception) as evaluate_mock, \
        patch('illud.repl.REPL.print', side_effect=output_or_exception) as print_mock:

        repl()

        assert read_mock.call_count == expected_input_call_count

        assert evaluate_mock.call_count == expected_evaluate_call_count
        evaluate_mock.assert_has_calls(map(call, expected_inputs))

        assert print_mock.call_count == expected_print_call_count
        print_mock.assert_has_calls(map(call, expected_results))


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
