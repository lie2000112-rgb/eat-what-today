cd "D:\个人经历\计算机\健身app"
.venv\Scripts\activate

# 创建并运行最简单的测试
echo 'from kivy.app import App
from kivy.uix.label import Label
class TestApp(App):
    def build(self):
        return Label(text="Hello Kivy!")
TestApp().run()' > test_simple.py

python test_simple.py