from twisted.internet import defer, reactor
from txboxdotnet.api_v2 import txBoxAPI

api = txBoxAPI(
    client_id='mz3m6rw1ur45nj1n2156mvs8jylu7pat',
    client_secret='nd4jwkfNkYzAr5zIXM1f4SmMlus2Qwm5',auth_redirect_uri="https://app.box.com/files/0/f/1720362018/bedahbuku")

print "api.auth_code =", api.auth_code

if not api.auth_code:
    print '\n'.join([
        'Visit the following URL in any web browser (firefox, chrome, safari, etc),',
            '  authorize there, confirm access permissions, and paste URL of an empty page',
            '  (starting with "https://success.box.com/") you will get',
            '  redirected to into "auth_code" value in "config" dict above.\n',
        'URL to visit:\n  {}'.format(api.auth_user_get_url()) ])
    exit()

if re.search(r'^https?://', api.auth_code):
    api.auth_user_process_url(api.auth_code)

@defer.inlineCallbacks
def do_stuff():

    # Print root directory listing
    print list(e['name'] for e in (yield api.listdir()))

    # Upload "test.txt" file from local current directory
    #file_info = yield api.put('test.txt')

    # Find just-uploaded "test.txt" file by name
    #file_id = yield api.resolve_path('test.txt')

    # Check that id matches uploaded file
    #assert file_info['id'] == file_id

    # Remove the file
    #yield api.delete(file_id)

do_stuff().addBoth(lambda ignored: reactor.stop())
reactor.run()