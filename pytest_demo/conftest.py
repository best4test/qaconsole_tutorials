import requests
from requests_toolbelt import MultipartEncoder

def pytest_terminal_summary(terminalreporter):
    if terminalreporter.config.getoption("--junitxml") is not None:
        xml_file = terminalreporter.config.getoption("--junitxml")

        m = MultipartEncoder(
        fields={'projectName': 'Pytest',
                'environment': 'Local',
                'apiKey': '6d1e2f42-a5a4-4331-a367-c8f0e41fef92',
                'result': ('result.xml', open(xml_file, 'rb'))}
        )

        requests.post('https://tutorials.qaconsole.io/testrunsJunitMultipart', data=m,
                    headers={'Content-Type': m.content_type})