"""
Author: Andrew Hredzak - November 2024

This program takes a power measurement from a U2022XA power sensor
and outputs the value.

It requires the VISA resource string of the instrument that can
be acquired by NImax or Keysight Connection app

requires:: pyvisa and tkinter

powersenseTool_v7_BEST.py
"""

import pyvisa
import tkinter as tk
from tkinter import ttk

def take_measurement():
    try:
        # Create a VISA resource manager
        rm = pyvisa.ResourceManager()

        # Open a connection to the power sensor
        power_sensor = rm.open_resource(visa_resource_string)

        # Configure the power sensor 
        power_sensor.write(f':FREQuency {frequency}')
        power_sensor.write(f':AVERage:COUNt {averaging_count}')
        power_sensor.write(f':MEASure:MODE {measurement_mode}')

        # Initiate a power measurement
        power_sensor.write(':INITiate:IMMediate')

        # Fetch the measured power value
        power_value = float(power_sensor.query(':FETCH:SCALar:POWer?'))

        # Update the result label
        result_label.config(text=f"Measured Power: {power_value:.3f} dBm")

    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

    finally:
        # Close the connection to the power sensor
        if 'power_sensor' in locals() and power_sensor:
            power_sensor.close()

        # Close the VISA resource manager
        rm.close()

def clear_error_queue():
    try:
        # Get VISA resource string from the entry box
        power_sensor_resource_string = visa_resource_entry.get()

        # Create a VISA resource manager
        rm = pyvisa.ResourceManager()

        # Open a connection to the power sensor
        power_sensor = rm.open_resource(power_sensor_resource_string)

        # Send the *CLS command
        power_sensor.write('*CLS')

        # Update the result label
        result_label.config(text="Error queue cleared.")

    except Exception as e:
        result_label.config(text=f"Error clearing queue: {e}")

    finally:
        # Close the connection to the power sensor
        if 'power_sensor' in locals() and power_sensor:
            power_sensor.close()

        # Close the VISA resource manager
        rm.close()

# --- Functions to set parameters ---
def set_visa_resource():
    global visa_resource_string 
    visa_resource_string = visa_resource_entry.get()
    result_label.config(text=f"VISA Resource set to: {visa_resource_string}")

def set_frequency():
    global frequency
    frequency = frequency_entry.get()
    result_label.config(text=f"Frequency set to: {frequency} ")

def set_averaging_count():
    global averaging_count
    averaging_count = int(averaging_var.get())
    result_label.config(text=f"Averaging Count set to: {averaging_count}")

def set_measurement_mode():
    global measurement_mode
    measurement_mode = measurement_mode_var.get()
    result_label.config(text=f"Measurement Mode set to: {measurement_mode}")

# --- GUI Setup ---
window = tk.Tk()
window.title("Power Measurement GUI")

# VISA resource input
visa_resource_label = ttk.Label(window, text="VISA Resource String:")
visa_resource_label.grid(row=0, column=0, padx=5, pady=5)

visa_resource_entry = ttk.Entry(window, width=50)
visa_resource_entry.grid(row=0, column=1, padx=5, pady=5)

# Frequency input
frequency_label = ttk.Label(window, text="Frequency (Hz):")
frequency_label.grid(row=1, column=0, padx=5, pady=5)

frequency_entry = ttk.Entry(window)
frequency_entry.grid(row=1, column=1, padx=5, pady=5)
frequency_entry.insert(0, "1GHz")

# Averaging factor selection
averaging_label = ttk.Label(window, text="Averaging Count:")
averaging_label.grid(row=2, column=0, padx=5, pady=5)

averaging_var = tk.StringVar(value="10")
averaging_options = ["","1", "10", "100", "1000"]
averaging_menu = ttk.OptionMenu(window, averaging_var, *averaging_options)
averaging_menu.grid(row=2, column=1, padx=5, pady=5)

# Measurement mode selection
measurement_mode_label = ttk.Label(window, text="Measurement Mode:")
measurement_mode_label.grid(row=3, column=0, padx=5, pady=5)

measurement_mode_var = tk.StringVar(value="AVERage")
measurement_mode_options = ["","AVERage", "PEAK", "SAMPle"]
measurement_mode_menu = ttk.OptionMenu(window, measurement_mode_var, *measurement_mode_options)
measurement_mode_menu.grid(row=3, column=1, padx=5, pady=5)

# --- Set Parameter Buttons ---
visa_set_button = ttk.Button(window, text="Set VISA", command=set_visa_resource)
visa_set_button.grid(row=0, column=2, padx=5, pady=5)

frequency_set_button = ttk.Button(window, text="Set Frequency", command=set_frequency)
frequency_set_button.grid(row=1, column=2, padx=5, pady=5)

averaging_set_button = ttk.Button(window, text="Set Averaging", command=set_averaging_count)
averaging_set_button.grid(row=2, column=2, padx=5, pady=5)

mode_set_button = ttk.Button(window, text="Set Mode", command=set_measurement_mode)
mode_set_button.grid(row=3, column=2, padx=5, pady=5)

# Take Measurement button
measure_button = ttk.Button(window, text="Take Measurement", command=take_measurement)
measure_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10)

# Clear Error Queue button
clear_button = ttk.Button(window, text="Clear Error Queue", command=clear_error_queue)
clear_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Result label
result_label = ttk.Label(window, text="")
result_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# --- Initialize parameters ---
visa_resource_string = ""
frequency = "1GHz"
averaging_count = 10
measurement_mode = "AVERage"

# Start the GUI event loop
window.mainloop()