"""Functional test"""

import datetime

from api_logic.sessions import (
    get_all_sessions,
    get_session_templates,
    get_session_attributes_data,
    add_session,
    calc_cost_api_logic,
    calc_cost_equally,
    get_billing_types,
)


def test_get_all_sessions(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.get_all_sessions.return_value = ["session1", "session2"]

    result = get_all_sessions()
    assert result == {"data": ["session1", "session2"]}


def test_get_session_templates(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.get_session_templates.return_value = [
        "template1",
        "template2",
    ]

    result = get_session_templates()
    assert result == {"data": ["template1", "template2"]}


def test_get_session_attributes_data(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.get_billing_types.return_value = ["Weighted", "Equally"]
    mock_service.return_value.get_session_templates.return_value = ["templateA"]

    result = get_session_attributes_data()
    assert result == {
        "data": {
            "billingTypes": ["Weighted", "Equally"],
            "sessionTemplates": ["templateA"],
        }
    }


def test_add_session(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.add_session.return_value = 123

    result = add_session(
        sessionName="Test Session",
        duration=60,
        sessionDate="2025-10-16",
        shiftTime="morning",
        location="HCMC",
    )
    assert result == {"data": {"sessionId": 123}}


def test_calc_cost_api_logic(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.calc_cost_amount.return_value = 250.0

    result = calc_cost_api_logic(
        participants=[{"name": "Alice", "weight": 1.0}],
        totalCost=250.0,
        rentalCost=100.0,
        shuttleAmount=2,
        shuttlePrice=25.0,
        players=["Alice"],
    )
    assert result["data"]["cost"] == 250.0
    assert result["data"]["sessionDate"] == datetime.date.today().strftime("%Y-%m-%d")


def test_calc_cost_equally(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.calc_cost_amount.return_value = 100.0

    result = calc_cost_equally(
        participants=[{"name": "Bob"}, {"name": "Carol"}],
        totalCost=200.0,
        rentalCost=50.0,
        shuttleAmount=2,
        shuttlePrice=25.0,
        numberOfPlayers=2,
    )
    assert result["data"]["cost"] == 100.0
    assert result["data"]["sessionDate"] == datetime.date.today().strftime("%Y-%m-%d")


def test_get_billing_types(mocker):
    mock_service = mocker.patch("api_logic.sessions.PracticeSessionService")
    mock_service.return_value.get_billing_types.return_value = ["Weighted", "Equally"]

    result = get_billing_types()
    assert result == {"data": ["Weighted", "Equally"]}
