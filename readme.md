# Power Measurement GUI
test text wwwwww
test text again the will be the first push

This is a simple Python program that uses PyVISA and Tkinter to take power measurements from a Keysight U2022XA power sensor.

## Requirements

* **Python:**  Make sure you have Python installed on your system.
* **PyVISA:** Install the PyVISA library using `pip install pyvisa`.
* **Keysight IO Libraries Suite:**  Download and install the Keysight IO Libraries Suite from the Keysight website to enable VISA communication with your instrument.

## How to Use

1.  **Connect the Power Sensor:** Connect the Keysight U2022XA power sensor to your computer.
2.  **Find the VISA Resource String:** Use Keysight Connection Expert or NI MAX to determine the VISA resource string for your power sensor. It will look something like `USB0::0x2A8D::0x1301::MY57502345::INSTR`.
3.  **Run the Program:** Execute the `powersenseTool_v7_BEST.py` script.
4.  **Enter Parameters:**
    *   Paste the VISA resource string into the "VISA Resource String" field and click "Set VISA".
    *   Enter the desired frequency in Hz (e.g., "1GHz") and click "Set Frequency".
    *   Select the averaging count from the dropdown menu and click "Set Averaging".
    *   Select the measurement mode ("AVERage", "PEAK", or "SAMPle") and click "Set Mode".
5.  **Take Measurement:** Click the "Take Measurement" button to get a power reading from the sensor. The result will be displayed in the result label.
6.  **Clear Error Queue:** If there are any errors, click the "Clear Error Queue" button to reset the instrument.

## Notes

*   Refer to the Keysight U2022XA documentation for more information on the instrument's features and specifications.
https://www.keysight.com/us/en/product/U2022XA/usb-peak-and-average-power-sensor-50-mhz-40-ghz.html


## Author

Andrew Hredzak - November 2024"# powersenseTool" 
