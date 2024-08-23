## Time Report

### 1. Project Setup
- **Task**: Create project structure, set up `virtualenv`, install dependencies
- **Time spent**: 30 minutes

### 2. Server Configuration
- **Task**: Create a configuration file (`config.json`) to store the current firmware version
- **Time spent**: 10 minutes

### 3. Implement Core Routes

- **Task**: Implement route for checking firmware version (`/version.txt`)
- **Time spent**: 1 hour
- **Task**: Implement route for downloading firmware (`/firmware.bin`)
- **Time spent**: 20 minutes

### 4. Request Validation and Device Data Handling

- **Task**: Implement logic to validate custom HTTP headers and save device data
- **Time spent**: 4,5 hours
- **Task**: Record and update the last seen time and update time for the device
- **Time spent**: 1,5 hours

### 5. Signal for Google Sheets Reporting

- **Task**: Implement a signal to trigger on new devices or firmware version changes
- **Time spent**: 2 hours

### 6. HTTPS Implementation and Access Control

- **Task**: Set up HTTPS and ensure only HTTPS requests are accepted with a specific key
- **Time spent**: 1 hour  
__NOT IMPLEMENTED__

### 7. Unit Testing

- **Task**: Create unit tests for core routes and functionality
- **Time spent**: 1,5 hours 

### 8. Systemd Service

- **Task**: Write a `systemd` service file for automatic server start/restart
- **Time spent**: 1 hour  
__NOT IMPLEMENTED__

### 9. Docker

- **Task**: Package the application into a Docker container
- **Estimated Time**: 30 minutes

### Total Spent Time: 14 hours (estimated time - 16 hours)