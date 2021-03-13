"""Test illud.__main__."""
from typing import List, Optional
from unittest.mock import MagicMock, patch

import pytest

from illud import __main__


# yapf: disable
@pytest.mark.parametrize('name, arguments, expect_main_called, expected_main_arguments', [
    ('', None, False, None),
    ('__main__', ['__main__.py'], True, []),
    ('__main__', ['__main__.py', 'foo.txt'], True, ['foo.txt']),
])
# yapf: enable
def test_package_main(name: str, arguments: Optional[List[str]], expect_main_called: bool,
                      expected_main_arguments: Optional[List[str]]) -> None:
    """Test illud.__main__.package_main."""
    main_exit_code = MagicMock()

    with patch.object(__main__, '__name__', name), \
        patch('sys.exit') as exit_mock, \
        patch('illud.__main__.main', return_value=main_exit_code) as main_mock, \
        patch('sys.argv', arguments):

        __main__.package_main()

        if expect_main_called:
            main_mock.assert_called_once_with(expected_main_arguments)
            exit_mock.assert_called_once_with(main_exit_code)
