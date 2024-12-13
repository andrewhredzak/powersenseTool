import pyvisa
import time


visa_resource_string = 'USB0::0x0957::0x7F18::MY57250002::0::INSTR'

rm = pyvisa.ResourceManager()
inst = rm.open_resource(visa_resource_string, timeout=5000)  # Increase timeout to 10 seconds
#open a connection to the power sensor
with rm.open_resource(visa_resource_string) as power_sensor:
    power_sensor.write(" *CLS")        # resets instrument
    power_sensor.write(" *RST")        # resets instrument
    power_sensor.write(" CAL:ZERO:AUTO ONCE")  # Zeroing the U2022 X
    power_sensor.write(" CAL:AUTO ONCE")       # calibrating the U2022 X
    print("cal done")
    cal_success = power_sensor.query(" *STB?")
    print("checking cal:", power_sensor.query(" *STB?"))
    print("typeca: ", type(cal_success))


print("cal_success:",cal_success)
test = " +0"
print("test type:", type(test))
print("STB output1:", cal_success == test)  
#print("STB output2:", cal_success == cal_success) 



if cal_success == "+0":
    print("STB new output1:", True)
else:
    print("STB new output1:", False)





cal_success = cal_success.strip()
if cal_success == "+0": 
    print("STB strip output1:", True)
else:
    print("STB strip output1:", False)


#assert cal_success == "+0", "Calibration and Zeroing failed." 


inst.close()
rm.close()