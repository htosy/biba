class Widget():
    def __init__(self,text,x,y):
        self.text = text 
        self.x = x
        self.y = y
    def print_info(self):
        print("Напис:",self.text)
        print("Розташування:", self.x,self.y)
class Button(Widget):
    def __init__(self,text,x,y,is_clicked):
        super().__init__(text,x,y)
        self.is_clicked = is_clicked
    def click(self):
        self.is_clicked = True
        print("Ви зареєестровані")
button1 = Button("Брати участь",100,100,False)
button1.print_info()
question = input("Хочете зареєструватися? (так/ні):")
if question.lower == "так":
    button1.click()
else:
    print("А шкода!1234567891011213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970")