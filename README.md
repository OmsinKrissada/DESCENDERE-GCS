# Ground Station
These will be our major tasks:

## Related Hardware:

- Laptop
- XBEE
- Antenna (Probably Yagi)

**Antenna ↔ XBEE ↔ Laptop**


## Our Jobs:

### Implement an ability to send the following commands
- ```CX```: Container Telemetry On/Off Command
	- send ```CXON``` to the container prior to launch
- ```ST```: Set Time
- ```SIM```: Simulation Mode Control Command
- ```SIMP```: Simulated Pressure Data (used in Simulation Mode only)
	- must be able to read pressure data profile file

### Saving .CSV file
- MUST INCLUDE PROPER HEADER
- Save received data in .csv file, one file for Payload and one for Container (Flight_<TEAM_ID>_C/P.csv)
- The file should be ready immediately after the launch via USB drive.

### Display and plot each data field in real time

### Send real time data to MQTT broker
