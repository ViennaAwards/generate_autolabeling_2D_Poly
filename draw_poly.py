from turtle import *
import cv2
import math
import numpy as np
#import matplotlib.pyplot as plt
from random import *
import os
#import numpy as np
import svgwrite
from svg_turtle import SvgTurtle
import cairosvg
from PIL import Image

shape('turtle')
hideturtle()
colormode(255)
Screen().bgcolor((102,102,102))
color('white')
radius = 0
speed(0)
min_x = 0.0
max_x = 0.0
min_y = 0.0
max_y = 0.0
center_x = 0.0
center_y = 0.0
xline = 0.0
yline = 0.0
def init_setting(initcolor,xpos,ypos,hex_number):
        global min_x,max_x,min_y,max_y
        color(initcolor)
        setpos(xpos,ypos)
        color(hex_number)
        min_x = xpos
        min_y = ypos
        max_x = xpos
        max_y = ypos

def findmin_max(xcor,ycor):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        if(xcor<min_x):
                min_x=xcor
        elif(xcor>max_x):
                max_x=xcor
        if(ycor<min_y):
                min_y=ycor
        elif(ycor>max_y):
                max_y=ycor
def draw_circle(radius):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        x = xcor()
        y = ycor()
        begin_fill()
        color(hex_number)
        circle(radius)
        end_fill()
        center_x = round((x+450)/900,6)
        center_y = 1-round(((y+300)+radius)/600,6)
        xline = round((radius*2*1.10)/900,6)
        yline = round((radius*2*1.10)/600,6)
        
def foursquare(side):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        init_setting('#666666',-200,-260,hex_number)

        begin_fill()
        color(hex_number)
        
        for i in range(4):
                forward(side)
                findmin_max(xcor(),ycor())
                left(90)
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)


def oblong(row,colunm):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        init_setting('#666666',-200,-260,hex_number)
        
        
        begin_fill()
        color(hex_number)
        for i in range(2):
                forward(row)
                findmin_max(xcor(),ycor())
                left(90)
                forward(colunm)
                findmin_max(xcor(),ycor())
                left(90)
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)

def rectangle(cross,radiusone,radiustwo,firstline,secondline):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        init_setting('#666666',-200,-260,hex_number)
        
        a = math.sqrt(math.pow(firstline*math.sin(math.pi*(radiusone/180)),2)+math.pow(cross-(firstline*math.cos(math.pi*(radiusone/180))),2))
        b = math.sqrt(math.pow(secondline*math.sin(math.pi*(radiustwo/180)),2)+math.pow(cross-(secondline*math.cos(math.pi*(radiustwo/180))),2))
        x = 57.295779513082323*math.acos((math.pow(a,2)+math.pow(firstline,2)-math.pow(cross,2))/(2*a*firstline))
        y1 = 57.295779513082323*math.acos((math.pow(a,2)+math.pow(cross,2)-math.pow(firstline,2))/(2*a*cross))
        y2 = 57.295779513082323*math.acos((math.pow(b,2)+math.pow(cross,2)-math.pow(secondline,2))/(2*b*cross))
        
        begin_fill()
        color(hex_number)
        forward(firstline)
        findmin_max(xcor(),ycor())
        left(180-x)
        forward(a)
        findmin_max(xcor(),ycor())
        left(180-(y1+y2))
        forward(b)
        findmin_max(xcor(),ycor())
        left(180-(360-radiusone-radiustwo-x-y1-y2))
        forward(secondline)
        findmin_max(xcor(),ycor())
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)

def trapezoid(radiusone,radiustwo,height):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        a = height/(math.sin(math.pi*(radiusone/180)))
        b = height/(math.sin(math.pi*(radiustwo/180)))
        bottoma = math.sqrt(math.pow(a,2)-math.pow(height,2))
        bottomb = math.sqrt(math.pow(b,2)-math.pow(height,2))
        bottomline = bottoma+bottomb+height
        x = 180-90-radiusone
        y = 180-90-radiustwo
        
        begin_fill()
        color(hex_number)
        forward(bottomline)
        findmin_max(xcor(),ycor())
        left(180-radiustwo)
        forward(b)
        findmin_max(xcor(),ycor())
        left(180-(y+90))
        forward(height)
        findmin_max(xcor(),ycor())
        left(180-(x+90))
        forward(a)
        findmin_max(xcor(),ycor())
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)
        
def parallelogram(lineone,linetwo,radiusone):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        begin_fill()
        color(hex_number)
        forward(lineone)
        findmin_max(xcor(),ycor())
        left(180-radiusone)
        forward(linetwo)
        findmin_max(xcor(),ycor())
        left(180-(180-radiusone))
        forward(lineone)
        findmin_max(xcor(),ycor())
        left(180-radiusone)
        forward(linetwo)
        findmin_max(xcor(),ycor())
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)
        
def equilateral_triangle(side):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        begin_fill()
        color(hex_number)
        for i in range(3):
                forward(side)
                findmin_max(xcor(),ycor())
                left(120)
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)

def right_triangle(underside,height):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        begin_fill()
        color(hex_number)
        forward(underside)
        findmin_max(xcor(),ycor())
        left(90)
        forward(height)
        findmin_max(xcor(),ycor())
        left(180-(57.295779513082323*math.atan(underside/height)))
        forward(math.sqrt((underside*underside)+(height*height)))
        findmin_max(xcor(),ycor())
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)


def isosceles_triangle(pointangle,underside):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        begin_fill()
        color(hex_number)
        forward(underside)
        findmin_max(xcor(),ycor())
        left(180-(180-((pointangle/2)+90)))
        forward((underside/2)/math.sin(math.pi*((pointangle/2)/180)))
        findmin_max(xcor(),ycor())
        left(180-pointangle)
        forward((underside/2)/math.sin(math.pi*((pointangle/2)/180)))
        findmin_max(xcor(),ycor())
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)

def triangle(angle,underside,otherside):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        begin_fill()
        color(hex_number)
        forward(underside)
        findmin_max(xcor(),ycor())
        left(180-angle)
        forward(otherside)
        findmin_max(xcor(),ycor())
        a = underside
        b = otherside
        c = math.sqrt(math.pow(otherside*math.sin(math.pi*(angle/180)),2)+math.pow((underside-(otherside*math.cos(math.pi*(angle/180)))),2))
        left(180-57.295779513082323*math.acos((b*b+c*c-a*a)/(2*b*c)))
        findmin_max(xcor(),ycor())
        end_fill()
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)

def pentagon(centerradiusone,centerradiustwo,centerradiusthree,centerradiusfour,crossline):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        a = centerradiusone/57.295779513082323
        pentagon_lineone = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusone/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusone/180)))),2))
        tempradiusone = 57.295779513082323*math.acos((crossline*crossline+pentagon_lineone*pentagon_lineone-crossline*crossline)/(2*crossline*pentagon_lineone))
        tempradiustwo =  180-tempradiusone-centerradiusone

        b = centerradiustwo/57.295779513082323
        pentagon_linetwo = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiustwo/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiustwo/180)))),2))
        tempradiusthree = 57.295779513082323*math.acos((crossline*crossline+pentagon_linetwo*pentagon_linetwo-crossline*crossline)/(2*crossline*pentagon_linetwo))
        tempradiusfour =  180-tempradiusthree-centerradiustwo

        c = centerradiusthree/57.295779513082323
        pentagon_linethree = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusthree/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusthree/180)))),2))
        tempradiusfive = 57.295779513082323*math.acos((crossline*crossline+pentagon_linethree*pentagon_linethree-crossline*crossline)/(2*crossline*pentagon_linethree))
        tempradiussix =  180-tempradiusfive-centerradiusthree

        d = centerradiusfour/57.295779513082323
        pentagon_linefour = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusfour/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusfour/180)))),2))
        tempradiusseven = 57.295779513082323*math.acos((crossline*crossline+pentagon_linefour*pentagon_linefour-crossline*crossline)/(2*crossline*pentagon_linefour))
        tempradiuseight =  180-tempradiusseven-centerradiusfour

        centerradiusfive = 360-centerradiusone-centerradiustwo-centerradiusthree-centerradiusfour
        e = (360-centerradiusone-centerradiustwo-centerradiusthree-centerradiusfour)/57.295779513082323
        pentagon_linefive = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusfive/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusfive/180)))),2))
        tempradiusnine = 57.295779513082323*math.acos((crossline*crossline+pentagon_linefive*pentagon_linefive-crossline*crossline)/(2*crossline*pentagon_linefive))
        tempradiusten =  180-tempradiusnine-centerradiusfive
        pentagonradiusone = tempradiustwo+tempradiusthree
        pentagonradiustwo = tempradiusfour+tempradiusfive
        pentagonradiusthree = tempradiussix+tempradiusseven
        pentagonradiusfour = tempradiuseight+tempradiusnine
        pentagonradiusfive = tempradiusten+tempradiusone
        begin_fill()
        color(hex_number)
        forward(pentagon_lineone)
        findmin_max(xcor(),ycor())
        left(180-pentagonradiusone)
        forward(pentagon_linetwo)
        findmin_max(xcor(),ycor())
        left(180-pentagonradiustwo)
        forward(pentagon_linethree)
        findmin_max(xcor(),ycor())
        left(180-pentagonradiusthree)
        forward(pentagon_linefour)
        findmin_max(xcor(),ycor())
        left(180-pentagonradiusfour)
        forward(pentagon_linefive)
        findmin_max(xcor(),ycor())
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)
        left(180-pentagonradiusfive)
        end_fill()

def hexagon(centerradiusone,centerradiustwo,centerradiusthree,centerradiusfour,centerradiusfive,crossline):
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        r = lambda : randint(0,255)
        hex_number = ('#%02X%02X%02X' % (r(),r(),r()))
        
        init_setting('#666666',-200,-260,hex_number)
        
        a = centerradiusone/57.295779513082323
        hexagon_lineone = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusone/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusone/180)))),2))
        tempradiusone = 57.295779513082323*math.acos((crossline*crossline+hexagon_lineone*hexagon_lineone-crossline*crossline)/(2*crossline*hexagon_lineone))
        tempradiustwo =  180-tempradiusone-centerradiusone

        b = centerradiustwo/57.295779513082323
        hexagon_linetwo = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiustwo/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiustwo/180)))),2))
        tempradiusthree = 57.295779513082323*math.acos((crossline*crossline+hexagon_linetwo*hexagon_linetwo-crossline*crossline)/(2*crossline*hexagon_linetwo))
        tempradiusfour =  180-tempradiusthree-centerradiustwo

        c = centerradiusthree/57.295779513082323
        hexagon_linethree = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusthree/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusthree/180)))),2))
        tempradiusfive = 57.295779513082323*math.acos((crossline*crossline+hexagon_linethree*hexagon_linethree-crossline*crossline)/(2*crossline*hexagon_linethree))
        tempradiussix =  180-tempradiusfive-centerradiusthree

        d = centerradiusfour/57.295779513082323
        hexagon_linefour = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusfour/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusfour/180)))),2))
        tempradiusseven = 57.295779513082323*math.acos((crossline*crossline+hexagon_linefour*hexagon_linefour-crossline*crossline)/(2*crossline*hexagon_linefour))
        tempradiuseight =  180-tempradiusseven-centerradiusfour

        e = centerradiusfive/57.295779513082323
        hexagon_lineffive = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiusfive/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiusfive/180)))),2))
        tempradiusnine = 57.295779513082323*math.acos((crossline*crossline+hexagon_lineffive*hexagon_lineffive-crossline*crossline)/(2*crossline*hexagon_lineffive))
        tempradiusten =  180-tempradiusnine-centerradiusfive

        centerradiussix = 360-centerradiusone-centerradiustwo-centerradiusthree-centerradiusfour-centerradiusfive
        f = centerradiussix/57.295779513082323
        hexagon_linesix = math.sqrt(math.pow(crossline*(math.sin(math.pi*(centerradiussix/180))),2)+math.pow((crossline-(crossline*math.cos(math.pi*(centerradiussix/180)))),2))
        tempradiuseleven = 57.295779513082323*math.acos((crossline*crossline+hexagon_linesix*hexagon_linesix-crossline*crossline)/(2*crossline*hexagon_linesix))
        tempradiustwelve =  180-tempradiuseleven-centerradiussix

        hexagonradiusone = tempradiustwo+tempradiusthree
        hexagonradiustwo = tempradiusfour+tempradiusfive
        hexagonradiusthree = tempradiussix+tempradiusseven
        hexagonradiusfour = tempradiuseight+tempradiusnine
        hexagonradiusfive = tempradiusten+tempradiuseleven
        hexagonradiussix = tempradiustwelve+tempradiusone
        if(centerradiussix>=180.0):
                print("???")
        begin_fill()
        color(hex_number)
        forward(hexagon_lineone)
        findmin_max(xcor(),ycor())
        left(180-hexagonradiusone)
        forward(hexagon_linetwo)
        findmin_max(xcor(),ycor())
        left(180-hexagonradiustwo)
        forward(hexagon_linethree)
        findmin_max(xcor(),ycor())
        left(180-hexagonradiusthree)
        forward(hexagon_linefour)
        findmin_max(xcor(),ycor())
        left(180-hexagonradiusfour)
        forward(hexagon_lineffive)
        findmin_max(xcor(),ycor())
        left(180-hexagonradiusfive)
        forward(hexagon_linesix)
        findmin_max(xcor(),ycor())
        center_x = round(((min_x+450+max_x+450)/2)/900,6)
        center_y =1-(round(((min_y+300+max_y+300)/2)/600,6))
        xline = round((max_x-min_x)/900*1.10,6)
        yline = round((max_y-min_y)/600*1.10,6)
        left(180-hexagonradiussix)
        end_fill()
        
def write_file(filename, size):
        global gray
        drawing = svgwrite.Drawing(filename, size=size)
        drawing.add(drawing.rect(fill='#666666', size=("100%", "100%")))
        t = SvgTurtle(drawing)
        Turtle._screen = t.screen
        Turtle._pen = t
        #foursquare(정사각형) class_num=0
        '''
        side = uniform(50.0,400.0)
        foursquare(side)
        '''
        #oblong(직사각형) class_num=1
        '''
        row = uniform(50.0,400.0)
        colunm = uniform(50.0,300.0)
        if(row*0.95<colunm and colunm<row*1.05):
                colunm = colunm *1.5
        
        elif(colunm*0.95<row and row<colunm*1.05):
                row = row *1.5
        oblong(row,colunm)
        '''
        #rectangle(사각형) class_num=2
        '''
        cross = uniform(30.0,200.0)
        radiusone = uniform(30.0,90.0)
        radiustwo = uniform(30.0,90.0)
        lineone = uniform(30.0,400.0)
        linetwo = uniform(30.0,300.0)
        rectangle(cross,radiusone,radiustwo,lineone,linetwo)
        '''
        #trapezoid(사다리꼴) class_num=3
        '''
        radiusone = uniform(10.0,80.0)
        radiustwo = uniform(10.0,80.0)
        height = uniform(30.0,250.0)
        trapezoid(radiusone,radiustwo,height)
        '''
        #parallelogram(평행사변형) class_num=4
        '''
        lineone = uniform(50.0,400.0)
        linetwo = uniform(50.0,400.0)
        radiusone = uniform(10.0,150.0)
        parallelogram(lineone,linetwo,radiusone)
        '''
        #equilateral_triangle(정삼각형) class_num=5
        '''
        side = uniform(200.0,400.0)
        equilateral_triangle(side)
        '''
        #right_triangle(직삼각형) class_num=6
        '''
        underside = uniform(50.0,500.0)
        height = uniform(50.0,400.0)
        right_triangle(underside,height)
        '''
        #isosceles_triangle(이등변삼각형) class_num=7
        '''
        pointangle = uniform(30.0,150.0)
        underside = uniform(100.0,600.0)
        isosceles_triangle(pointangle,underside)
        '''
        #triangle(삼각형) class_num=8
        '''
        angle = uniform(30.0,150.0)
        underside = uniform(50.0,500.0)
        otherside = uniform(50.0,400.0)
        triangle(angle,underside,otherside)
        '''
        #pentagon(오각형) class_num=9
        '''
        total_radius = 360.0
        centerradiusone = uniform(10.0,90.0)
        centerradiustwo = uniform(10.0,90.0)
        centerradiusthree = uniform(10.0,90.0)
        centerradiusfour = uniform(10.0,90.0)
        if total_radius <= centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour :
                centerradiusfour = centerradiusfour/2.0
        elif 170 <= centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour <= 190:
                centerradiusone = centerradiusone-10.0
                centerradiustwo = centerradiustwo-10.0
                centerradiusthree = centerradiusthree-10.0
                centerradiusfour = centerradiusfour-10.0
        elif 40.0<=centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour<=45.0:
                centerradiusone = centerradiusone*5.0
                centerradiustwo = centerradiustwo*5.0
                centerradiusthree = centerradiusthree*5.0
                centerradiusfour = centerradiusfour*5.0
        elif 45.0<centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour<=60.0:
                centerradiusone = centerradiusone*4.0
                centerradiustwo = centerradiustwo*4.0
                centerradiusthree = centerradiusthree*4.0
                centerradiusfour = centerradiusfour*4.0
        elif 60.0<centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour<=90.0:
                centerradiusone = centerradiusone*3.0
                centerradiustwo = centerradiustwo*3.0
                centerradiusthree = centerradiusthree*3.0
                centerradiusfour = centerradiusfour*3.0
        elif 90.0<centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour<180.0:
                centerradiusone = centerradiusone*2.0
                centerradiustwo = centerradiustwo*2.0
                centerradiusthree = centerradiusthree*2.0
                centerradiusfour = centerradiusfour*2.0
        crossline = uniform(90.0,300.0)
        pentagon(centerradiusone,centerradiustwo,centerradiusthree,centerradiusfour,crossline)
        '''
        #hexagon(육각형) class_num=10
        '''
        total_radius = 360.0
        centerradiusone = uniform(10.0,72.0)
        centerradiustwo = uniform(10.0,72.0)
        centerradiusthree = uniform(10.0,72.0)
        centerradiusfour = uniform(10.0,72.0)
        centerradiusfive = uniform(10.0,72.0)
        if total_radius <= centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive :
                centerradiusfive = centerradiusfive/2.0
        
        elif 170 <= centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour <= 190:
                centerradiusone = centerradiusone-10.0
                centerradiustwo = centerradiustwo-10.0
                centerradiusthree = centerradiusthree-10.0
                centerradiusfour = centerradiusfour-10.0
                centerradiusfive = centerradiusfive-10.0
                
        elif 45.0<centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive<=60.0:
                centerradiusone = centerradiusone*4.0
                centerradiustwo = centerradiustwo*4.0
                centerradiusthree = centerradiusthree*4.0
                centerradiusfour = centerradiusfour*4.0
                centerradiusfive = centerradiusfive*4.0
        elif 60.0<centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive<=90.0:
                centerradiusone = centerradiusone*3.0
                centerradiustwo = centerradiustwo*3.0
                centerradiusthree = centerradiusthree*3.0
                centerradiusfour = centerradiusfour*3.0
                centerradiusfive = centerradiusfive*3.0
        elif 90.0<centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive and centerradiusone+centerradiustwo+centerradiusthree+centerradiusfour+centerradiusfive<180.0:
                centerradiusone = centerradiusone*2.0
                centerradiustwo = centerradiustwo*2.0
                centerradiusthree = centerradiusthree*2.0
                centerradiusfour = centerradiusfour*2.0
                centerradiusfive = centerradiusfive*2.0
                
        crossline = uniform(90.0,300.0)
        hexagon(centerradiusone,centerradiustwo,centerradiusthree,centerradiusfour,centerradiusfive,crossline)
        '''
        #circle(원) class_num = 11
        radius = uniform(50.0,250.0)
        draw_circle(radius)
        
        drawing.save()

def generator():
        global min_x,max_x,min_y,max_y,center_x,center_y,xline,yline
        for i in range(600):
                center_x = 0
                center_y = 0
                xline = 0
                yline = 0
                min_x=0
                max_x=0
                min_y=0
                max_y=0
                write_file(r'C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_'+str(i)+'.svg',size=("900px","600px"))
                
                area = ((450+min_x),(300-max_y),(max_x-min_x+450+min_x),(max_y-min_y+300-max_y))
                print(area)
                
                cairosvg.svg2png(url=r"C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_"+str(i)+".svg", write_to=r"C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_"+str(i)+".jpg", dpi = 100)
                img = Image.open(r"C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_"+str(i)+".jpg")
                os.remove(r'C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_'+str(i)+'.svg')
                #try:
                #        crop_image = img.crop(area)
                #        #img.show(crop_image)
                #        crop_image.save(r"C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_"+str(i)+".jpg")
                #except:
                #        os.remove(r'C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_'+str(i)+'.jpg')
                #        continue
                #finally:
                #        os.remove(r'C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_'+str(i)+'.svg')
                if (300-max_y)<0 or ((max_x-min_x+450+min_x)-(450+min_x))>700 or (450+min_x)<0:
                        print("out of bound")
                        os.remove(r'C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\circle\11_'+str(i)+'.jpg')
                        continue
                #f = open(r"C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\5_"+str(i)+".txt", 'w')
                #f.write("5 ")
                #f.write(str(center_x)+' ')
                #f.write(str(center_y)+' ')
                #f.write(str(xline)+' ')
                #f.write(str(yline))
                #f.close()
generator()
#foursquare(100)
#rectangle(80,60,40,50,60)
#oblong(100,200)
#equilateral_triangle(50)
#right_triangle(400,400)
#isosceles_triangle(50,100)
#triangle(100,400,50)
#rectangle(80,60,40,50,60)
#trapezoid(80,60,200)
#parallelogram(50,100,50)
#draw_ellipse(192,192,100,50)
#pentagon(72,72,72,72,72,100)
#hexagon(90,70,80,50,50,100)

#img = Image.open(r"C:\Users\Bouls\Desktop\background_delete_2D_Test_Image\hexagon\10_"+str(1)+".jpg")
#if img.size[0]>img.size[1]:
#        size = img.size[0]
#elif img.size[0]<img.size[1]:
#        size = img.size[1]
#else:
#        size = img.size[0]
#crop_image = img.crop((-10,-10,size*1.2,size*1.2))
#img.show(crop_image)
#crop_image.save('Test.png')
