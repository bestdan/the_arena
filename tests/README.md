# Tests

Automated tests for The Arena documentation site.

## Running Tests

### Search Functionality Test

Tests that the MkDocs search feature works correctly.

```bash
# Install test dependencies
pip install -r requirements-test.txt
playwright install chromium

# Run the test
python tests/test_search.py
```

This test verifies:
- Search results appear via URL parameters
- Typing in the search box returns results
- Search results are clickable
- Search index file is valid and contains documents

## CI/CD Integration

Search tests are automatically run on every pull request via the `test-docs-build.yml` workflow.
