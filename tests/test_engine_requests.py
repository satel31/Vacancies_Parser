import pytest
from src.engine_requests import HHRequest, SJRequest


# tests of HHRequest class
@pytest.fixture
def hh():
    return HHRequest('python')


def test_hhrequest_init(hh):
    """Test of initialization of the class HHRequest without new per_page"""
    assert hh.key_word == 'python'
    assert hh.per_page == 100


def test_hhrequest_init_two_var():
    """Test of initialization of the class HHRequest with new per_page"""
    hh = HHRequest('python', 10)
    assert hh.key_word == 'python'
    assert hh.per_page == 10


def test_hhrequest_request_data_good(hh):
    """Test of request_data method with responce status 200"""
    data = hh.request_data()
    assert len(data) != 0


def test_hhrequest_request_data_bad(hh):
    """Test of request_data method with other responce status"""
    data = hh.request_data(-1)
    assert data is None

# tests of SJRequest class
@pytest.fixture
def sj():
    return SJRequest('python')


def test_sjrequest_init(sj):
    """Test of initialization of the class SJRequest without new per_page"""
    assert sj.key_word == 'python'
    assert sj.per_page == 100


def test_sjrequest_init_two_var():
    """Test of initialization of the class SJRequest with new per_page"""
    sj = SJRequest('python', 10)
    assert sj.key_word == 'python'
    assert sj.per_page == 10


def test_sjrequest_request_data_good(sj):
    """Test of request_data method with responce status 200"""
    data = sj.request_data()
    assert len(data) != 0
