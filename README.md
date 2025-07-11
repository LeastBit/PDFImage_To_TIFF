# 🎯 PDF/图片转TIFF - 几乎无损转换工具

<div align="center">

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Quality](https://img.shields.io/badge/Quality-Near--Lossless-green.svg)](#)
[![Format](https://img.shields.io/badge/Format-PDF%2FPNG%2FJPG→TIFF-orange.svg)](#)

[中文](./README.md) | [English](./README_EN.md)

**专业级PDF和图片转TIFF工具，采用先进算法实现几乎无损的高质量转换**

</div>

## ✨ 核心特色

### 🔥 几乎无损转换
- **高精度渲染**：使用PyMuPDF专业级PDF渲染引擎，保持原始文档的精确细节
- **无损压缩**：采用TIFF LZW无损压缩算法，在减小文件大小的同时保证图像质量
- **高分辨率支持**：默认400 DPI输出，可自定义至更高分辨率，确保专业印刷级质量
- **色彩保真**：RGB色彩空间精确转换，保持原始色彩的真实性

### 🚀 强大功能
- **多格式支持**：完美支持PDF、PNG、JPG/JPEG格式转换
- **多页TIFF**：PDF多页文档转换为单个多页TIFF文件，保持文档完整性
- **批量处理**：一键批量转换整个文件夹，大幅提升工作效率
- **智能输出**：自动创建输出目录，智能命名，避免文件冲突

## 🛠️ 技术优势

### 质量保证
- **像素级精确**：每个像素都经过精确计算和转换
- **文本清晰度**：特别优化文本渲染，确保小字体依然清晰可读
- **图像保真**：保持原始图像的细节和层次感
- **专业输出**：符合印刷和存档标准的TIFF格式

## 📦 环境依赖

请确保已安装以下 Python 库：

```bash
pip install pymupdf Pillow
```

**依赖库说明：**
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**：专业PDF渲染引擎
- **[Pillow](https://pillow.readthedocs.io/)**：强大的图像处理库

## 🚀 使用方法

### 快速开始

```bash
# 基础用法 - 转换input_folder中的所有文件
python Main.py input_folder

# 指定输出文件夹
python Main.py input_folder output_folder

# 自定义高分辨率输出（推荐印刷用途）
python Main.py input_folder output_folder 600
```

### 详细参数说明

```bash
python Main.py <输入文件夹> [输出文件夹] [DPI]
```

| 参数 | 说明 | 默认值 | 推荐设置 |
|------|------|--------|----------|
| `输入文件夹` | 包含PDF/PNG/JPG文件的文件夹路径 | 必填 | - |
| `输出文件夹` | TIFF文件保存路径 | `输入文件夹/tiff_output` | 独立文件夹 |
| `DPI` | 输出分辨率 | 400 | 300(网络)、400(标准)、600+(印刷) |

### 使用场景示例

```bash
# 📄 文档存档 - 标准质量
python Main.py ./documents ./archive 400

# 🖼️ 图片转换 - 高质量
python Main.py ./photos ./tiff_photos 600

# 📚 批量处理 - 快速转换
python Main.py ./batch_files
```

## 📊 转换效果展示

### 实时转换进度
```
找到 5 个文件，开始转换为TIFF...
[1/5] 正在转换: contract.pdf -> contract.tiff
[2/5] 正在转换: photo.png -> photo.tiff
[3/5] 正在转换: scan.jpg -> scan.tiff
[4/5] 正在转换: manual.pdf -> manual.tiff
[5/5] 正在转换: image.jpeg -> image.tiff

转换完成! 成功: 5/5, 用时: 15.2秒
TIFF文件已保存至: ./tiff_output
```
### 注意事项
- ✅ 自动创建输出文件夹，无需手动创建
- ✅ 支持中文路径和文件名
- ✅ 智能跳过不支持的文件格式
- ⚠️ 高DPI设置会增加处理时间和文件大小
- ⚠️ 确保有足够的磁盘空间存储输出文件

## 📄 许可证

本项目基于 **MIT 许可证** 开源，欢迎自由使用、修改和分发。

---

<div align="center">

**🌟 如果这个工具对您有帮助，请给个Star支持一下！**

Made with ❤️ by [leastbit](https://github.com/leastbit)

</div>