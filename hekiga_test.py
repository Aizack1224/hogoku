#hekiga_test ver.1.0

import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(200,200,fps=60)
        pyxel.cls(11)
        pyxel.load("hekiga.pyxres")
        self.frame_count = 0
        self.framenow = 0
        self.flag1 =0
        self.cur=0
        self.ene1 = 0
        self.ene2 = 0
        self.scene = 0 #0選択 1表示
        pyxel.playm(0,loop=True)
        pyxel.run(self.update,self.draw)
        
    def update(self):
        
        
        self.frame_count +=1
        if self.scene == 0:
            self.update_title_scene()
        elif self.scene == 1:
            self.update_play_scene()

    def draw(self):
        if self.scene == 0:
            self.draw_title_scene()
        elif self.scene == 1:
            self.draw_play_scene()

    # エネ選択画面の処理
    def update_title_scene(self):#タイトル画面で実行する処理です
        if pyxel.btnp(pyxel.KEY_SPACE):#強制退場
            self.flag1=0
        if self.flag1 ==0:#待機画面
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.flag1 =1
                self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.flag1=1
                self.framenow = self.frame_count
        elif self.flag1 ==1:#エネルギー1を選択する
            if pyxel.btnp(pyxel.KEY_D):
                self.cur+=1
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.cur+=1
            elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.cur+=1
            if pyxel.btnp(pyxel.KEY_A):
                self.cur-=1
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.cur-=1
            elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.cur-=1
            if pyxel.btnp(pyxel.KEY_0):
                self.cur = 0
            elif pyxel.btnp(pyxel.KEY_1):
                self.cur = 1
            elif pyxel.btnp(pyxel.KEY_2):
                self.cur = 2
            elif pyxel.btnp(pyxel.KEY_3):
                self.cur = 3
            elif pyxel.btnp(pyxel.KEY_4):
                self.cur = 4
            elif pyxel.btnp(pyxel.KEY_5):
                self.cur = 5
            elif pyxel.btnp(pyxel.KEY_6):
                self.cur = 6
            elif pyxel.btnp(pyxel.KEY_7):
                self.cur = 7
            elif pyxel.btnp(pyxel.KEY_8):
                self.cur = 8
            elif pyxel.btnp(pyxel.KEY_9):
                self.cur = 9

            if self.cur <= 0:
                self.cur =0
            elif self.cur >= 9:
                self.cur = 9

            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 2
                    self.ene1 = self.cur
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                 if self.frame_count -self.framenow >= 10:
                    self.flag1=2
                    self.ene1 = self.cur
                    self.cur=0
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 0
                    self.cur = 0
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 0
                    self.cur = 0
                    self.framenow = self.frame_count
        elif self.flag1 ==2:#エネルギー2を選択する
            if pyxel.btnp(pyxel.KEY_D):
                self.cur+=1
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.cur+=1
            elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.cur+=1
            if pyxel.btnp(pyxel.KEY_A):
                self.cur-=1
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.cur-=1
            elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.cur-=1
            if pyxel.btnp(pyxel.KEY_0):
                self.cur = 0
            elif pyxel.btnp(pyxel.KEY_1):
                self.cur = 1
            elif pyxel.btnp(pyxel.KEY_2):
                self.cur = 2
            elif pyxel.btnp(pyxel.KEY_3):
                self.cur = 3
            elif pyxel.btnp(pyxel.KEY_4):
                self.cur = 4
            elif pyxel.btnp(pyxel.KEY_5):
                self.cur = 5
            elif pyxel.btnp(pyxel.KEY_6):
                self.cur = 6
            elif pyxel.btnp(pyxel.KEY_9):
                self.cur = 9

            if self.cur <= 0:
                self.cur =0
            elif self.cur >= 9:
                self.cur = 9

            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.frame_count -self.framenow >= 10:
                    
                    self.ene2 = self.cur
                    self.cur=0
                    self.flag1 = 3
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                 if self.frame_count -self.framenow >= 10:
                    self.ene2 = self.cur
                    self.cur=0
                    self.flag1=3
                    self.framenow = self.frame_count
            
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 1
                    self.cur = 0
                    self.framenow = self.frame_count
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                if self.frame_count -self.framenow >= 10:
                    self.flag1 = 1
                    self.cur = 0
                    self.framenow = self.frame_count
        elif self.flag1 ==3:#確認画面
            if pyxel.btn(pyxel.KEY_D):
                self.cur=1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.cur=1
            elif pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.cur=1
            if pyxel.btn(pyxel.KEY_A):
                self.cur=0
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.cur=0
            elif pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.cur=0
            if self.cur ==0:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 0
                        self.framenow = self.frame_count
                        self.scene = 1
                elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 0
                        self.framenow = self.frame_count
                        self.scene = 1
            elif self.cur ==1:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 1
                        self.cur = 0
                        self.framenow = self.frame_count
                if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                    if self.frame_count -self.framenow >= 10:
                        self.flag1 = 1
                        self.cur = 0
                        self.framenow = self.frame_count

    # エネ選択画面の描画
    def draw_title_scene(self):
        #タイトル画面を表示しているときの表示です
        pyxel.cls(11)
        if self.flag1 ==0:
            pyxel.text(70, 150,"GENERATION GAME",7)
            pyxel.text(65, 160,"Choose Two Energies",7)
            pyxel.text(30, 170,"The environment changes as you choose!",7)
            pyxel.text(87, 140,"--ENTER--",7)
        elif self.flag1 ==1:
            pyxel.text(75, 150,"ENEGEY? (1)",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
            pyxel.text(52, 170,"0",7)
            pyxel.text(62, 170,"1",7)
            pyxel.text(72, 170,"2",7)
            pyxel.text(82, 170,"3",7)
            pyxel.text(92, 170,"4",7)
            pyxel.text(102, 170,"5",7)
            pyxel.text(112, 170,"6",7)
            pyxel.text(122, 170,"7",7)
            pyxel.text(132, 170,"8",7)
            pyxel.text(142, 170,"9",7)
            pyxel.trib(53+self.cur*10,177,51+self.cur*10,181,55+self.cur*10,181,1)
            pyxel.blt(50, 160,0,0,80,8,8,6)
            pyxel.blt(60, 160,0,8,80,8,8,6)
            pyxel.blt(70, 160,0,0,88,8,8,6)
            pyxel.blt(80, 160,0,8,88,8,8,6)
            pyxel.blt(90, 160,0,0,96,8,8,6)
            pyxel.blt(100, 160,0,8,96,8,8,6)
            pyxel.blt(110, 160,0,0,104,8,8,6)
            pyxel.blt(120, 160,0,8,104,8,8,6)
            pyxel.blt(130, 160,0,0,112,8,8,6)
            pyxel.blt(140, 160,0,8,112,8,8,6)
        elif self.flag1 ==2:
            pyxel.text(75, 150,"ENEGEY? (2)",7)
            pyxel.text(75, 190,"ENTER to NEXT",7)
            pyxel.text(75, 140,"ENE1 = ",7)
            if self.ene1 ==0:
                pyxel.blt(100, 138,0,0,80,8,8,6)
            elif self.ene1 ==1:
                pyxel.blt(100, 138,0,8,80,8,8,6)
            elif self.ene1 ==2:
                pyxel.blt(100, 138,0,0,88,8,8,6)
            elif self.ene1 ==3:
                pyxel.blt(100, 138,0,8,88,8,8,6)
            elif self.ene1 ==4:
                pyxel.blt(100, 138,0,0,96,8,8,6)
            elif self.ene1 ==5:
                pyxel.blt(100, 138,0,8,96,8,8,6)
            elif self.ene1 ==6:
                pyxel.blt(100, 138,0,0,104,8,8,6)
            elif self.ene1 ==7:
                pyxel.blt(100, 138,0,8,104,8,8,6)
            elif self.ene1 ==8:
                pyxel.blt(100, 138,0,0,112,8,8,6)
            elif self.ene1 ==9:
                pyxel.blt(100, 138,0,8,112,8,8,6)
            pyxel.text(52, 170,"0",7)
            pyxel.text(62, 170,"1",7)
            pyxel.text(72, 170,"2",7)
            pyxel.text(82, 170,"3",7)
            pyxel.text(92, 170,"4",7)
            pyxel.text(102, 170,"5",7)
            pyxel.text(112, 170,"6",7)
            pyxel.text(122, 170,"7",7)
            pyxel.text(132, 170,"8",7)
            pyxel.text(142, 170,"9",7)
            pyxel.trib(53+self.cur*10,177,51+self.cur*10,181,55+self.cur*10,181,1)
            pyxel.blt(50, 160,0,0,80,8,8,6)
            pyxel.blt(60, 160,0,8,80,8,8,6)
            pyxel.blt(70, 160,0,0,88,8,8,6)
            pyxel.blt(80, 160,0,8,88,8,8,6)
            pyxel.blt(90, 160,0,0,96,8,8,6)
            pyxel.blt(100, 160,0,8,96,8,8,6)
            pyxel.blt(110, 160,0,0,104,8,8,6)
            pyxel.blt(120, 160,0,8,104,8,8,6)
            pyxel.blt(130, 160,0,0,112,8,8,6)
            pyxel.blt(140, 160,0,8,112,8,8,6)
        elif self.flag1 ==3:
            pyxel.text(75, 140,"ENE1 = ",7)
            if self.ene1 ==0:
                pyxel.blt(100, 138,0,0,80,8,8,6)
            elif self.ene1 ==1:
                pyxel.blt(100, 138,0,8,80,8,8,6)
            elif self.ene1 ==2:
                pyxel.blt(100, 138,0,0,88,8,8,6)
            elif self.ene1 ==3:
                pyxel.blt(100, 138,0,8,88,8,8,6)
            elif self.ene1 ==4:
                pyxel.blt(100, 138,0,0,96,8,8,6)
            elif self.ene1 ==5:
                pyxel.blt(100, 138,0,8,96,8,8,6)
            elif self.ene1 ==6:
                pyxel.blt(100, 138,0,0,104,8,8,6)
            elif self.ene1 ==7:
                pyxel.blt(100, 138,0,8,104,8,8,6)
            elif self.ene1 ==8:
                pyxel.blt(100, 138,0,0,112,8,8,6)
            elif self.ene1 ==9:
                pyxel.blt(100, 138,0,8,112,8,8,6)
            pyxel.text(75, 150,"ENE2 = ",7)
            if self.ene2 ==0:
                pyxel.blt(100, 148,0,0,80,8,8,6)
            elif self.ene2 ==1:
                pyxel.blt(100, 148,0,8,80,8,8,6)
            elif self.ene2 ==2:
                pyxel.blt(100, 148,0,0,88,8,8,6)
            elif self.ene2 ==3:
                pyxel.blt(100, 148,0,8,88,8,8,6)
            elif self.ene2 ==4:
                pyxel.blt(100, 148,0,0,96,8,8,6)
            elif self.ene2 ==5:
                pyxel.blt(100, 148,0,8,96,8,8,6)
            elif self.ene2 ==6:
                pyxel.blt(100, 148,0,0,104,8,8,6)
            elif self.ene2 ==7:
                pyxel.blt(100, 148,0,8,104,8,8,6)
            elif self.ene2 ==8:
                pyxel.blt(100, 148,0,0,112,8,8,6)
            elif self.ene2 ==9:
                pyxel.blt(100, 148,0,8,112,8,8,6)

            pyxel.text(60, 130,"Right?",7)
            pyxel.text(70, 170, "YES",7)
            pyxel.text(110, 170, "NO",7)
            if self.cur ==0:
                pyxel.trib(73,177,71,181,75,181,1)
            elif self.cur ==1:
                pyxel.trib(113,177,111,181,115,181,1)


    #表示画面について
    def update_play_scene(self):
        #エンター押したら帰るだけ
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.frame_count -self.framenow >= 10:
                self.flag1 = 0
                self.ene1 = 0
                self.ene2 =0
                self.cur =0
                self.framenow = self.frame_count
                self.scene = 0
        elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            if self.frame_count -self.framenow >= 10:
                self.flag1 = 0
                self.ene1 = 0
                self.ene2 =0
                self.cur =0
                self.framenow = self.frame_count
                self.scene = 0

    #表示画面の描画
    def draw_play_scene(self):
        pyxel.cls(11)
        if self.ene1 ==0:#炎
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"HITOKAGE",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"BORUKENION",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"RESHIZEKU",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"KAPUSAIJI NO SHINKA",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"MAFOKUSHI-",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"HERUGA-",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"HI-DORAN",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"RESHIRAM",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"KAENJISHI",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"BASHA-MO",7)

        elif self.ene1 ==1:#水
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"BORUKENION",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"ZENIGAME",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"CHONCHI-",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"RUNPAPPA",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"MARIRU",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"GEKKOUGA",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"EMPERUTO",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"PARUKIA",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"PERIPPA-",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"U-RAOSU",7)

        elif self.ene1 ==2:#雷
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"HI-TO ROTOM",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"MIZU ROTOM",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"PIKACHU",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"KATTO ROTOM",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"ROTOM",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"MORUPEKO",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"KOIRU",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"ZEKUROM",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"KAIDEN",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"PA-MOTTO",7)

        elif self.ene1 ==3:#草
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"KAPUSAIJI NO SHINKA",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"RUNPAPPA",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"KATTO ROTOM",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"FUSHIGIDANE",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"DADARIN",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"FUSHIGIBANA",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"KAMITURUGI",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"MEGA JYUKAIN",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"TOROPIUS",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"DODAITOSU",7)

        elif self.ene1 ==4:#超
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"SHANDERA",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"KAPU REHIRE",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"KAPU KOKEKO",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"BADOREKKUSU",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"RIGURE-",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"E-FI TO BURAKKI-",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"GIRUGARUDO",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"GIRATENA",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"RUGIA",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"MA-SHADO-",7)

        elif self.ene1 ==5:#悪
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"HERUGA-",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"GEKKOUGA",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"MORUPEKO",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"MASUKA-NYA",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"GENGA-",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"ZOROA",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"KIRIKIZAN",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"SAZANDORA",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"DONKARASU",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"ZURUZUKIN",7)

        elif self.ene1 ==6:#鋼
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"HI-DORAN",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"ALO-RA SANDO",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"TOGEDEMARU",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"NATTOREI",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"ZASHIAN",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"DODOGEZAN",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"MIMIZUZU",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"JYURARUDON",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"A-MA-GAA",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"ZAMAZENTA",7)
        elif self.ene1 ==7:#龍
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"UGATU-HOMURA",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"SEGUREIBU",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"MIRAIDON",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"KAMICYU",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"DORAPARUTO",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"MUGENDAINA",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"BURIJYURASU",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"REJI-DORAGO",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"JIJI-RON",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"KORAIDON",7)
        elif self.ene1 ==8:#無
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"SHISHIKO",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"PERIPPA-",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"TAIKAIDEN",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"SHIKIJIKA",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"PURIN",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"TAGINGURU",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"EA-MUDO",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"KAIRYU-",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"NYA-SU",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"A-KEOSU",7)
        elif self.ene1 ==9:#闘
            if self.ene2 ==0:#炎
                pyxel.text(70, 150,"BASYA-MO",7)
            elif self.ene2 ==1:#水
                pyxel.text(70, 150,"TORITODON",7)
            elif self.ene2 ==2:#雷
                pyxel.text(70, 150,"TETUNO IBARA",7)
            elif self.ene2 ==3:#草
                pyxel.text(70, 150,"ISHIZUE O-GAPON",7)
            elif self.ene2 ==4:#超
                pyxel.text(70, 150,"GORU-GU",7)
            elif self.ene2 ==5:#悪
                pyxel.text(70, 150,"DOOH-",7)
            elif self.ene2 ==6:#鋼
                pyxel.text(70, 150,"DAINO-ZU",7)
            elif self.ene2 ==7:#ドラゴン
                pyxel.text(70, 150,"JYARAKO",7)
            elif self.ene2 ==8:#無
                pyxel.text(70, 150,"GACHIGUMA",7)
            elif self.ene2 ==9:#闘
                pyxel.text(70, 150,"YO-GIRASU",7)

App()