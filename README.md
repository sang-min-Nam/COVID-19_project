## COVID-19_project
## 1. 목표 : 코로나 블루 대처를 위한 스마트 로봇 및 어플 개발
    최근에 전국 269만 초중고학생들이 학교에서 수업을 받고 있지만 10명 중 1명은 불안해서 또는 의심 증상이 있다는 이유로 학교에 가지 않고 있으며, 학교 전체가 등교를 미룬 곳도 800곳을 넘어서고 있습니다.

    이에 학부모의 불안이 고조되고 있는 현 상황에서 학부모들이 가정 및 직장에서 아이의 건강상태 및 심리상태를 비대면으로 모니터링을 하고, 아이들에게 친숙한 펭수로봇을 통해 질병관리본부에서 제작한 감염병예방수칙을 홍보하면서 아이들의 표정변화 등을 빅데이터 및 AI 기술을 적용한 시제품을 개발하기로 했습니다.

## 2. 개발중점 :  
    ● H/W시스템 : 엣지컴퓨팅으로 AI를 설계 및 구현­ AI기반의 안면인식 시스템 설계 및 구현
    - 표정변화를 인식하기 위한 트래킹기술 구현
    - 로봇의 기능제어를 위한 제어 설계 및 구현
    - 라즈베리파이 4B 기반의 Ubuntu OS Build
    - 자율주행이 가능한 초음파센서를 이용한 제어 설계 및 구현
    - 영상을 분석하기 위한 영상획득 및 정제
    - 열감지(적외선) 센서를 이용한 열감지 측정 설계 및 구현
    - Wifi를 이용한 영상스트리밍 전송 시스템 설계 및 구현
    - 디스플레이를 활용한 저장정보 재생 시스템 설계 및 구현
    - 음성인식데이터를 Text로 전환하는 시스템 설계 및 구현

    ● S/W시스템 : 비대면 상담 및 치료 스마트폰 및 디스플레이용 앱개발
    - Cross-Platform인 Kivy를 활용한 UI/UX 설계 및 구현
    - 로봇에서 전송되는 정보를 활용한 빅데이터 시각화 설계 및 구현
    - 얼굴표정인식 정보를 활용한 표정분석 패턴분석 설계 및 구현
    - 아이들의 그림정보를 획득하여 AI분석을 위한 피처분석 설계 및 구현
    - CAT검사와 비슷한 단어분석검사를 이용한 AI분석을 위한 피처분석 설계 및 구현
    - 아이들의 특정모습을 녹화 재생할 수 있는 Animation 설계 및 구현
    - 관리자, 어린이, 부모용 로그인정보 DB설계 및 구현

    ● DB시스템 : PySpark를 기반으로 한 .DB시스템 설계 및 구축
    - PySpark Linux 서버 시스템 Build
    - PySpark를 활용한 데이터 레이크 및 데이터웨어하우스 설계 및 구현
    - PySpark를 활용한 정규표현식 기반의 정제 코드 빌드
    - PySpark기반의 Mongo DB 설계 및 구현
    - PySpark 데이터전송 코드 빌드
    - PySpark 시리시간 스트리밍전송 시스템 설계 및 구현
    - 음성인식을 텍스트로 형태소 분리 저장하는 시스템 설계 및 구현

    ● 빅데이터 및 AI 플랫폼 : AI를 기반으로 한 분석 및 데이터빌드 플랫폼 구축
    - CNN 기반의 영상분석 및 자기학습 시스템 설계 및 구현
    - Regression 알고리즘을 적용한 ML 설계 및 구현
    - Classification 알고리즘을 적용한 ML 설계 및 구현
    - Clustering 알고리즘을 적용한 ML 설계 및 구현
    - ML알고리즘에 Dimensionality reduction 설계 및 구현
    - 기능 및 특성별 Model selection 설계 및 구현
    - 데이터의 효율성과 전자동화를 위한 Preprocessing 설계 및 구현
    - TensorFlow를 활용한 분산 데이터를 사용한 머신러닝 설계 및 구현
    - 구글코랩을 활용한 ML(DL) 설계 및 구현
    - Supervised, Unsupervised, Reinforcement, Deep Learning을 기반으로한 학습모델 및 예측모델 설계 및 구현





## 3. 개발 스펙
### (1) OS 환경
- OS환경 Linux, Window

### (2) Python 3.6.7

### (3) 사용 라이브러리 
- opencv, kivy , pygame, PIL, speech_recognition, pyaudio, pyglet 


## 4. 담당업무
    ● Tkinter를 이용하여 로봇 화면 초기버전 구현
    Tkinter를 활용하여 로봇 화면 초기디자인을 완성하였습니다. 로봇 화면의 프론트앤드 개발을 하여 계획적인 개발이 가능하도록 하였습니다. 
    
    ![dd](C:/Users/w/Desktop/dd/dd.jpg)

    ● Python과 kivy를 이용해 로봇 디스플레이화면 기획 및 개발
    Kivy는 프론트앤드 개발전문 Python 라이브러리입니다. Kivy를 이용하여 로봇 화면의 UI 및 UX를 설계하고 구현하였습니다. 노래듣기, 사진촬영, 기본적인볼륨제어, 음성 및 사진을 저장하고 전송하는 기능 등을 구현 했습니다.또한 폭포수 모델이 아닌 애자일 모델로 설계하여 컴포넌트별로 구현이 가능합니다. 컴포넌트란 독립적인 단위 모델로, 팀원들과 파트를 분담하여 개발한 뒤, 마지막으로 완성도를 높이며 합쳤습니다. 

    ● 팽수 로봇이 실시간으로 음성을 저장하고 판단하는(‘사람 살려’, ‘구해줘’ 등 응급상황이나 아이들과 말동무) 기능을 하는 백앤드 부분을 담당했으며, 로봇의 임베디드 부분, 하드웨어 부분을 담당 했습니다.