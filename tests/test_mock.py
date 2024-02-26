def test_mocker_fixture(mocker):
    mock = mocker.MagicMock(return_value=True)
    assert mock() == True
