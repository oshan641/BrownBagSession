# Python Coding Standards & Best Practices
## OneOrigin Team Brown Bag Session

### 1. Code Formatting with Ruff
- **Why Ruff?**
  - Fast (written in Rust)
  - Compatible with existing tools (Black, isort, Pylint)
  - Extensive rule set
  - Auto-fixes many issues



#### Setting up Ruff
```python
# install ruff
python3 -m pip install ruff
```

```python
# pyproject.toml
# exclude ignored directories
exclude = []
[tool.ruff]
line-length = 88
indent-width = 4
# assuming python 3.9
target-version = "py39" 

[tool.ruff.format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false
```

### 2. PEP 8 Naming Conventions

PEP(Python Enhancement Proposals) - 
Design Document which describes new features or proposals for Python Language

![](/image.png)

#### Naming Conventions
- *Camel Case* - eg: firstName, lastName
- *Snake Case* - eg: user_name, employee_id
- *Kebab Case* - eg: first-name, last-name 
- *Pascal Case* - eg: UserProfile, EmployeeProfile


#### Variables & Functions
- Use lowercase with underscores: `user_name`, `calculate_total`
- Descriptive names: `process_user_input()` vs `process()`
- Avoid single-letter names except for counters/iterators

#### Classes
- Use CapWords convention: `UserProfile`, `TranscriptProcessor`
- Suffix exception classes with "Error": `ValidationError`

#### Constants
- All uppercase with underscores: `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`, `DELAY_TIME`

### Database Name
 students, users


### 3. Type Hints 
#### Variables
```python
name: str = "John"
age: int = 30
is_active: bool = True
prices: list[float] = [19.99, 29.99, 39.99]
user_scores: dict[str, int] = {"John": 85, "Jane": 92}
```

#### Functions
```python
def calculate_discount(price: float, percentage: float) -> float:
    return price * (1 - percentage / 100)

def get_user_by_id(user_id: int) -> Optional[User]:
    """Return user if found, None otherwise"""
    return User.query.get(user_id)
```

### 4. REST API Best Practices

![](https://lh7-us.googleusercontent.com/eS8tb2HUmn15yRXq2rDt82novETDuwTylHydJZ8LIBnl4him6INKjiRhIajisQxnQs5l0IgVV6YjGP2C1O3w7_2Kfmckot8IZI8_LjtvM4Slm0V05g3T49VSikHuss4pFDoW0q3oTWIkD-SbsFKb2fQ)


#### URL Structure
```python
# Good
GET /api/v1/students
GET /api/v1/students/{id}
GET /api/v1/class/{class_id}/students/{id}

GET /api/v1/class?class_id={cid}&student_id={sid}
POST /api/v1/students
PATCH /api/v1/students/{id}
DELETE /api/v1/students/{id}

# Bad
GET /api/v1/getStudents
POST /api/v1/createStudent
```


#### Response Format
```python
# Success Response
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "John Doe"
    }
}

# Error Response
{
    "status": "error",
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid email format",
        "details": ["Email must contain @ symbol"]
    }
}
```

#### Versioning 
```python
# versioning is breaking changes in api response format
GET /api/v1/students
GET /api/v2/students
```

#### Util Endpoints 
```python
# Health Endpoint 
GET /api/v1/health
```

### 5. Context Managers
```python
f = open('filename')
# reading lines
f.close()
# Use context managers for resource handling
from contextlib import contextmanager

with open('file.txt') as f:
    content = f.read()

# Custom context manager
@contextmanager
def db_transaction():
    try:
        yield
        db.commit()
    except Exception:
        db.rollback()
        raise

with db_transaction() as db_manager:
    pass
```
### 6. Modules & Packages


```python
- package-example/
    | - calculator/ ----> Python package
    |   | - __init__.py ----> this file makes calculator folder as a python package
    |   | - operation.py ----> module
    |   | - operation2.py ----> module
    | - main.py 
    | - folder/ ----> normal folder
    | - | - utils.py
    | - | - main.py

```

- Module is a file containing python function and statements

- Packages is a collection of modules

- `__init__.py` files initializes package once it's imported. If this file is not present, then you cannot import any module inside the folder


### 6. Implementation Plan
 **Setup Phase**
   - Install Ruff in CI/CD pipeline
   - Configure pre-commit hooks
   - Set up VS Code formatting


### 7. Code Review Checklist
- [ ] Ruff formatting passed
- [ ] PEP 8 naming conventions followed
- [ ] Appropriate error handling implemented
- [ ] API endpoints follow REST conventions
- [ ] Tests included for new code
- [ ] Documentation updated
- [ ] No hardcoded values
- [ ] Logging implemented where appropriate


### Resources & Video References
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Ruff Documentation](https://beta.ruff.rs/docs/)
- [REST API Best Practices](https://restfulapi.net/)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)

- [Clean Code Playlist by Uncle Bob](https://youtube.com/playlist?list=PLmmYSbUCWJ4x1GO839azG_BBw8rkh-zOj&feature=shared)
- [Raymond Hettinger Talks Playlist](https://youtube.com/playlist?list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA&feature=shared)
