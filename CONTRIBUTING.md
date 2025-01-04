# Contributing to Hamasisho

## Development Process
1. Fork the repository
2. Create feature branch from `development`
3. Make changes
4. Write/update tests
5. Submit PR to `development`

## Branch Strategy
- `main`: Production releases
- `development`: Active development
- `feature/*`: New features
- `fix/*`: Bug fixes

## Setup Development Environment
```batch
git clone https://github.com/<your-username>/hamasisho.git
cd hamasisho
git checkout development
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask db init
flask db upgrade
flask db seed
```

## Code Standards
- Follow PEP 8
- Add docstrings to functions
- Keep functions focused
- Use type hints
- Maximum line length: 88 characters
- Testing
- Write tests for new features
- Run existing tests before PR
- Maintain >80% coverage

## Testing
- Write tests for new features
- Run existing tests before PR
- Maintain >80% coverage

```batch
pytest -v --cov=app
```

## PR Guidelines
1. Reference issue number
2. Include test coverage
3. Update documentation
4. Add to CHANGELOG.md
5. Commit Messages
6. Use present tense
7. Be descriptive
8. Reference issues

## Commit Messages
-Use present tense
- Be descriptive
- Reference issues

Example: `Add user authentication #1`

## Documentation
- Update README.md for features
- Add inline comments
- Document API endpoints
- Add docstrings to functions
- Write comments for complex code

## Questions?
Open an issue or contact maintainers.