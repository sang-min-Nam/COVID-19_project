from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '600')
import playmo as pl
import kivy
from kivy.app import App
from kivymd.app import MDApp

from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty,NumericProperty,ListProperty
from kivy.uix.actionbar import ActionBar , ActionItem, ActionView, ActionPrevious, ActionGroup, ActionButton
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
###키비폰트 정하기
# from kivy.core.text import LabelBase, DEFAULT_FONT
# from kivy.resources import resource_add_path
# resource_add_path('c:/windows/fonts')
# LabelBase.register(DEFAULT_FONT, 'ngulim.TTF')
# from kivy.lang import Builder
# with open("C:/Users/w/middle_of_project/test/switch.kv", encoding='utf-8') as f: # Note the name of the .kv 
#     Builder.load_string(f.read())

# from kivy.core.text import LabelBase, DEFAULT_FONT
# from kivy.resources import resource_add_path
# resource_add_path('c:/windows/fonts')
# LabelBase.register(DEFAULT_FONT, 'malgunbd.ttf')
# from kivy.lang import Builder

# with open("C:/Users/w/middle_of_project/test/switch.kv", encoding='windows-1252') as f: # Note the name of the .kv 
#     Builder.load_string(f.read())
from kivy.uix.button import Button 
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
import pandas as pd
# ##맷립 임포트
import matplotlib
matplotlib.use(r'module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt

##비디오목록

import playmo
from kivy.uix.videoplayer import VideoPlayer
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
import os

from kivy.uix.recycleview import RecycleView

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label

global path_real
path_real='asdkjfsdkjfkl'
class Make():
    def make_graph(self,kidName,kidData,now_date):
        fig, ax = plt.subplots()#그래프틀

        #체온(아동)그리기위해 csv에서 data가공함
        kidData['hour']=kidData['time'].apply( lambda x: int(x.split(":")[0]))
        kidData2=kidData[ kidData['name']==kidName]
        kidData3=kidData2[ kidData['date']==now_date]
        kidData4=kidData3.groupby('hour').mean()
        x1 = kidData4['temp'].keys()
        y1 = kidData4['temp'].values
        list(x1)
        plty1=list(y1)
        plty1=[ round(x,1) for x in plty1]
        xlay1 = [str(x)+"시" for x in list(x1)]
        ylay1 = plty1

        #체온(반평균)그리기위해 csv에서 data가공함
        df2=kidData[ kidData['date']==now_date]
        df3=df2.groupby('hour').mean()
        x = df3['temp'].keys()
        y = df3['temp'].values
        list(x)
        plty=list(y)
        plty=[ round(x,1) for x in plty]
        xlay = [str(x)+"시" for x in list(x)]
        ylay = plty
        plt.ylim(34, 40)

        #체온(아동)그래프그림
        plot = plt.bar(xlay1, ylay1, label="{0}".format(kidName), color="sandybrown")
        plt.xticks(fontsize = 15, color = 'k')
        plt.yticks(fontsize = 15, color = 'k')

        #그래프 색상조건
        for i in range(len(ylay1)):
            if ylay1[i] >=37.3:
                col = 'crimson'
            else:
                col = 'sandybrown'
            plt.bar(xlay1[i],ylay1[i],color=col)
        #그래프 값출력
        for value in plot:
            height = value.get_height()
            ax.text(value.get_x() + value.get_width()/2.,
                    1.002*height, height, ha='center', va='bottom', size=15)

        #기존그래프에 새그래프 추가함
        plot = plt.plot(xlay, ylay, marker='o', label="반평균", linewidth=4, markersize=8, color='darkblue')
        plt.title('{0} / 반 평균체온'.format(kidName), fontsize=20)
        plt.ylim(34, 40)
        plt.yticks(fontsize = 15, color = 'k')
        plt.legend(fontsize=14)

        return fig.canvas 

class MyBox(BoxLayout):
    def __init__(self,**kwargs):
        super(MyBox,self).__init__(orientation='vertical')
        #변수에 어린이이름/전체엑셀데이터 추가
        self.kidName='배주현'
        self.kidData=pd.read_csv(r'last/temp.csv', encoding='cp949')
        self.make = Make()
        #데이터에서 유니크날짜뽑아서 스피너 꾸미기
        date_list = list(self.kidData['date'].unique())
        self.mySpinner = Spinner(text=date_list[-1], values=(date_list))
        self.mySpinner.size_hint  = (0.3, 0.05)
        self.mySpinner.background_color = [250,250,250,1]
        self.mySpinner.color = [0,0,0,1]

        self.mySpinner.pos_hint={'right': 1, 'top':1}
        #스피너에 함수추가
        self.mySpinner.bind(text=self.spinner_change)
        #박스에 스피너추가
        self.add_widget(self.mySpinner)
        
        #그래프추가
        self.graph = Make().make_graph(self.kidName,self.kidData,self.mySpinner.text)
        self.add_widget(self.graph)

        #버튼추가
        # self.add_widget(Button())

    def spinner_change(self,widget,value):
        #기존그래프 제거
        self.remove_widget(self.graph)
        #새 그래프 이름도 self.graph로 재생성후 add_widget
        self.graph = self.make.make_graph(self.kidName,self.kidData,self.mySpinner.text)
        self.add_widget(self.graph)



class FirstScreen(Screen): #login Screen
    def do_login(self, usernameText, passwordText): #do_login 함수에 loginText, passwordText입력받아라.
        app = App.get_running_app() 
        app.username = usernameText
        app.password = passwordText
        
        info = self.ids.info
        if app.username == "" :
            info.text = '[color=#FF0000]Insert ID[/color]'
        
        elif app.password == "" :
            info.text = '[color=#FF0000]Insert PW[/color]'
        
        elif app.username == "1" and app.password == "1":
            
            self.manager.current = 'second'

        elif app.username == "2" and app.password == "2":
            
            self.manager.current = 'second'

        elif app.username == "3" and app.password == "3":
            
            self.manager.current = 'show'
        else:
            info.text = '[color=#FF0000]Check ID&PW again[/color]'

        app.config.read(app.get_application_config()) # LoginApp 클래스에 get_application_config 함수를 읽어라
        app.config.write()  # LoginApp 클래스에 get_application_config 함수를 실행시켜라
  
    def do_signup(self):
        self.manager.current = 'signup'

    def resetForm(self):  
        self.ids['username'].text = "" # resetForm 함수에 loi
        self.ids['password'].text = ""
class SignupScreen(Screen):
    pass

class Actionbar(Widget):
    pass
class SecondScreen(Screen):
    pass

class GraphScreen(Screen):
    pass

class DrawingScreen(Screen):
    pass

class InputScreen(Screen):
    pass

class VideoScreen(Screen):
    pass
class ThirdScreen(Screen):    
    pass






class Vid(VideoPlayer):
    

    path = StringProperty('last/covid.avi')

    def on_state(self, instance, value):
        global path_real
        path_real = instance
        print(instance.source)        
        print(value)
        return super().on_state(instance, value)
    

    
        
class Rv(RecycleView):
    def __init__(self, **kwargs):
        super(Rv, self).__init__(**kwargs)
        list_ = ListProperty([])
        pl.FuncMp3()
        list_ = pl.FuncMp3.file_list
        
        # self.data = [{'text':str(i)} for i in fm.Func_Class.file_list]#data 를 만들 때 튜플 형식으로 만들어야 한다.(key:vlaue)
        for item in list_:
            self.data.append({'text':str(item),'font_name':'HANDotum'} )#data 를 만들 때 튜플 형식으로 만들어야 한다.(key:vlaue)
####################셀렉트 만들기########################
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):# 셀렉트 리스트 화면 구성
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):#셀렉트 리스트가 동작 하는것을 감지 하는 클래스
    

    def __init__(self,**kwargs):
        super(SelectableLabel,self).__init__()
        self.m = pl.FuncMp3()
        self.realpath = os.path.realpath('.')
        print(self.realpath)
        
        
        
        

    ''' Add selection support to the Label '''
    index = None
    
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)
    
    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        global path_real
        ''' Respond to the selection of items in the view. '''        
        self.selected = is_selected
        if is_selected:            
            print("selection changed to {0}".format(rv.data[index]))
            print(rv.data[index]['text'])
            print (path_real)
            path_real.source = 'last/' + rv.data[index]['text']
            # self.m.path_chk(aa)
            # self.m.song_play(rv.data[index]['text'])
            
        else:
            print("selection removed for {0}".format(rv.data[index]))
            

class Manager(ScreenManager):
    pass

class switchApp(MDApp):
    username = StringProperty(None) # 이름 입력값
    password = StringProperty(None) # P/W 입력값
    
    def build(self):
        return Manager()



if __name__ == '__main__':
    switchApp().run()