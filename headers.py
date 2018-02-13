def setHeaders(
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.', 
    accept_encoding = 'gzip, deflate',
    accept_language = 'en-US,en;q=0.5',
    connection = 'keep-alive',
    cookies = '',
    host = '',
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:52.9) Gecko/20100101 Goanna/3.3 Firefox/52.9 PaleMoon/27.5.1', 
    referrer = ''
):
    headers = {}
    if accept:
        headers.update({'Accept': accept,})
    if accept_encoding:
        headers.update({'Accept-Encoding': accept_encoding,})
    if accept_language:
        headers.update({'Accept-Language': accept_language,})
    if connection:
        headers.update({'Connection': connection,})
    if cookies:
        headers.update({'Cookie': cookies,})
    if host:
        headers.update({'Host': host,})
    if user_agent:
        headers.update({'User-Agent': user_agent,})
    return headers
    