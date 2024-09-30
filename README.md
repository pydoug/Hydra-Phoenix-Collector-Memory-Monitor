# Hydra Phoenix Collector Memory Monitor 🔨🤖🔧

The **Hydra Phoenix Collector Memory Monitor** is a memory pointer monitoring tool designed to track values within the *Path of Exile* game process. It accesses memory values, calculates stock prices, and determines the value to be moved. This project utilizes the `pymem` library to access and manipulate the process memory in real time.

## 📜 Features

- **Pointer Tracking**: Resolves a chain of memory pointers following specific offsets.
- **Real-time Memory Access**: Uses the `pymem` library to connect and read memory from the running `PathOfExile.exe` process.
- **Data Calculation**: Reads memory values such as stock and price data, performing calculations based on specific rules to determine the value to move.
- **Error Handling**: Robust error handling ensures that pointer resolution issues or memory access errors are logged clearly.

## 🛠️ Requirements

- **Python 3.x**
- `pymem` library (for reading and writing process memory)

### Install `pymem`

To install the `pymem` library, run the following command:

```
pip install pymem
```
⚙️ How to Use
Clone the repository:

```

git clone https://github.com/pydoug/Hydra-Phoenix-Collector-Memory-Monitor.git
cd Hydra-Phoenix-Collector-Memory-Monitor```

Run the script:
```python main.py```
Once the script is running, it will connect to the PathOfExile.exe process and begin monitoring the configured memory pointers. The program will read memory values such as STOCK and Price Base, calculate the prices, and output results to the terminal.

📝 Example Output
HYDRA PHOENIX COLLECTOR MEMORY MONITOR
Connecting "PathOfExile.exe" 12345
```
Pointer 1
  Base address: 0x308ab70, Initial address: 0x7ff6c8c0ab70
  Offset 0: 0x8, Address: 0x7ff6c8c0ab70, Value: 0x7ff6c8c0abcd
  ...
  Final offset: 0x8, Final address: 0x7ff6c8c0abcd
  STOCK: 500
  Price Base: 50
  Price Base 2: 2
  Price: 25.0
  Value to move: 20.0```
The output will show a series of memory pointers being tracked, along with the calculated values.

🛡️ Error Handling
If any memory pointer cannot be resolved due to invalid offsets or access violations, the script will catch and log the error, allowing it to continue with the next pointer.
Division by zero errors during price calculations are handled gracefully, and the script provides feedback to avoid crashes.
🚀 Future Improvements
Add graphical UI for easier monitoring and memory analysis.
Implement configuration files for flexible pointer and offset settings.
Expand support for other processes and games beyond Path of Exile.
⚖️ License
This project is licensed under the MIT License. See the LICENSE file for details.
