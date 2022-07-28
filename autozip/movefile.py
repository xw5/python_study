import os
import shutil
import datetime
# from zipfile import ZipFile

def find_file(search_path, include_str=None, filter_strs=None):
    """
    查找指定目录下所有的文件（不包含以__开头和结尾的文件）或指定格式的文件，若不同目录存在相同文件名，只返回第1个文件的路径
    :param search_path: 查找的目录路径
    :param include_str: 获取包含字符串的名称
    :param filter_strs: 过滤包含字符串的名称
    """
    if filter_strs is None:
        filter_strs = []

    files = []
    # 获取路径下所有文件
    names = os.listdir(search_path)
    for name in names:
        path = os.path.abspath(os.path.join(search_path, name))
        if os.path.isfile(path):
            # 如果不包含指定字符串则
            if include_str is not None and include_str not in name:
                continue

            # 如果未break，说明不包含filter_strs中的字符
            for filter_str in filter_strs:
                if filter_str in name:
                    break
            else:
                files.append(path)
        else:
            files += find_file(path, include_str=include_str, filter_strs=filter_strs)
    return files


if __name__ == '__main__':
    # # 使用示例
    # # 获取包含指定字符的文件
    # f = find_file("./test", include_str=".py")
    # print(f)
    #
    # # 获取不包含指定字符的文件
    # f = find_file("./test", filter_strs=[".pyc", "__init__"])
    # print(f)
    #
    # # 获取包含指定字符且不包含某些指定字符的文件
    # f = find_file("./test", include_str=".py", filter_strs=[".pyc", "__init__"])
    # print(f)

    # 生成时间字符串
    curr_time = datetime.datetime.now()
    newsFileName = curr_time.strftime("%Y%m%d%H%M%S")
    print(newsFileName)
    # 获取全部文件
    orign_path = 'D:\\work\\workspace\\microLearning_web\\src1'
    target_path = 'D:\\work\\workspace\\' + newsFileName

    # 创建日期目录
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    # 读取文件
    files = find_file(orign_path)
    # 移入的文件夹名 0 1 2依次递增
    newFileDir = 0
    # 当前代码行数
    codeLines = 0
    # 存储已经完成操作的文件
    copyFileNames = []
    copyErrorFileNames = []
    # 存储已经完成操作的文件数量
    copyFileCount = 0
    copyErrorFileCount = 0

    # zipHandle = ZipFile('{}\\{}.zip'.format(target_path, newFileDir), 'w')
    for file in files:
        fileName = file.split('\\')[-1]
        try:
            count = len(open(file, 'r', encoding='utf-8').readlines())
            codeLines = codeLines + count
            if codeLines >= 300000:
                codeLines = count
                newFileDir = newFileDir + 1
                # zipHandle.close()
                # zipHandle = ZipFile('{}\\{}.zip'.format(target_path, newFileDir), 'w')
            tempDir = target_path + '\\' + str(newFileDir)
            copyFileNames.append(fileName)
            copyFileCount = copyFileCount + 1
            if not os.path.exists(tempDir):
                os.mkdir(tempDir)
            shutil.copyfile(file, target_path + '\\' + str(newFileDir) + '\\' + fileName)
            # shutil.move(file, target_path + '\\' + str(newFileDir) + '\\' + fileName)
            # zipHandle.write(file)
        except Exception as err:
            copyErrorFileNames.append(fileName)
            copyErrorFileCount = copyErrorFileCount + 1
    # zipHandle.close()
    print("="*20)
    print('操作成功的文件列表：{}，操作文件数{}'.format('\n'.join(copyFileNames), copyFileCount))
    print("=" * 20)
    print('操作失败的文件列表：{}，操作文件数{}'.format('\n'.join(copyErrorFileNames), copyErrorFileCount))
    print("=" * 20)
