Problem:
1. Create python layer:
pip install <libs> -t python
Note: libs must be compatible with linux os
pip install --platform manylinux2014_x86_64 --target=. --implementation cp --python-version 3.11 --only-binary=:all: --upgrade fastapi pydantic

2.