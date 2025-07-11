import fitz  # PyMuPDF
from PIL import Image
import os
import sys
import time

def file_to_tiff(input_file, output_tiff, dpi=400):
    """
    将PDF、PNG或JPG文件转换为TIFF格式
    """
    try:
        if input_file.lower().endswith('.pdf'):
            # 处理PDF文件
            doc = fitz.open(input_file)
            images = []
            for page in doc:
                pix = page.get_pixmap(dpi=dpi, colorspace="rgb")
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                images.append(img)
            if images:
                images[0].save(
                    output_tiff,
                    save_all=True,
                    append_images=images[1:],
                    compression="tiff_lzw",
                    dpi=(dpi, dpi),
                    resolution_unit=2
                )
            doc.close()
        elif input_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 处理PNG或JPG文件
            img = Image.open(input_file)
            img.save(output_tiff, format="TIFF", compression="tiff_lzw", dpi=(dpi, dpi))
        else:
            print(f"不支持的文件格式: {input_file}")
            return False
        return True
    except Exception as e:
        print(f"转换 {input_file} 时出错: {e}")
        return False

def batch_convert_files(input_folder, output_folder=None, dpi=400):
    """
    批量转换文件夹中所有PDF、PNG和JPG文件为TIFF
    
    参数:
        input_folder: 输入文件夹路径
        output_folder: 输出文件夹路径，默认为输入文件夹下的"tiff_output"子文件夹
        dpi: 转换分辨率
    """
    # 确保输入文件夹存在
    if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
        print(f"错误: 输入文件夹 '{input_folder}' 不存在!")
        return
        
    # 如果未指定输出文件夹，在输入文件夹内创建tiff_output子文件夹
    if output_folder is None:
        output_folder = os.path.join(input_folder, "tiff_output")
    os.makedirs(output_folder, exist_ok=True)

    # 获取所有支持的文件
    supported_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg'))]
    if not supported_files:
        print(f"未在 '{input_folder}' 找到支持的文件!")
        return

    total = len(supported_files)
    succeeded = 0
    print(f"找到 {total} 个文件，开始转换为TIFF...")
    start_time = time.time()

    # 逐个转换文件
    for i, file in enumerate(supported_files, 1):
        input_path = os.path.join(input_folder, file)
        output_filename = os.path.splitext(file)[0] + '.tiff'
        output_path = os.path.join(output_folder, output_filename)
        print(f"[{i}/{total}] 正在转换: {file} -> {output_filename}")
        success = file_to_tiff(input_path, output_path, dpi)
        if success:
            succeeded += 1

    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"\n转换完成! 成功: {succeeded}/{total}, 用时: {elapsed:.1f}秒")
    print(f"TIFF文件已保存至: {output_folder}")

if __name__ == "__main__":
    # 如果有命令行参数，使用第一个参数作为输入文件夹
    if len(sys.argv) > 1:
        input_folder = sys.argv[1]
        
        # 使用第二个参数作为输出文件夹（如果提供）
        output_folder = sys.argv[2] if len(sys.argv) > 2 else None
        
        # 使用第三个参数作为DPI（如果提供）
        dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 400
        
        batch_convert_files(input_folder, output_folder, dpi)
    else:
        # 没有命令行参数时，使用当前目录
        print("请指定一个包含PDF文件的文件夹路径:")
        print("用法: python Main.py <输入文件夹> [输出文件夹] [DPI]")
        print("示例: python Main.py ./input_files ./tiff_files 300")
        #英文
        print("Usage: python Main.py <input_folder> [output_folder] [DPI]")
        print("Example: python Main.py ./input_files ./tiff_files 300")
