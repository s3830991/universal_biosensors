import pspython.pspyinstruments as pspyinstruments
import pspython.pspymethods as pspymethods


def new_eis_data_callback(new_data):
    for type, value in new_data.items():
        print(type + ' = ' + str(value))
    return


manager = pspyinstruments.InstrumentManager(new_data_callback=new_eis_data_callback)
available_instruments = manager.discover_instruments()
print('connecting to ' + available_instruments[0].name)
success = manager.connect(available_instruments[0])

# ca = pspymethods.chronoamperometry(interval_time=0.01, e=1.0, run_time=5.0)
eis = pspymethods.electrochemical_impedance_spectroscopy()

if success is 1:
    print('connection established')

    measurement = manager.measure(eis)
    if measurement is not None:
        print('measurement finished')
    else:
        print('failed to start measurement')

    success = manager.disconnect()

    if success is 1:
        print('disconnected')
    else:
        print('error while disconnecting')
else:
    print('connection failed')




