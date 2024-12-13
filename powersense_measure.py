import pyvisa
import time


visa_resource_string = 'USB0::0x0957::0x7F18::MY57250002::0::INSTR'
measurement_mode = "PEAK"

rm = pyvisa.ResourceManager()
inst = rm.open_resource(visa_resource_string, timeout=5000)  # Increase timeout to 10 seconds
#v1
"""
with rm.open_resource(visa_resource_string) as power_sensor:
    power_sensor.write(f' :MEASure:MODE {measurement_mode}')
    power_sensor.write(' :INITiate:IMMediate')
    power_value = float(power_sensor.query(' :FETCH:SCALar:POWer?'))
    print(f"Measured Power: {power_value:.3f} dBm")
"""

#v2
with rm.open_resource(visa_resource_string) as power_sensor:
    power_sensor.write(' *RST')
    power_sensor.write(' *CLS')
    power_sensor.write(' *RST')
    power_sensor.write(' CONF1')
    print("after conf1")
    power_sensor.write(' INIT1')
    power_value = float(power_sensor.query(' FETC1?'))
    print(f"Measured Power: {power_value:.3f} dBm")


inst.close()
rm.close()