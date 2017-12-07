#!/usr/bin/env python

"""\
Demo: Simple USSD example

Simple demo app that initiates a USSD session, reads the string response and closes the session
(if it wasn't closed by the network)

Note: for this to work, a valid USSD string for your network must be used.
"""

from __future__ import print_function

import logging
import sys
import traceback
import time
#PORT = '/dev/ttyUSB2'
if len(sys.argv) > 2:
    PORT = sys.argv[1]
    USSD_STRING = sys.argv[2]
BAUDRATE = 115200
#USSD_STRING = '*101#'
PIN = None # SIM card PIN (if any)
DEBUG=False
from gsmmodem.modem import GsmModem

def handleSms(sms):
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))
    print("-" * 100)
    #print('Replying to SMS...')
    #sms.reply(u'SMS received: "{0}{1}"'.format(sms.text[:20], '...' if len(sms.text) > 20 else ''))
    #print('SMS sent.\n')

def main(com=None, number=None):
    if com:
        PORT=com
    if number:
        USSD_STRING=number
    if DEBUG:
        print('Initializing modem...')
    #logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    #modem = GsmModem(PORT, BAUDRATE)
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handleSms)
    #a = modem.listStoredSms()
    #print modem.listStoredSMS()
    modem.connect(PIN)
    modem.waitForNetworkCoverage(10)    
    print('Sending USSD string: {0}'.format(USSD_STRING))
    response = modem.sendUssd(USSD_STRING) # response type: gsmmodem.modem.Ussd
    print('USSD reply received: {0}'.format(response.message))
    while 1:
        #try:
        if response.sessionActive:
            q = raw_input('replay: ')
            if str(q).lower() == 'q':
                #if response.sessionActive:
                    #response.cancel()
                sys.exit(0)
            q1 = response.reply(q)
            if str(q1).lower() == 'q':
                #if response.sessionActive:
                    #response.cancel()
                sys.exit(0)            
            print('USSD reply received: {0}'.format(q1.message))
            #if DEBUG:
                #print('Closing USSD session.')
            ## At this point, you could also reply to the USSD message by using response.reply()
            #response.cancel()
        else:
            print('USSD session was ended by network.')
            break
    time.sleep(5)
    #except KeyboardInterrupt:
            #sys.exit(0)
        #except:
            #if DEBUG:
                #traceback.format_exc()
            #else:
                #pass
    modem.close()
    
def usage():
    import argparse
    parse = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, version='1.0')
    parse.add_argument('COM', help='COM Port or DEV tty Path (*nux|*nix), example: COM13 or /dev/ttyUSB2', action='store')
    parse.add_argument('NUMBER', help='Number of USSD', action='store')
    parse.add_argument('-V', '--debug', help='Debug mode', action='store_true')
    if len(sys.argv) == 1:
        parse.print_help()
    else:
        args = parse.parse_args()
        if args.debug:
            DEBUG = True
        main(args.COM, args.NUMBER)

if __name__ == '__main__':
    #~ main()
    try:
        usage()
    except:
        if DEBUG:
            traceback.format_exc()
        else:
            pass
