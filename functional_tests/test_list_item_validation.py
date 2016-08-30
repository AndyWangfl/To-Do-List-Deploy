from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):    
    def test_cannot_add_empty_list_items(self):
        #伊迪斯访问首页，不小心提交了一个空代办事项
        #输入框内没有输入内容就按下了回车键

        #首页刷新了，显示一个错误信息
        #提示代办事项不能为空

        #她输入了一些文字，然后再次提交，这次没有问题了

        #她又提交了一个空代办事项

        #在清单页面看到了一个类似的错误信息

        #输入文字之后就没有问题了
        self.fail('write me!')
        

