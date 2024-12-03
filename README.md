# imageEase

### Program Description

This program is a GUI tool for **converting** image files (PNG, JPG, etc.) to WebP format by drag & drop, using Python's `TkinterDnD` for drag & drop and the `Pillow` library for conversion.

#### Main Features

1. **Drag & Drop support**:.
   - By dragging and dropping files into the dedicated area, they will be registered in the list.

2. **Conversion to WebP format**: Convert dropped image files to WebP format.
   - Converts dropped image files to WebP format.
   - The converted files will be saved in an `img` folder created in the program's execution directory. 3.

3. **Concise GUI**:.
   - Visually clear design with dark theme.
   - It has a file list, conversion status display, and conversion button.

--- ......................

### How to use

#### 1. install required libraries

This program uses the following libraries. Please install them beforehand.

```bash
pip install pillow customtkinter tkinterdnd2
````

#### 2. run the program

Run the Python script.

```bash
python script_name.py
````

#### 3. Instructions for use

1. **Drag and Drop Files**:.
   - Drag and drop the image files you wish to convert into the area labeled “Drag and Drop Images” at the top of the window.
   - The path of the dropped file will appear in the center list. 2.

2. **Press the Convert button**:.
   - Press the “Convert to WebP” button at the bottom to convert all registered image files to WebP format. 3.

3. **Check the conversion result**:.
   - The converted WebP files will be saved in the `img` folder in the same directory as the script.
   - A status label will indicate the number of files converted and their status.

#### 4. Notes

- Supported file formats are the image formats supported by `Pillow` (PNG, JPG, BMP, etc.).
- If the input file is corrupted, an error will be displayed and the file will not be converted.
- If a WebP file with the same name as an already existing file is created, it will be overwritten.

--- ...

### program structure

1. **Main Logic**:.
   - Describe GUI construction and event settings in the `main` function. 2.

2. **Conversion process**: In the `convert_to_webP` function, write the following.
   - Convert images to WebP format with `convert_to_webp` function.
   - Check the output directory (`img` folder) and create it if it does not exist. 3.

3. **Drag and drop processing**: Use `on_drop` function.
   - Register the dragged and dropped files in the list with `on_drop` function. 4.

4. **Entry point**: Register the file in the list with `on_drop` function.
   - Call `main` function in `if __name__ == “__main__”:` block.

---

### Intended users.

- **General users who need image conversion**:.
   - People who want to convert multiple images to WebP format easily.
- **Web developers**:.
   - People who want to improve the performance of their sites by generating WebP-formatted images.

--- ......................

### room for improvement

- **Customize supported formats**:.
   - Filtering of input file formats.
- **Quality adjustment after conversion**:.
   - Added option to set compression ratio and quality of WebP.
- **Progress display**:.
   - Progress bar to show conversion progress.
