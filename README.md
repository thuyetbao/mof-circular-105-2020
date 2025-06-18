<div align="center">
  <a href="https://github.com/thuyetbao/mof-circular-105-2020.git">
    <!-- <img src="docs/assets/images/banner/background-banner.png" alt="Package Banner" height="300" width="100%"> -->
  </a>
</div>

<div align="center">
  <h3>MOF - Circular 105/2020</h3>
</div>

<div align="center">
  <a href="https://github.com/thuyetbao/mof-circular-105-2020.git" target="_blank">
    <img src="https://img.shields.io/badge/package-mof--circular--105--2020--version_0.4.10-darkgreen?logo=c" alt="Package Version">
  </a>
</div>

<div align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/python-3.12.8-teal?logo=python" alt="Python 3.12">
  </a>
  <a href="https://pre-commit.com/" target="_blank">
    <img src="https://img.shields.io/badge/pre--commit-enabled-teal?logo=pre-commit" alt="pre-commit enabled">
  </a>
  <br>
  <a href="https://github.com/features/actions" target="_blank">
    <img src="https://img.shields.io/badge/cicd-github--action-teal?logo=github-actions" alt="Github Action">
  </a>
</div>

---

**mof-circular-105-2020** is the implement of [Circular 105/2020/TT-BTC [Hanoi, December 03, 2020]](https://thuvienphapluat.vn/van-ban/Thuong-mai/Circular-105-2020-TT-BTC-guiding-the-implementation-of-Decision-27-2020-QD-TTg-433301.aspx#tab2)

**Feature**:

- Reusable models related concepts of financial product in financial markets

- Native support of Python

## **Usage**

Install package by following component

```bash
pip install mof_circular_105_2020
```

The core function is to `parse_tin` that parse TIN

```python
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
```

**Documentation**:

Documentation of the package is deployed at `docs` folder

**Code Storage**:

Repository: [GitHub > Repository `mof-circular-105-2020`](https://github.com/thuyetbao/mof-circular-105-2020)

**Releases**:

Releases: [GitHub > Repository > `mof-circular-105-2020` > Releases](https://github.com/thuyetbao/mof-circular-105-2020/releases)

<!-- Bundle URL -->

<!--

| [![PEP8][badges-pep8]](https://peps.python.org/pep-0008/)                                |
| [![httpx][badges-httpx]](https://www.python-httpx.org/)                                  |
[badges-pep8]: https://img.shields.io/badge/pep8-compliance-brightgreen -->
