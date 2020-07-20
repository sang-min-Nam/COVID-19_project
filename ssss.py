# -*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics','width',100)
Config.set('graphics','height',100)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty,ObservableList

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.label import Label
#리스트 생성 관련
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior





class ScreenMain(Screen):#main page   
    pass

    
    
class Rv(RecycleView):
    def __init__(self, **kwargs):
        super(Rv, self).__init__(**kwargs)
        list_ = ListProperty([])
        list_ = [1,2,3,4,5,6,7]
        # self.data = [{'text':str(i)} for i in fm.Func_Class.file_list]#data 를 만들 때 튜플 형식으로 만들어야 한다.(key:vlaue)
        for item in list_:
            self.data.append({'text':str(item),'font_name':'HANDotum'} )#data 를 만들 때 튜플 형식으로 만들어야 한다.(key:vlaue)
####################셀렉트 만들기########################
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):# 셀렉트 리스트 화면 구성
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):#셀렉트 리스트가 동작 하는것을 감지 하는 클래스
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
        ''' Respond to the selection of items in the view. '''        
        self.selected = is_selected
        if is_selected:
            
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))
#########################################################

class Manager(ScreenManager):#스크린 전환을 위한 screen manager 
    pass

class aaApp(App):
    def build(self):#kivy를 상속 받아 실행 했을 시 가장 처음에 실해후 실행 안함(init과 동일한 기능) - life cycle참조
        print('build')

        return Manager()

          
    def on_stop(self):
       
        print('종료')
        return super().on_stop()

if __name__ == '__main__':    
    aaApp().run()