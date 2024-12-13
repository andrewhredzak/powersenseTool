import pyvisa
import time

rm = pyvisa.ResourceManager()
inst = rm.open_resource('USB0::0x0957::0x7F18::MY57250002::0::INSTR', timeout=10000)  # Increase timeout to 10 seconds


inst.write('*IDN?')



inst.write(" *CLS")
print("after clear")
time.sleep(3)
print("after 3 sec sleep")
inst.write(" *RST")
print("after *RST")
time.sleep(3)
inst.write(" CONF1")
print("after CONF1")
time.sleep(3)
inst.write(" INIT1")
print("after INIT1")
time.sleep(3)
measurement = inst.query("FETC1?")    # Retrieves the CALCulate1 measurement.
print("after FETC1?")
time.sleep(3)
print(measurement)

inst.close()
rm.close()