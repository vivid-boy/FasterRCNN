import os
import xml.etree.ElementTree as ET


def check_grayscale_images(folder_path):
    grayscale_images = []

    # 遍历文件夹下的所有文件
    for file_name in os.listdir(folder_path):
        annotation_file = os.path.join(folder_path, file_name)
        tree = ET.parse(annotation_file)
        root = tree.getroot()
        assert tree != None, "Failed to parse %s" % annotation_file
        assert len(root.findall("size")) == 1
        size = root.find("size")
        assert len(size.findall("depth")) == 1
        depth = int(size.find("depth").text)
        if depth != 3:
            grayscale_images.append((file_name, 1))

    return grayscale_images


# 指定文件夹路径
folder_path = "../datasets/VOC2028/Annotations"

# 检查灰度图像并输出文件名和深度
grayscale_images = check_grayscale_images(folder_path)
print("[")
for image_name, depth in grayscale_images:
    print(f"'{image_name[:-4]}',")
print("]")