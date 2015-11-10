问题和解决方案
======
问题1：安装时遇到encoding问题
使用pip install openpyxl遇到encoding的问题
后去pypi下载openpyxl后安装，仍然出现类似问题
下载地址https://pypi.python.org/pypi/openpyxl/2.3.0
解决：
在setup.py的import sys下行增加
reload(sys)
sys.setdefaultencoding('Cp1252')
======
问题2：import时遇到encoding问题
在import openpyxl时出现encoding问题
解决：
在mimetypes.py中增加上面同样的代码
======
问题3：openpyxl.load_workbook出现异常
我在使用openpyxl.load_workbook指定了一个首行有格式的xlsx文件出现异常
查了stackoverflow的相关文章，发现可能是openpyxl不支持样式的一个bug
将xlsx文件首行的样式去掉，就ok了