#导入模块
import wget
import os
import shutil
import zipfile
import subprocess
#输出信息
print("欢迎使用繁星若尘客户端下载器")
print("程序当前工作目录为"+os.getcwd())
#检查用户是否拥有java环境
def check_jre():
    print("正在检测用户java环境")
    (status, uploadRes) = subprocess.getstatusoutput('java -version')
    if uploadRes.find("1.8.0"):
        print("检测到java环境，继续下载客户端")
    elif status == '1':
        print("未检测到java，正在下载安装包")
        java_download = wget.download("https://sdlc-esd.oracle.com/ESD6/JSCDL/jdk/8u241-b07/1f5b5a70bf22433b84d0e960903adac8/jre-8u241-windows-x64.exe?GroupName=JSC&FilePath=/ESD6/JSCDL/jdk/8u241-b07/1f5b5a70bf22433b84d0e960903adac8/jre-8u241-windows-x64.exe&BHost=javadl.sun.com&File=jre-8u241-windows-x64.exe&AuthParam=1586321164_dbf1468e5f336b9e1104b6ad8e273b77&ext=.exe")
        os.system(java_download)
        print("下载完成后请手动安装java")
    else:
        print("未检测到java，正在自动安装")
check_jre()
#让用户选择是否下载客户端
def choice():
    global zip_src
    choice = input("请输入y以下载客户端，或输入n退出程序")
    if choice == "n":
        assert(True)
    elif choice == "y" :
        #下面的是安装包地址，必须使用zip格式
        zip_src = wget.download("http://192.168.199.198/test.zip")
    else:
        print("无效操作，请重试！")
        choice()
choice()
#解压客户端
unzip_dir = input('\n'+"请输入客户端安装目录的绝对路径(输入a自动安装):")
print('正在解压中')
unzip_dir.replace('/','\\')
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')
if unzip_dir == "a":
    #当选择自动安装后，程序将会被解压至C:\fxrc文件夹
    #可自行修改
    unzip_file(zip_src,'C:\\fxrc')
else:
    unzip_file(zip_src,unzip_dir)
print("解压完毕，正在退出程序")
#git中文乱码了，特意又添加了一句
