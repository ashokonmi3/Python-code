import time

import serial

# open() This will open the serial port
# close() This will close the serial port
# readline() This will read a string from the serial port
# read(size)  This will read n number of bytes from the serial port
# write(data) This will write the data passed to the function to the serial port
# in_waiting  This variable holds the number of bytes in the buffer
# =================
#
# serialPort = serial.Serial(port = "COM4", baudrate=115200,
#                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
#
# print(serialPort)
#
# time.sleep(3)
#
# serialPort.write(b'A')      #transmit 'A' (8bit) to micro/Arduino
#
# serialPort.close()
# =====================
# import serial
# ser = serial.Serial('/dev/ttyUSB0')  # open serial port
# print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string
# ser.close()
# ================
# with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
#     x = ser.read()          # read one byte
#     s = ser.read(10)        # read up to ten bytes (timeout)
#     line = ser.readline()
#
# =================

# ser = serial.Serial(
#     # Serial Port to read the data from
#     port='/dev/ttyUSB0',
#
#     # Rate at which the information is shared to the communication channel
#     baudrate=9600,
#
#     # Applying Parity Checking (none in this case)
#     parity=serial.PARITY_NONE,
#
#     # Pattern of Bits to be read
#     stopbits=serial.STOPBITS_ONE,
#
#     # Total number of bits to be read
#     bytesize=serial.EIGHTBITS,
#
#     # Number of serial commands to accept before timing out
#     timeout=1
# )
# # Pause the program for 1 second to avoid overworking the serial port
# while 1:
#     x = ser.readline()
#     print (x)
# =====================
import time
import serial

ser = serial.Serial(
    # Serial Port to read the data from
    port='/dev/ttyUSB0',

    # Rate at which the information is shared to the communication channel
    baudrate=9600,

    # Applying Parity Checking (none in this case)
    parity=serial.PARITY_NONE,

    # Pattern of Bits to be read
    stopbits=serial.STOPBITS_ONE,

    # Total number of bits to be read
    bytesize=serial.EIGHTBITS,

    # Number of serial commands to accept before timing out
    timeout=1
)
counter = 0

# Mentions the Current Counter number for each line written
# Pauses for one second each iteration to avoid overworking the port
while 1:
    ser.write("Write counter: %d \n" % (counter))
    time.sleep(1)
    counter += 1

# ===================
import nidigital
import time

with nidigital.Session(resource_name='PXI1Slot2') as session:

    channels = 'PXI1Slot2/0,PXI1Slot2/1'

    # Configure PPMU measurements
    session.channels[channels].ppmu_aperture_time = 0.000004
    session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

    session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

    session.channels[channels].ppmu_current_level_range = 0.000002
    session.channels[channels].ppmu_current_level = 0.000002
    session.channels[channels].ppmu_voltage_limit_high = 3.3
    session.channels[channels].ppmu_voltage_limit_low = 0

    # Sourcing
    session.channels[channels].ppmu_source()

    # Settling time between sourcing and measuring
    time.sleep(0.01)

    # Measuring
    current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
    voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

    print('{:<20} {:<10} {:<10}'.format('Channel Name', 'Current', 'Voltage'))
    for channel, current, voltage in zip(channels.split(','), current_measurements, voltage_measurements):
        print('{:<20} {:<10f} {:<10f}'.format(channel, current, voltage))

    # Disconnect all channels using programmable onboard switching
    session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT