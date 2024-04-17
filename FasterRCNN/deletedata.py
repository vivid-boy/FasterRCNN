import os

ll = [
'000318',
'000324',
'000560',
'000639',
'000645',
'000680',
'000808',
'000949',
'001036',
'001052',
'001071',
'001076',
'001081',
'001094',
'001144',
'001179',
'001241',
'001291',
'001354',
'001397',
'001660',
'part2_001622',
'PartB_00059',
'PartB_00416',
'PartB_00456',
'PartB_00480',
'PartB_00874',
'PartB_00943',
'PartB_00987',
'PartB_00989',
'PartB_01021',
'PartB_01491',
'PartB_01551',
'PartB_01752',
'PartB_01786',
'PartB_01789',
'PartB_01805',
'PartB_01806',
'PartB_01815',
'PartB_01828',
'PartB_01972',
'PartB_01975',
'PartB_02018',
'PartB_02114',
'PartB_02233',
'PartB_02382',
]

PATH = "../datasets/VOC2028/ImageSets/Main/"

with open(PATH + "test.txt", 'r') as f:
    data = f.read().splitlines()
new_data = [line for line in data if line not in ll]
with open(PATH + "test.txt", 'w') as f:
    f.write('\n'.join(new_data))

with open(PATH + "train.txt", 'r') as f:
    data = f.read().splitlines()
new_data = [line for line in data if line not in ll]
with open(PATH + "train.txt", 'w') as f:
    f.write('\n'.join(new_data))

with open(PATH + "trainval.txt", 'r') as f:
    data = f.read().splitlines()
new_data = [line for line in data if line not in ll]
with open(PATH + "trainval.txt", 'w') as f:
    f.write('\n'.join(new_data))

with open(PATH + "val.txt", 'r') as f:
    data = f.read().splitlines()
new_data = [line for line in data if line not in ll]
with open(PATH + "val.txt", 'w') as f:
    f.write('\n'.join(new_data))

Annotations = "../datasets/VOC2028/Annotations"
JPEGImages = "../datasets/VOC2028/JPEGImages"


def delete_files_in_folder(folder_path, file_ext):
    # 遍历列表中的文件名
    for file_name in ll:
        file_path = os.path.join(folder_path, file_name + '.' + file_ext)
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 删除文件
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print(f"File does not exist: {file_path}")


# 删除文件夹中指定的文件
delete_files_in_folder(Annotations, 'xml')
delete_files_in_folder(JPEGImages, 'jpg')

