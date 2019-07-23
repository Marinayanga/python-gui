import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture=Application("C:\\Users\\kokorevama\\Desktop\\Папка в папке\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
