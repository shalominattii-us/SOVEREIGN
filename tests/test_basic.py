"""
SOVEREIGN Test Suite
Basic tests for the sovereign operating system framework
"""

import pytest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_project_structure():
    """Test that the basic project structure exists"""
    assert os.path.exists('core')
    assert os.path.exists('kernel')
    assert os.path.exists('agentic')
    assert os.path.exists('mesh')
    assert os.path.exists('governance')
    assert os.path.exists('installer')
    assert os.path.exists('README.md')
    assert os.path.exists('SOVEREIGN-MANIFEST.json')


def test_manifest_loading():
    """Test that the manifest can be loaded"""
    import json

    with open('SOVEREIGN-MANIFEST.json', 'r') as f:
        manifest = json.load(f)

    assert 'name' in manifest
    assert manifest['name'] == 'SOVEREIGN'
    assert 'version' in manifest
    assert 'components' in manifest


def test_bootstrap_directories():
    """Test that bootstrap directories were created"""
    assert os.path.exists('build')
    assert os.path.exists('logs')
    assert os.path.exists('temp')


def test_requirements_available():
    """Test that key dependencies are available"""
    try:
        import pytest
        import yaml
        import requests
        assert True
    except ImportError:
        assert False, "Required dependencies not available"


if __name__ == '__main__':
    pytest.main([__file__])