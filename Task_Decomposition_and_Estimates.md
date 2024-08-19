## Time Estimations

### 1. Project Setup

- **Task**: Create project structure, set up `virtualenv`, install dependencies
- **Estimated Time**: 1 hour

### 2. Server Configuration

- **Task**: Create a configuration file (`config.json`) to store the current firmware version
- **Estimated Time**: 30 minutes

### 3. Implement Core Routes

- **Task**: Implement route for checking firmware version (`/version.txt`)
- **Estimated Time**: 1 hour
- **Task**: Implement route for downloading firmware (`/firmware.bin`)
- **Estimated Time**: 1 hour

### 4. Request Validation and Device Data Handling

- **Task**: Implement logic to validate custom HTTP headers and save device data
- **Estimated Time**: 2 hours
- **Task**: Record and update the last seen time and update time for the device
- **Estimated Time**: 1 hour

### 5. Signal for Google Sheets Reporting

- **Task**: Implement a signal to trigger on new devices or firmware version changes
- **Estimated Time**: 2 hours

### 6. HTTPS Implementation and Access Control

- **Task**: Set up HTTPS and ensure only HTTPS requests are accepted with a specific key
- **Estimated Time**: 2 hours

### 7. Unit Testing

- **Task**: Create unit tests for core routes and functionality
- **Estimated Time**: 2.5 hours

### 8. Systemd Service

- **Task**: Write a `systemd` service file for automatic server start/restart
- **Estimated Time**: 1 hour

### 9. Docker

- **Task**: Package the application into a Docker container
- **Estimated Time**: 2 hours

### Total Estimated Time: 16 hours