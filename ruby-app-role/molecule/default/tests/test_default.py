import os
import pytest
import testinfra

@pytest.mark.parametrize("name", [
    "puma"
])
def test_services_running_and_enabled(host, name):
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled

def test_application_files(host):
    app_files = [
        "/app/public",
        "/app/public/config.ru"
    ]
    for file_path in app_files:
        file = host.file(file_path)
        assert file.exists
        assert file.is_file or file.is_directory
