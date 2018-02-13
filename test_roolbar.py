import rollbar

rollbar.init('e878e48a6fdd42208d94727c31fa27e6')
#  rollbar.init('9fbdbd271df24d87b9aa7cda818c4e7c')

try:
    b = a + 1
except:
    rollbar.report_exc_info()