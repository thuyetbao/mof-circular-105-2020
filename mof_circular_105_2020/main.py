#!/bin/python3

# Global
import re
from typing import TypedDict, Literal, Any, Optional


class SubNodeMetadata(TypedDict):
    value: Any
    description: str


class NodeVerificationResult(TypedDict):
    code: str
    status: bool
    metadata: SubNodeMetadata


class DetailVerificationTin(TypedDict):
    length: NodeVerificationResult
    n1n2: NodeVerificationResult
    n3n4n5n6n7n8n9: NodeVerificationResult
    n10: NodeVerificationResult
    dash: NodeVerificationResult
    n11n12n13: NodeVerificationResult



class ResultParseTinFromC105mof(TypedDict):
    is_valid: bool
    tin: Optional[str]
    issued_province_id: Optional[str]
    entity: Optional[Literal["Affiliated", "Independent"]]
    detail: DetailVerificationTin


def parse_tin(obj: str) -> ResultParseTinFromC105mof:
    """Parse Taxpayer Identification Number (TIN) based on Article 5 of Circular 105/2020 from Ministry of Finance

    Structure
    ---------

    TIN syntax: N1N2N3N4N5N6N7N8N9N10 - N11N12N13

    Where:

    - The first two digits N1N2 indicate the province that issued TIN.

    - The next 7 digits N3N4N5N6N7N8N9 that incremental from range of 0000001 to 9999999.

    - N10 is the check digit.

    - Three digits N11N12N13 are formed in ascending order from 001 to 999.

    - A dash (-) is used to separate the first 10-digit element and the last 3-digit element.

    Usage
    -----
    >>> from mof_circular_105_2020 import parse_tin
    >>> parse_tin(obj="0317273020")
    {
        'is_valid': True,
        'tin': '0317273020',
        'entity': 'Independent',
        'issued_province_id': '03',
        'detail': {
            'length': {'code': 'LENGTH', 'status': True, 'metadata': {'value': 10, 'description': 'Length of TIN is (10, 14)'}},
            'n1n2': {'code': 'N1N2', 'status': True, 'metadata': {'value': '03', 'description': 'Province ID that issued TIN'}},
            'n3n4n5n6n7n8n9': {'code': 'N3N4N5N6N7N8N9', 'status': True, 'metadata': {'value': '1727302'}},
            'n10': {'code': 'N10', 'status': True, 'metadata': {'value': '0', 'description': 'Check Digit Number'}},
            'dash': {'code': 'DASH', 'status': False, 'metadata': {'value': None, 'description': 'The dash seperator'}},
            'n11n12n13': {'code': 'N11N12N13', 'status': False, 'metadata': {'value': None, 'description': 'Three digits N11N12N13 are formed in ascending order from 001 to 999'}}
        }
    }
    """

    if not isinstance(obj, str):
        raise ValueError(f"Invalid type of `obj`. Required string or integer. Got type={type(obj)}")

    # Component
    element = obj.strip()

    # Data Component
    n1n2 = None
    n3n4n5n6n7n8n9 = None
    n10 = None
    dash = None
    n11n12n13 = None

    # Pattern
    pattern_tin = re.compile(r"^(?P<n1n2>\d{2})(?P<n3n4n5n6n7n8n9>\d{7})(?P<n10>\d{1})((?P<dash>\-)(?P<n11n12n13>\d{3}))?$")
    pattern_search_result = pattern_tin.match(element)

    if pattern_search_result is not None:
        bucket = pattern_search_result.groupdict()
        n1n2 = bucket.get("n1n2", None)
        n3n4n5n6n7n8n9 = bucket.get("n3n4n5n6n7n8n9", None)
        n10 = bucket.get("n10", None)
        dash = bucket.get("dash", None)
        n11n12n13 = bucket.get("n11n12n13", None)

    # Component
    result = ResultParseTinFromC105mof(is_valid=False, tin=None, issued_province_id=None, entity=None, detail=None)
    node_length = NodeVerificationResult(code="LENGTH", status=False, metadata={"value": len(element), "description": "Length of TIN is (10, 14)"})
    node_n1n2 = NodeVerificationResult(code="N1N2", status=False, metadata={"value": n1n2, "description": "Province ID that issued TIN"})
    node_n3n4n5n6n7n8n9 = NodeVerificationResult(code="N3N4N5N6N7N8N9", status=False, metadata={"value": n3n4n5n6n7n8n9})
    node_n10 = NodeVerificationResult(code="N10", status=False, metadata={"value": n10, "description": "Check Digit Number"})
    node_dash = NodeVerificationResult(code="DASH", status=False, metadata={"value": dash, "description": "The dash seperator"})
    node_n11n12n13 = NodeVerificationResult(
        code="N11N12N13",
        status=False,
        metadata={
            "value": n11n12n13,
            "description": "Three digits N11N12N13 are formed in ascending order from 001 to 999"
        }
    )

    # Valid
    if any([len(element) == 10, len(element) == 14]):
        node_length["status"] = True

    # Valid
    try:
        if n1n2 is not None:
            if n1n2 not in ("00"):
                node_n1n2["status"] = True
    except Exception:
        pass

    # Valid
    try:
        if n3n4n5n6n7n8n9 is not None:
            if 1 <= int(n3n4n5n6n7n8n9) <= 9999999:
                node_n3n4n5n6n7n8n9["status"] = True
    except Exception:
        pass

    # Valid
    try:
        if n10 is not None:
            if 0 <= int(n10) <= 9:
                node_n10["status"] = True
    except Exception:
        pass

    # In case length is 14
    if len(element) == 14:

        # Valid
        try:
            if dash is not None:
                if node_dash["metadata"]["value"] == "-":
                    node_dash["status"] = True
        except Exception:
            pass

        # Valid
        try:
            if n11n12n13 is not None:
                if 1 <= int(n11n12n13) <= 999:
                    node_n11n12n13["status"] = True
        except Exception:
            pass

    # Handle
    node_validate = [node_length, node_n1n2, node_n3n4n5n6n7n8n9, node_n10]
    if len(element) == 14:
        node_validate = [*node_validate, node_dash, node_n11n12n13]

    # Valid
    result["is_valid"] = all([node["status"] is True for node in node_validate if node["metadata"]["value"] is not None])
    result["detail"] = DetailVerificationTin(
        length=node_length,
        n1n2=node_n1n2,
        n3n4n5n6n7n8n9=node_n3n4n5n6n7n8n9,
        n10=node_n10,
        dash=node_dash,
        n11n12n13=node_n11n12n13,
    )

    if result["is_valid"]:

        # Pack TIN
        result["tin"] = element
        result["issued_province_id"] = node_n1n2["metadata"]["value"]

        # Pack Entity
        if len(element) == 10:
            result["entity"] = "Independent"
        elif len(element) == 14:
            result["entity"] = "Affiliated"

    return result
