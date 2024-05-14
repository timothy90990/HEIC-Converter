# HEIC to Image Converter

A user-friendly GUI application to convert HEIC files to various image formats (JPEG, PNG, BMP, GIF, TIFF) with support for both dark and light themes. This tool allows bulk import of HEIC files and lets users choose the export directory. It is built using Python, `customtkinter`, and `pillow_heif`.

## Features

- Convert HEIC files to JPEG, PNG, BMP, GIF, and TIFF.
- Bulk import of HEIC files.
- Choose export directory.
- Status bar showing conversion progress.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Install Required Libraries

```sh
pip install customtkinter pillow_heif
```

## Usage

### Running the Script Directly

1. Clone the repository:
    ```sh
    git clone https://github.com/timothy90990/HEIC-Converter.git
    cd HEIC-Converter
    ```

2. Run the script:
    ```sh
    python heic_converter.py
    ```

### Creating an Executable (Windows)

1. Install `pyinstaller`:
    ```sh
    pip install pyinstaller
    ```

2. Create the executable:
    ```sh
    pyinstaller --onefile --windowed heic_converter.py
    ```

3. The executable will be created in the `dist` directory.


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


## Acknowledgments

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern and customizable GUI components.
- [pillow_heif](https://github.com/carsales/pillow-heif) for HEIC file support in Pillow.
