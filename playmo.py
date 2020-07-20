import pygame
from pygame import mixer
import os
from kivy import event

# from moviepy.editor import VideoFileClip
# from moviepy.editor import *



class FuncMp3():   
    def __init__(self):
        self.path_dir =  os.path.realpath('.') + '/last/mp4/'  #mp3 root 위치 변수
        print(self.path_dir)
        FuncMp3.file_list = os.listdir(self.path_dir) #폴더내의 파일 list 생성
        print(FuncMp3.file_list)
        
        # FuncMp3.file_list.sort() #리스트내 이름정렬
        mixer.init()#mixer init
        
    
    #노래 재생
    def song_play(self,path):   
    #     '''
    #     음악 재생
    #     path = 음악경로
    #     '''       
    #     print('ahahahahah:', self.path_dir + path)
        
    #     pygame.mixer.music.load(self.path_dir + path)#파일 load
    #     pygame.mixer.music.play()#mp3 play
        
        clip = VideoFileClip(self.path_dir + path)
        clip.play()
        with VideoFileClip(path) as clip2:
           pass  # Implicit close called by context manager.

    def song_stop(self):
        mixer.music.stop()
if __name__ == '__main__':
    print('ahahahahahahhahahah')
    FuncMp3()
   

