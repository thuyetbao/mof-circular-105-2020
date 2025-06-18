<div align="center">
  <a href="https://github.com/thuyetbao/mof-circular-105-2020.git">
    <img src="docs/assets/images/banner/colorful-package-banner.png" alt="Package Banner" height="200" width="100%">
  </a>
</div>

<div align="center">
  <h3>MOF - Circular 105/2020</h3>
</div>

<div align="center">
  <a href="https://github.com/thuyetbao/mof-circular-105-2020.git" target="_blank">
    <img src="https://img.shields.io/pypi/v/mof_circular_105_2020.svg?logo=pypi" alt="Package Version">
  </a>
</div>

<div align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/mof_circular_105_2020.svg?logo=python" alt="Supported Python Version">
  </a>
  <br>
  <a href="https://pre-commit.com/" target="_blank">
    <img src="https://img.shields.io/badge/pre--commit-enabled-teal?logo=pre-commit" alt="pre-commit enabled">
  </a>
  <a href="https://pre-commit.com/" target="_blank">
    <img src="https://img.shields.io/badge/pep8-enabled-teal?logo=python" alt="pep8 enabled">
  </a>
  <a href="https://github.com/features/actions" target="_blank">
    <img src="https://img.shields.io/badge/cicd-github--action-teal?logo=github-actions" alt="Github Action">
  </a>
</div>

---

## **Features**

- Provides function implementations based on [Circular 105/2020/TT-BTC [Hanoi, December 03, 2020]](https://thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Thong-tu-105-2020-TT-BTC-huong-dan-dang-ky-thue-459433.aspx)

- Native Python support

## **Usage**

Install package from PyPI

```bash
pip install mof_circular_105_2020
```

Use `parse_tin` to parse Taxpayer Identification Number (TIN) based on the circular reference.

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

**Documentation**: //

<!-- Documentation of the package is deployed at `docs` folder -->

**Code Storage**:

Repository: [GitHub > Repository:`mof-circular-105-2020`](https://github.com/thuyetbao/mof-circular-105-2020)

**Releases**:

Releases: [GitHub > Repository:`mof-circular-105-2020` > Releases](https://github.com/thuyetbao/mof-circular-105-2020/releases)

**PyPI**:

Distribution: [PyPI > Project > `mof-circular-105-2020`](https://pypi.org/project/mof-circular-105-2020/)
