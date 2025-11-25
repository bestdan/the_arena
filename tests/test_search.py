#!/usr/bin/env python3
"""
Test search functionality on the MkDocs site to prevent regressions.
This test verifies that:
1. The search worker initializes properly
2. Search results are returned when typing in the search box
3. Search results can be navigated via URL parameters
"""

import subprocess
import time
import requests
from playwright.sync_api import sync_playwright


def wait_for_server(url, timeout=30):
    """Wait for the MkDocs server to be ready."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass
        time.sleep(0.5)
    return False


def test_search_functionality():
    """Test that search works correctly on the MkDocs site."""
    # Start MkDocs server
    server_process = subprocess.Popen(
        ['mkdocs', 'serve', '--dev-addr=127.0.0.1:8765'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    try:
        # Wait for server to be ready
        base_url = 'http://127.0.0.1:8765'
        assert wait_for_server(base_url), "MkDocs server failed to start"
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Test 1: Search via URL parameter works
            print("Test 1: Testing search via URL parameter...")
            page.goto(f'{base_url}/?q=panache')
            page.wait_for_timeout(3000)  # Wait for search to initialize
            
            # Check that search results appear
            search_result_text = page.locator('[data-md-component="search-result"]').text_content()
            assert 'matching documents' in search_result_text.lower(), \
                f"Expected search results, got: {search_result_text}"
            print("✓ Search via URL parameter works")
            
            # Test 2: Search by typing in search box
            print("Test 2: Testing search by typing in search box...")
            page.goto(base_url)
            page.wait_for_timeout(1000)  # Wait for page load
            
            # Click search box and wait for initialization
            search_box = page.get_by_role('textbox', name='Search')
            search_box.click()
            
            # Wait for search to finish initializing
            page.wait_for_selector('text=Type to start searching', timeout=10000)
            print("  ✓ Search worker initialized")
            
            # Type search query slowly (character by character)
            search_box.press_sequentially('crowd', delay=100)
            page.wait_for_timeout(1000)  # Wait for results
            
            # Check that results appear
            search_result = page.locator('[data-md-component="search-result"]')
            result_text = search_result.text_content()
            assert 'matching documents' in result_text.lower(), \
                f"Expected search results after typing, got: {result_text}"
            print("✓ Search by typing works")
            
            # Test 3: Verify search results are displayed and clickable
            print("Test 3: Verifying search results are clickable...")
            page.goto(f'{base_url}/?q=snak')
            page.wait_for_timeout(3000)  # Wait for search results
            
            # Find first search result link
            first_result = page.locator('[data-md-component="search-result"] a').first
            assert first_result.is_visible(), "First search result should be visible"
            
            # Click the first result
            first_result.click()
            page.wait_for_timeout(1000)
            
            # Check that we navigated
            current_url = page.url
            assert current_url != f'{base_url}/?q=snak', \
                f"Expected navigation after clicking result, but URL is still: {current_url}"
            print("✓ Search results are clickable and navigation works")
            
            # Test 4: Verify search index file exists and is valid
            print("Test 4: Verifying search index file...")
            response = requests.get(f'{base_url}/search/search_index.json')
            assert response.status_code == 200, "Search index file not found"
            search_data = response.json()
            assert 'docs' in search_data, "Search index missing 'docs' field"
            assert len(search_data['docs']) > 0, "Search index has no documents"
            print(f"✓ Search index valid with {len(search_data['docs'])} documents")
            
            browser.close()
            
        print("\n✅ All search functionality tests passed!")
        return True
        
    finally:
        # Clean up server process
        server_process.terminate()
        server_process.wait(timeout=5)


if __name__ == '__main__':
    try:
        test_search_functionality()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        exit(1)
