# TNApi
Temp-mail.org free API, written in Python

## Installation
1. Install from sources:
```bash
git clone https://github.com/katant/TPApi.git
cd TPApi
python3 setup.py install
```

## Usage
Example code to get domains:
```python
from TPApi import TPApi

api = TPApi()
print(api.domains())
```

