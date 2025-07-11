# 🎯 PDF/Image to TIFF - Near-Lossless Conversion Tool

<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Quality](https://img.shields.io/badge/Quality-Near--Lossless-green.svg)](#)
[![Format](https://img.shields.io/badge/Format-PDF%2FPNG%2FJPG→TIFF-orange.svg)](#)

[中文](./README.md) | [English](./README_EN.md)

**Professional-grade PDF and image to TIFF converter with advanced algorithms for near-lossless high-quality conversion**

</div>

## ✨ Core Features

### 🔥 Near-Lossless Conversion
- **High-Precision Rendering**: Uses PyMuPDF professional PDF rendering engine to maintain precise document details
- **Lossless Compression**: Employs TIFF LZW lossless compression algorithm to reduce file size while preserving image quality
- **High-Resolution Support**: Default 400 DPI output, customizable to higher resolutions for professional print-quality results
- **Color Fidelity**: Accurate RGB color space conversion maintaining original color authenticity

### 🚀 Powerful Capabilities
- **Multi-Format Support**: Perfect support for PDF, PNG, JPG/JPEG format conversion
- **Multi-Page TIFF**: Converts PDF multi-page documents to single multi-page TIFF files, maintaining document integrity
- **Batch Processing**: One-click batch conversion of entire folders, dramatically improving work efficiency
- **Smart Output**: Automatically creates output directories with intelligent naming to avoid file conflicts

## 🛠️ Technical Advantages

### Quality Assurance
- **Pixel-Perfect Accuracy**: Every pixel is precisely calculated and converted
- **Text Clarity**: Specially optimized text rendering ensuring small fonts remain crisp and readable
- **Image Fidelity**: Maintains original image details and depth
- **Professional Output**: TIFF format compliant with printing and archival standards

## 📦 Dependencies

Please ensure the following Python libraries are installed:

```bash
pip install pymupdf Pillow
```

**Library Description:**
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**: Professional PDF rendering engine
- **[Pillow](https://pillow.readthedocs.io/)**: Powerful image processing library

## 🚀 Usage

### Quick Start

```bash
# Basic usage - convert all files in input_folder
python Main.py input_folder

# Specify output folder
python Main.py input_folder output_folder

# Custom high-resolution output (recommended for printing)
python Main.py input_folder output_folder 600
```

### Detailed Parameters

```bash
python Main.py <input_folder> [output_folder] [DPI]
```

| Parameter | Description | Default | Recommended |
|-----------|-------------|---------|-------------|
| `input_folder` | Folder path containing PDF/PNG/JPG files | Required | - |
| `output_folder` | TIFF file save path | `input_folder/tiff_output` | Separate folder |
| `DPI` | Output resolution | 400 | 300(web), 400(standard), 600+(print) |

### Usage Scenarios

```bash
# 📄 Document archiving - standard quality
python Main.py ./documents ./archive 400

# 🖼️ Image conversion - high quality
python Main.py ./photos ./tiff_photos 600

# 📚 Batch processing - quick conversion
python Main.py ./batch_files
```
## 📊 Conversion Results

### Real-time Progress
```
Found 5 files, starting TIFF conversion...
[1/5] Converting: contract.pdf -> contract.tiff
[2/5] Converting: photo.png -> photo.tiff
[3/5] Converting: scan.jpg -> scan.tiff
[4/5] Converting: manual.pdf -> manual.tiff
[5/5] Converting: image.jpeg -> image.tiff

Conversion complete! Success: 5/5, Time: 15.2 seconds
TIFF files saved to: ./tiff_output
```

### Notes
- ✅ Automatically creates output folders, no manual creation needed
- ✅ Supports Unicode paths and filenames
- ✅ Intelligently skips unsupported file formats
- ⚠️ Higher DPI settings increase processing time and file size
- ⚠️ Ensure sufficient disk space for output files

## 📄 License

This project is open-sourced under the **MIT License**. Feel free to use, modify, and distribute.

---

<div align="center">

**🌟 If this tool helps you, please give it a Star!**

</div>