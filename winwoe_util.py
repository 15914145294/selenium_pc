# -*- coding:utf-8 _*-
""" 
@author:Administrator 
@file: window_util.py 
@time: 2018/06/08 
"""
import win32gui
import win32con
import win32api


class WindowUtil(object):
    @staticmethod
    def get_child_windows(parent):
        """
        获取主窗口胡所有子窗体handle
        :param parent: 主窗体handle
        :return: 子窗体handle list
        """
        if not parent:
            return
        hwnd_child_list = []
        win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwnd_child_list)
        return hwnd_child_list

    def find_parent_handle(self, class_name, window_title):
        """
        to get the parent handle of window
        :param class_name: the class name of windwo
        :param window_title: the title of window
        :return: the window handle
        """
        handle = win32gui.FindWindow(class_name, window_title)
        return handle

    def find_subhandle_index(self, parent_handle, sub_class_name, index=0):
        """
        根据子窗口的窗体类名，寻找第index号个同类型的兄弟窗口
        :param parent_handle:the paren window handle
        :param sub_class_name: the class name of sub window
        :param index:the title name of sub window
        :return:the handle of sub window
        """
        assert type(index) == int and index >= 0
        handle = win32gui.FindWindowEx(parent_handle, 0, sub_class_name, None)
        while index > 0:
            handle = win32gui.FindWindowEx(parent_handle, handle, sub_class_name, None)
            index -= 1
        return handle

    def find_subhandles(self, parent_handle, class_name_list):
        """
        递归寻找子窗体的handle
        :param parent_handle: 主窗口handle
        :param class_name_list: 子窗口窗体类型list such as:[("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)]
        :return:
        """
        assert type(class_name_list) == list
        if len(class_name_list) == 1:
            return self.find_subhandle_index(parent_handle, class_name_list[0][0], class_name_list[0][1])
        else:
            parent_handle = self.find_subhandle_index(parent_handle, class_name_list[0][0], class_name_list[0][1])
            return self.find_subhandles(parent_handle, class_name_list[1:])


class MenuUtil(object):
    """
    GetMenu(hwnd)
        描述：获取窗口的菜单句柄。
    参数：
        hwnd：整型，需要获取菜单的窗口的句柄。
        说明：获取的是插图中黄色的部分。
    GetSubMenu(hMenu, nPos)
        描述：获取菜单的下拉菜单或者子菜单。
    参数：
        hMenu：整型，菜单的句柄，从GetMenu获得。
        nPos：整型，下拉菜单或子菜单的的索引，从0算起。
        说明：这个可以获取插图中蓝色的部分z；如描述所述，这个不仅可以获取本例中的下拉菜单，还可以获取子菜单。
    GetMenuItemID(hMenu, nPos)
        描述：获取菜单中特定项目的标识符。
    参数：
        hMenu：整型，包含所需菜单项的菜单句柄，从GetSubMenu获得。
        nPos：整型，菜单项的索引，从0算起。
    PostMessage(hWnd, Msg, wParam, lParam)
        描述：在消息队列中加入为指定的窗体加入一条消息，并马上返回，不等待线程对消息的处理。
    参数：
        hWnd：整型，接收消息的窗体句柄
        Msg：整型，要发送的消息，这些消息都是windows预先定义好的，可以参见系统定义消息(System-Defined Messages))
        wParam：整型，消息的wParam参数
        lParam：整型，消息的lParam参数
    """

    def __init__(self, fgFilePath=None):
        self.Mhandle = win32gui.FindWindow("FaceGenMainWinClass", None)
        self.menu = win32gui.GetMenu(self.Mhandle)
        # the first sub menu to linitialize
        self.menu = win32gui.GetSubMenu(self.menu, 0)
        print "FaceGen initialization compeleted"

    def menu_command(self, command):
        """
        菜单操作 然后定义一个菜单操作的方法
        返回弹出的打开或保存的对话框的句柄 dig_handle
        返回确定按钮的句柄 confBTN_handle
        """
        command_dict = {  # [目录的编号, 打开的窗口名]
            "open": [2, u"打开"],
            "save_to_image": [5, u"另存为"],
        }
        cmd_ID = win32gui.GetMenuItemID(self.menu, command_dict[command][0])
        win32gui.PostMessage(self.Mhandle, win32con.WM_COMMAND, cmd_ID, 0)
        for i in range(10):
            if win32gui.FindWindow(None, command_dict[command][1]):
                break  # 如果找到了打开或者另存为的对话框，就跳出循环
            else:
                win32api.Sleep(200)  # 利用这个函数等待200ms，就不需要再额外导入time模块了
        dig_handle = win32gui.FindWindow(None, command_dict[command][1])
        confBTN_handle = win32gui.FindWindowEx(dig_handle, 0, "Button", None)
        print win32gui.Gett
        return dig_handle, confBTN_handle


if __name__ == "__main__":
    s=MenuUtil('d:/test/Debby.fg').menu_command('save_to_image')
    print s
