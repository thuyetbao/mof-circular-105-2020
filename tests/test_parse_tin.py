#!/bin/python3

# External
import pytest

# Internal
from mof_circular_105_2020 import parse_tin


@pytest.mark.parametrize("element", [
    ("0317273020"),
    ("4601634689"),
    ("0100109106"),
    ("0107349019"),
    ("0318914414"),
    ("0318913386"),
    ("5702182984"),
    ("2401019019"),
    ("1301145113"),
    ("1301145177"),
])
def test_valid_tin_in_independent(element: str):
    """Case: Valid TIN with entity of Independent"""

    result = parse_tin(obj=element)
    assert result["is_valid"] is True
    assert result["tin"] is not None and result["tin"] == element.strip()
    assert result["issued_province_id"] is not None
    assert result["entity"] is not None
    assert result["detail"] is not None
    assert all([
        node["status"] is True
        for key, node in result["detail"].items()
        if key in ("length", "n1n2", "n3n4n5n6n7n8n9", "n10")
    ]), result["detail"]


@pytest.mark.parametrize("element", [
    ("2803158679-003"),
    ("8334256196-001"),
    ("0317080597-004"),
    ("0317080597-004"),
    ("0301420946-003"),
    ("0316314958-005"),
    ("0318320160-001"),
    ("0317381178-002"),
    ("0316126418-001"),
    ("0318467484-001"),
])
def test_valid_tin_in_affiliated(element: str):
    """Case: Valid TIN with entity of Affiliated"""

    result = parse_tin(obj=element)
    assert result["is_valid"] is True
    assert result["tin"] is not None and result["tin"] == element.strip()
    assert result["issued_province_id"] is not None
    assert result["entity"] is not None
    assert result["detail"] is not None
    assert all([
        node["status"] is True
        for key, node in result["detail"].items()
        if key in ("length", "n1n2", "n3n4n5n6n7n8n9", "n10", "dash", "n11n12n13")
    ]), result["detail"]


@pytest.mark.parametrize("element", [
    ("0317273"),
    ("4601634689123"),
    ("01001091111111106233"),
    ("0107342229022233"),
    ("034"),
    ("01")
])
def test_failure_on_length(element: str):
    """Test cases where the length of the TIN is not correct"""

    result = parse_tin(obj=element)
    assert result["is_valid"] is False
    assert result["tin"] is None
    assert result["issued_province_id"] is None
    assert result["entity"] is None
    assert result["detail"] is not None
    assert result["detail"]["length"]["status"] is False
    assert result["detail"]["length"]["metadata"]["value"] == len(element)
