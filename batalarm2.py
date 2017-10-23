import wmi
import winsound
import sys, traceback
import time

def check():
    c = wmi.WMI()
    t = wmi.WMI(moniker = "//./root/wmi")

    batts1 = c.CIM_Battery(Caption = 'Portable Battery')
    for i, b in enumerate(batts1):
        print 'Battery %d Design Capacity: %d mWh' % (i, b.DesignCapacity or 0)


    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        print ('Battery %d Fully Charged Capacity: %d mWh' % 
              (i, b.FullChargedCapacity))

    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    onLine = True
    for i, b in enumerate(batts):
        # print '\nBattery %d ***************' % i
        # print 'Tag:               ' , str(b.Tag)
        # print 'Name:              ' , b.InstanceName

        print 'PowerOnline:       ' , str(b.PowerOnline)
        onLine = b.PowerOnline
        # print 'Discharging:       ' + str(b.Discharging)
        # print 'Charging:          ' + str(b.Charging)
        # print 'Voltage:           ' + str(b.Voltage)
        # print 'DischargeRate:     ' + str(b.DischargeRate)
        # print 'ChargeRate:        ' + str(b.ChargeRate)
        # print 'RemainingCapacity: ' + str(b.RemainingCapacity)
        # print 'Active:            ' + str(b.Active)
        # print 'Critical:          ' + str(b.Critical)
    return onLine

while 1:
    try:
        onLine = check()
        print "onLine 1 =", onLine
        if not str(onLine) is "True":
            winsound.PlaySound(r'f:\SOUNDS\WAV\06. Alarm 6.wav', winsound.SND_FILENAME)
        else:
            print "onLine 2 =", onLine
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print traceback.format_exc()