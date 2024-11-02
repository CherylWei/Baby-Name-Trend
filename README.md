# Baby Names Trend
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![tkinter](https://img.shields.io/badge/tkinter-GUI-brightgreen?logo=tkinter&logoColor=white)
![FullStack](https://img.shields.io/badge/Full--stack-Project-brightgreen?logo=stackshare&logoColor=white)

Baby Names Trend is a comprehensive full-stack project that visualizes the popularity trends of baby names from 1900 to the present. It includes a graphical user interface for interaction, backed by data processing and visualization components.

## Features

- **🖥️ Interactive GUI**: A user-friendly interface built with `tkinter` for easy interaction.
- **📈 Historical Data Visualization**: Visualize the popularity trends of baby names over multiple decades.
- **🔍 Search Functionality**: Case-insensitive substring search within baby names.
- **⚡ Real-time Updates**: Dynamic plotting of data as the user requests different names.

## Project Structure

```plaintext
.
├── client/
│   ├── babygraphics.py    # Main GUI application
│   ├── babygraphicsgui.py # GUI setup and handling
├── server/
│   ├── babynames.py       # Backend data processing
│   ├── data/              # Contains baby name data files for various years
│       ├── baby-1900.txt
│       ├── baby-1910.txt
│       ...                # More files up to 2020
│       └── baby-2020.txt
└── README.md              # Project documentation
```

## Installation

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/baby-names-visualization.git
    cd baby-names-visualization
    ```

2. **Install dependencies**:

    From the project root, install required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the server**:

    Navigate to the `server/` directory and run the backend server (if applicable):

    ```bash
    cd server
    python babynames.py
    ```

4. **Run the client application**:

    Navigate to the `client/` directory and run the GUI application:

    ```bash
    cd client
    python babygraphics.py
    ```

## Usage

- **Run the Application**:
  - Execute `babygraphics.py` from the `client/` directory to start the GUI.

- **Enter a Baby Name**:
  - Type a baby name into the input field and press `Enter` to plot its ranking trend.

- **Search Baby Names**:
  - Use the search bar at the bottom to find names containing a specific substring.


## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- This project is inspired and adapted from Nick Parlante and Jerry Liao's Ghost assignment.

## 🧑‍💻 Author

- Cheryl Lin 我是雪兒 - [@Cheryl_Wei]
