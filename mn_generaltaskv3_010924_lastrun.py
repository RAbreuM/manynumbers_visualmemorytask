#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Tue Jan  9 10:25:33 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_3
meanb1 = 0
# Run 'Before Experiment' code from code_42
beginning_exp = ''
timer = ''
timer_exp = ''
beginning_exp = ''
beginning_exp2 = ''


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'mn_generaltaskv3_010924'  # from the Builder filename that created this script
expInfo = {
    'Enter_Participant_ID': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Enter_Participant_ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/robertoabreu/Documents/indiana/manynumbers/mn_general_taskv_final_010924/mn_generaltaskv3_010924_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='hex',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "mng_welcome" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome!',
    font='Arial',
    pos=[0,0], height=0.155, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_instructions" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='I am going to show you some pictures. Then, you will point to the pictures you just saw.\n\nReady?',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_practice_counter" ---

# --- Initialize components for Routine "mng_blank" ---
blank_box = visual.TextStim(win=win, name='blank_box',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_probe_sample" ---
P1_sample = visual.ImageStim(
    win=win,
    name='P1_sample', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test_sample" ---
# Run 'Begin Experiment' code from code
incorr = 0
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
P1T_rectangle = visual.Rect(
    win=win, name='P1T_rectangle',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P2T_rectangle = visual.Rect(
    win=win, name='P2T_rectangle',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P1T = visual.ImageStim(
    win=win,
    name='P1T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
P2T = visual.ImageStim(
    win=win,
    name='P2T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
finish = visual.ShapeStim(
    win=win, name='finish',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# --- Initialize components for Routine "mng_feedback_practice_2" ---
text_28 = visual.TextStim(win=win, name='text_28',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from code_41
feedback_sound = ['kids_cheering.wav','crowdohh.wav']
feedback_image = ['happy.png','sad.png']
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "mng_check_practice" ---

# --- Initialize components for Routine "mng_repeat_instructions" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='Remember!\nPoint to the picture you just saw.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_ready" ---
key_resp_14 = keyboard.Keyboard()
text_24 = visual.TextStim(win=win, name='text_24',
    text='Ready?',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from code_31
acc_thr = 66

# --- Initialize components for Routine "mng_blank" ---
blank_box = visual.TextStim(win=win, name='blank_box',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_probe_1target" ---
P1_sample_2 = visual.ImageStim(
    win=win,
    name='P1_sample_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test_1target_2objects" ---
# Run 'Begin Experiment' code from code_3
incorr = 0
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
P2T_rectangle_1t = visual.Rect(
    win=win, name='P2T_rectangle_1t',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_1t = visual.Rect(
    win=win, name='P3T_rectangle_1t',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P1T_1t = visual.ImageStim(
    win=win,
    name='P1T_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
P2T_1t = visual.ImageStim(
    win=win,
    name='P2T_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
P3T_1t = visual.ImageStim(
    win=win,
    name='P3T_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
P4T_1t = visual.ImageStim(
    win=win,
    name='P4T_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P5T_1t = visual.ImageStim(
    win=win,
    name='P5T_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P6T_1t = visual.ImageStim(
    win=win,
    name='P6T_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P7t_1t = visual.ImageStim(
    win=win,
    name='P7t_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P8t_1t = visual.ImageStim(
    win=win,
    name='P8t_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P9t_1t = visual.ImageStim(
    win=win,
    name='P9t_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
finish_2 = visual.ShapeStim(
    win=win, name='finish_2',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-13.0, interpolate=True)

# --- Initialize components for Routine "mng_test_1target_3objects" ---
# Run 'Begin Experiment' code from code_7
incorr = 0
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
P1T_rectangle_1t_2 = visual.Rect(
    win=win, name='P1T_rectangle_1t_2',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P4T_rectangle_1t_2 = visual.Rect(
    win=win, name='P4T_rectangle_1t_2',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P5T_rectangle_1t_2 = visual.Rect(
    win=win, name='P5T_rectangle_1t_2',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P1T_1t_2 = visual.ImageStim(
    win=win,
    name='P1T_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
P2T_1t_2 = visual.ImageStim(
    win=win,
    name='P2T_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
P3T_1t_2 = visual.ImageStim(
    win=win,
    name='P3T_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P4T_1t_2 = visual.ImageStim(
    win=win,
    name='P4T_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P5T_1t_2 = visual.ImageStim(
    win=win,
    name='P5T_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P6T_1t_2 = visual.ImageStim(
    win=win,
    name='P6T_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P7t_1t_2 = visual.ImageStim(
    win=win,
    name='P7t_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P8t_1t_2 = visual.ImageStim(
    win=win,
    name='P8t_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P9t_1t_2 = visual.ImageStim(
    win=win,
    name='P9t_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
finish_3 = visual.ShapeStim(
    win=win, name='finish_3',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-14.0, interpolate=True)

# --- Initialize components for Routine "mng_test_1target_4objects" ---
# Run 'Begin Experiment' code from code_8
incorr = 0
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
P2T_rectangle_1t_3 = visual.Rect(
    win=win, name='P2T_rectangle_1t_3',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_1t_3 = visual.Rect(
    win=win, name='P3T_rectangle_1t_3',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_1t_3 = visual.Rect(
    win=win, name='P6T_rectangle_1t_3',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_1t_3 = visual.ShapeStim(
    win=win, name='P7T_rectangle_1t_3',
    size=(0.2, 0.2), vertices='triangle',
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P1T_1t_3 = visual.ImageStim(
    win=win,
    name='P1T_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
P2T_1t_3 = visual.ImageStim(
    win=win,
    name='P2T_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P3T_1t_3 = visual.ImageStim(
    win=win,
    name='P3T_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P4T_1t_3 = visual.ImageStim(
    win=win,
    name='P4T_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P5T_1t_3 = visual.ImageStim(
    win=win,
    name='P5T_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P6T_1t_3 = visual.ImageStim(
    win=win,
    name='P6T_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P7t_1t_3 = visual.ImageStim(
    win=win,
    name='P7t_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P8t_1t_3 = visual.ImageStim(
    win=win,
    name='P8t_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P9t_1t_3 = visual.ImageStim(
    win=win,
    name='P9t_1t_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
finish_4 = visual.ShapeStim(
    win=win, name='finish_4',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-15.0, interpolate=True)

# --- Initialize components for Routine "mng_test_1target_5objects" ---
# Run 'Begin Experiment' code from code_9
incorr = 0
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
P1T_rectangle_1t_4 = visual.Rect(
    win=win, name='P1T_rectangle_1t_4',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P4T_rectangle_1t_4 = visual.Rect(
    win=win, name='P4T_rectangle_1t_4',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P5T_rectangle_1t_4 = visual.Rect(
    win=win, name='P5T_rectangle_1t_4',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P8T_rectangle_1t_4 = visual.Rect(
    win=win, name='P8T_rectangle_1t_4',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.500, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P9T_rectangle_1t_4 = visual.Rect(
    win=win, name='P9T_rectangle_1t_4',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.500, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P1T_1t_4 = visual.ImageStim(
    win=win,
    name='P1T_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P2T_1t_4 = visual.ImageStim(
    win=win,
    name='P2T_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P3T_1t_4 = visual.ImageStim(
    win=win,
    name='P3T_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P4T_1t_4 = visual.ImageStim(
    win=win,
    name='P4T_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P5T_1t_4 = visual.ImageStim(
    win=win,
    name='P5T_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P6T_1t_4 = visual.ImageStim(
    win=win,
    name='P6T_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P7t_1t_4 = visual.ImageStim(
    win=win,
    name='P7t_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P8t_1t_4 = visual.ImageStim(
    win=win,
    name='P8t_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P9t_1t_4 = visual.ImageStim(
    win=win,
    name='P9t_1t_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
finish_5 = visual.ShapeStim(
    win=win, name='finish_5',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-16.0, interpolate=True)

# --- Initialize components for Routine "mng_instructions2" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text="Now, we are going to see more pictures.\nLet's practice!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_practice_counter_2" ---

# --- Initialize components for Routine "mng_blank_sample2" ---
blank_box_3 = visual.TextStim(win=win, name='blank_box_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_18 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_probe_sample2" ---
P2_sample2_2t = visual.ImageStim(
    win=win,
    name='P2_sample2_2t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
P3_sample2_2t = visual.ImageStim(
    win=win,
    name='P3_sample2_2t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_11 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test_sample2" ---
# Run 'Begin Experiment' code from code_19
incorr = 0
mouse_15 = event.Mouse(win=win)
x, y = [None, None]
mouse_15.mouseClock = core.Clock()
P2T_rectangle_2t_sample = visual.Rect(
    win=win, name='P2T_rectangle_2t_sample',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_2t_sample = visual.Rect(
    win=win, name='P3T_rectangle_2t_sample',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_2t_sample = visual.Rect(
    win=win, name='P6T_rectangle_2t_sample',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_2t_sample = visual.Rect(
    win=win, name='P7T_rectangle_2t_sample',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P1T_1t_14 = visual.ImageStim(
    win=win,
    name='P1T_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
P2T_1t_14 = visual.ImageStim(
    win=win,
    name='P2T_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P3T_1t_14 = visual.ImageStim(
    win=win,
    name='P3T_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P4T_1t_14 = visual.ImageStim(
    win=win,
    name='P4T_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P5T_1t_14 = visual.ImageStim(
    win=win,
    name='P5T_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P6T_1t_14 = visual.ImageStim(
    win=win,
    name='P6T_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P7t_1t_14 = visual.ImageStim(
    win=win,
    name='P7t_1t_14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
finish_15 = visual.ShapeStim(
    win=win, name='finish_15',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-13.0, interpolate=True)

# --- Initialize components for Routine "mng_feedback_practice" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from code_30
feedback_sound = ['kids_cheering.wav','crowdohh.wav']
#feedback_image = ['happy139.png','sad139.png']
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "mng_check_practice_2" ---

# --- Initialize components for Routine "mng_repeat_instructions_2" ---
text_25 = visual.TextStim(win=win, name='text_25',
    text='Remember!\nPoint to the pictures you just saw.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_15 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_ready_3" ---
key_resp_21 = keyboard.Keyboard()
text_26 = visual.TextStim(win=win, name='text_26',
    text='Ready?',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from code_39
acc_thr = 66

# --- Initialize components for Routine "mng_blank_b2" ---
blank_box_2 = visual.TextStim(win=win, name='blank_box_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_probe_2target" ---
P2_sample_2t = visual.ImageStim(
    win=win,
    name='P2_sample_2t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
P3_sample_2t = visual.ImageStim(
    win=win,
    name='P3_sample_2t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test_2target_4objects" ---
# Run 'Begin Experiment' code from code_10
incorr = 0
mouse_18 = event.Mouse(win=win)
x, y = [None, None]
mouse_18.mouseClock = core.Clock()
P2T_rectangle_2t_4 = visual.Rect(
    win=win, name='P2T_rectangle_2t_4',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_2t_4 = visual.Rect(
    win=win, name='P3T_rectangle_2t_4',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_2t_4 = visual.Rect(
    win=win, name='P6T_rectangle_2t_4',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_2t_4 = visual.Rect(
    win=win, name='P7T_rectangle_2t_4',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P1T_1t_5 = visual.ImageStim(
    win=win,
    name='P1T_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
P2T_1t_5 = visual.ImageStim(
    win=win,
    name='P2T_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P3T_1t_5 = visual.ImageStim(
    win=win,
    name='P3T_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P4T_1t_5 = visual.ImageStim(
    win=win,
    name='P4T_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P5T_1t_5 = visual.ImageStim(
    win=win,
    name='P5T_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P6T_1t_5 = visual.ImageStim(
    win=win,
    name='P6T_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P7t_1t_5 = visual.ImageStim(
    win=win,
    name='P7t_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P8t_1t_5 = visual.ImageStim(
    win=win,
    name='P8t_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P9t_1t_5 = visual.ImageStim(
    win=win,
    name='P9t_1t_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
finish_6 = visual.ShapeStim(
    win=win, name='finish_6',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-15.0, interpolate=True)

# --- Initialize components for Routine "mng_test_2target_5objects" ---
# Run 'Begin Experiment' code from code_11
incorr = 0
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
P1T_rectangle_2t_5 = visual.Rect(
    win=win, name='P1T_rectangle_2t_5',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P4T_rectangle_2t_5 = visual.Rect(
    win=win, name='P4T_rectangle_2t_5',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P5T_rectangle_2t_5 = visual.Rect(
    win=win, name='P5T_rectangle_2t_5',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P8T_rectangle_2t_5 = visual.Rect(
    win=win, name='P8T_rectangle_2t_5',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.500, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P9T_rectangle_2t_5 = visual.Rect(
    win=win, name='P9T_rectangle_2t_5',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.500, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P1T_1t_6 = visual.ImageStim(
    win=win,
    name='P1T_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P2T_1t_6 = visual.ImageStim(
    win=win,
    name='P2T_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P3T_1t_6 = visual.ImageStim(
    win=win,
    name='P3T_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P4T_1t_6 = visual.ImageStim(
    win=win,
    name='P4T_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P5T_1t_6 = visual.ImageStim(
    win=win,
    name='P5T_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P6T_1t_6 = visual.ImageStim(
    win=win,
    name='P6T_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P7t_1t_6 = visual.ImageStim(
    win=win,
    name='P7t_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P8t_1t_6 = visual.ImageStim(
    win=win,
    name='P8t_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P9t_1t_6 = visual.ImageStim(
    win=win,
    name='P9t_1t_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
finish_7 = visual.ShapeStim(
    win=win, name='finish_7',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-16.0, interpolate=True)

# --- Initialize components for Routine "mng_test_2target_6objects" ---
# Run 'Begin Experiment' code from code_12
incorr = 0
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
P2T_rectangle_2t_6 = visual.Rect(
    win=win, name='P2T_rectangle_2t_6',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_2t_6 = visual.Rect(
    win=win, name='P3T_rectangle_2t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_2t_6 = visual.Rect(
    win=win, name='P6T_rectangle_2t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_2t_6 = visual.Rect(
    win=win, name='P7T_rectangle_2t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P10T_rectangle_2t_6 = visual.Rect(
    win=win, name='P10T_rectangle_2t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P11T_rectangle_2t_6 = visual.Rect(
    win=win, name='P11T_rectangle_2t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
P1T_1t_7 = visual.ImageStim(
    win=win,
    name='P1T_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P2T_1t_7 = visual.ImageStim(
    win=win,
    name='P2T_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P3T_1t_7 = visual.ImageStim(
    win=win,
    name='P3T_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P4T_1t_7 = visual.ImageStim(
    win=win,
    name='P4T_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P5T_1t_7 = visual.ImageStim(
    win=win,
    name='P5T_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P6T_1t_7 = visual.ImageStim(
    win=win,
    name='P6T_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P7t_1t_7 = visual.ImageStim(
    win=win,
    name='P7t_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P8t_1t_7 = visual.ImageStim(
    win=win,
    name='P8t_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
P9t_1t_7 = visual.ImageStim(
    win=win,
    name='P9t_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
P10t_1t_7 = visual.ImageStim(
    win=win,
    name='P10t_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P11_1t_7 = visual.ImageStim(
    win=win,
    name='P11_1t_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
finish_8 = visual.ShapeStim(
    win=win, name='finish_8',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-19.0, interpolate=True)

# --- Initialize components for Routine "mng_blank_3" ---
blank_box_4 = visual.TextStim(win=win, name='blank_box_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_19 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_probe_3target" ---
P1_sample_3t = visual.ImageStim(
    win=win,
    name='P1_sample_3t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
P4_sample_3t = visual.ImageStim(
    win=win,
    name='P4_sample_3t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
P5_sample_3t = visual.ImageStim(
    win=win,
    name='P5_sample_3t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test_3target_5objects" ---
# Run 'Begin Experiment' code from code_13
incorr = 0
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
P1T_rectangle_3t_5 = visual.Rect(
    win=win, name='P1T_rectangle_3t_5',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P4T_rectangle_3t_5 = visual.Rect(
    win=win, name='P4T_rectangle_3t_5',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P5T_rectangle_3t_5 = visual.Rect(
    win=win, name='P5T_rectangle_3t_5',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.250, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P8T_rectangle_3t_5 = visual.Rect(
    win=win, name='P8T_rectangle_3t_5',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.500, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P9T_rectangle_3t_5 = visual.Rect(
    win=win, name='P9T_rectangle_3t_5',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.500, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P1T_1t_8 = visual.ImageStim(
    win=win,
    name='P1T_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P2T_1t_8 = visual.ImageStim(
    win=win,
    name='P2T_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P3T_1t_8 = visual.ImageStim(
    win=win,
    name='P3T_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P4T_1t_8 = visual.ImageStim(
    win=win,
    name='P4T_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P5T_1t_8 = visual.ImageStim(
    win=win,
    name='P5T_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P6T_1t_8 = visual.ImageStim(
    win=win,
    name='P6T_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P7t_1t_8 = visual.ImageStim(
    win=win,
    name='P7t_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P8t_1t_8 = visual.ImageStim(
    win=win,
    name='P8t_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P9t_1t_8 = visual.ImageStim(
    win=win,
    name='P9t_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
finish_9 = visual.ShapeStim(
    win=win, name='finish_9',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-16.0, interpolate=True)

# --- Initialize components for Routine "mng_test_3target_6objects" ---
# Run 'Begin Experiment' code from code_14
incorr = 0
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()
P2T_rectangle_3t_6 = visual.Rect(
    win=win, name='P2T_rectangle_3t_6',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_3t_6 = visual.Rect(
    win=win, name='P3T_rectangle_3t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_3t_6 = visual.Rect(
    win=win, name='P6T_rectangle_3t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_3t_6 = visual.Rect(
    win=win, name='P7T_rectangle_3t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P10T_rectangle_3t_6 = visual.Rect(
    win=win, name='P10T_rectangle_3t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P11T_rectangle_3t_6 = visual.Rect(
    win=win, name='P11T_rectangle_3t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
P1T_1t_9 = visual.ImageStim(
    win=win,
    name='P1T_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P2T_1t_9 = visual.ImageStim(
    win=win,
    name='P2T_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P3T_1t_9 = visual.ImageStim(
    win=win,
    name='P3T_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P4T_1t_9 = visual.ImageStim(
    win=win,
    name='P4T_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P5T_1t_9 = visual.ImageStim(
    win=win,
    name='P5T_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P6T_1t_9 = visual.ImageStim(
    win=win,
    name='P6T_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P7t_1t_9 = visual.ImageStim(
    win=win,
    name='P7t_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P8t_1t_9 = visual.ImageStim(
    win=win,
    name='P8t_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
P9t_1t_9 = visual.ImageStim(
    win=win,
    name='P9t_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
P10t_1t = visual.ImageStim(
    win=win,
    name='P10t_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P11_1t = visual.ImageStim(
    win=win,
    name='P11_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
finish_10 = visual.ShapeStim(
    win=win, name='finish_10',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-19.0, interpolate=True)

# --- Initialize components for Routine "mng_test_3target_8objects" ---
# Run 'Begin Experiment' code from code_15
incorr = 0
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
P2T_rectangle_3t_8 = visual.Rect(
    win=win, name='P2T_rectangle_3t_8',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_3t_8 = visual.Rect(
    win=win, name='P3T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125,.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_3t_8 = visual.Rect(
    win=win, name='P6T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_3t_8 = visual.Rect(
    win=win, name='P7T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P12T_rectangle_3t_8 = visual.Rect(
    win=win, name='P12T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.125, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P13T_rectangle_3t_8 = visual.Rect(
    win=win, name='P13T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.125, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
P14T_rectangle_3t_8 = visual.Rect(
    win=win, name='P14T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.375, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
P15T_rectangle_3t_8 = visual.Rect(
    win=win, name='P15T_rectangle_3t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
P1T_1t_10 = visual.ImageStim(
    win=win,
    name='P1T_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P2T_1t_10 = visual.ImageStim(
    win=win,
    name='P2T_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P3T_1t_10 = visual.ImageStim(
    win=win,
    name='P3T_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P4T_1t_10 = visual.ImageStim(
    win=win,
    name='P4T_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P5T_1t_10 = visual.ImageStim(
    win=win,
    name='P5T_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P6T_1t_10 = visual.ImageStim(
    win=win,
    name='P6T_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
P7t_1t_10 = visual.ImageStim(
    win=win,
    name='P7t_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
P8t_1t_10 = visual.ImageStim(
    win=win,
    name='P8t_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P9t_1t_10 = visual.ImageStim(
    win=win,
    name='P9t_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
P10t_1t_8 = visual.ImageStim(
    win=win,
    name='P10t_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
P11_1t_8 = visual.ImageStim(
    win=win,
    name='P11_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
P12_1t_8 = visual.ImageStim(
    win=win,
    name='P12_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.125, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
P13_1t_8 = visual.ImageStim(
    win=win,
    name='P13_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.125, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
P14_1t_8 = visual.ImageStim(
    win=win,
    name='P14_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.375, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
P15_1t_8 = visual.ImageStim(
    win=win,
    name='P15_1t_8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
finish_11 = visual.ShapeStim(
    win=win, name='finish_11',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-25.0, interpolate=True)

# --- Initialize components for Routine "mng_blank_4" ---
blank_box_5 = visual.TextStim(win=win, name='blank_box_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_probe_4target" ---
P2_sample_4t = visual.ImageStim(
    win=win,
    name='P2_sample_4t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
P3_sample_4t = visual.ImageStim(
    win=win,
    name='P3_sample_4t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
P6_sample_4t = visual.ImageStim(
    win=win,
    name='P6_sample_4t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
P7_sample_4t = visual.ImageStim(
    win=win,
    name='P7_sample_4t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_10 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test_4target_6objects" ---
# Run 'Begin Experiment' code from code_16
incorr = 0
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
P2T_rectangle_4t_6 = visual.Rect(
    win=win, name='P2T_rectangle_4t_6',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_4t_6 = visual.Rect(
    win=win, name='P3T_rectangle_4t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_4t_6 = visual.Rect(
    win=win, name='P6T_rectangle_4t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_4t_6 = visual.Rect(
    win=win, name='P7T_rectangle_4t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P10T_rectangle_4t_6 = visual.Rect(
    win=win, name='P10T_rectangle_4t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P11T_rectangle_4t_6 = visual.Rect(
    win=win, name='P11T_rectangle_4t_6',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
P1T_1t_11 = visual.ImageStim(
    win=win,
    name='P1T_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P2T_1t_11 = visual.ImageStim(
    win=win,
    name='P2T_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P3T_1t_11 = visual.ImageStim(
    win=win,
    name='P3T_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P4T_1t_11 = visual.ImageStim(
    win=win,
    name='P4T_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P5T_1t_11 = visual.ImageStim(
    win=win,
    name='P5T_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P6T_1t_11 = visual.ImageStim(
    win=win,
    name='P6T_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P7t_1t_11 = visual.ImageStim(
    win=win,
    name='P7t_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P8t_1t_11 = visual.ImageStim(
    win=win,
    name='P8t_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
P9t_1t_11 = visual.ImageStim(
    win=win,
    name='P9t_1t_11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
P10t_1t_2 = visual.ImageStim(
    win=win,
    name='P10t_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P11_1t_2 = visual.ImageStim(
    win=win,
    name='P11_1t_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
finish_12 = visual.ShapeStim(
    win=win, name='finish_12',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-19.0, interpolate=True)

# --- Initialize components for Routine "mng_test_4target_8objects" ---
# Run 'Begin Experiment' code from code_17
incorr = 0
mouse_13 = event.Mouse(win=win)
x, y = [None, None]
mouse_13.mouseClock = core.Clock()
P2T_rectangle_4t_8 = visual.Rect(
    win=win, name='P2T_rectangle_4t_8',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P3T_rectangle_4t_8 = visual.Rect(
    win=win, name='P3T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.125,.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P6T_rectangle_4t_8 = visual.Rect(
    win=win, name='P6T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.375, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P7T_rectangle_4t_8 = visual.Rect(
    win=win, name='P7T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P12T_rectangle_4t_8 = visual.Rect(
    win=win, name='P12T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.125, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P13T_rectangle_4t_8 = visual.Rect(
    win=win, name='P13T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.125, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
P14T_rectangle_4t_8 = visual.Rect(
    win=win, name='P14T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.375, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
P15T_rectangle_4t_8 = visual.Rect(
    win=win, name='P15T_rectangle_4t_8',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.375, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
P1T_1t_12 = visual.ImageStim(
    win=win,
    name='P1T_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P2T_1t_12 = visual.ImageStim(
    win=win,
    name='P2T_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P3T_1t_12 = visual.ImageStim(
    win=win,
    name='P3T_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P4T_1t_12 = visual.ImageStim(
    win=win,
    name='P4T_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P5T_1t_12 = visual.ImageStim(
    win=win,
    name='P5T_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P6T_1t_12 = visual.ImageStim(
    win=win,
    name='P6T_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
P7t_1t_12 = visual.ImageStim(
    win=win,
    name='P7t_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
P8t_1t_12 = visual.ImageStim(
    win=win,
    name='P8t_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P9t_1t_12 = visual.ImageStim(
    win=win,
    name='P9t_1t_12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
P10t_1t_9 = visual.ImageStim(
    win=win,
    name='P10t_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
P11_1t_9 = visual.ImageStim(
    win=win,
    name='P11_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
P12_1t = visual.ImageStim(
    win=win,
    name='P12_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.125, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
P13_1t = visual.ImageStim(
    win=win,
    name='P13_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.125, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
P14_1t = visual.ImageStim(
    win=win,
    name='P14_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.375, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
P15_1t = visual.ImageStim(
    win=win,
    name='P15_1t', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
finish_13 = visual.ShapeStim(
    win=win, name='finish_13',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-25.0, interpolate=True)

# --- Initialize components for Routine "mng_test_4target_10objects" ---
# Run 'Begin Experiment' code from code_18
incorr = 0
mouse_14 = event.Mouse(win=win)
x, y = [None, None]
mouse_14.mouseClock = core.Clock()
P1T_rectangle_4t_10 = visual.Rect(
    win=win, name='P1T_rectangle_4t_10',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P4T_rectangle_4t_10 = visual.Rect(
    win=win, name='P4T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.250,.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P5T_rectangle_4t_10 = visual.Rect(
    win=win, name='P5T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.250, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P8T_rectangle_4t_10 = visual.Rect(
    win=win, name='P8T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.500, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P9T_rectangle_4t_10 = visual.Rect(
    win=win, name='P9T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.500, .150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P16T_rectangle_4t_10 = visual.Rect(
    win=win, name='P16T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
P17T_rectangle_4t_10 = visual.Rect(
    win=win, name='P17T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.250, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
P18T_rectangle_4t_10 = visual.Rect(
    win=win, name='P18T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.250, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
P19T_rectangle_4t_10 = visual.Rect(
    win=win, name='P19T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(.500, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
P20T_rectangle_4t_10 = visual.Rect(
    win=win, name='P20T_rectangle_4t_10',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-.500, -.150), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
P1T_1t_13 = visual.ImageStim(
    win=win,
    name='P1T_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
P2T_1t_13 = visual.ImageStim(
    win=win,
    name='P2T_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
P3T_1t_13 = visual.ImageStim(
    win=win,
    name='P3T_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
P4T_1t_13 = visual.ImageStim(
    win=win,
    name='P4T_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
P5T_1t_13 = visual.ImageStim(
    win=win,
    name='P5T_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
P6T_1t_13 = visual.ImageStim(
    win=win,
    name='P6T_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
P7t_1t_13 = visual.ImageStim(
    win=win,
    name='P7t_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
P8t_1t_13 = visual.ImageStim(
    win=win,
    name='P8t_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, .150), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
P9t_1t_13 = visual.ImageStim(
    win=win,
    name='P9t_1t_13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
P10t_1t_10 = visual.ImageStim(
    win=win,
    name='P10t_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
P11_1t_10 = visual.ImageStim(
    win=win,
    name='P11_1t_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, .150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
P12_1t_9 = visual.ImageStim(
    win=win,
    name='P12_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.125, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
P13_1t_9 = visual.ImageStim(
    win=win,
    name='P13_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.125, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
P14_1t_9 = visual.ImageStim(
    win=win,
    name='P14_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.375, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
P15_1t_9 = visual.ImageStim(
    win=win,
    name='P15_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.375, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
P16_1t_9 = visual.ImageStim(
    win=win,
    name='P16_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-27.0)
P17_1t_9 = visual.ImageStim(
    win=win,
    name='P17_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.250, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-28.0)
P18_1t_9 = visual.ImageStim(
    win=win,
    name='P18_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.250, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-29.0)
P19_1t_9 = visual.ImageStim(
    win=win,
    name='P19_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(.500, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-30.0)
P20_1t_9 = visual.ImageStim(
    win=win,
    name='P20_1t_9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-.500, -.150), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-31.0)
finish_14 = visual.ShapeStim(
    win=win, name='finish_14',
    size=(0.07, 0.07), vertices='triangle',
    ori=90.0, pos=(0.625, -.35), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-32.0, interpolate=True)

# --- Initialize components for Routine "mng_end" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='Thank you!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_42
globalClock = core.Clock()
beginning_exp = globalClock.getTime()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "mng_welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
mng_welcomeComponents = [text, key_resp_2]
for thisComponent in mng_welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mng_welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mng_welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mng_welcome" ---
for thisComponent in mng_welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "mng_welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "mng_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
mng_instructionsComponents = [text_5, key_resp_4]
for thisComponent in mng_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mng_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mng_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mng_instructions" ---
for thisComponent in mng_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "mng_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mng_practice_loop = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='mng_practice_loop')
thisExp.addLoop(mng_practice_loop)  # add the loop to the experiment
thisMng_practice_loop = mng_practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMng_practice_loop.rgb)
if thisMng_practice_loop != None:
    for paramName in thisMng_practice_loop:
        exec('{} = thisMng_practice_loop[paramName]'.format(paramName))

for thisMng_practice_loop in mng_practice_loop:
    currentLoop = mng_practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMng_practice_loop.rgb)
    if thisMng_practice_loop != None:
        for paramName in thisMng_practice_loop:
            exec('{} = thisMng_practice_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_practice_counter" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    ncount = 0
    # keep track of which components have finished
    mng_practice_counterComponents = []
    for thisComponent in mng_practice_counterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_practice_counter" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_practice_counterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_practice_counter" ---
    for thisComponent in mng_practice_counterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "mng_practice_counter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mng_practice = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('mn_generaltask_practice.csv', selection='0:1'),
        seed=None, name='mng_practice')
    thisExp.addLoop(mng_practice)  # add the loop to the experiment
    thisMng_practice = mng_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMng_practice.rgb)
    if thisMng_practice != None:
        for paramName in thisMng_practice:
            exec('{} = thisMng_practice[paramName]'.format(paramName))
    
    for thisMng_practice in mng_practice:
        currentLoop = mng_practice
        # abbreviate parameter names if possible (e.g. rgb = thisMng_practice.rgb)
        if thisMng_practice != None:
            for paramName in thisMng_practice:
                exec('{} = thisMng_practice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mng_blank" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        mng_blankComponents = [blank_box, key_resp_3]
        for thisComponent in mng_blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_blank" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_box* updates
            if blank_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_box.frameNStart = frameN  # exact frame index
                blank_box.tStart = t  # local t and not account for scr refresh
                blank_box.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_box, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_box.started')
                blank_box.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_blank" ---
        for thisComponent in mng_blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        mng_practice.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            mng_practice.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "mng_blank" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "mng_probe_sample" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        P1_sample.setImage(probe_p1)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        mng_probe_sampleComponents = [P1_sample, key_resp]
        for thisComponent in mng_probe_sampleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_probe_sample" ---
        while continueRoutine and routineTimer.getTime() < 3.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *P1_sample* updates
            if P1_sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P1_sample.frameNStart = frameN  # exact frame index
                P1_sample.tStart = t  # local t and not account for scr refresh
                P1_sample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P1_sample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1_sample.started')
                P1_sample.setAutoDraw(True)
            if P1_sample.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > P1_sample.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    P1_sample.tStop = t  # not accounting for scr refresh
                    P1_sample.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'P1_sample.stopped')
                    P1_sample.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_probe_sampleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_probe_sample" ---
        for thisComponent in mng_probe_sampleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        mng_practice.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            mng_practice.addData('key_resp.rt', key_resp.rt)
        # Run 'End Routine' code from code_44
        beginning_trial = globalClock.getTime();
        thisExp.addData("start", beginning_trial);
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.500000)
        
        # --- Prepare to start Routine "mng_test_sample" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        incorr = 1
        ClickCount1 = 0
        startTime = globalClock.getTime()
        
        
        clicked1 = 0
        clicked2 = 0
        clicked3 = 0
        clicked4 = 0
        clicked5 = 0
        clicked6 = 0
        lineColor = 'white'
        msg = 'Incorrect'
        
        P1T_rectangle_color = 0
        P2T_rectangle_color = 0
        
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        P1T.setImage(test_p2)
        P2T.setImage(test_p3)
        # keep track of which components have finished
        mng_test_sampleComponents = [mouse, P1T_rectangle, P2T_rectangle, P1T, P2T, finish]
        for thisComponent in mng_test_sampleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_test_sample" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            #print(ClickCount1)
            if mouse.isPressedIn(P1T_rectangle):
                if clicked1 == 0:
                    clicked1 = 1
                    if lineColor == 'white':
                        P1T_rectangle.lineColor = 'black'
                        lineColor = 'black'
                        P1T_rectangle_color = 1
                        thisExp.addData('P1T_rectangle', 1) #OR exp.addData('letter', letter)
                    elif lineColor == 'black':
                        P1T_rectangle.lineColor = 'white'
                        lineColor = 'white'
                        P1T_rectangle_color = 0
                        thisExp.addData('P1T_rectangle', 0)
            elif clicked1 == 1:
                clicked1 = 0
            
            if mouse.isPressedIn(P2T_rectangle):
                if clicked2 == 0:
                    clicked2 = 1
                    if lineColor == 'white':
                        P2T_rectangle.lineColor = 'black'
                        lineColor = 'black'
                        thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                        P2T_rectangle_color = 1
                    elif lineColor == 'black':
                        P2T_rectangle.lineColor = 'white'
                        lineColor = 'white'
                        thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                        P2T_rectangle_color = 0
            elif clicked2 == 1:
                clicked2 = 0
            
            if mouse.isPressedIn(finish):
                continueRoutine = False
                end_trial = globalClock.getTime();
                thisExp.addData("end", end_trial);
                time_exp = (end_trial - beginning_trial)
                thisExp.addData("rt", time_exp);
            
            #print(mouse.time[0])
            #rtList.append(mouse.time[0])
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([P1T_rectangle, P2T_rectangle])
                            clickableList = [P1T_rectangle, P2T_rectangle]
                        except:
                            clickableList = [[P1T_rectangle, P2T_rectangle]]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            
            # *P1T_rectangle* updates
            if P1T_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P1T_rectangle.frameNStart = frameN  # exact frame index
                P1T_rectangle.tStart = t  # local t and not account for scr refresh
                P1T_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P1T_rectangle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1T_rectangle.started')
                P1T_rectangle.setAutoDraw(True)
            
            # *P2T_rectangle* updates
            if P2T_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2T_rectangle.frameNStart = frameN  # exact frame index
                P2T_rectangle.tStart = t  # local t and not account for scr refresh
                P2T_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2T_rectangle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2T_rectangle.started')
                P2T_rectangle.setAutoDraw(True)
            
            # *P1T* updates
            if P1T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P1T.frameNStart = frameN  # exact frame index
                P1T.tStart = t  # local t and not account for scr refresh
                P1T.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P1T, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1T.started')
                P1T.setAutoDraw(True)
            
            # *P2T* updates
            if P2T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2T.frameNStart = frameN  # exact frame index
                P2T.tStart = t  # local t and not account for scr refresh
                P2T.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2T, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2T.started')
                P2T.setAutoDraw(True)
            
            # *finish* updates
            if finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                finish.frameNStart = frameN  # exact frame index
                finish.tStart = t  # local t and not account for scr refresh
                finish.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(finish, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'finish.started')
                finish.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_test_sampleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_test_sample" ---
        for thisComponent in mng_test_sampleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        #print(ClickCount1)
        ClickCount1 = 0
        P1T_rectangle.lineColor = 'white'
        P2T_rectangle.lineColor = 'white'
        
        print("finish")
        print(float(P2T_rectangle_color))
        print(float(corr_p2))
        print(type(float(P2T_rectangle_color)))
        print(type(float(corr_p2)))
        
        print("correct")
        print(corr_p2)
        print(corr_p3)
        print(type(corr_p2))
        print(type(corr_p3))
        print("choices")
        print(P1T_rectangle_color)
        print(P2T_rectangle_color)
        print(type(P1T_rectangle_color))
        print(type(P2T_rectangle_color))
        
        
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p1) == float(P1T_rectangle_color))):
            mng_practice.addData('accuracy', 1) #OR exp.addData('letter', letter)
            feedback_outcome_sound = feedback_sound[0]
            feedback_outcome_image = feedback_image[0]
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            feedback_outcome_sound = feedback_sound[1]
            feedback_outcome_image = feedback_image[1]
            incorr = 1
            mng_practice.addData('accuracy', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
          
        #beginning_trial = globalClock.getTime();  
        #end_trial = globalClock.getTime();
        #thisExp.addData("end", end_trial);
        #time_exp = (end_trial - beginning_trial)
        #thisExp.addData("rt", time_exp);
        
        thisExp.addData("presented", 1)
        # store data for mng_practice (TrialHandler)
        mng_practice.addData('mouse.x', mouse.x)
        mng_practice.addData('mouse.y', mouse.y)
        mng_practice.addData('mouse.leftButton', mouse.leftButton)
        mng_practice.addData('mouse.midButton', mouse.midButton)
        mng_practice.addData('mouse.rightButton', mouse.rightButton)
        mng_practice.addData('mouse.time', mouse.time)
        mng_practice.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "mng_test_sample" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "mng_feedback_practice_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        image.setImage(feedback_outcome_image)
        # keep track of which components have finished
        mng_feedback_practice_2Components = [text_28, image]
        for thisComponent in mng_feedback_practice_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_feedback_practice_2" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_28* updates
            if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_28.frameNStart = frameN  # exact frame index
                text_28.tStart = t  # local t and not account for scr refresh
                text_28.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_28.started')
                text_28.setAutoDraw(True)
            if text_28.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_28.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_28.tStop = t  # not accounting for scr refresh
                    text_28.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_28.stopped')
                    text_28.setAutoDraw(False)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_feedback_practice_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_feedback_practice_2" ---
        for thisComponent in mng_feedback_practice_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'mng_practice'
    
    
    # --- Prepare to start Routine "mng_check_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    ncount = ncount + 1
    
    if ncount == 1:
        nCorr2_loop1 = int(mng_practice.data['accuracy'].mean()*100)
        print(nCorr2_loop1)
        if nCorr2_loop1 ==100:
            mng_practice_loop.finished=1
            
    if ncount == 2:
        nCorr2_loop2 = int(mng_practice.data['accuracy'].mean()*100)
        nCorr2_loop2 = nCorr2_loop2-nCorr2_loop1
        if nCorr2_loop2 == 100:
            mng_practice_loop.finished=1
    # keep track of which components have finished
    mng_check_practiceComponents = []
    for thisComponent in mng_check_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_check_practice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_check_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_check_practice" ---
    for thisComponent in mng_check_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "mng_check_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_repeat_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    if ncount == 1:
        if nCorr2_loop1 == 100:
            continueRoutine=False
            
    if ncount == 2:
        if nCorr2_loop2 == 100:
            continueRoutine=False
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    mng_repeat_instructionsComponents = [text_7, key_resp_6]
    for thisComponent in mng_repeat_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_repeat_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            text_7.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_repeat_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_repeat_instructions" ---
    for thisComponent in mng_repeat_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    mng_practice_loop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        mng_practice_loop.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "mng_repeat_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'mng_practice_loop'


# --- Prepare to start Routine "mng_ready" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
mng_readyComponents = [key_resp_14, text_24]
for thisComponent in mng_readyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mng_ready" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_14.started')
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_24.started')
        text_24.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mng_readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mng_ready" ---
for thisComponent in mng_readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()
# the Routine "mng_ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mng_exptrials_t1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mn_generaltask_t1trials_good.csv'),
    seed=None, name='mng_exptrials_t1')
thisExp.addLoop(mng_exptrials_t1)  # add the loop to the experiment
thisMng_exptrials_t1 = mng_exptrials_t1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t1.rgb)
if thisMng_exptrials_t1 != None:
    for paramName in thisMng_exptrials_t1:
        exec('{} = thisMng_exptrials_t1[paramName]'.format(paramName))

for thisMng_exptrials_t1 in mng_exptrials_t1:
    currentLoop = mng_exptrials_t1
    # abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t1.rgb)
    if thisMng_exptrials_t1 != None:
        for paramName in thisMng_exptrials_t1:
            exec('{} = thisMng_exptrials_t1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_blank" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    mng_blankComponents = [blank_box, key_resp_3]
    for thisComponent in mng_blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_blank" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_box* updates
        if blank_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_box.frameNStart = frameN  # exact frame index
            blank_box.tStart = t  # local t and not account for scr refresh
            blank_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_box.started')
            blank_box.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_blank" ---
    for thisComponent in mng_blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    mng_exptrials_t1.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        mng_exptrials_t1.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "mng_blank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_probe_1target" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    P1_sample_2.setImage(probe_p1)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    mng_probe_1targetComponents = [P1_sample_2, key_resp_5]
    for thisComponent in mng_probe_1targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_probe_1target" ---
    while continueRoutine and routineTimer.getTime() < 3.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *P1_sample_2* updates
        if P1_sample_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1_sample_2.frameNStart = frameN  # exact frame index
            P1_sample_2.tStart = t  # local t and not account for scr refresh
            P1_sample_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1_sample_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1_sample_2.started')
            P1_sample_2.setAutoDraw(True)
        if P1_sample_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P1_sample_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                P1_sample_2.tStop = t  # not accounting for scr refresh
                P1_sample_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1_sample_2.stopped')
                P1_sample_2.setAutoDraw(False)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_5.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=None, waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_probe_1targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_probe_1target" ---
    for thisComponent in mng_probe_1targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    mng_exptrials_t1.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        mng_exptrials_t1.addData('key_resp_5.rt', key_resp_5.rt)
    # Run 'End Routine' code from code_43
    beginning_trial = globalClock.getTime();  
    thisExp.addData("start", beginning_trial);
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.500000)
    
    # --- Prepare to start Routine "mng_test_1target_2objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    if objects > 2:
        continueRoutine=False
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    #P1T_rectangle_color_1t = 0
    P2T_rectangle_color_1t2o = 0
    P3T_rectangle_color_1t2o = 0
    #P4T_rectangle_color_1t2o = 0
    #P5T_rectangle_color_1t2o = 0
    #P6T_rectangle_color_1t2o = 0
    #P7T_rectangle_color_1t2o = 0
    #P8T_rectangle_color_1t2o = 0
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t.setImage(test_p1)
    P2T_1t.setImage(test_p2)
    P3T_1t.setImage(test_p3)
    P4T_1t.setImage(test_p4)
    P5T_1t.setImage(test_p5)
    P6T_1t.setImage(test_p6)
    P7t_1t.setImage(test_p7)
    P8t_1t.setImage(test_p8)
    P9t_1t.setImage(test_p9)
    # keep track of which components have finished
    mng_test_1target_2objectsComponents = [mouse_2, P2T_rectangle_1t, P3T_rectangle_1t, P1T_1t, P2T_1t, P3T_1t, P4T_1t, P5T_1t, P6T_1t, P7t_1t, P8t_1t, P9t_1t, finish_2]
    for thisComponent in mng_test_1target_2objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_1target_2objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_3
        #print(ClickCount1)
        
        if mouse.isPressedIn(P2T_rectangle_1t):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_1t.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color_1t2o = 1
                elif lineColor == 'black':
                    P2T_rectangle_1t.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color_1t2o = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse.isPressedIn(P3T_rectangle_1t):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_1t.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color_1t2o = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_1t.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color_1t2o = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse.isPressedIn(finish_2):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_1t* updates
        if P2T_rectangle_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_1t.frameNStart = frameN  # exact frame index
            P2T_rectangle_1t.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_1t.started')
            P2T_rectangle_1t.setAutoDraw(True)
        
        # *P3T_rectangle_1t* updates
        if P3T_rectangle_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_1t.frameNStart = frameN  # exact frame index
            P3T_rectangle_1t.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_1t.started')
            P3T_rectangle_1t.setAutoDraw(True)
        
        # *P1T_1t* updates
        if P1T_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t.frameNStart = frameN  # exact frame index
            P1T_1t.tStart = t  # local t and not account for scr refresh
            P1T_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t.started')
            P1T_1t.setAutoDraw(True)
        
        # *P2T_1t* updates
        if P2T_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t.frameNStart = frameN  # exact frame index
            P2T_1t.tStart = t  # local t and not account for scr refresh
            P2T_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t.started')
            P2T_1t.setAutoDraw(True)
        
        # *P3T_1t* updates
        if P3T_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t.frameNStart = frameN  # exact frame index
            P3T_1t.tStart = t  # local t and not account for scr refresh
            P3T_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t.started')
            P3T_1t.setAutoDraw(True)
        
        # *P4T_1t* updates
        if P4T_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t.frameNStart = frameN  # exact frame index
            P4T_1t.tStart = t  # local t and not account for scr refresh
            P4T_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t.started')
            P4T_1t.setAutoDraw(True)
        
        # *P5T_1t* updates
        if P5T_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t.frameNStart = frameN  # exact frame index
            P5T_1t.tStart = t  # local t and not account for scr refresh
            P5T_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t.started')
            P5T_1t.setAutoDraw(True)
        
        # *P6T_1t* updates
        if P6T_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t.frameNStart = frameN  # exact frame index
            P6T_1t.tStart = t  # local t and not account for scr refresh
            P6T_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t.started')
            P6T_1t.setAutoDraw(True)
        
        # *P7t_1t* updates
        if P7t_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t.frameNStart = frameN  # exact frame index
            P7t_1t.tStart = t  # local t and not account for scr refresh
            P7t_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t.started')
            P7t_1t.setAutoDraw(True)
        
        # *P8t_1t* updates
        if P8t_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t.frameNStart = frameN  # exact frame index
            P8t_1t.tStart = t  # local t and not account for scr refresh
            P8t_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t.started')
            P8t_1t.setAutoDraw(True)
        
        # *P9t_1t* updates
        if P9t_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t.frameNStart = frameN  # exact frame index
            P9t_1t.tStart = t  # local t and not account for scr refresh
            P9t_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t.started')
            P9t_1t.setAutoDraw(True)
        
        # *finish_2* updates
        if finish_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_2.frameNStart = frameN  # exact frame index
            finish_2.tStart = t  # local t and not account for scr refresh
            finish_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_2.started')
            finish_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_1target_2objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_1target_2objects" ---
    for thisComponent in mng_test_1target_2objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_3
    #print(ClickCount1)
    ClickCount1 = 0
    P2T_rectangle_1t.lineColor = 'white'
    P3T_rectangle_1t.lineColor = 'white'
    print("block1_1target")
    print("correct")
    print(corr_p2)
    print(corr_p3)
    print(type(corr_p2))
    print(type(corr_p3))
    print("choices")
    print(P2T_rectangle_color_1t2o)
    print(P3T_rectangle_color_1t2o)
    print(type(P2T_rectangle_color_1t2o))
    print(type(P3T_rectangle_color_1t2o))
    
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    #if objects == 2:
    #    if float(corr_p2) == float(P2T_rectangle_color_1t2o):
    #        print("corr_p1 correct")
    #        if float(corr_p3) == float(P3T_rectangle_color_1t2o):
    #            print("corr_p2 correct")
    #            mng_exptrials_t1.addData('accuracy_t1_o2', 1) #OR exp.addData('letter', letter)
    #            msg = "Correct"
    #            incorr = 0
    #    else:
    #        print("Incorrect")
    #        msg = "Incorrect"
    #        incorr = 1
    #        mng_exptrials_t1.addData('accuracy_t1_o2', 0) #OR exp.addData('letter', letter)
    #        print("value incorr")
    #        print(incorr)
            
            
    if objects ==2:
        if ((float(corr_p2) == float(P2T_rectangle_color_1t2o)) & (float(corr_p3) == float(P3T_rectangle_color_1t2o))):
            mng_exptrials_t1.addData('accuracy_t1_o2', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t1.addData('accuracy_t1_o2', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime();  
    #end_trial = globalClock.getTime();
    #thisExp.addData("end", end_trial);
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    thisExp.addData("presented", 1)
    # store data for mng_exptrials_t1 (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([P2T_rectangle_1t, P3T_rectangle_1t, finish_2])
            clickableList = [P2T_rectangle_1t, P3T_rectangle_1t, finish_2]
        except:
            clickableList = [[P2T_rectangle_1t, P3T_rectangle_1t, finish_2]]
        for obj in clickableList:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    mng_exptrials_t1.addData('mouse_2.x', x)
    mng_exptrials_t1.addData('mouse_2.y', y)
    mng_exptrials_t1.addData('mouse_2.leftButton', buttons[0])
    mng_exptrials_t1.addData('mouse_2.midButton', buttons[1])
    mng_exptrials_t1.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        mng_exptrials_t1.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    # the Routine "mng_test_1target_2objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_1target_3objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_7
    if objects > 3:
        continueRoutine=False
    #beginning_trial = globalClock.getTime();
    #thisExp.addData("start", beginning_trial);
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_2.setImage(test_p1)
    P2T_1t_2.setImage(test_p2)
    P3T_1t_2.setImage(test_p3)
    P4T_1t_2.setImage(test_p4)
    P5T_1t_2.setImage(test_p5)
    P6T_1t_2.setImage(test_p6)
    P7t_1t_2.setImage(test_p7)
    P8t_1t_2.setImage(test_p8)
    P9t_1t_2.setImage(test_p9)
    # keep track of which components have finished
    mng_test_1target_3objectsComponents = [mouse_3, P1T_rectangle_1t_2, P4T_rectangle_1t_2, P5T_rectangle_1t_2, P1T_1t_2, P2T_1t_2, P3T_1t_2, P4T_1t_2, P5T_1t_2, P6T_1t_2, P7t_1t_2, P8t_1t_2, P9t_1t_2, finish_3]
    for thisComponent in mng_test_1target_3objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_1target_3objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_7
        #print(ClickCount1)
        if mouse_3.isPressedIn(P1T_rectangle_1t_2):
            if clicked1 == 0:
                clicked1 = 1
                if lineColor == 'white':
                    P1T_rectangle_1t_2.lineColor = 'black'
                    lineColor = 'black'
                    P1T_rectangle_color = 1
                    thisExp.addData('P1T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P1T_rectangle_1t_2.lineColor = 'white'
                    lineColor = 'white'
                    P1T_rectangle_color = 0
                    thisExp.addData('P1T_rectangle', 0)
        elif clicked1 == 1:
            clicked1 = 0
        
        if mouse_3.isPressedIn(P4T_rectangle_1t_2):
            if clicked4 == 0:
                clicked4 = 1
                if lineColor == 'white':
                    P4T_rectangle_1t_2.lineColor = 'black'
                    lineColor = 'black'
                    P4T_rectangle_color = 1
                    thisExp.addData('P4T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P4T_rectangle_1t_2.lineColor = 'white'
                    lineColor = 'white'
                    P4T_rectangle_color = 0
                    thisExp.addData('P4T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked4 == 1:
            clicked4 = 0
        
        if mouse_3.isPressedIn(P5T_rectangle_1t_2):
            if clicked5 == 0:
                clicked5 = 1
                if lineColor == 'white':
                    P5T_rectangle_1t_2.lineColor = 'black'
                    lineColor = 'black'
                    P5T_rectangle_color = 1
                    thisExp.addData('P5T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P5T_rectangle_1t_2.lineColor = 'white'
                    lineColor = 'white'
                    P5T_rectangle_color = 0
                    thisExp.addData('P5T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked5 == 1:
            clicked5 = 0
        
        if mouse_3.isPressedIn(finish_3):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        
        # *P1T_rectangle_1t_2* updates
        if P1T_rectangle_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_rectangle_1t_2.frameNStart = frameN  # exact frame index
            P1T_rectangle_1t_2.tStart = t  # local t and not account for scr refresh
            P1T_rectangle_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_rectangle_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_rectangle_1t_2.started')
            P1T_rectangle_1t_2.setAutoDraw(True)
        
        # *P4T_rectangle_1t_2* updates
        if P4T_rectangle_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_rectangle_1t_2.frameNStart = frameN  # exact frame index
            P4T_rectangle_1t_2.tStart = t  # local t and not account for scr refresh
            P4T_rectangle_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_rectangle_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_rectangle_1t_2.started')
            P4T_rectangle_1t_2.setAutoDraw(True)
        
        # *P5T_rectangle_1t_2* updates
        if P5T_rectangle_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_rectangle_1t_2.frameNStart = frameN  # exact frame index
            P5T_rectangle_1t_2.tStart = t  # local t and not account for scr refresh
            P5T_rectangle_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_rectangle_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_rectangle_1t_2.started')
            P5T_rectangle_1t_2.setAutoDraw(True)
        
        # *P1T_1t_2* updates
        if P1T_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_2.frameNStart = frameN  # exact frame index
            P1T_1t_2.tStart = t  # local t and not account for scr refresh
            P1T_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_2.started')
            P1T_1t_2.setAutoDraw(True)
        
        # *P2T_1t_2* updates
        if P2T_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_2.frameNStart = frameN  # exact frame index
            P2T_1t_2.tStart = t  # local t and not account for scr refresh
            P2T_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_2.started')
            P2T_1t_2.setAutoDraw(True)
        
        # *P3T_1t_2* updates
        if P3T_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_2.frameNStart = frameN  # exact frame index
            P3T_1t_2.tStart = t  # local t and not account for scr refresh
            P3T_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_2.started')
            P3T_1t_2.setAutoDraw(True)
        
        # *P4T_1t_2* updates
        if P4T_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_2.frameNStart = frameN  # exact frame index
            P4T_1t_2.tStart = t  # local t and not account for scr refresh
            P4T_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_2.started')
            P4T_1t_2.setAutoDraw(True)
        
        # *P5T_1t_2* updates
        if P5T_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_2.frameNStart = frameN  # exact frame index
            P5T_1t_2.tStart = t  # local t and not account for scr refresh
            P5T_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_2.started')
            P5T_1t_2.setAutoDraw(True)
        
        # *P6T_1t_2* updates
        if P6T_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_2.frameNStart = frameN  # exact frame index
            P6T_1t_2.tStart = t  # local t and not account for scr refresh
            P6T_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_2.started')
            P6T_1t_2.setAutoDraw(True)
        
        # *P7t_1t_2* updates
        if P7t_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_2.frameNStart = frameN  # exact frame index
            P7t_1t_2.tStart = t  # local t and not account for scr refresh
            P7t_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_2.started')
            P7t_1t_2.setAutoDraw(True)
        
        # *P8t_1t_2* updates
        if P8t_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_2.frameNStart = frameN  # exact frame index
            P8t_1t_2.tStart = t  # local t and not account for scr refresh
            P8t_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_2.started')
            P8t_1t_2.setAutoDraw(True)
        
        # *P9t_1t_2* updates
        if P9t_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_2.frameNStart = frameN  # exact frame index
            P9t_1t_2.tStart = t  # local t and not account for scr refresh
            P9t_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_2.started')
            P9t_1t_2.setAutoDraw(True)
        
        # *finish_3* updates
        if finish_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_3.frameNStart = frameN  # exact frame index
            finish_3.tStart = t  # local t and not account for scr refresh
            finish_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_3.started')
            finish_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_1target_3objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_1target_3objects" ---
    for thisComponent in mng_test_1target_3objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_7
    #print(ClickCount1)
    ClickCount1 = 0
    P1T_rectangle_1t_2.lineColor = 'white'
    P4T_rectangle_1t_2.lineColor = 'white'
    P5T_rectangle_1t_2.lineColor = 'white'
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    
    #if objects == 3:
    #    if float(corr_p4) == float(P4T_rectangle_color):
    #        if float(corr_p1) == float(P1T_rectangle_color):
    #            if float(corr_p5) == float(P5T_rectangle_color):
    #                mng_exptrials_t1.addData('accuracy_t1_o3', 1) #OR exp.addData('letter', letter)
    #                msg = "Correct"
    #                incorr = 0
    #    else:
    #        msg = "Incorrect"
    #        incorr = 1
    #        mng_exptrials_t1.addData('accuracy_t1_o3', 0) #OR exp.addData('letter', letter)
    #        print("value incorr")
    #        print(incorr)
    
    if objects ==3:
        if ((float(corr_p4) == float(P4T_rectangle_color)) & (float(corr_p1) == float(P1T_rectangle_color)) & (float(corr_p5) == float(P5T_rectangle_color))):
            mng_exptrials_t1.addData('accuracy_t1_o3', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t1.addData('accuracy_t1_o3', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime();  
    #end_trial = globalClock.getTime();
    #thisExp.addData("end", end_trial);
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    thisExp.addData("presented", 1)
    # store data for mng_exptrials_t1 (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([P1T_rectangle_1t_2, P4T_rectangle_1t_2, P5T_rectangle_1t_2])
            clickableList = [P1T_rectangle_1t_2, P4T_rectangle_1t_2, P5T_rectangle_1t_2]
        except:
            clickableList = [[P1T_rectangle_1t_2, P4T_rectangle_1t_2, P5T_rectangle_1t_2]]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    mng_exptrials_t1.addData('mouse_3.x', x)
    mng_exptrials_t1.addData('mouse_3.y', y)
    mng_exptrials_t1.addData('mouse_3.leftButton', buttons[0])
    mng_exptrials_t1.addData('mouse_3.midButton', buttons[1])
    mng_exptrials_t1.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        mng_exptrials_t1.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    # the Routine "mng_test_1target_3objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_1target_4objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_8
    if objects > 4:
        continueRoutine=False
    #beginning_trial = globalClock.getTime() 
    #thisExp.addData("start", beginning_trial);
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_3.setImage(test_p1)
    P2T_1t_3.setImage(test_p2)
    P3T_1t_3.setImage(test_p3)
    P4T_1t_3.setImage(test_p4)
    P5T_1t_3.setImage(test_p5)
    P6T_1t_3.setImage(test_p6)
    P7t_1t_3.setImage(test_p7)
    P8t_1t_3.setImage(test_p8)
    P9t_1t_3.setImage(test_p9)
    # keep track of which components have finished
    mng_test_1target_4objectsComponents = [mouse_4, P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3, P1T_1t_3, P2T_1t_3, P3T_1t_3, P4T_1t_3, P5T_1t_3, P6T_1t_3, P7t_1t_3, P8t_1t_3, P9t_1t_3, finish_4]
    for thisComponent in mng_test_1target_4objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_1target_4objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_8
        #print(ClickCount1)
        
        if mouse_4.isPressedIn(P2T_rectangle_1t_3):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_1t_3.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_1t_3.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_4.isPressedIn(P3T_rectangle_1t_3):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_1t_3.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_1t_3.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_4.isPressedIn(P6T_rectangle_1t_3):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_1t_3.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_1t_3.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_4.isPressedIn(P7T_rectangle_1t_3):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_1t_3.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_1t_3.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
           
        
        if mouse_4.isPressedIn(finish_4):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        # *mouse_4* updates
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_4.started', t)
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_1t_3* updates
        if P2T_rectangle_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_1t_3.frameNStart = frameN  # exact frame index
            P2T_rectangle_1t_3.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_1t_3.started')
            P2T_rectangle_1t_3.setAutoDraw(True)
        
        # *P3T_rectangle_1t_3* updates
        if P3T_rectangle_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_1t_3.frameNStart = frameN  # exact frame index
            P3T_rectangle_1t_3.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_1t_3.started')
            P3T_rectangle_1t_3.setAutoDraw(True)
        
        # *P6T_rectangle_1t_3* updates
        if P6T_rectangle_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_1t_3.frameNStart = frameN  # exact frame index
            P6T_rectangle_1t_3.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_1t_3.started')
            P6T_rectangle_1t_3.setAutoDraw(True)
        
        # *P7T_rectangle_1t_3* updates
        if P7T_rectangle_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_1t_3.frameNStart = frameN  # exact frame index
            P7T_rectangle_1t_3.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_1t_3.started')
            P7T_rectangle_1t_3.setAutoDraw(True)
        
        # *P1T_1t_3* updates
        if P1T_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_3.frameNStart = frameN  # exact frame index
            P1T_1t_3.tStart = t  # local t and not account for scr refresh
            P1T_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_3.started')
            P1T_1t_3.setAutoDraw(True)
        
        # *P2T_1t_3* updates
        if P2T_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_3.frameNStart = frameN  # exact frame index
            P2T_1t_3.tStart = t  # local t and not account for scr refresh
            P2T_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_3.started')
            P2T_1t_3.setAutoDraw(True)
        
        # *P3T_1t_3* updates
        if P3T_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_3.frameNStart = frameN  # exact frame index
            P3T_1t_3.tStart = t  # local t and not account for scr refresh
            P3T_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_3.started')
            P3T_1t_3.setAutoDraw(True)
        
        # *P4T_1t_3* updates
        if P4T_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_3.frameNStart = frameN  # exact frame index
            P4T_1t_3.tStart = t  # local t and not account for scr refresh
            P4T_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_3.started')
            P4T_1t_3.setAutoDraw(True)
        
        # *P5T_1t_3* updates
        if P5T_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_3.frameNStart = frameN  # exact frame index
            P5T_1t_3.tStart = t  # local t and not account for scr refresh
            P5T_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_3.started')
            P5T_1t_3.setAutoDraw(True)
        
        # *P6T_1t_3* updates
        if P6T_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_3.frameNStart = frameN  # exact frame index
            P6T_1t_3.tStart = t  # local t and not account for scr refresh
            P6T_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_3.started')
            P6T_1t_3.setAutoDraw(True)
        
        # *P7t_1t_3* updates
        if P7t_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_3.frameNStart = frameN  # exact frame index
            P7t_1t_3.tStart = t  # local t and not account for scr refresh
            P7t_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_3.started')
            P7t_1t_3.setAutoDraw(True)
        
        # *P8t_1t_3* updates
        if P8t_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_3.frameNStart = frameN  # exact frame index
            P8t_1t_3.tStart = t  # local t and not account for scr refresh
            P8t_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_3.started')
            P8t_1t_3.setAutoDraw(True)
        
        # *P9t_1t_3* updates
        if P9t_1t_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_3.frameNStart = frameN  # exact frame index
            P9t_1t_3.tStart = t  # local t and not account for scr refresh
            P9t_1t_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_3.started')
            P9t_1t_3.setAutoDraw(True)
        
        # *finish_4* updates
        if finish_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_4.frameNStart = frameN  # exact frame index
            finish_4.tStart = t  # local t and not account for scr refresh
            finish_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_4.started')
            finish_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_1target_4objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_1target_4objects" ---
    for thisComponent in mng_test_1target_4objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_8
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_1t_3.lineColor = 'white'
    P3T_rectangle_1t_3.lineColor = 'white'
    P6T_rectangle_1t_3.lineColor = 'white'
    P7T_rectangle_1t_3.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects ==4:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color))):
                        mng_exptrials_t1.addData('accuracy_t1_o4', 1) #OR exp.addData('letter', letter)
                        msg = "Correct"
                        incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t1.addData('accuracy_t1_o4', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime();  
    #end_trial = globalClock.getTime();
    #thisExp.addData("end", end_trial);
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    thisExp.addData("presented", 1)
    # store data for mng_exptrials_t1 (TrialHandler)
    x, y = mouse_4.getPos()
    buttons = mouse_4.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3])
            clickableList = [P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3]
        except:
            clickableList = [[P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3]]
        for obj in clickableList:
            if obj.contains(mouse_4):
                gotValidClick = True
                mouse_4.clicked_name.append(obj.name)
    mng_exptrials_t1.addData('mouse_4.x', x)
    mng_exptrials_t1.addData('mouse_4.y', y)
    mng_exptrials_t1.addData('mouse_4.leftButton', buttons[0])
    mng_exptrials_t1.addData('mouse_4.midButton', buttons[1])
    mng_exptrials_t1.addData('mouse_4.rightButton', buttons[2])
    if len(mouse_4.clicked_name):
        mng_exptrials_t1.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
    # the Routine "mng_test_1target_4objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_1target_5objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_9
    if objects < 4:
        continueRoutine=False
    #beginning_trial = globalClock.getTime(); 
    #thisExp.addData("start", beginning_trial);
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    # setup some python lists for storing info about the mouse_5
    mouse_5.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_4.setImage(test_p1)
    P2T_1t_4.setImage(test_p2)
    P3T_1t_4.setImage(test_p3)
    P4T_1t_4.setImage(test_p4)
    P5T_1t_4.setImage(test_p5)
    P6T_1t_4.setImage(test_p6)
    P7t_1t_4.setImage(test_p7)
    P8t_1t_4.setImage(test_p8)
    P9t_1t_4.setImage(test_p9)
    # keep track of which components have finished
    mng_test_1target_5objectsComponents = [mouse_5, P1T_rectangle_1t_4, P4T_rectangle_1t_4, P5T_rectangle_1t_4, P8T_rectangle_1t_4, P9T_rectangle_1t_4, P1T_1t_4, P2T_1t_4, P3T_1t_4, P4T_1t_4, P5T_1t_4, P6T_1t_4, P7t_1t_4, P8t_1t_4, P9t_1t_4, finish_5]
    for thisComponent in mng_test_1target_5objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_1target_5objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_9
        #print(ClickCount1)
        if mouse_5.isPressedIn(P1T_rectangle_1t_4):
            if clicked1 == 0:
                clicked1 = 1
                if lineColor == 'white':
                    P1T_rectangle_1t_4.lineColor = 'black'
                    lineColor = 'black'
                    P1T_rectangle_color = 1
                    thisExp.addData('P1T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P1T_rectangle_1t_4.lineColor = 'white'
                    lineColor = 'white'
                    P1T_rectangle_color = 0
                    thisExp.addData('P1T_rectangle', 0)
        elif clicked1 == 1:
            clicked1 = 0
        
        if mouse_5.isPressedIn(P4T_rectangle_1t_4):
            if clicked4 == 0:
                clicked4 = 1
                if lineColor == 'white':
                    P4T_rectangle_1t_4.lineColor = 'black'
                    lineColor = 'black'
                    P4T_rectangle_color = 1
                    thisExp.addData('P4T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P4T_rectangle_1t_4.lineColor = 'white'
                    lineColor = 'white'
                    P4T_rectangle_color = 0
                    thisExp.addData('P4T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked4 == 1:
            clicked4 = 0
        
        if mouse_5.isPressedIn(P5T_rectangle_1t_4):
            if clicked5 == 0:
                clicked5 = 1
                if lineColor == 'white':
                    P5T_rectangle_1t_4.lineColor = 'black'
                    lineColor = 'black'
                    P5T_rectangle_color = 1
                    thisExp.addData('P5T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P5T_rectangle_1t_4.lineColor = 'white'
                    lineColor = 'white'
                    P5T_rectangle_color = 0
                    thisExp.addData('P5T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked5 == 1:
            clicked5 = 0
        
        if mouse_5.isPressedIn(P8T_rectangle_1t_4):
            if clicked8 == 0:
                clicked8 = 1
                if lineColor == 'white':
                    P8T_rectangle_1t_4.lineColor = 'black'
                    lineColor = 'black'
                    P8T_rectangle_color = 1
                    thisExp.addData('P8T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P8T_rectangle_1t_4.lineColor = 'white'
                    lineColor = 'white'
                    P8T_rectangle_color = 0
                    thisExp.addData('P8T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked8 == 1:
            clicked8 = 0
            
        if mouse_5.isPressedIn(P9T_rectangle_1t_4):
            if clicked9 == 0:
                clicked9 = 1
                if lineColor == 'white':
                    P9T_rectangle_1t_4.lineColor = 'black'
                    lineColor = 'black'
                    P9T_rectangle_color = 1
                    thisExp.addData('P9T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P9T_rectangle_1t_4.lineColor = 'white'
                    lineColor = 'white'
                    P9T_rectangle_color = 0
                    thisExp.addData('P9T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked9 == 1:
            clicked9 = 0
        
        if mouse_5.isPressedIn(finish_5):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        # *mouse_5* updates
        if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_5.frameNStart = frameN  # exact frame index
            mouse_5.tStart = t  # local t and not account for scr refresh
            mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_5.started', t)
            mouse_5.status = STARTED
            mouse_5.mouseClock.reset()
            prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
        
        # *P1T_rectangle_1t_4* updates
        if P1T_rectangle_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_rectangle_1t_4.frameNStart = frameN  # exact frame index
            P1T_rectangle_1t_4.tStart = t  # local t and not account for scr refresh
            P1T_rectangle_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_rectangle_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_rectangle_1t_4.started')
            P1T_rectangle_1t_4.setAutoDraw(True)
        
        # *P4T_rectangle_1t_4* updates
        if P4T_rectangle_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_rectangle_1t_4.frameNStart = frameN  # exact frame index
            P4T_rectangle_1t_4.tStart = t  # local t and not account for scr refresh
            P4T_rectangle_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_rectangle_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_rectangle_1t_4.started')
            P4T_rectangle_1t_4.setAutoDraw(True)
        
        # *P5T_rectangle_1t_4* updates
        if P5T_rectangle_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_rectangle_1t_4.frameNStart = frameN  # exact frame index
            P5T_rectangle_1t_4.tStart = t  # local t and not account for scr refresh
            P5T_rectangle_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_rectangle_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_rectangle_1t_4.started')
            P5T_rectangle_1t_4.setAutoDraw(True)
        
        # *P8T_rectangle_1t_4* updates
        if P8T_rectangle_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8T_rectangle_1t_4.frameNStart = frameN  # exact frame index
            P8T_rectangle_1t_4.tStart = t  # local t and not account for scr refresh
            P8T_rectangle_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8T_rectangle_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8T_rectangle_1t_4.started')
            P8T_rectangle_1t_4.setAutoDraw(True)
        
        # *P9T_rectangle_1t_4* updates
        if P9T_rectangle_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9T_rectangle_1t_4.frameNStart = frameN  # exact frame index
            P9T_rectangle_1t_4.tStart = t  # local t and not account for scr refresh
            P9T_rectangle_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9T_rectangle_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9T_rectangle_1t_4.started')
            P9T_rectangle_1t_4.setAutoDraw(True)
        
        # *P1T_1t_4* updates
        if P1T_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_4.frameNStart = frameN  # exact frame index
            P1T_1t_4.tStart = t  # local t and not account for scr refresh
            P1T_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_4.started')
            P1T_1t_4.setAutoDraw(True)
        
        # *P2T_1t_4* updates
        if P2T_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_4.frameNStart = frameN  # exact frame index
            P2T_1t_4.tStart = t  # local t and not account for scr refresh
            P2T_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_4.started')
            P2T_1t_4.setAutoDraw(True)
        
        # *P3T_1t_4* updates
        if P3T_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_4.frameNStart = frameN  # exact frame index
            P3T_1t_4.tStart = t  # local t and not account for scr refresh
            P3T_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_4.started')
            P3T_1t_4.setAutoDraw(True)
        
        # *P4T_1t_4* updates
        if P4T_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_4.frameNStart = frameN  # exact frame index
            P4T_1t_4.tStart = t  # local t and not account for scr refresh
            P4T_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_4.started')
            P4T_1t_4.setAutoDraw(True)
        
        # *P5T_1t_4* updates
        if P5T_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_4.frameNStart = frameN  # exact frame index
            P5T_1t_4.tStart = t  # local t and not account for scr refresh
            P5T_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_4.started')
            P5T_1t_4.setAutoDraw(True)
        
        # *P6T_1t_4* updates
        if P6T_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_4.frameNStart = frameN  # exact frame index
            P6T_1t_4.tStart = t  # local t and not account for scr refresh
            P6T_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_4.started')
            P6T_1t_4.setAutoDraw(True)
        
        # *P7t_1t_4* updates
        if P7t_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_4.frameNStart = frameN  # exact frame index
            P7t_1t_4.tStart = t  # local t and not account for scr refresh
            P7t_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_4.started')
            P7t_1t_4.setAutoDraw(True)
        
        # *P8t_1t_4* updates
        if P8t_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_4.frameNStart = frameN  # exact frame index
            P8t_1t_4.tStart = t  # local t and not account for scr refresh
            P8t_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_4.started')
            P8t_1t_4.setAutoDraw(True)
        
        # *P9t_1t_4* updates
        if P9t_1t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_4.frameNStart = frameN  # exact frame index
            P9t_1t_4.tStart = t  # local t and not account for scr refresh
            P9t_1t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_4.started')
            P9t_1t_4.setAutoDraw(True)
        
        # *finish_5* updates
        if finish_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_5.frameNStart = frameN  # exact frame index
            finish_5.tStart = t  # local t and not account for scr refresh
            finish_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_5.started')
            finish_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_1target_5objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_1target_5objects" ---
    for thisComponent in mng_test_1target_5objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_9
    #print(ClickCount1)
    ClickCount1 = 0
    P1T_rectangle_1t_4.lineColor = 'white'
    P4T_rectangle_1t_4.lineColor = 'white'
    P5T_rectangle_1t_4.lineColor = 'white'
    P8T_rectangle_1t_4.lineColor = 'white'
    P9T_rectangle_1t_4.lineColor = 'white'
    
    
    if objects == 5:
        if ((float(corr_p1) == float(P1T_rectangle_color)) & (float(corr_p4) == float(P4T_rectangle_color)) & (float(corr_p5) == float(P5T_rectangle_color)) & (float(corr_p8) == float(P8T_rectangle_color)) & (float(corr_p9) == float(P9T_rectangle_color))):
            mng_exptrials_t1.addData('accuracy_t1_o5', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t1.addData('accuracy_t1_o5', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime();  
    #end_trial = globalClock.getTime();
    #thisExp.addData("end", end_trial);
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    thisExp.addData("presented", 1)
    # store data for mng_exptrials_t1 (TrialHandler)
    x, y = mouse_5.getPos()
    buttons = mouse_5.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([P1T_rectangle_1t_4, P4T_rectangle_1t_4, P5T_rectangle_1t_4, P8T_rectangle_1t_4, P9T_rectangle_1t_4])
            clickableList = [P1T_rectangle_1t_4, P4T_rectangle_1t_4, P5T_rectangle_1t_4, P8T_rectangle_1t_4, P9T_rectangle_1t_4]
        except:
            clickableList = [[P1T_rectangle_1t_4, P4T_rectangle_1t_4, P5T_rectangle_1t_4, P8T_rectangle_1t_4, P9T_rectangle_1t_4]]
        for obj in clickableList:
            if obj.contains(mouse_5):
                gotValidClick = True
                mouse_5.clicked_name.append(obj.name)
    mng_exptrials_t1.addData('mouse_5.x', x)
    mng_exptrials_t1.addData('mouse_5.y', y)
    mng_exptrials_t1.addData('mouse_5.leftButton', buttons[0])
    mng_exptrials_t1.addData('mouse_5.midButton', buttons[1])
    mng_exptrials_t1.addData('mouse_5.rightButton', buttons[2])
    if len(mouse_5.clicked_name):
        mng_exptrials_t1.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
    # the Routine "mng_test_1target_5objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mng_exptrials_t1'


# --- Prepare to start Routine "mng_instructions2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# Run 'Begin Routine' code from code_27
corr_block_t1_o2 = int(mng_exptrials_t1.data['accuracy_t1_o2'].mean()*100)
print(corr_block_t1_o2)
corr_block_t1_o3 = int(mng_exptrials_t1.data['accuracy_t1_o3'].mean()*100)
print(corr_block_t1_o3)
corr_block_t1_o4 = int(mng_exptrials_t1.data['accuracy_t1_o4'].mean()*100)
print(corr_block_t1_o4)
corr_block_t1_o5 = int(mng_exptrials_t1.data['accuracy_t1_o5'].mean()*100)
print(corr_block_t1_o5)

meanb1 = (corr_block_t1_o2 +corr_block_t1_o3  + corr_block_t1_o4 + corr_block_t1_o5)/4
# keep track of which components have finished
mng_instructions2Components = [text_8, key_resp_7]
for thisComponent in mng_instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mng_instructions2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_8.started')
        text_8.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_7.started')
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # Run 'Each Frame' code from code_27
    if meanb1 < acc_thr:
            continueRoutine=False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mng_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mng_instructions2" ---
for thisComponent in mng_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "mng_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mng_practice2_loop = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='mng_practice2_loop')
thisExp.addLoop(mng_practice2_loop)  # add the loop to the experiment
thisMng_practice2_loop = mng_practice2_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMng_practice2_loop.rgb)
if thisMng_practice2_loop != None:
    for paramName in thisMng_practice2_loop:
        exec('{} = thisMng_practice2_loop[paramName]'.format(paramName))

for thisMng_practice2_loop in mng_practice2_loop:
    currentLoop = mng_practice2_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMng_practice2_loop.rgb)
    if thisMng_practice2_loop != None:
        for paramName in thisMng_practice2_loop:
            exec('{} = thisMng_practice2_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_practice_counter_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_25
    ncount2 = 0
    
    if meanb1 < acc_thr:
            mng_practice2_loop.finished=1
            
    
    # keep track of which components have finished
    mng_practice_counter_2Components = []
    for thisComponent in mng_practice_counter_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_practice_counter_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_25
        if meanb1 < acc_thr:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_practice_counter_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_practice_counter_2" ---
    for thisComponent in mng_practice_counter_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "mng_practice_counter_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mng_practice2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('mn_generaltask_practice2.xlsx'),
        seed=None, name='mng_practice2')
    thisExp.addLoop(mng_practice2)  # add the loop to the experiment
    thisMng_practice2 = mng_practice2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMng_practice2.rgb)
    if thisMng_practice2 != None:
        for paramName in thisMng_practice2:
            exec('{} = thisMng_practice2[paramName]'.format(paramName))
    
    for thisMng_practice2 in mng_practice2:
        currentLoop = mng_practice2
        # abbreviate parameter names if possible (e.g. rgb = thisMng_practice2.rgb)
        if thisMng_practice2 != None:
            for paramName in thisMng_practice2:
                exec('{} = thisMng_practice2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mng_blank_sample2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_18.keys = []
        key_resp_18.rt = []
        _key_resp_18_allKeys = []
        # keep track of which components have finished
        mng_blank_sample2Components = [blank_box_3, key_resp_18]
        for thisComponent in mng_blank_sample2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_blank_sample2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_box_3* updates
            if blank_box_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_box_3.frameNStart = frameN  # exact frame index
                blank_box_3.tStart = t  # local t and not account for scr refresh
                blank_box_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_box_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_box_3.started')
                blank_box_3.setAutoDraw(True)
            
            # *key_resp_18* updates
            waitOnFlip = False
            if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_18.frameNStart = frameN  # exact frame index
                key_resp_18.tStart = t  # local t and not account for scr refresh
                key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_18.started')
                key_resp_18.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_18.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_18_allKeys.extend(theseKeys)
                if len(_key_resp_18_allKeys):
                    key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                    key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_36
            if meanb1 < acc_thr:
                    continueRoutine=False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_blank_sample2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_blank_sample2" ---
        for thisComponent in mng_blank_sample2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_18.keys in ['', [], None]:  # No response was made
            key_resp_18.keys = None
        mng_practice2.addData('key_resp_18.keys',key_resp_18.keys)
        if key_resp_18.keys != None:  # we had a response
            mng_practice2.addData('key_resp_18.rt', key_resp_18.rt)
        # the Routine "mng_blank_sample2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "mng_probe_sample2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        P2_sample2_2t.setImage(probe_p2)
        P3_sample2_2t.setImage(probe_p3)
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # keep track of which components have finished
        mng_probe_sample2Components = [P2_sample2_2t, P3_sample2_2t, key_resp_11]
        for thisComponent in mng_probe_sample2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_probe_sample2" ---
        while continueRoutine and routineTimer.getTime() < 5.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *P2_sample2_2t* updates
            if P2_sample2_2t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2_sample2_2t.frameNStart = frameN  # exact frame index
                P2_sample2_2t.tStart = t  # local t and not account for scr refresh
                P2_sample2_2t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2_sample2_2t, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2_sample2_2t.started')
                P2_sample2_2t.setAutoDraw(True)
            if P2_sample2_2t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > P2_sample2_2t.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    P2_sample2_2t.tStop = t  # not accounting for scr refresh
                    P2_sample2_2t.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'P2_sample2_2t.stopped')
                    P2_sample2_2t.setAutoDraw(False)
            
            # *P3_sample2_2t* updates
            if P3_sample2_2t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P3_sample2_2t.frameNStart = frameN  # exact frame index
                P3_sample2_2t.tStart = t  # local t and not account for scr refresh
                P3_sample2_2t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P3_sample2_2t, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P3_sample2_2t.started')
                P3_sample2_2t.setAutoDraw(True)
            if P3_sample2_2t.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > P3_sample2_2t.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    P3_sample2_2t.tStop = t  # not accounting for scr refresh
                    P3_sample2_2t.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'P3_sample2_2t.stopped')
                    P3_sample2_2t.setAutoDraw(False)
            
            # *key_resp_11* updates
            waitOnFlip = False
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_11.started')
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_11.tStartRefresh + 5.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_11.tStop = t  # not accounting for scr refresh
                    key_resp_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_11.stopped')
                    key_resp_11.status = FINISHED
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=None, waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # Run 'Each Frame' code from code_29
            if meanb1 < acc_thr:
                    continueRoutine=False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_probe_sample2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_probe_sample2" ---
        for thisComponent in mng_probe_sample2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        mng_practice2.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            mng_practice2.addData('key_resp_11.rt', key_resp_11.rt)
        # Run 'End Routine' code from code_29
        beginning_trial = globalClock.getTime();
        thisExp.addData("start", beginning_trial);
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.500000)
        
        # --- Prepare to start Routine "mng_test_sample2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_19
        incorr = 1
        ClickCount1 = 0
        startTime = globalClock.getTime()
        end_trial = 0
        #beginning_trial = globalClock.getTime();  
        
        clicked1 = 0
        clicked2 = 0
        clicked3 = 0
        clicked4 = 0
        clicked5 = 0
        clicked6 = 0
        clicked6 = 0
        clicked7 = 0
        clicked8 = 0
        lineColor = 'white'
        msg = 'Incorrect'
        
        P1T_rectangle_color = 0
        P2T_rectangle_color = 0
        P3T_rectangle_color = 0
        P4T_rectangle_color = 0
        P5T_rectangle_color = 0
        P6T_rectangle_color = 0
        P7T_rectangle_color = 0
        P8T_rectangle_color = 0
        # setup some python lists for storing info about the mouse_15
        mouse_15.x = []
        mouse_15.y = []
        mouse_15.leftButton = []
        mouse_15.midButton = []
        mouse_15.rightButton = []
        mouse_15.time = []
        mouse_15.clicked_name = []
        gotValidClick = False  # until a click is received
        P1T_1t_14.setImage(test_p1)
        P2T_1t_14.setImage(test_p2)
        P3T_1t_14.setImage(test_p3)
        P4T_1t_14.setImage(test_p4)
        P5T_1t_14.setImage(test_p5)
        P6T_1t_14.setImage(test_p6)
        P7t_1t_14.setImage(test_p7)
        # keep track of which components have finished
        mng_test_sample2Components = [mouse_15, P2T_rectangle_2t_sample, P3T_rectangle_2t_sample, P6T_rectangle_2t_sample, P7T_rectangle_2t_sample, P1T_1t_14, P2T_1t_14, P3T_1t_14, P4T_1t_14, P5T_1t_14, P6T_1t_14, P7t_1t_14, finish_15]
        for thisComponent in mng_test_sample2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_test_sample2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_19
            if meanb1 < acc_thr:
                    continueRoutine=False
            #print(ClickCount1)
            
            if mouse_15.isPressedIn(P2T_rectangle_2t_sample):
                if clicked2 == 0:
                    clicked2 = 1
                    if lineColor == 'white':
                        P2T_rectangle_2t_sample.lineColor = 'black'
                        lineColor = 'black'
                        thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                        P2T_rectangle_color = 1
                    elif lineColor == 'black':
                        P2T_rectangle_2t_sample.lineColor = 'white'
                        lineColor = 'white'
                        thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                        P2T_rectangle_color = 0
            elif clicked2 == 1:
                clicked2 = 0
            
            if mouse_15.isPressedIn(P3T_rectangle_2t_sample):
                if clicked3 == 0:
                    clicked3 = 1
                    if lineColor == 'white':
                        P3T_rectangle_2t_sample.lineColor = 'black'
                        lineColor = 'black'
                        P3T_rectangle_color = 1
                        thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                    elif lineColor == 'black':
                        P3T_rectangle_2t_sample.lineColor = 'white'
                        lineColor = 'white'
                        P3T_rectangle_color = 0
                        thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
            elif clicked3 == 1:
                clicked3 = 0
            
            if mouse_15.isPressedIn(P6T_rectangle_2t_sample):
                if clicked6 == 0:
                    clicked6 = 1
                    if lineColor == 'white':
                        P6T_rectangle_2t_sample.lineColor = 'black'
                        lineColor = 'black'
                        P6T_rectangle_color = 1
                        thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                    elif lineColor == 'black':
                        P6T_rectangle_2t_sample.lineColor = 'white'
                        lineColor = 'white'
                        P6T_rectangle_color = 0
                        thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
            elif clicked6 == 1:
                clicked6 = 0
                
            if mouse_15.isPressedIn(P7T_rectangle_2t_sample):
                if clicked7 == 0:
                    clicked7 = 1
                    if lineColor == 'white':
                        P7T_rectangle_2t_sample.lineColor = 'black'
                        lineColor = 'black'
                        P7T_rectangle_color = 1
                        thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                    elif lineColor == 'black':
                        P7T_rectangle_2t_sample.lineColor = 'white'
                        lineColor = 'white'
                        P7T_rectangle_color = 0
                        thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
            elif clicked7 == 1:
                clicked7 = 0
               
            if mouse_15.isPressedIn(finish_15):
                continueRoutine = False
                end_trial = globalClock.getTime();
                thisExp.addData("end", end_trial);
                time_exp = (end_trial - beginning_trial)
                thisExp.addData("rt", time_exp);
            else:
                time_exp = 0;
                thisExp.addData("rt", time_exp);
            # *mouse_15* updates
            if mouse_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_15.frameNStart = frameN  # exact frame index
                mouse_15.tStart = t  # local t and not account for scr refresh
                mouse_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_15.started', t)
                mouse_15.status = STARTED
                mouse_15.mouseClock.reset()
                prevButtonState = mouse_15.getPressed()  # if button is down already this ISN'T a new click
            if mouse_15.status == STARTED:  # only update if started and not finished!
                buttons = mouse_15.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3])
                            clickableList = [P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3]
                        except:
                            clickableList = [[P2T_rectangle_1t_3, P3T_rectangle_1t_3, P6T_rectangle_1t_3, P7T_rectangle_1t_3]]
                        for obj in clickableList:
                            if obj.contains(mouse_15):
                                gotValidClick = True
                                mouse_15.clicked_name.append(obj.name)
                        x, y = mouse_15.getPos()
                        mouse_15.x.append(x)
                        mouse_15.y.append(y)
                        buttons = mouse_15.getPressed()
                        mouse_15.leftButton.append(buttons[0])
                        mouse_15.midButton.append(buttons[1])
                        mouse_15.rightButton.append(buttons[2])
                        mouse_15.time.append(mouse_15.mouseClock.getTime())
            
            # *P2T_rectangle_2t_sample* updates
            if P2T_rectangle_2t_sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2T_rectangle_2t_sample.frameNStart = frameN  # exact frame index
                P2T_rectangle_2t_sample.tStart = t  # local t and not account for scr refresh
                P2T_rectangle_2t_sample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2T_rectangle_2t_sample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2T_rectangle_2t_sample.started')
                P2T_rectangle_2t_sample.setAutoDraw(True)
            
            # *P3T_rectangle_2t_sample* updates
            if P3T_rectangle_2t_sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P3T_rectangle_2t_sample.frameNStart = frameN  # exact frame index
                P3T_rectangle_2t_sample.tStart = t  # local t and not account for scr refresh
                P3T_rectangle_2t_sample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P3T_rectangle_2t_sample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P3T_rectangle_2t_sample.started')
                P3T_rectangle_2t_sample.setAutoDraw(True)
            
            # *P6T_rectangle_2t_sample* updates
            if P6T_rectangle_2t_sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P6T_rectangle_2t_sample.frameNStart = frameN  # exact frame index
                P6T_rectangle_2t_sample.tStart = t  # local t and not account for scr refresh
                P6T_rectangle_2t_sample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P6T_rectangle_2t_sample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P6T_rectangle_2t_sample.started')
                P6T_rectangle_2t_sample.setAutoDraw(True)
            
            # *P7T_rectangle_2t_sample* updates
            if P7T_rectangle_2t_sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P7T_rectangle_2t_sample.frameNStart = frameN  # exact frame index
                P7T_rectangle_2t_sample.tStart = t  # local t and not account for scr refresh
                P7T_rectangle_2t_sample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P7T_rectangle_2t_sample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P7T_rectangle_2t_sample.started')
                P7T_rectangle_2t_sample.setAutoDraw(True)
            
            # *P1T_1t_14* updates
            if P1T_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P1T_1t_14.frameNStart = frameN  # exact frame index
                P1T_1t_14.tStart = t  # local t and not account for scr refresh
                P1T_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P1T_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1T_1t_14.started')
                P1T_1t_14.setAutoDraw(True)
            
            # *P2T_1t_14* updates
            if P2T_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2T_1t_14.frameNStart = frameN  # exact frame index
                P2T_1t_14.tStart = t  # local t and not account for scr refresh
                P2T_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2T_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2T_1t_14.started')
                P2T_1t_14.setAutoDraw(True)
            
            # *P3T_1t_14* updates
            if P3T_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P3T_1t_14.frameNStart = frameN  # exact frame index
                P3T_1t_14.tStart = t  # local t and not account for scr refresh
                P3T_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P3T_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P3T_1t_14.started')
                P3T_1t_14.setAutoDraw(True)
            
            # *P4T_1t_14* updates
            if P4T_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P4T_1t_14.frameNStart = frameN  # exact frame index
                P4T_1t_14.tStart = t  # local t and not account for scr refresh
                P4T_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P4T_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P4T_1t_14.started')
                P4T_1t_14.setAutoDraw(True)
            
            # *P5T_1t_14* updates
            if P5T_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P5T_1t_14.frameNStart = frameN  # exact frame index
                P5T_1t_14.tStart = t  # local t and not account for scr refresh
                P5T_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P5T_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P5T_1t_14.started')
                P5T_1t_14.setAutoDraw(True)
            
            # *P6T_1t_14* updates
            if P6T_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P6T_1t_14.frameNStart = frameN  # exact frame index
                P6T_1t_14.tStart = t  # local t and not account for scr refresh
                P6T_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P6T_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P6T_1t_14.started')
                P6T_1t_14.setAutoDraw(True)
            
            # *P7t_1t_14* updates
            if P7t_1t_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P7t_1t_14.frameNStart = frameN  # exact frame index
                P7t_1t_14.tStart = t  # local t and not account for scr refresh
                P7t_1t_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P7t_1t_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P7t_1t_14.started')
                P7t_1t_14.setAutoDraw(True)
            
            # *finish_15* updates
            if finish_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                finish_15.frameNStart = frameN  # exact frame index
                finish_15.tStart = t  # local t and not account for scr refresh
                finish_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(finish_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'finish_15.started')
                finish_15.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_test_sample2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_test_sample2" ---
        for thisComponent in mng_test_sample2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_19
        #print(ClickCount1)
        ClickCount1 = 0
        
        P2T_rectangle_2t_sample.lineColor = 'white'
        P3T_rectangle_2t_sample.lineColor = 'white'
        P6T_rectangle_2t_sample.lineColor = 'white'
        P7T_rectangle_2t_sample.lineColor = 'white'
        
        
        print("finish")
        print(float(P2T_rectangle_color))
        print(float(corr_p2))
        
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color))):
            mng_practice2.addData('accuracy', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            feedback_outcome_sound = feedback_sound[0]
            feedback_outcome_image = feedback_image[0]
            incorr = 0
        else:
            msg = "Incorrect"
            feedback_outcome_sound = feedback_sound[1]
            feedback_outcome_image = feedback_image[1]
            incorr = 1
            mng_practice2.addData('accuracy', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
        
        
        #end_trial = globalClock.getTime();
        #time_exp = (end_trial - beginning_trial)
        #thisExp.addData("rt", time_exp);
        
        if meanb1 < acc_thr:
                continueRoutine=False
                thisExp.addData("presented", 0)
        else:
            thisExp.addData("presented", 1)
        # store data for mng_practice2 (TrialHandler)
        mng_practice2.addData('mouse_15.x', mouse_15.x)
        mng_practice2.addData('mouse_15.y', mouse_15.y)
        mng_practice2.addData('mouse_15.leftButton', mouse_15.leftButton)
        mng_practice2.addData('mouse_15.midButton', mouse_15.midButton)
        mng_practice2.addData('mouse_15.rightButton', mouse_15.rightButton)
        mng_practice2.addData('mouse_15.time', mouse_15.time)
        mng_practice2.addData('mouse_15.clicked_name', mouse_15.clicked_name)
        # the Routine "mng_test_sample2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "mng_feedback_practice" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        image_2.setImage(feedback_outcome_image)
        # keep track of which components have finished
        mng_feedback_practiceComponents = [text_3, image_2]
        for thisComponent in mng_feedback_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mng_feedback_practice" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    text_3.setAutoDraw(False)
            # Run 'Each Frame' code from code_30
            if meanb1 < acc_thr:
                    continueRoutine=False
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.stopped')
                    image_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mng_feedback_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mng_feedback_practice" ---
        for thisComponent in mng_feedback_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'mng_practice2'
    
    
    # --- Prepare to start Routine "mng_check_practice_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_23
    ncount2 = ncount2 + 1
    
    if ncount2 == 1:
        nCorr2_loop1 = int(mng_practice2.data['accuracy'].mean()*100)
        print(nCorr2_loop1)
        if nCorr2_loop1 ==100:
            mng_practice2_loop.finished=1
            
    if ncount2 == 2:
        nCorr2_loop2 = int(mng_practice2.data['accuracy'].mean()*100)
        nCorr2_loop2 = nCorr2_loop2-nCorr2_loop1
        if nCorr2_loop2 == 100:
            mng_practice2_loop.finished=1
    # keep track of which components have finished
    mng_check_practice_2Components = []
    for thisComponent in mng_check_practice_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_check_practice_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_23
        if meanb1 < acc_thr:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_check_practice_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_check_practice_2" ---
    for thisComponent in mng_check_practice_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "mng_check_practice_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_repeat_instructions_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_24
    if ncount2 == 1:
        if nCorr2_loop1 == 100:
            continueRoutine=False
            
    if ncount2 == 2:
        if nCorr2_loop2 == 100:
            continueRoutine=False
    key_resp_15.keys = []
    key_resp_15.rt = []
    _key_resp_15_allKeys = []
    # keep track of which components have finished
    mng_repeat_instructions_2Components = [text_25, key_resp_15]
    for thisComponent in mng_repeat_instructions_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_repeat_instructions_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_24
        if meanb1 < acc_thr:
                continueRoutine=False
        
        # *text_25* updates
        if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_25.frameNStart = frameN  # exact frame index
            text_25.tStart = t  # local t and not account for scr refresh
            text_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_25.started')
            text_25.setAutoDraw(True)
        
        # *key_resp_15* updates
        waitOnFlip = False
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_15.started')
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_15_allKeys.extend(theseKeys)
            if len(_key_resp_15_allKeys):
                key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_repeat_instructions_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_repeat_instructions_2" ---
    for thisComponent in mng_repeat_instructions_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_15.keys in ['', [], None]:  # No response was made
        key_resp_15.keys = None
    mng_practice2_loop.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        mng_practice2_loop.addData('key_resp_15.rt', key_resp_15.rt)
    # the Routine "mng_repeat_instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'mng_practice2_loop'


# --- Prepare to start Routine "mng_ready_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_21.keys = []
key_resp_21.rt = []
_key_resp_21_allKeys = []
# keep track of which components have finished
mng_ready_3Components = [key_resp_21, text_26]
for thisComponent in mng_ready_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mng_ready_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_21* updates
    waitOnFlip = False
    if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.tStart = t  # local t and not account for scr refresh
        key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_21.started')
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_21.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_21.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_21_allKeys.extend(theseKeys)
        if len(_key_resp_21_allKeys):
            key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
            key_resp_21.rt = _key_resp_21_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_26.started')
        text_26.setAutoDraw(True)
    # Run 'Each Frame' code from code_39
    if meanb1 < acc_thr:
            continueRoutine=False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mng_ready_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mng_ready_3" ---
for thisComponent in mng_ready_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_21.keys in ['', [], None]:  # No response was made
    key_resp_21.keys = None
thisExp.addData('key_resp_21.keys',key_resp_21.keys)
if key_resp_21.keys != None:  # we had a response
    thisExp.addData('key_resp_21.rt', key_resp_21.rt)
thisExp.nextEntry()
# the Routine "mng_ready_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mng_exptrials_t2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mn_generaltask_t2trials_final.xlsx'),
    seed=None, name='mng_exptrials_t2')
thisExp.addLoop(mng_exptrials_t2)  # add the loop to the experiment
thisMng_exptrials_t2 = mng_exptrials_t2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t2.rgb)
if thisMng_exptrials_t2 != None:
    for paramName in thisMng_exptrials_t2:
        exec('{} = thisMng_exptrials_t2[paramName]'.format(paramName))

for thisMng_exptrials_t2 in mng_exptrials_t2:
    currentLoop = mng_exptrials_t2
    # abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t2.rgb)
    if thisMng_exptrials_t2 != None:
        for paramName in thisMng_exptrials_t2:
            exec('{} = thisMng_exptrials_t2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_blank_b2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # keep track of which components have finished
    mng_blank_b2Components = [blank_box_2, key_resp_17]
    for thisComponent in mng_blank_b2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_blank_b2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_box_2* updates
        if blank_box_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_box_2.frameNStart = frameN  # exact frame index
            blank_box_2.tStart = t  # local t and not account for scr refresh
            blank_box_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_box_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_box_2.started')
            blank_box_2.setAutoDraw(True)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_17.started')
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_35
        if meanb1 < acc_thr:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_blank_b2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_blank_b2" ---
    for thisComponent in mng_blank_b2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    mng_exptrials_t2.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        mng_exptrials_t2.addData('key_resp_17.rt', key_resp_17.rt)
    # the Routine "mng_blank_b2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_probe_2target" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    P2_sample_2t.setImage(probe_p2)
    P3_sample_2t.setImage(probe_p3)
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    mng_probe_2targetComponents = [P2_sample_2t, P3_sample_2t, key_resp_8]
    for thisComponent in mng_probe_2targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_probe_2target" ---
    while continueRoutine and routineTimer.getTime() < 5.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *P2_sample_2t* updates
        if P2_sample_2t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2_sample_2t.frameNStart = frameN  # exact frame index
            P2_sample_2t.tStart = t  # local t and not account for scr refresh
            P2_sample_2t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2_sample_2t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2_sample_2t.started')
            P2_sample_2t.setAutoDraw(True)
        if P2_sample_2t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P2_sample_2t.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P2_sample_2t.tStop = t  # not accounting for scr refresh
                P2_sample_2t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2_sample_2t.stopped')
                P2_sample_2t.setAutoDraw(False)
        
        # *P3_sample_2t* updates
        if P3_sample_2t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3_sample_2t.frameNStart = frameN  # exact frame index
            P3_sample_2t.tStart = t  # local t and not account for scr refresh
            P3_sample_2t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3_sample_2t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3_sample_2t.started')
            P3_sample_2t.setAutoDraw(True)
        if P3_sample_2t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P3_sample_2t.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                P3_sample_2t.tStop = t  # not accounting for scr refresh
                P3_sample_2t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P3_sample_2t.stopped')
                P3_sample_2t.setAutoDraw(False)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_8.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_8.tStop = t  # not accounting for scr refresh
                key_resp_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.stopped')
                key_resp_8.status = FINISHED
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=None, waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
        # Run 'Each Frame' code from code_32
        if meanb1 < acc_thr:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_probe_2targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_probe_2target" ---
    for thisComponent in mng_probe_2targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    mng_exptrials_t2.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        mng_exptrials_t2.addData('key_resp_8.rt', key_resp_8.rt)
    # Run 'End Routine' code from code_32
    beginning_trial = globalClock.getTime();
    thisExp.addData("start", beginning_trial);
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.500000)
    
    # --- Prepare to start Routine "mng_test_2target_4objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_10
    if objects > 4:
        continueRoutine=False
    #beginning_trial = globalClock.getTime();
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    # setup some python lists for storing info about the mouse_18
    gotValidClick = False  # until a click is received
    P1T_1t_5.setImage(test_p1)
    P2T_1t_5.setImage(test_p2)
    P3T_1t_5.setImage(test_p3)
    P4T_1t_5.setImage(test_p4)
    P5T_1t_5.setImage(test_p5)
    P6T_1t_5.setImage(test_p6)
    P7t_1t_5.setImage(test_p7)
    P8t_1t_5.setImage(test_p8)
    P9t_1t_5.setImage(test_p9)
    # keep track of which components have finished
    mng_test_2target_4objectsComponents = [mouse_18, P2T_rectangle_2t_4, P3T_rectangle_2t_4, P6T_rectangle_2t_4, P7T_rectangle_2t_4, P1T_1t_5, P2T_1t_5, P3T_1t_5, P4T_1t_5, P5T_1t_5, P6T_1t_5, P7t_1t_5, P8t_1t_5, P9t_1t_5, finish_6]
    for thisComponent in mng_test_2target_4objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_2target_4objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_10
        if meanb1 < acc_thr:
                continueRoutine=False
        #print(ClickCount1)
        
        if mouse_18.isPressedIn(P2T_rectangle_2t_4):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_2t_4.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_2t_4.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_18.isPressedIn(P3T_rectangle_2t_4):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_2t_4.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_2t_4.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_18.isPressedIn(P6T_rectangle_2t_4):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_2t_4.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_2t_4.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_18.isPressedIn(P7T_rectangle_2t_4):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_2t_4.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_2t_4.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
           
        
        if mouse_18.isPressedIn(finish_6):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_18* updates
        if mouse_18.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_18.frameNStart = frameN  # exact frame index
            mouse_18.tStart = t  # local t and not account for scr refresh
            mouse_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_18.started', t)
            mouse_18.status = STARTED
            mouse_18.mouseClock.reset()
            prevButtonState = mouse_18.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_2t_4* updates
        if P2T_rectangle_2t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_2t_4.frameNStart = frameN  # exact frame index
            P2T_rectangle_2t_4.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_2t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_2t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_2t_4.started')
            P2T_rectangle_2t_4.setAutoDraw(True)
        
        # *P3T_rectangle_2t_4* updates
        if P3T_rectangle_2t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_2t_4.frameNStart = frameN  # exact frame index
            P3T_rectangle_2t_4.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_2t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_2t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_2t_4.started')
            P3T_rectangle_2t_4.setAutoDraw(True)
        
        # *P6T_rectangle_2t_4* updates
        if P6T_rectangle_2t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_2t_4.frameNStart = frameN  # exact frame index
            P6T_rectangle_2t_4.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_2t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_2t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_2t_4.started')
            P6T_rectangle_2t_4.setAutoDraw(True)
        
        # *P7T_rectangle_2t_4* updates
        if P7T_rectangle_2t_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_2t_4.frameNStart = frameN  # exact frame index
            P7T_rectangle_2t_4.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_2t_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_2t_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_2t_4.started')
            P7T_rectangle_2t_4.setAutoDraw(True)
        
        # *P1T_1t_5* updates
        if P1T_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_5.frameNStart = frameN  # exact frame index
            P1T_1t_5.tStart = t  # local t and not account for scr refresh
            P1T_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_5.started')
            P1T_1t_5.setAutoDraw(True)
        
        # *P2T_1t_5* updates
        if P2T_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_5.frameNStart = frameN  # exact frame index
            P2T_1t_5.tStart = t  # local t and not account for scr refresh
            P2T_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_5.started')
            P2T_1t_5.setAutoDraw(True)
        
        # *P3T_1t_5* updates
        if P3T_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_5.frameNStart = frameN  # exact frame index
            P3T_1t_5.tStart = t  # local t and not account for scr refresh
            P3T_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_5.started')
            P3T_1t_5.setAutoDraw(True)
        
        # *P4T_1t_5* updates
        if P4T_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_5.frameNStart = frameN  # exact frame index
            P4T_1t_5.tStart = t  # local t and not account for scr refresh
            P4T_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_5.started')
            P4T_1t_5.setAutoDraw(True)
        
        # *P5T_1t_5* updates
        if P5T_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_5.frameNStart = frameN  # exact frame index
            P5T_1t_5.tStart = t  # local t and not account for scr refresh
            P5T_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_5.started')
            P5T_1t_5.setAutoDraw(True)
        
        # *P6T_1t_5* updates
        if P6T_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_5.frameNStart = frameN  # exact frame index
            P6T_1t_5.tStart = t  # local t and not account for scr refresh
            P6T_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_5.started')
            P6T_1t_5.setAutoDraw(True)
        
        # *P7t_1t_5* updates
        if P7t_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_5.frameNStart = frameN  # exact frame index
            P7t_1t_5.tStart = t  # local t and not account for scr refresh
            P7t_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_5.started')
            P7t_1t_5.setAutoDraw(True)
        
        # *P8t_1t_5* updates
        if P8t_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_5.frameNStart = frameN  # exact frame index
            P8t_1t_5.tStart = t  # local t and not account for scr refresh
            P8t_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_5.started')
            P8t_1t_5.setAutoDraw(True)
        
        # *P9t_1t_5* updates
        if P9t_1t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_5.frameNStart = frameN  # exact frame index
            P9t_1t_5.tStart = t  # local t and not account for scr refresh
            P9t_1t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_5.started')
            P9t_1t_5.setAutoDraw(True)
        
        # *finish_6* updates
        if finish_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_6.frameNStart = frameN  # exact frame index
            finish_6.tStart = t  # local t and not account for scr refresh
            finish_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_6.started')
            finish_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_2target_4objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_2target_4objects" ---
    for thisComponent in mng_test_2target_4objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_10
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_2t_4.lineColor = 'white'
    P3T_rectangle_2t_4.lineColor = 'white'
    P6T_rectangle_2t_4.lineColor = 'white'
    P7T_rectangle_2t_4.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects == 4:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color))):
            mng_exptrials_t2.addData('accuracy_t2_o4', 1) #OR exp.addData('letter', letter)
            #mng_exptrials_t2.addData('test_accuracy', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t2.addData('accuracy_t2_o4', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t2 (TrialHandler)
    x, y = mouse_18.getPos()
    buttons = mouse_18.getPressed()
    mng_exptrials_t2.addData('mouse_18.x', x)
    mng_exptrials_t2.addData('mouse_18.y', y)
    mng_exptrials_t2.addData('mouse_18.leftButton', buttons[0])
    mng_exptrials_t2.addData('mouse_18.midButton', buttons[1])
    mng_exptrials_t2.addData('mouse_18.rightButton', buttons[2])
    # the Routine "mng_test_2target_4objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_2target_5objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_11
    if objects > 5:
        continueRoutine=False
    
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    # setup some python lists for storing info about the mouse_7
    gotValidClick = False  # until a click is received
    P1T_1t_6.setImage(test_p1)
    P2T_1t_6.setImage(test_p2)
    P3T_1t_6.setImage(test_p3)
    P4T_1t_6.setImage(test_p4)
    P5T_1t_6.setImage(test_p5)
    P6T_1t_6.setImage(test_p6)
    P7t_1t_6.setImage(test_p7)
    P8t_1t_6.setImage(test_p8)
    P9t_1t_6.setImage(test_p9)
    # keep track of which components have finished
    mng_test_2target_5objectsComponents = [mouse_7, P1T_rectangle_2t_5, P4T_rectangle_2t_5, P5T_rectangle_2t_5, P8T_rectangle_2t_5, P9T_rectangle_2t_5, P1T_1t_6, P2T_1t_6, P3T_1t_6, P4T_1t_6, P5T_1t_6, P6T_1t_6, P7t_1t_6, P8t_1t_6, P9t_1t_6, finish_7]
    for thisComponent in mng_test_2target_5objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_2target_5objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_11
        if meanb1 < acc_thr:
                continueRoutine=False
        #print(ClickCount1)
        if mouse_7.isPressedIn(P1T_rectangle_2t_5):
            if clicked1 == 0:
                clicked1 = 1
                if lineColor == 'white':
                    P1T_rectangle_2t_5.lineColor = 'black'
                    lineColor = 'black'
                    P1T_rectangle_color = 1
                    thisExp.addData('P1T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P1T_rectangle_2t_5.lineColor = 'white'
                    lineColor = 'white'
                    P1T_rectangle_color = 0
                    thisExp.addData('P1T_rectangle', 0)
        elif clicked1 == 1:
            clicked1 = 0
        
        if mouse_7.isPressedIn(P4T_rectangle_2t_5):
            if clicked4 == 0:
                clicked4 = 1
                if lineColor == 'white':
                    P4T_rectangle_2t_5.lineColor = 'black'
                    lineColor = 'black'
                    P4T_rectangle_color = 1
                    thisExp.addData('P4T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P4T_rectangle_2t_5.lineColor = 'white'
                    lineColor = 'white'
                    P4T_rectangle_color = 0
                    thisExp.addData('P4T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked4 == 1:
            clicked4 = 0
        
        if mouse_7.isPressedIn(P5T_rectangle_2t_5):
            if clicked5 == 0:
                clicked5 = 1
                if lineColor == 'white':
                    P5T_rectangle_2t_5.lineColor = 'black'
                    lineColor = 'black'
                    P5T_rectangle_color = 1
                    thisExp.addData('P5T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P5T_rectangle_2t_5.lineColor = 'white'
                    lineColor = 'white'
                    P5T_rectangle_color = 0
                    thisExp.addData('P5T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked5 == 1:
            clicked5 = 0
        
        if mouse_7.isPressedIn(P8T_rectangle_2t_5):
            if clicked8 == 0:
                clicked8 = 1
                if lineColor == 'white':
                    P8T_rectangle_2t_5.lineColor = 'black'
                    lineColor = 'black'
                    P8T_rectangle_color = 1
                    thisExp.addData('P8T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P8T_rectangle_2t_5.lineColor = 'white'
                    lineColor = 'white'
                    P8T_rectangle_color = 0
                    thisExp.addData('P8T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked8 == 1:
            clicked8 = 0
            
        if mouse_7.isPressedIn(P9T_rectangle_2t_5):
            if clicked9 == 0:
                clicked9 = 1
                if lineColor == 'white':
                    P9T_rectangle_2t_5.lineColor = 'black'
                    lineColor = 'black'
                    P9T_rectangle_color = 1
                    thisExp.addData('P9T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P9T_rectangle_2t_5.lineColor = 'white'
                    lineColor = 'white'
                    P9T_rectangle_color = 0
                    thisExp.addData('P9T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked9 == 1:
            clicked9 = 0
        
        if mouse_7.isPressedIn(finish_7):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_7* updates
        if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.tStart = t  # local t and not account for scr refresh
            mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_7.started', t)
            mouse_7.status = STARTED
            mouse_7.mouseClock.reset()
            prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
        
        # *P1T_rectangle_2t_5* updates
        if P1T_rectangle_2t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_rectangle_2t_5.frameNStart = frameN  # exact frame index
            P1T_rectangle_2t_5.tStart = t  # local t and not account for scr refresh
            P1T_rectangle_2t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_rectangle_2t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_rectangle_2t_5.started')
            P1T_rectangle_2t_5.setAutoDraw(True)
        
        # *P4T_rectangle_2t_5* updates
        if P4T_rectangle_2t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_rectangle_2t_5.frameNStart = frameN  # exact frame index
            P4T_rectangle_2t_5.tStart = t  # local t and not account for scr refresh
            P4T_rectangle_2t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_rectangle_2t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_rectangle_2t_5.started')
            P4T_rectangle_2t_5.setAutoDraw(True)
        
        # *P5T_rectangle_2t_5* updates
        if P5T_rectangle_2t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_rectangle_2t_5.frameNStart = frameN  # exact frame index
            P5T_rectangle_2t_5.tStart = t  # local t and not account for scr refresh
            P5T_rectangle_2t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_rectangle_2t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_rectangle_2t_5.started')
            P5T_rectangle_2t_5.setAutoDraw(True)
        
        # *P8T_rectangle_2t_5* updates
        if P8T_rectangle_2t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8T_rectangle_2t_5.frameNStart = frameN  # exact frame index
            P8T_rectangle_2t_5.tStart = t  # local t and not account for scr refresh
            P8T_rectangle_2t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8T_rectangle_2t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8T_rectangle_2t_5.started')
            P8T_rectangle_2t_5.setAutoDraw(True)
        
        # *P9T_rectangle_2t_5* updates
        if P9T_rectangle_2t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9T_rectangle_2t_5.frameNStart = frameN  # exact frame index
            P9T_rectangle_2t_5.tStart = t  # local t and not account for scr refresh
            P9T_rectangle_2t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9T_rectangle_2t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9T_rectangle_2t_5.started')
            P9T_rectangle_2t_5.setAutoDraw(True)
        
        # *P1T_1t_6* updates
        if P1T_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_6.frameNStart = frameN  # exact frame index
            P1T_1t_6.tStart = t  # local t and not account for scr refresh
            P1T_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_6.started')
            P1T_1t_6.setAutoDraw(True)
        
        # *P2T_1t_6* updates
        if P2T_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_6.frameNStart = frameN  # exact frame index
            P2T_1t_6.tStart = t  # local t and not account for scr refresh
            P2T_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_6.started')
            P2T_1t_6.setAutoDraw(True)
        
        # *P3T_1t_6* updates
        if P3T_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_6.frameNStart = frameN  # exact frame index
            P3T_1t_6.tStart = t  # local t and not account for scr refresh
            P3T_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_6.started')
            P3T_1t_6.setAutoDraw(True)
        
        # *P4T_1t_6* updates
        if P4T_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_6.frameNStart = frameN  # exact frame index
            P4T_1t_6.tStart = t  # local t and not account for scr refresh
            P4T_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_6.started')
            P4T_1t_6.setAutoDraw(True)
        
        # *P5T_1t_6* updates
        if P5T_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_6.frameNStart = frameN  # exact frame index
            P5T_1t_6.tStart = t  # local t and not account for scr refresh
            P5T_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_6.started')
            P5T_1t_6.setAutoDraw(True)
        
        # *P6T_1t_6* updates
        if P6T_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_6.frameNStart = frameN  # exact frame index
            P6T_1t_6.tStart = t  # local t and not account for scr refresh
            P6T_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_6.started')
            P6T_1t_6.setAutoDraw(True)
        
        # *P7t_1t_6* updates
        if P7t_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_6.frameNStart = frameN  # exact frame index
            P7t_1t_6.tStart = t  # local t and not account for scr refresh
            P7t_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_6.started')
            P7t_1t_6.setAutoDraw(True)
        
        # *P8t_1t_6* updates
        if P8t_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_6.frameNStart = frameN  # exact frame index
            P8t_1t_6.tStart = t  # local t and not account for scr refresh
            P8t_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_6.started')
            P8t_1t_6.setAutoDraw(True)
        
        # *P9t_1t_6* updates
        if P9t_1t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_6.frameNStart = frameN  # exact frame index
            P9t_1t_6.tStart = t  # local t and not account for scr refresh
            P9t_1t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_6.started')
            P9t_1t_6.setAutoDraw(True)
        
        # *finish_7* updates
        if finish_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_7.frameNStart = frameN  # exact frame index
            finish_7.tStart = t  # local t and not account for scr refresh
            finish_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_7.started')
            finish_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_2target_5objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_2target_5objects" ---
    for thisComponent in mng_test_2target_5objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_11
    #print(ClickCount1)
    ClickCount1 = 0
    P1T_rectangle_2t_5.lineColor = 'white'
    P4T_rectangle_2t_5.lineColor = 'white'
    P5T_rectangle_2t_5.lineColor = 'white'
    P8T_rectangle_2t_5.lineColor = 'white'
    P9T_rectangle_2t_5.lineColor = 'white'
    
    if objects == 5:
        if ((float(corr_p1) == float(P1T_rectangle_color)) & (float(corr_p4) == float(P4T_rectangle_color)) & (float(corr_p5) == float(P5T_rectangle_color)) & (float(corr_p8) == float(P8T_rectangle_color)) & (float(corr_p9) == float(P9T_rectangle_color))):
            mng_exptrials_t2.addData('accuracy_t2_o5', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t2.addData('accuracy_t2_o5', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t2 (TrialHandler)
    x, y = mouse_7.getPos()
    buttons = mouse_7.getPressed()
    mng_exptrials_t2.addData('mouse_7.x', x)
    mng_exptrials_t2.addData('mouse_7.y', y)
    mng_exptrials_t2.addData('mouse_7.leftButton', buttons[0])
    mng_exptrials_t2.addData('mouse_7.midButton', buttons[1])
    mng_exptrials_t2.addData('mouse_7.rightButton', buttons[2])
    # the Routine "mng_test_2target_5objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_2target_6objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_12
    if objects < 5:
        continueRoutine=False
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    clicked10 = 0
    clicked11 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    P10T_rectangle_color = 0
    P11T_rectangle_color = 0
    
    # setup some python lists for storing info about the mouse_8
    gotValidClick = False  # until a click is received
    P1T_1t_7.setImage(test_p1)
    P2T_1t_7.setImage(test_p2)
    P3T_1t_7.setImage(test_p3)
    P4T_1t_7.setImage(test_p4)
    P5T_1t_7.setImage(test_p5)
    P6T_1t_7.setImage(test_p6)
    P7t_1t_7.setImage(test_p7)
    P8t_1t_7.setImage(test_p8)
    P9t_1t_7.setImage(test_p9)
    P10t_1t_7.setImage(test_p10)
    P11_1t_7.setImage(test_p11)
    # keep track of which components have finished
    mng_test_2target_6objectsComponents = [mouse_8, P2T_rectangle_2t_6, P3T_rectangle_2t_6, P6T_rectangle_2t_6, P7T_rectangle_2t_6, P10T_rectangle_2t_6, P11T_rectangle_2t_6, P1T_1t_7, P2T_1t_7, P3T_1t_7, P4T_1t_7, P5T_1t_7, P6T_1t_7, P7t_1t_7, P8t_1t_7, P9t_1t_7, P10t_1t_7, P11_1t_7, finish_8]
    for thisComponent in mng_test_2target_6objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_2target_6objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_12
        if meanb1 < acc_thr:
                continueRoutine=False
        #print(ClickCount1)
        
        if mouse_8.isPressedIn(P2T_rectangle_2t_6):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_2t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_2t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_8.isPressedIn(P3T_rectangle_2t_6):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_2t_6.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_2t_6.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_8.isPressedIn(P6T_rectangle_2t_6):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_2t_6.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_2t_6.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_8.isPressedIn(P7T_rectangle_2t_6):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_2t_6.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_2t_6.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
        
        if mouse_8.isPressedIn(P10T_rectangle_2t_6):
            if clicked10 == 0:
                clicked10 = 1
                if lineColor == 'white':
                    P10T_rectangle_2t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P10T_rectangle', 1) #OR exp.addData('letter', letter)
                    P10T_rectangle_color = 1
                elif lineColor == 'black':
                    P10T_rectangle_2t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P10T_rectangle', 0) #OR exp.addData('letter', letter)
                    P10T_rectangle_color = 0
        elif clicked10 == 1:
            clicked10 = 0
            
        if mouse_8.isPressedIn(P11T_rectangle_2t_6):
            if clicked11 == 0:
                clicked11 = 1
                if lineColor == 'white':
                    P11T_rectangle_2t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P11T_rectangle', 1) #OR exp.addData('letter', letter)
                    P11T_rectangle_color = 1
                elif lineColor == 'black':
                    P11T_rectangle_2t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P11T_rectangle', 0) #OR exp.addData('letter', letter)
                    P11T_rectangle_color = 0
        elif clicked11 == 1:
            clicked11 = 0
        
        if mouse_8.isPressedIn(finish_8):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_8* updates
        if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_8.started', t)
            mouse_8.status = STARTED
            mouse_8.mouseClock.reset()
            prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_2t_6* updates
        if P2T_rectangle_2t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_2t_6.frameNStart = frameN  # exact frame index
            P2T_rectangle_2t_6.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_2t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_2t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_2t_6.started')
            P2T_rectangle_2t_6.setAutoDraw(True)
        
        # *P3T_rectangle_2t_6* updates
        if P3T_rectangle_2t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_2t_6.frameNStart = frameN  # exact frame index
            P3T_rectangle_2t_6.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_2t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_2t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_2t_6.started')
            P3T_rectangle_2t_6.setAutoDraw(True)
        
        # *P6T_rectangle_2t_6* updates
        if P6T_rectangle_2t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_2t_6.frameNStart = frameN  # exact frame index
            P6T_rectangle_2t_6.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_2t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_2t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_2t_6.started')
            P6T_rectangle_2t_6.setAutoDraw(True)
        
        # *P7T_rectangle_2t_6* updates
        if P7T_rectangle_2t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_2t_6.frameNStart = frameN  # exact frame index
            P7T_rectangle_2t_6.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_2t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_2t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_2t_6.started')
            P7T_rectangle_2t_6.setAutoDraw(True)
        
        # *P10T_rectangle_2t_6* updates
        if P10T_rectangle_2t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10T_rectangle_2t_6.frameNStart = frameN  # exact frame index
            P10T_rectangle_2t_6.tStart = t  # local t and not account for scr refresh
            P10T_rectangle_2t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10T_rectangle_2t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10T_rectangle_2t_6.started')
            P10T_rectangle_2t_6.setAutoDraw(True)
        
        # *P11T_rectangle_2t_6* updates
        if P11T_rectangle_2t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11T_rectangle_2t_6.frameNStart = frameN  # exact frame index
            P11T_rectangle_2t_6.tStart = t  # local t and not account for scr refresh
            P11T_rectangle_2t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11T_rectangle_2t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11T_rectangle_2t_6.started')
            P11T_rectangle_2t_6.setAutoDraw(True)
        
        # *P1T_1t_7* updates
        if P1T_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_7.frameNStart = frameN  # exact frame index
            P1T_1t_7.tStart = t  # local t and not account for scr refresh
            P1T_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_7.started')
            P1T_1t_7.setAutoDraw(True)
        
        # *P2T_1t_7* updates
        if P2T_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_7.frameNStart = frameN  # exact frame index
            P2T_1t_7.tStart = t  # local t and not account for scr refresh
            P2T_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_7.started')
            P2T_1t_7.setAutoDraw(True)
        
        # *P3T_1t_7* updates
        if P3T_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_7.frameNStart = frameN  # exact frame index
            P3T_1t_7.tStart = t  # local t and not account for scr refresh
            P3T_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_7.started')
            P3T_1t_7.setAutoDraw(True)
        
        # *P4T_1t_7* updates
        if P4T_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_7.frameNStart = frameN  # exact frame index
            P4T_1t_7.tStart = t  # local t and not account for scr refresh
            P4T_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_7.started')
            P4T_1t_7.setAutoDraw(True)
        
        # *P5T_1t_7* updates
        if P5T_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_7.frameNStart = frameN  # exact frame index
            P5T_1t_7.tStart = t  # local t and not account for scr refresh
            P5T_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_7.started')
            P5T_1t_7.setAutoDraw(True)
        
        # *P6T_1t_7* updates
        if P6T_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_7.frameNStart = frameN  # exact frame index
            P6T_1t_7.tStart = t  # local t and not account for scr refresh
            P6T_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_7.started')
            P6T_1t_7.setAutoDraw(True)
        
        # *P7t_1t_7* updates
        if P7t_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_7.frameNStart = frameN  # exact frame index
            P7t_1t_7.tStart = t  # local t and not account for scr refresh
            P7t_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_7.started')
            P7t_1t_7.setAutoDraw(True)
        
        # *P8t_1t_7* updates
        if P8t_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_7.frameNStart = frameN  # exact frame index
            P8t_1t_7.tStart = t  # local t and not account for scr refresh
            P8t_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_7.started')
            P8t_1t_7.setAutoDraw(True)
        
        # *P9t_1t_7* updates
        if P9t_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_7.frameNStart = frameN  # exact frame index
            P9t_1t_7.tStart = t  # local t and not account for scr refresh
            P9t_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_7.started')
            P9t_1t_7.setAutoDraw(True)
        
        # *P10t_1t_7* updates
        if P10t_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10t_1t_7.frameNStart = frameN  # exact frame index
            P10t_1t_7.tStart = t  # local t and not account for scr refresh
            P10t_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10t_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10t_1t_7.started')
            P10t_1t_7.setAutoDraw(True)
        
        # *P11_1t_7* updates
        if P11_1t_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11_1t_7.frameNStart = frameN  # exact frame index
            P11_1t_7.tStart = t  # local t and not account for scr refresh
            P11_1t_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11_1t_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11_1t_7.started')
            P11_1t_7.setAutoDraw(True)
        
        # *finish_8* updates
        if finish_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_8.frameNStart = frameN  # exact frame index
            finish_8.tStart = t  # local t and not account for scr refresh
            finish_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_8.started')
            finish_8.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_2target_6objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_2target_6objects" ---
    for thisComponent in mng_test_2target_6objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_12
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_2t_6.lineColor = 'white'
    P3T_rectangle_2t_6.lineColor = 'white'
    P6T_rectangle_2t_6.lineColor = 'white'
    P7T_rectangle_2t_6.lineColor = 'white'
    P10T_rectangle_2t_6.lineColor = 'white'
    P11T_rectangle_2t_6.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects == 6:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color)) & (float(corr_p10) == float(P10T_rectangle_color)) & (float(corr_p11) == float(P11T_rectangle_color))):
            mng_exptrials_t2.addData('accuracy_t2_o6', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t2.addData('accuracy_t2_o6', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t2 (TrialHandler)
    x, y = mouse_8.getPos()
    buttons = mouse_8.getPressed()
    mng_exptrials_t2.addData('mouse_8.x', x)
    mng_exptrials_t2.addData('mouse_8.y', y)
    mng_exptrials_t2.addData('mouse_8.leftButton', buttons[0])
    mng_exptrials_t2.addData('mouse_8.midButton', buttons[1])
    mng_exptrials_t2.addData('mouse_8.rightButton', buttons[2])
    # the Routine "mng_test_2target_6objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mng_exptrials_t2'


# set up handler to look after randomisation of conditions etc
mng_exptrials_t3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mn_generaltask_t3trials_final.xlsx'),
    seed=None, name='mng_exptrials_t3')
thisExp.addLoop(mng_exptrials_t3)  # add the loop to the experiment
thisMng_exptrials_t3 = mng_exptrials_t3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t3.rgb)
if thisMng_exptrials_t3 != None:
    for paramName in thisMng_exptrials_t3:
        exec('{} = thisMng_exptrials_t3[paramName]'.format(paramName))

for thisMng_exptrials_t3 in mng_exptrials_t3:
    currentLoop = mng_exptrials_t3
    # abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t3.rgb)
    if thisMng_exptrials_t3 != None:
        for paramName in thisMng_exptrials_t3:
            exec('{} = thisMng_exptrials_t3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_blank_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
    # Run 'Begin Routine' code from code_37
    corr_block_t2_o4 = int(mng_exptrials_t2.data['accuracy_t2_o4'].mean()*100)
    corr_block_t2_o5 = int(mng_exptrials_t2.data['accuracy_t2_o5'].mean()*100)
    corr_block_t2_o6 = int(mng_exptrials_t2.data['accuracy_t2_o6'].mean()*100)
    
    meanb2 = (corr_block_t2_o4 + corr_block_t2_o5  + corr_block_t2_o6)/3
    # keep track of which components have finished
    mng_blank_3Components = [blank_box_4, key_resp_19]
    for thisComponent in mng_blank_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_blank_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_box_4* updates
        if blank_box_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_box_4.frameNStart = frameN  # exact frame index
            blank_box_4.tStart = t  # local t and not account for scr refresh
            blank_box_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_box_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_box_4.started')
            blank_box_4.setAutoDraw(True)
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_19.started')
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_37
        if meanb1 < 66:
                continueRoutine=False
                
        if meanb2 < 66:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_blank_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_blank_3" ---
    for thisComponent in mng_blank_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    mng_exptrials_t3.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        mng_exptrials_t3.addData('key_resp_19.rt', key_resp_19.rt)
    # the Routine "mng_blank_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_probe_3target" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    P1_sample_3t.setImage(probe_p1)
    P4_sample_3t.setImage(probe_p4)
    P5_sample_3t.setImage(probe_p5)
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    mng_probe_3targetComponents = [P1_sample_3t, P4_sample_3t, P5_sample_3t, key_resp_9]
    for thisComponent in mng_probe_3targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_probe_3target" ---
    while continueRoutine and routineTimer.getTime() < 5.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *P1_sample_3t* updates
        if P1_sample_3t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1_sample_3t.frameNStart = frameN  # exact frame index
            P1_sample_3t.tStart = t  # local t and not account for scr refresh
            P1_sample_3t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1_sample_3t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1_sample_3t.started')
            P1_sample_3t.setAutoDraw(True)
        if P1_sample_3t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P1_sample_3t.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P1_sample_3t.tStop = t  # not accounting for scr refresh
                P1_sample_3t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1_sample_3t.stopped')
                P1_sample_3t.setAutoDraw(False)
        
        # *P4_sample_3t* updates
        if P4_sample_3t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4_sample_3t.frameNStart = frameN  # exact frame index
            P4_sample_3t.tStart = t  # local t and not account for scr refresh
            P4_sample_3t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4_sample_3t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4_sample_3t.started')
            P4_sample_3t.setAutoDraw(True)
        if P4_sample_3t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P4_sample_3t.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                P4_sample_3t.tStop = t  # not accounting for scr refresh
                P4_sample_3t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P4_sample_3t.stopped')
                P4_sample_3t.setAutoDraw(False)
        
        # *P5_sample_3t* updates
        if P5_sample_3t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5_sample_3t.frameNStart = frameN  # exact frame index
            P5_sample_3t.tStart = t  # local t and not account for scr refresh
            P5_sample_3t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5_sample_3t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5_sample_3t.started')
            P5_sample_3t.setAutoDraw(True)
        if P5_sample_3t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P5_sample_3t.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                P5_sample_3t.tStop = t  # not accounting for scr refresh
                P5_sample_3t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P5_sample_3t.stopped')
                P5_sample_3t.setAutoDraw(False)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_9.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_9.tStop = t  # not accounting for scr refresh
                key_resp_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.stopped')
                key_resp_9.status = FINISHED
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=None, waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
        # Run 'Each Frame' code from code_33
        if meanb1 < acc_thr:
                continueRoutine=False
                
        if meanb2 < 66:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_probe_3targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_probe_3target" ---
    for thisComponent in mng_probe_3targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    mng_exptrials_t3.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        mng_exptrials_t3.addData('key_resp_9.rt', key_resp_9.rt)
    # Run 'End Routine' code from code_33
    beginning_trial = globalClock.getTime();
    thisExp.addData("start", beginning_trial);
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.500000)
    
    # --- Prepare to start Routine "mng_test_3target_5objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_13
    if objects > 5:
        continueRoutine=False
    
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    # setup some python lists for storing info about the mouse_9
    gotValidClick = False  # until a click is received
    P1T_1t_8.setImage(test_p1)
    P2T_1t_8.setImage(test_p2)
    P3T_1t_8.setImage(test_p3)
    P4T_1t_8.setImage(test_p4)
    P5T_1t_8.setImage(test_p5)
    P6T_1t_8.setImage(test_p6)
    P7t_1t_8.setImage(test_p7)
    P8t_1t_8.setImage(test_p8)
    P9t_1t_8.setImage(test_p9)
    # keep track of which components have finished
    mng_test_3target_5objectsComponents = [mouse_9, P1T_rectangle_3t_5, P4T_rectangle_3t_5, P5T_rectangle_3t_5, P8T_rectangle_3t_5, P9T_rectangle_3t_5, P1T_1t_8, P2T_1t_8, P3T_1t_8, P4T_1t_8, P5T_1t_8, P6T_1t_8, P7t_1t_8, P8t_1t_8, P9t_1t_8, finish_9]
    for thisComponent in mng_test_3target_5objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_3target_5objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_13
        if meanb1 < acc_thr:
                continueRoutine=False
                        
        if meanb2 < 66:
                continueRoutine=False
        #print(ClickCount1)
        if mouse_9.isPressedIn(P1T_rectangle_3t_5):
            if clicked1 == 0:
                clicked1 = 1
                if lineColor == 'white':
                    P1T_rectangle_3t_5.lineColor = 'black'
                    lineColor = 'black'
                    P1T_rectangle_color = 1
                    thisExp.addData('P1T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P1T_rectangle_3t_5.lineColor = 'white'
                    lineColor = 'white'
                    P1T_rectangle_color = 0
                    thisExp.addData('P1T_rectangle', 0)
        elif clicked1 == 1:
            clicked1 = 0
        
        if mouse_9.isPressedIn(P4T_rectangle_3t_5):
            if clicked4 == 0:
                clicked4 = 1
                if lineColor == 'white':
                    P4T_rectangle_3t_5.lineColor = 'black'
                    lineColor = 'black'
                    P4T_rectangle_color = 1
                    thisExp.addData('P4T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P4T_rectangle_3t_5.lineColor = 'white'
                    lineColor = 'white'
                    P4T_rectangle_color = 0
                    thisExp.addData('P4T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked4 == 1:
            clicked4 = 0
        
        if mouse_9.isPressedIn(P5T_rectangle_3t_5):
            if clicked5 == 0:
                clicked5 = 1
                if lineColor == 'white':
                    P5T_rectangle_3t_5.lineColor = 'black'
                    lineColor = 'black'
                    P5T_rectangle_color = 1
                    thisExp.addData('P5T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P5T_rectangle_3t_5.lineColor = 'white'
                    lineColor = 'white'
                    P5T_rectangle_color = 0
                    thisExp.addData('P5T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked5 == 1:
            clicked5 = 0
        
        if mouse_9.isPressedIn(P8T_rectangle_3t_5):
            if clicked8 == 0:
                clicked8 = 1
                if lineColor == 'white':
                    P8T_rectangle_3t_5.lineColor = 'black'
                    lineColor = 'black'
                    P8T_rectangle_color = 1
                    thisExp.addData('P8T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P8T_rectangle_3t_5.lineColor = 'white'
                    lineColor = 'white'
                    P8T_rectangle_color = 0
                    thisExp.addData('P8T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked8 == 1:
            clicked8 = 0
            
        if mouse_9.isPressedIn(P9T_rectangle_3t_5):
            if clicked9 == 0:
                clicked9 = 1
                if lineColor == 'white':
                    P9T_rectangle_3t_5.lineColor = 'black'
                    lineColor = 'black'
                    P9T_rectangle_color = 1
                    thisExp.addData('P9T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P9T_rectangle_3t_5.lineColor = 'white'
                    lineColor = 'white'
                    P9T_rectangle_color = 0
                    thisExp.addData('P9T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked9 == 1:
            clicked9 = 0
        
        if mouse_9.isPressedIn(finish_9):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_9* updates
        if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.tStart = t  # local t and not account for scr refresh
            mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_9.started', t)
            mouse_9.status = STARTED
            mouse_9.mouseClock.reset()
            prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
        
        # *P1T_rectangle_3t_5* updates
        if P1T_rectangle_3t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_rectangle_3t_5.frameNStart = frameN  # exact frame index
            P1T_rectangle_3t_5.tStart = t  # local t and not account for scr refresh
            P1T_rectangle_3t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_rectangle_3t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_rectangle_3t_5.started')
            P1T_rectangle_3t_5.setAutoDraw(True)
        
        # *P4T_rectangle_3t_5* updates
        if P4T_rectangle_3t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_rectangle_3t_5.frameNStart = frameN  # exact frame index
            P4T_rectangle_3t_5.tStart = t  # local t and not account for scr refresh
            P4T_rectangle_3t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_rectangle_3t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_rectangle_3t_5.started')
            P4T_rectangle_3t_5.setAutoDraw(True)
        
        # *P5T_rectangle_3t_5* updates
        if P5T_rectangle_3t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_rectangle_3t_5.frameNStart = frameN  # exact frame index
            P5T_rectangle_3t_5.tStart = t  # local t and not account for scr refresh
            P5T_rectangle_3t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_rectangle_3t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_rectangle_3t_5.started')
            P5T_rectangle_3t_5.setAutoDraw(True)
        
        # *P8T_rectangle_3t_5* updates
        if P8T_rectangle_3t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8T_rectangle_3t_5.frameNStart = frameN  # exact frame index
            P8T_rectangle_3t_5.tStart = t  # local t and not account for scr refresh
            P8T_rectangle_3t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8T_rectangle_3t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8T_rectangle_3t_5.started')
            P8T_rectangle_3t_5.setAutoDraw(True)
        
        # *P9T_rectangle_3t_5* updates
        if P9T_rectangle_3t_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9T_rectangle_3t_5.frameNStart = frameN  # exact frame index
            P9T_rectangle_3t_5.tStart = t  # local t and not account for scr refresh
            P9T_rectangle_3t_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9T_rectangle_3t_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9T_rectangle_3t_5.started')
            P9T_rectangle_3t_5.setAutoDraw(True)
        
        # *P1T_1t_8* updates
        if P1T_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_8.frameNStart = frameN  # exact frame index
            P1T_1t_8.tStart = t  # local t and not account for scr refresh
            P1T_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_8.started')
            P1T_1t_8.setAutoDraw(True)
        
        # *P2T_1t_8* updates
        if P2T_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_8.frameNStart = frameN  # exact frame index
            P2T_1t_8.tStart = t  # local t and not account for scr refresh
            P2T_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_8.started')
            P2T_1t_8.setAutoDraw(True)
        
        # *P3T_1t_8* updates
        if P3T_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_8.frameNStart = frameN  # exact frame index
            P3T_1t_8.tStart = t  # local t and not account for scr refresh
            P3T_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_8.started')
            P3T_1t_8.setAutoDraw(True)
        
        # *P4T_1t_8* updates
        if P4T_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_8.frameNStart = frameN  # exact frame index
            P4T_1t_8.tStart = t  # local t and not account for scr refresh
            P4T_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_8.started')
            P4T_1t_8.setAutoDraw(True)
        
        # *P5T_1t_8* updates
        if P5T_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_8.frameNStart = frameN  # exact frame index
            P5T_1t_8.tStart = t  # local t and not account for scr refresh
            P5T_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_8.started')
            P5T_1t_8.setAutoDraw(True)
        
        # *P6T_1t_8* updates
        if P6T_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_8.frameNStart = frameN  # exact frame index
            P6T_1t_8.tStart = t  # local t and not account for scr refresh
            P6T_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_8.started')
            P6T_1t_8.setAutoDraw(True)
        
        # *P7t_1t_8* updates
        if P7t_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_8.frameNStart = frameN  # exact frame index
            P7t_1t_8.tStart = t  # local t and not account for scr refresh
            P7t_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_8.started')
            P7t_1t_8.setAutoDraw(True)
        
        # *P8t_1t_8* updates
        if P8t_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_8.frameNStart = frameN  # exact frame index
            P8t_1t_8.tStart = t  # local t and not account for scr refresh
            P8t_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_8.started')
            P8t_1t_8.setAutoDraw(True)
        
        # *P9t_1t_8* updates
        if P9t_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_8.frameNStart = frameN  # exact frame index
            P9t_1t_8.tStart = t  # local t and not account for scr refresh
            P9t_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_8.started')
            P9t_1t_8.setAutoDraw(True)
        
        # *finish_9* updates
        if finish_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_9.frameNStart = frameN  # exact frame index
            finish_9.tStart = t  # local t and not account for scr refresh
            finish_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_9.started')
            finish_9.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_3target_5objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_3target_5objects" ---
    for thisComponent in mng_test_3target_5objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_13
    #print(ClickCount1)
    ClickCount1 = 0
    P1T_rectangle_3t_5.lineColor = 'white'
    P4T_rectangle_3t_5.lineColor = 'white'
    P5T_rectangle_3t_5.lineColor = 'white'
    P8T_rectangle_3t_5.lineColor = 'white'
    P9T_rectangle_3t_5.lineColor = 'white'
    
    if objects == 5:
        if ((float(corr_p1) == float(P1T_rectangle_color)) & (float(corr_p4) == float(P4T_rectangle_color)) & (float(corr_p5) == float(P5T_rectangle_color)) & (float(corr_p8) == float(P8T_rectangle_color)) & (float(corr_p9) == float(P9T_rectangle_color))):
            mng_exptrials_t3.addData('accuracy_t3_o5', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t3.addData('accuracy_t3_o5', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)        
    elif meanb2 < 66:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t3 (TrialHandler)
    # the Routine "mng_test_3target_5objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_3target_6objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_14
    if objects > 6:
        continueRoutine=False
    
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    clicked10 = 0
    clicked11 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    P10T_rectangle_color = 0
    P11T_rectangle_color = 0
    
    # setup some python lists for storing info about the mouse_10
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_9.setImage(test_p1)
    P2T_1t_9.setImage(test_p2)
    P3T_1t_9.setImage(test_p3)
    P4T_1t_9.setImage(test_p4)
    P5T_1t_9.setImage(test_p5)
    P6T_1t_9.setImage(test_p6)
    P7t_1t_9.setImage(test_p7)
    P8t_1t_9.setImage(test_p8)
    P9t_1t_9.setImage(test_p9)
    P10t_1t.setImage(test_p10)
    P11_1t.setImage(test_p11)
    # keep track of which components have finished
    mng_test_3target_6objectsComponents = [mouse_10, P2T_rectangle_3t_6, P3T_rectangle_3t_6, P6T_rectangle_3t_6, P7T_rectangle_3t_6, P10T_rectangle_3t_6, P11T_rectangle_3t_6, P1T_1t_9, P2T_1t_9, P3T_1t_9, P4T_1t_9, P5T_1t_9, P6T_1t_9, P7t_1t_9, P8t_1t_9, P9t_1t_9, P10t_1t, P11_1t, finish_10]
    for thisComponent in mng_test_3target_6objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_3target_6objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_14
        if meanb1 < acc_thr:
                continueRoutine=False
                        
        if meanb2 < 66:
                continueRoutine=False
        #print(ClickCount1)
        
        if mouse_10.isPressedIn(P2T_rectangle_3t_6):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_3t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_3t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_10.isPressedIn(P3T_rectangle_3t_6):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_3t_6.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_3t_6.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_10.isPressedIn(P6T_rectangle_3t_6):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_3t_6.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_3t_6.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_10.isPressedIn(P7T_rectangle_3t_6):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_3t_6.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_3t_6.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
        
        if mouse_10.isPressedIn(P10T_rectangle_3t_6):
            if clicked10 == 0:
                clicked10 = 1
                if lineColor == 'white':
                    P10T_rectangle_3t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P10T_rectangle', 1) #OR exp.addData('letter', letter)
                    P10T_rectangle_color = 1
                elif lineColor == 'black':
                    P10T_rectangle_3t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P10T_rectangle', 0) #OR exp.addData('letter', letter)
                    P10T_rectangle_color = 0
        elif clicked10 == 1:
            clicked10 = 0
            
        if mouse_10.isPressedIn(P11T_rectangle_3t_6):
            if clicked11 == 0:
                clicked11 = 1
                if lineColor == 'white':
                    P11T_rectangle_3t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P11T_rectangle', 1) #OR exp.addData('letter', letter)
                    P11T_rectangle_color = 1
                elif lineColor == 'black':
                    P11T_rectangle_3t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P11T_rectangle', 0) #OR exp.addData('letter', letter)
                    P11T_rectangle_color = 0
        elif clicked11 == 1:
            clicked11 = 0
        
        if mouse_10.isPressedIn(finish_10):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        # *mouse_10* updates
        if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_10.started', t)
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_3t_6* updates
        if P2T_rectangle_3t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_3t_6.frameNStart = frameN  # exact frame index
            P2T_rectangle_3t_6.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_3t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_3t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_3t_6.started')
            P2T_rectangle_3t_6.setAutoDraw(True)
        
        # *P3T_rectangle_3t_6* updates
        if P3T_rectangle_3t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_3t_6.frameNStart = frameN  # exact frame index
            P3T_rectangle_3t_6.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_3t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_3t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_3t_6.started')
            P3T_rectangle_3t_6.setAutoDraw(True)
        
        # *P6T_rectangle_3t_6* updates
        if P6T_rectangle_3t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_3t_6.frameNStart = frameN  # exact frame index
            P6T_rectangle_3t_6.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_3t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_3t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_3t_6.started')
            P6T_rectangle_3t_6.setAutoDraw(True)
        
        # *P7T_rectangle_3t_6* updates
        if P7T_rectangle_3t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_3t_6.frameNStart = frameN  # exact frame index
            P7T_rectangle_3t_6.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_3t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_3t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_3t_6.started')
            P7T_rectangle_3t_6.setAutoDraw(True)
        
        # *P10T_rectangle_3t_6* updates
        if P10T_rectangle_3t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10T_rectangle_3t_6.frameNStart = frameN  # exact frame index
            P10T_rectangle_3t_6.tStart = t  # local t and not account for scr refresh
            P10T_rectangle_3t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10T_rectangle_3t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10T_rectangle_3t_6.started')
            P10T_rectangle_3t_6.setAutoDraw(True)
        
        # *P11T_rectangle_3t_6* updates
        if P11T_rectangle_3t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11T_rectangle_3t_6.frameNStart = frameN  # exact frame index
            P11T_rectangle_3t_6.tStart = t  # local t and not account for scr refresh
            P11T_rectangle_3t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11T_rectangle_3t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11T_rectangle_3t_6.started')
            P11T_rectangle_3t_6.setAutoDraw(True)
        
        # *P1T_1t_9* updates
        if P1T_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_9.frameNStart = frameN  # exact frame index
            P1T_1t_9.tStart = t  # local t and not account for scr refresh
            P1T_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_9.started')
            P1T_1t_9.setAutoDraw(True)
        
        # *P2T_1t_9* updates
        if P2T_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_9.frameNStart = frameN  # exact frame index
            P2T_1t_9.tStart = t  # local t and not account for scr refresh
            P2T_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_9.started')
            P2T_1t_9.setAutoDraw(True)
        
        # *P3T_1t_9* updates
        if P3T_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_9.frameNStart = frameN  # exact frame index
            P3T_1t_9.tStart = t  # local t and not account for scr refresh
            P3T_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_9.started')
            P3T_1t_9.setAutoDraw(True)
        
        # *P4T_1t_9* updates
        if P4T_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_9.frameNStart = frameN  # exact frame index
            P4T_1t_9.tStart = t  # local t and not account for scr refresh
            P4T_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_9.started')
            P4T_1t_9.setAutoDraw(True)
        
        # *P5T_1t_9* updates
        if P5T_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_9.frameNStart = frameN  # exact frame index
            P5T_1t_9.tStart = t  # local t and not account for scr refresh
            P5T_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_9.started')
            P5T_1t_9.setAutoDraw(True)
        
        # *P6T_1t_9* updates
        if P6T_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_9.frameNStart = frameN  # exact frame index
            P6T_1t_9.tStart = t  # local t and not account for scr refresh
            P6T_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_9.started')
            P6T_1t_9.setAutoDraw(True)
        
        # *P7t_1t_9* updates
        if P7t_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_9.frameNStart = frameN  # exact frame index
            P7t_1t_9.tStart = t  # local t and not account for scr refresh
            P7t_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_9.started')
            P7t_1t_9.setAutoDraw(True)
        
        # *P8t_1t_9* updates
        if P8t_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_9.frameNStart = frameN  # exact frame index
            P8t_1t_9.tStart = t  # local t and not account for scr refresh
            P8t_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_9.started')
            P8t_1t_9.setAutoDraw(True)
        
        # *P9t_1t_9* updates
        if P9t_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_9.frameNStart = frameN  # exact frame index
            P9t_1t_9.tStart = t  # local t and not account for scr refresh
            P9t_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_9.started')
            P9t_1t_9.setAutoDraw(True)
        
        # *P10t_1t* updates
        if P10t_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10t_1t.frameNStart = frameN  # exact frame index
            P10t_1t.tStart = t  # local t and not account for scr refresh
            P10t_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10t_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10t_1t.started')
            P10t_1t.setAutoDraw(True)
        
        # *P11_1t* updates
        if P11_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11_1t.frameNStart = frameN  # exact frame index
            P11_1t.tStart = t  # local t and not account for scr refresh
            P11_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11_1t.started')
            P11_1t.setAutoDraw(True)
        
        # *finish_10* updates
        if finish_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_10.frameNStart = frameN  # exact frame index
            finish_10.tStart = t  # local t and not account for scr refresh
            finish_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_10.started')
            finish_10.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_3target_6objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_3target_6objects" ---
    for thisComponent in mng_test_3target_6objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_14
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_3t_6.lineColor = 'white'
    P3T_rectangle_3t_6.lineColor = 'white'
    P6T_rectangle_3t_6.lineColor = 'white'
    P7T_rectangle_3t_6.lineColor = 'white'
    P10T_rectangle_3t_6.lineColor = 'white'
    P11T_rectangle_3t_6.lineColor = 'white'
    
    print("block 3 6 objects")
    print("check colors")
    print(float(P2T_rectangle_color))
    print(float(P3T_rectangle_color))
    print(float(P6T_rectangle_color))
    print(float(P7T_rectangle_color))
    print(float(P10T_rectangle_color))
    print(float(P11T_rectangle_color))
    
    print("check corrs")
    print(float(corr_p2))
    print(float(corr_p3))
    print(float(corr_p6))
    print(float(corr_p7))
    print(float(corr_p10))
    print(float(corr_p11))
    
    if objects == 6:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color)) & (float(corr_p10) == float(P10T_rectangle_color)) & (float(corr_p11) == float(P11T_rectangle_color))):
            mng_exptrials_t3.addData('accuracy_t3_o6', 1) #OR exp.addData('letter', letter)
        else:
            msg = "Incorrect"
            print("Incorrect")
            incorr = 1
            mng_exptrials_t3.addData('accuracy_t3_o6', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)        
    elif meanb2 < 66:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t3 (TrialHandler)
    # the Routine "mng_test_3target_6objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_3target_8objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_15
    if objects < 5:
        continueRoutine=False
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    clicked10 = 0
    clicked11 = 0
    clicked12 = 0
    clicked13 = 0
    clicked14 = 0
    clicked15 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    P10T_rectangle_color = 0
    P11T_rectangle_color = 0
    P12T_rectangle_color = 0
    P13T_rectangle_color = 0
    P14T_rectangle_color = 0
    P15T_rectangle_color = 0
    
    # setup some python lists for storing info about the mouse_11
    mouse_11.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_10.setImage(test_p1)
    P2T_1t_10.setImage(test_p2)
    P3T_1t_10.setImage(test_p3)
    P4T_1t_10.setImage(test_p4)
    P5T_1t_10.setImage(test_p5)
    P6T_1t_10.setImage(test_p6)
    P7t_1t_10.setImage(test_p7)
    P8t_1t_10.setImage(test_p8)
    P9t_1t_10.setImage(test_p9)
    P10t_1t_8.setImage(test_p10)
    P11_1t_8.setImage(test_p11)
    P12_1t_8.setImage(test_p12)
    P13_1t_8.setImage(test_p13)
    P14_1t_8.setImage(test_p14)
    P15_1t_8.setImage(test_p15)
    # keep track of which components have finished
    mng_test_3target_8objectsComponents = [mouse_11, P2T_rectangle_3t_8, P3T_rectangle_3t_8, P6T_rectangle_3t_8, P7T_rectangle_3t_8, P12T_rectangle_3t_8, P13T_rectangle_3t_8, P14T_rectangle_3t_8, P15T_rectangle_3t_8, P1T_1t_10, P2T_1t_10, P3T_1t_10, P4T_1t_10, P5T_1t_10, P6T_1t_10, P7t_1t_10, P8t_1t_10, P9t_1t_10, P10t_1t_8, P11_1t_8, P12_1t_8, P13_1t_8, P14_1t_8, P15_1t_8, finish_11]
    for thisComponent in mng_test_3target_8objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_3target_8objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_15
        if meanb1 < acc_thr:
                continueRoutine=False
                        
        if meanb2 < acc_thr:
                continueRoutine=False
        #print(ClickCount1)
        
        if mouse_11.isPressedIn(P2T_rectangle_3t_8):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_11.isPressedIn(P3T_rectangle_3t_8):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_11.isPressedIn(P6T_rectangle_3t_8):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_11.isPressedIn(P7T_rectangle_3t_8):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
        
        if mouse_11.isPressedIn(P12T_rectangle_3t_8):
            if clicked12 == 0:
                clicked12 = 1
                if lineColor == 'white':
                    P12T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P12T_rectangle', 1) #OR exp.addData('letter', letter)
                    P12T_rectangle_color = 1
                elif lineColor == 'black':
                    P12T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P12T_rectangle', 0) #OR exp.addData('letter', letter)
                    P12T_rectangle_color = 0
        elif clicked12 == 1:
            clicked12 = 0
            
        if mouse_11.isPressedIn(P13T_rectangle_3t_8):
            if clicked13 == 0:
                clicked13 = 1
                if lineColor == 'white':
                    P13T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P13T_rectangle', 1) #OR exp.addData('letter', letter)
                    P13T_rectangle_color = 1
                elif lineColor == 'black':
                    P13T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P13T_rectangle', 0) #OR exp.addData('letter', letter)
                    P13T_rectangle_color = 0
        elif clicked13 == 1:
            clicked13 = 0
        
        if mouse_11.isPressedIn(P14T_rectangle_3t_8):
            if clicked14 == 0:
                clicked14 = 1
                if lineColor == 'white':
                    P14T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P14T_rectangle', 1) #OR exp.addData('letter', letter)
                    P14T_rectangle_color = 1
                elif lineColor == 'black':
                    P14T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P14T_rectangle', 0) #OR exp.addData('letter', letter)
                    P14T_rectangle_color = 0
        elif clicked14 == 1:
            clicked14 = 0
            
        if mouse_11.isPressedIn(P15T_rectangle_3t_8):
            if clicked15 == 0:
                clicked15 = 1
                if lineColor == 'white':
                    P15T_rectangle_3t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P15T_rectangle', 1) #OR exp.addData('letter', letter)
                    P15T_rectangle_color = 1
                elif lineColor == 'black':
                    P15T_rectangle_3t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P15T_rectangle', 0) #OR exp.addData('letter', letter)
                    P15T_rectangle_color = 0
        elif clicked15 == 1:
            clicked15 = 0
        
        
        if mouse_11.isPressedIn(finish_11):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_11* updates
        if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.tStart = t  # local t and not account for scr refresh
            mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_11.started', t)
            mouse_11.status = STARTED
            mouse_11.mouseClock.reset()
            prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_3t_8* updates
        if P2T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P2T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_3t_8.started')
            P2T_rectangle_3t_8.setAutoDraw(True)
        
        # *P3T_rectangle_3t_8* updates
        if P3T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P3T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_3t_8.started')
            P3T_rectangle_3t_8.setAutoDraw(True)
        
        # *P6T_rectangle_3t_8* updates
        if P6T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P6T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_3t_8.started')
            P6T_rectangle_3t_8.setAutoDraw(True)
        
        # *P7T_rectangle_3t_8* updates
        if P7T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P7T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_3t_8.started')
            P7T_rectangle_3t_8.setAutoDraw(True)
        
        # *P12T_rectangle_3t_8* updates
        if P12T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P12T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P12T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P12T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P12T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P12T_rectangle_3t_8.started')
            P12T_rectangle_3t_8.setAutoDraw(True)
        
        # *P13T_rectangle_3t_8* updates
        if P13T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P13T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P13T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P13T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P13T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P13T_rectangle_3t_8.started')
            P13T_rectangle_3t_8.setAutoDraw(True)
        
        # *P14T_rectangle_3t_8* updates
        if P14T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P14T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P14T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P14T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P14T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P14T_rectangle_3t_8.started')
            P14T_rectangle_3t_8.setAutoDraw(True)
        
        # *P15T_rectangle_3t_8* updates
        if P15T_rectangle_3t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P15T_rectangle_3t_8.frameNStart = frameN  # exact frame index
            P15T_rectangle_3t_8.tStart = t  # local t and not account for scr refresh
            P15T_rectangle_3t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P15T_rectangle_3t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P15T_rectangle_3t_8.started')
            P15T_rectangle_3t_8.setAutoDraw(True)
        
        # *P1T_1t_10* updates
        if P1T_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_10.frameNStart = frameN  # exact frame index
            P1T_1t_10.tStart = t  # local t and not account for scr refresh
            P1T_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_10.started')
            P1T_1t_10.setAutoDraw(True)
        
        # *P2T_1t_10* updates
        if P2T_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_10.frameNStart = frameN  # exact frame index
            P2T_1t_10.tStart = t  # local t and not account for scr refresh
            P2T_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_10.started')
            P2T_1t_10.setAutoDraw(True)
        
        # *P3T_1t_10* updates
        if P3T_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_10.frameNStart = frameN  # exact frame index
            P3T_1t_10.tStart = t  # local t and not account for scr refresh
            P3T_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_10.started')
            P3T_1t_10.setAutoDraw(True)
        
        # *P4T_1t_10* updates
        if P4T_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_10.frameNStart = frameN  # exact frame index
            P4T_1t_10.tStart = t  # local t and not account for scr refresh
            P4T_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_10.started')
            P4T_1t_10.setAutoDraw(True)
        
        # *P5T_1t_10* updates
        if P5T_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_10.frameNStart = frameN  # exact frame index
            P5T_1t_10.tStart = t  # local t and not account for scr refresh
            P5T_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_10.started')
            P5T_1t_10.setAutoDraw(True)
        
        # *P6T_1t_10* updates
        if P6T_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_10.frameNStart = frameN  # exact frame index
            P6T_1t_10.tStart = t  # local t and not account for scr refresh
            P6T_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_10.started')
            P6T_1t_10.setAutoDraw(True)
        
        # *P7t_1t_10* updates
        if P7t_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_10.frameNStart = frameN  # exact frame index
            P7t_1t_10.tStart = t  # local t and not account for scr refresh
            P7t_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_10.started')
            P7t_1t_10.setAutoDraw(True)
        
        # *P8t_1t_10* updates
        if P8t_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_10.frameNStart = frameN  # exact frame index
            P8t_1t_10.tStart = t  # local t and not account for scr refresh
            P8t_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_10.started')
            P8t_1t_10.setAutoDraw(True)
        
        # *P9t_1t_10* updates
        if P9t_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_10.frameNStart = frameN  # exact frame index
            P9t_1t_10.tStart = t  # local t and not account for scr refresh
            P9t_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_10.started')
            P9t_1t_10.setAutoDraw(True)
        
        # *P10t_1t_8* updates
        if P10t_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10t_1t_8.frameNStart = frameN  # exact frame index
            P10t_1t_8.tStart = t  # local t and not account for scr refresh
            P10t_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10t_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10t_1t_8.started')
            P10t_1t_8.setAutoDraw(True)
        
        # *P11_1t_8* updates
        if P11_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11_1t_8.frameNStart = frameN  # exact frame index
            P11_1t_8.tStart = t  # local t and not account for scr refresh
            P11_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11_1t_8.started')
            P11_1t_8.setAutoDraw(True)
        
        # *P12_1t_8* updates
        if P12_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P12_1t_8.frameNStart = frameN  # exact frame index
            P12_1t_8.tStart = t  # local t and not account for scr refresh
            P12_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P12_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P12_1t_8.started')
            P12_1t_8.setAutoDraw(True)
        
        # *P13_1t_8* updates
        if P13_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P13_1t_8.frameNStart = frameN  # exact frame index
            P13_1t_8.tStart = t  # local t and not account for scr refresh
            P13_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P13_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P13_1t_8.started')
            P13_1t_8.setAutoDraw(True)
        
        # *P14_1t_8* updates
        if P14_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P14_1t_8.frameNStart = frameN  # exact frame index
            P14_1t_8.tStart = t  # local t and not account for scr refresh
            P14_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P14_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P14_1t_8.started')
            P14_1t_8.setAutoDraw(True)
        
        # *P15_1t_8* updates
        if P15_1t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P15_1t_8.frameNStart = frameN  # exact frame index
            P15_1t_8.tStart = t  # local t and not account for scr refresh
            P15_1t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P15_1t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P15_1t_8.started')
            P15_1t_8.setAutoDraw(True)
        
        # *finish_11* updates
        if finish_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_11.frameNStart = frameN  # exact frame index
            finish_11.tStart = t  # local t and not account for scr refresh
            finish_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_11.started')
            finish_11.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_3target_8objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_3target_8objects" ---
    for thisComponent in mng_test_3target_8objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_15
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_3t_8.lineColor = 'white'
    P3T_rectangle_3t_8.lineColor = 'white'
    P6T_rectangle_3t_8.lineColor = 'white'
    P7T_rectangle_3t_8.lineColor = 'white'
    P12T_rectangle_3t_8.lineColor = 'white'
    P13T_rectangle_3t_8.lineColor = 'white'
    P14T_rectangle_3t_8.lineColor = 'white'
    P15T_rectangle_3t_8.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects == 8:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color)) & (float(corr_p10) == float(P10T_rectangle_color)) & (float(corr_p11) == float(P11T_rectangle_color)) & (float(corr_p12) == float(P12T_rectangle_color)) & (float(corr_p13) == float(P13T_rectangle_color)) & (float(corr_p14) == float(P14T_rectangle_color)) & (float(corr_p15) == float(P15T_rectangle_color))):
            mng_exptrials_t3.addData('accuracy_t3_o8', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t3.addData('accuracy_t3_o8', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)        
    elif meanb2 < 66:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t3 (TrialHandler)
    # the Routine "mng_test_3target_8objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mng_exptrials_t3'


# set up handler to look after randomisation of conditions etc
mng_exptrials_t4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mn_generaltask_t4trials_final.xlsx'),
    seed=None, name='mng_exptrials_t4')
thisExp.addLoop(mng_exptrials_t4)  # add the loop to the experiment
thisMng_exptrials_t4 = mng_exptrials_t4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t4.rgb)
if thisMng_exptrials_t4 != None:
    for paramName in thisMng_exptrials_t4:
        exec('{} = thisMng_exptrials_t4[paramName]'.format(paramName))

for thisMng_exptrials_t4 in mng_exptrials_t4:
    currentLoop = mng_exptrials_t4
    # abbreviate parameter names if possible (e.g. rgb = thisMng_exptrials_t4.rgb)
    if thisMng_exptrials_t4 != None:
        for paramName in thisMng_exptrials_t4:
            exec('{} = thisMng_exptrials_t4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_blank_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # Run 'Begin Routine' code from code_38
    corr_block_t3_o5 = int(mng_exptrials_t3.data['accuracy_t3_o5'].mean()*100)
    corr_block_t3_o6 = int(mng_exptrials_t3.data['accuracy_t3_o6'].mean()*100)
    corr_block_t3_o8 = int(mng_exptrials_t3.data['accuracy_t3_o8'].mean()*100)
    
    meanb3 = (corr_block_t3_o5 + corr_block_t3_o6  + corr_block_t3_o8)/3
    # keep track of which components have finished
    mng_blank_4Components = [blank_box_5, key_resp_20]
    for thisComponent in mng_blank_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_blank_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_box_5* updates
        if blank_box_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_box_5.frameNStart = frameN  # exact frame index
            blank_box_5.tStart = t  # local t and not account for scr refresh
            blank_box_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_box_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_box_5.started')
            blank_box_5.setAutoDraw(True)
        
        # *key_resp_20* updates
        waitOnFlip = False
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_20.started')
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_38
        if meanb1 < acc_thr:
                continueRoutine=False
        
        if meanb2 < acc_thr:
                continueRoutine=False
                
        if meanb3 < acc_thr:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_blank_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_blank_4" ---
    for thisComponent in mng_blank_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    mng_exptrials_t4.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        mng_exptrials_t4.addData('key_resp_20.rt', key_resp_20.rt)
    # the Routine "mng_blank_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_probe_4target" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    P2_sample_4t.setImage(probe_p2)
    P3_sample_4t.setImage(probe_p3)
    P6_sample_4t.setImage(probe_p6)
    P7_sample_4t.setImage(probe_p7)
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # keep track of which components have finished
    mng_probe_4targetComponents = [P2_sample_4t, P3_sample_4t, P6_sample_4t, P7_sample_4t, key_resp_10]
    for thisComponent in mng_probe_4targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_probe_4target" ---
    while continueRoutine and routineTimer.getTime() < 5.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *P2_sample_4t* updates
        if P2_sample_4t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2_sample_4t.frameNStart = frameN  # exact frame index
            P2_sample_4t.tStart = t  # local t and not account for scr refresh
            P2_sample_4t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2_sample_4t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2_sample_4t.started')
            P2_sample_4t.setAutoDraw(True)
        if P2_sample_4t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P2_sample_4t.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P2_sample_4t.tStop = t  # not accounting for scr refresh
                P2_sample_4t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2_sample_4t.stopped')
                P2_sample_4t.setAutoDraw(False)
        
        # *P3_sample_4t* updates
        if P3_sample_4t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3_sample_4t.frameNStart = frameN  # exact frame index
            P3_sample_4t.tStart = t  # local t and not account for scr refresh
            P3_sample_4t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3_sample_4t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3_sample_4t.started')
            P3_sample_4t.setAutoDraw(True)
        if P3_sample_4t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P3_sample_4t.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                P3_sample_4t.tStop = t  # not accounting for scr refresh
                P3_sample_4t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P3_sample_4t.stopped')
                P3_sample_4t.setAutoDraw(False)
        
        # *P6_sample_4t* updates
        if P6_sample_4t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6_sample_4t.frameNStart = frameN  # exact frame index
            P6_sample_4t.tStart = t  # local t and not account for scr refresh
            P6_sample_4t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6_sample_4t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6_sample_4t.started')
            P6_sample_4t.setAutoDraw(True)
        if P6_sample_4t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P6_sample_4t.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                P6_sample_4t.tStop = t  # not accounting for scr refresh
                P6_sample_4t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P6_sample_4t.stopped')
                P6_sample_4t.setAutoDraw(False)
        
        # *P7_sample_4t* updates
        if P7_sample_4t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7_sample_4t.frameNStart = frameN  # exact frame index
            P7_sample_4t.tStart = t  # local t and not account for scr refresh
            P7_sample_4t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7_sample_4t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7_sample_4t.started')
            P7_sample_4t.setAutoDraw(True)
        if P7_sample_4t.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P7_sample_4t.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P7_sample_4t.tStop = t  # not accounting for scr refresh
                P7_sample_4t.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P7_sample_4t.stopped')
                P7_sample_4t.setAutoDraw(False)
        
        # *key_resp_10* updates
        waitOnFlip = False
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_10.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_10.tStop = t  # not accounting for scr refresh
                key_resp_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_10.stopped')
                key_resp_10.status = FINISHED
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=None, waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
        # Run 'Each Frame' code from code_34
        if meanb1 < acc_thr:
                continueRoutine=False
                
        if meanb2 < acc_thr:
                continueRoutine=False
                
        if meanb3 < acc_thr:
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_probe_4targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_probe_4target" ---
    for thisComponent in mng_probe_4targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    mng_exptrials_t4.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        mng_exptrials_t4.addData('key_resp_10.rt', key_resp_10.rt)
    # Run 'End Routine' code from code_34
    beginning_trial = globalClock.getTime();
    thisExp.addData("start", beginning_trial);
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.500000)
    
    # --- Prepare to start Routine "mng_test_4target_6objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_16
    if objects > 6:
        continueRoutine=False
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    clicked10 = 0
    clicked11 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    P10T_rectangle_color = 0
    P11T_rectangle_color = 0
    
    # setup some python lists for storing info about the mouse_12
    mouse_12.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_11.setImage(test_p1)
    P2T_1t_11.setImage(test_p2)
    P3T_1t_11.setImage(test_p3)
    P4T_1t_11.setImage(test_p4)
    P5T_1t_11.setImage(test_p5)
    P6T_1t_11.setImage(test_p6)
    P7t_1t_11.setImage(test_p7)
    P8t_1t_11.setImage(test_p8)
    P9t_1t_11.setImage(test_p9)
    P10t_1t_2.setImage(test_p10)
    P11_1t_2.setImage(test_p11)
    # keep track of which components have finished
    mng_test_4target_6objectsComponents = [mouse_12, P2T_rectangle_4t_6, P3T_rectangle_4t_6, P6T_rectangle_4t_6, P7T_rectangle_4t_6, P10T_rectangle_4t_6, P11T_rectangle_4t_6, P1T_1t_11, P2T_1t_11, P3T_1t_11, P4T_1t_11, P5T_1t_11, P6T_1t_11, P7t_1t_11, P8t_1t_11, P9t_1t_11, P10t_1t_2, P11_1t_2, finish_12]
    for thisComponent in mng_test_4target_6objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_4target_6objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_16
        if meanb1 < acc_thr:
                continueRoutine=False        
        
        if meanb2 < acc_thr:
                continueRoutine=False
        
        if meanb3 < acc_thr:
                continueRoutine=False
        
        if mouse_12.isPressedIn(P2T_rectangle_4t_6):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_4t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_4t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_12.isPressedIn(P3T_rectangle_4t_6):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_4t_6.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_4t_6.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_12.isPressedIn(P6T_rectangle_4t_6):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_4t_6.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_4t_6.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_12.isPressedIn(P7T_rectangle_4t_6):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_4t_6.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_4t_6.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
        
        if mouse_12.isPressedIn(P10T_rectangle_4t_6):
            if clicked10 == 0:
                clicked10 = 1
                if lineColor == 'white':
                    P10T_rectangle_4t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P10T_rectangle', 1) #OR exp.addData('letter', letter)
                    P10T_rectangle_color = 1
                elif lineColor == 'black':
                    P10T_rectangle_4t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P10T_rectangle', 0) #OR exp.addData('letter', letter)
                    P10T_rectangle_color = 0
        elif clicked10 == 1:
            clicked10 = 0
            
        if mouse_12.isPressedIn(P11T_rectangle_4t_6):
            if clicked11 == 0:
                clicked11 = 1
                if lineColor == 'white':
                    P11T_rectangle_4t_6.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P11T_rectangle', 1) #OR exp.addData('letter', letter)
                    P11T_rectangle_color = 1
                elif lineColor == 'black':
                    P11T_rectangle_4t_6.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P11T_rectangle', 0) #OR exp.addData('letter', letter)
                    P11T_rectangle_color = 0
        elif clicked11 == 1:
            clicked11 = 0
        
        if mouse_12.isPressedIn(finish_12):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_12* updates
        if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_12.frameNStart = frameN  # exact frame index
            mouse_12.tStart = t  # local t and not account for scr refresh
            mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_12.started', t)
            mouse_12.status = STARTED
            mouse_12.mouseClock.reset()
            prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_4t_6* updates
        if P2T_rectangle_4t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_4t_6.frameNStart = frameN  # exact frame index
            P2T_rectangle_4t_6.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_4t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_4t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_4t_6.started')
            P2T_rectangle_4t_6.setAutoDraw(True)
        
        # *P3T_rectangle_4t_6* updates
        if P3T_rectangle_4t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_4t_6.frameNStart = frameN  # exact frame index
            P3T_rectangle_4t_6.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_4t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_4t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_4t_6.started')
            P3T_rectangle_4t_6.setAutoDraw(True)
        
        # *P6T_rectangle_4t_6* updates
        if P6T_rectangle_4t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_4t_6.frameNStart = frameN  # exact frame index
            P6T_rectangle_4t_6.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_4t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_4t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_4t_6.started')
            P6T_rectangle_4t_6.setAutoDraw(True)
        
        # *P7T_rectangle_4t_6* updates
        if P7T_rectangle_4t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_4t_6.frameNStart = frameN  # exact frame index
            P7T_rectangle_4t_6.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_4t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_4t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_4t_6.started')
            P7T_rectangle_4t_6.setAutoDraw(True)
        
        # *P10T_rectangle_4t_6* updates
        if P10T_rectangle_4t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10T_rectangle_4t_6.frameNStart = frameN  # exact frame index
            P10T_rectangle_4t_6.tStart = t  # local t and not account for scr refresh
            P10T_rectangle_4t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10T_rectangle_4t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10T_rectangle_4t_6.started')
            P10T_rectangle_4t_6.setAutoDraw(True)
        
        # *P11T_rectangle_4t_6* updates
        if P11T_rectangle_4t_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11T_rectangle_4t_6.frameNStart = frameN  # exact frame index
            P11T_rectangle_4t_6.tStart = t  # local t and not account for scr refresh
            P11T_rectangle_4t_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11T_rectangle_4t_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11T_rectangle_4t_6.started')
            P11T_rectangle_4t_6.setAutoDraw(True)
        
        # *P1T_1t_11* updates
        if P1T_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_11.frameNStart = frameN  # exact frame index
            P1T_1t_11.tStart = t  # local t and not account for scr refresh
            P1T_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_11.started')
            P1T_1t_11.setAutoDraw(True)
        
        # *P2T_1t_11* updates
        if P2T_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_11.frameNStart = frameN  # exact frame index
            P2T_1t_11.tStart = t  # local t and not account for scr refresh
            P2T_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_11.started')
            P2T_1t_11.setAutoDraw(True)
        
        # *P3T_1t_11* updates
        if P3T_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_11.frameNStart = frameN  # exact frame index
            P3T_1t_11.tStart = t  # local t and not account for scr refresh
            P3T_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_11.started')
            P3T_1t_11.setAutoDraw(True)
        
        # *P4T_1t_11* updates
        if P4T_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_11.frameNStart = frameN  # exact frame index
            P4T_1t_11.tStart = t  # local t and not account for scr refresh
            P4T_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_11.started')
            P4T_1t_11.setAutoDraw(True)
        
        # *P5T_1t_11* updates
        if P5T_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_11.frameNStart = frameN  # exact frame index
            P5T_1t_11.tStart = t  # local t and not account for scr refresh
            P5T_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_11.started')
            P5T_1t_11.setAutoDraw(True)
        
        # *P6T_1t_11* updates
        if P6T_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_11.frameNStart = frameN  # exact frame index
            P6T_1t_11.tStart = t  # local t and not account for scr refresh
            P6T_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_11.started')
            P6T_1t_11.setAutoDraw(True)
        
        # *P7t_1t_11* updates
        if P7t_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_11.frameNStart = frameN  # exact frame index
            P7t_1t_11.tStart = t  # local t and not account for scr refresh
            P7t_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_11.started')
            P7t_1t_11.setAutoDraw(True)
        
        # *P8t_1t_11* updates
        if P8t_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_11.frameNStart = frameN  # exact frame index
            P8t_1t_11.tStart = t  # local t and not account for scr refresh
            P8t_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_11.started')
            P8t_1t_11.setAutoDraw(True)
        
        # *P9t_1t_11* updates
        if P9t_1t_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_11.frameNStart = frameN  # exact frame index
            P9t_1t_11.tStart = t  # local t and not account for scr refresh
            P9t_1t_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_11.started')
            P9t_1t_11.setAutoDraw(True)
        
        # *P10t_1t_2* updates
        if P10t_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10t_1t_2.frameNStart = frameN  # exact frame index
            P10t_1t_2.tStart = t  # local t and not account for scr refresh
            P10t_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10t_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10t_1t_2.started')
            P10t_1t_2.setAutoDraw(True)
        
        # *P11_1t_2* updates
        if P11_1t_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11_1t_2.frameNStart = frameN  # exact frame index
            P11_1t_2.tStart = t  # local t and not account for scr refresh
            P11_1t_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11_1t_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11_1t_2.started')
            P11_1t_2.setAutoDraw(True)
        
        # *finish_12* updates
        if finish_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_12.frameNStart = frameN  # exact frame index
            finish_12.tStart = t  # local t and not account for scr refresh
            finish_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_12.started')
            finish_12.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_4target_6objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_4target_6objects" ---
    for thisComponent in mng_test_4target_6objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_16
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_4t_6.lineColor = 'white'
    P3T_rectangle_4t_6.lineColor = 'white'
    P6T_rectangle_4t_6.lineColor = 'white'
    P7T_rectangle_4t_6.lineColor = 'white'
    P10T_rectangle_4t_6.lineColor = 'white'
    P11T_rectangle_4t_6.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects == 6:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color)) & (float(corr_p10) == float(P10T_rectangle_color)) & (float(corr_p11) == float(P11T_rectangle_color))):
            mng_exptrials_t4.addData('accuracy_t4_o6', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t4.addData('accuracy_t4_o6', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)        
    elif meanb2 < 66:
            continueRoutine=False
            thisExp.addData("presented", 0)
    elif meanb3 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t4 (TrialHandler)
    # the Routine "mng_test_4target_6objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_4target_8objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_17
    if objects > 8:
        continueRoutine=False
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    clicked10 = 0
    clicked11 = 0
    clicked12 = 0
    clicked13 = 0
    clicked14 = 0
    clicked15 = 0
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    P10T_rectangle_color = 0
    P11T_rectangle_color = 0
    P12T_rectangle_color = 0
    P13T_rectangle_color = 0
    P14T_rectangle_color = 0
    P15T_rectangle_color = 0
    
    # setup some python lists for storing info about the mouse_13
    mouse_13.clicked_name = []
    gotValidClick = False  # until a click is received
    P1T_1t_12.setImage(test_p1)
    P2T_1t_12.setImage(test_p2)
    P3T_1t_12.setImage(test_p3)
    P4T_1t_12.setImage(test_p4)
    P5T_1t_12.setImage(test_p5)
    P6T_1t_12.setImage(test_p6)
    P7t_1t_12.setImage(test_p7)
    P8t_1t_12.setImage(test_p8)
    P9t_1t_12.setImage(test_p9)
    P10t_1t_9.setImage(test_p10)
    P11_1t_9.setImage(test_p11)
    P12_1t.setImage(test_p12)
    P13_1t.setImage(test_p13)
    P14_1t.setImage(test_p14)
    P15_1t.setImage(test_p15)
    # keep track of which components have finished
    mng_test_4target_8objectsComponents = [mouse_13, P2T_rectangle_4t_8, P3T_rectangle_4t_8, P6T_rectangle_4t_8, P7T_rectangle_4t_8, P12T_rectangle_4t_8, P13T_rectangle_4t_8, P14T_rectangle_4t_8, P15T_rectangle_4t_8, P1T_1t_12, P2T_1t_12, P3T_1t_12, P4T_1t_12, P5T_1t_12, P6T_1t_12, P7t_1t_12, P8t_1t_12, P9t_1t_12, P10t_1t_9, P11_1t_9, P12_1t, P13_1t, P14_1t, P15_1t, finish_13]
    for thisComponent in mng_test_4target_8objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_4target_8objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_17
        if meanb1 < acc_thr:
                continueRoutine=False
                
        if meanb2 < acc_thr:
                continueRoutine=False 
        
        if meanb3 < acc_thr:
                continueRoutine=False
        
        if mouse_13.isPressedIn(P2T_rectangle_4t_8):
            if clicked2 == 0:
                clicked2 = 1
                if lineColor == 'white':
                    P2T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P2T_rectangle', 1) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 1
                elif lineColor == 'black':
                    P2T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P2T_rectangle', 0) #OR exp.addData('letter', letter)
                    P2T_rectangle_color = 0
        elif clicked2 == 1:
            clicked2 = 0
        
        if mouse_13.isPressedIn(P3T_rectangle_4t_8):
            if clicked3 == 0:
                clicked3 = 1
                if lineColor == 'white':
                    P3T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    P3T_rectangle_color = 1
                    thisExp.addData('P3T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P3T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    P3T_rectangle_color = 0
                    thisExp.addData('P3T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked3 == 1:
            clicked3 = 0
        
        if mouse_13.isPressedIn(P6T_rectangle_4t_8):
            if clicked6 == 0:
                clicked6 = 1
                if lineColor == 'white':
                    P6T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    P6T_rectangle_color = 1
                    thisExp.addData('P6T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P6T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    P6T_rectangle_color = 0
                    thisExp.addData('P6T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked6 == 1:
            clicked6 = 0
            
        if mouse_13.isPressedIn(P7T_rectangle_4t_8):
            if clicked7 == 0:
                clicked7 = 1
                if lineColor == 'white':
                    P7T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    P7T_rectangle_color = 1
                    thisExp.addData('P7T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P7T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    P7T_rectangle_color = 0
                    thisExp.addData('P7T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked7 == 1:
            clicked7 = 0
        
        if mouse_13.isPressedIn(P12T_rectangle_4t_8):
            if clicked12 == 0:
                clicked12 = 1
                if lineColor == 'white':
                    P12T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P12T_rectangle', 1) #OR exp.addData('letter', letter)
                    P12T_rectangle_color = 1
                elif lineColor == 'black':
                    P12T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P12T_rectangle', 0) #OR exp.addData('letter', letter)
                    P12T_rectangle_color = 0
        elif clicked12 == 1:
            clicked12 = 0
            
        if mouse_13.isPressedIn(P13T_rectangle_4t_8):
            if clicked13 == 0:
                clicked13 = 1
                if lineColor == 'white':
                    P13T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P13T_rectangle', 1) #OR exp.addData('letter', letter)
                    P13T_rectangle_color = 1
                elif lineColor == 'black':
                    P13T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P13T_rectangle', 0) #OR exp.addData('letter', letter)
                    P13T_rectangle_color = 0
        elif clicked13 == 1:
            clicked13 = 0
        
        if mouse_13.isPressedIn(P14T_rectangle_4t_8):
            if clicked14 == 0:
                clicked14 = 1
                if lineColor == 'white':
                    P14T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P14T_rectangle', 1) #OR exp.addData('letter', letter)
                    P14T_rectangle_color = 1
                elif lineColor == 'black':
                    P14T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P14T_rectangle', 0) #OR exp.addData('letter', letter)
                    P14T_rectangle_color = 0
        elif clicked14 == 1:
            clicked14 = 0
            
        if mouse_13.isPressedIn(P15T_rectangle_4t_8):
            if clicked15 == 0:
                clicked15 = 1
                if lineColor == 'white':
                    P15T_rectangle_4t_8.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P15T_rectangle', 1) #OR exp.addData('letter', letter)
                    P15T_rectangle_color = 1
                elif lineColor == 'black':
                    P15T_rectangle_4t_8.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P15T_rectangle', 0) #OR exp.addData('letter', letter)
                    P15T_rectangle_color = 0
        elif clicked15 == 1:
            clicked15 = 0
        
        if mouse_13.isPressedIn(finish_11):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_13* updates
        if mouse_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_13.frameNStart = frameN  # exact frame index
            mouse_13.tStart = t  # local t and not account for scr refresh
            mouse_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_13.started', t)
            mouse_13.status = STARTED
            mouse_13.mouseClock.reset()
            prevButtonState = mouse_13.getPressed()  # if button is down already this ISN'T a new click
        
        # *P2T_rectangle_4t_8* updates
        if P2T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P2T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P2T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_rectangle_4t_8.started')
            P2T_rectangle_4t_8.setAutoDraw(True)
        
        # *P3T_rectangle_4t_8* updates
        if P3T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P3T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P3T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle_4t_8.started')
            P3T_rectangle_4t_8.setAutoDraw(True)
        
        # *P6T_rectangle_4t_8* updates
        if P6T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P6T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P6T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle_4t_8.started')
            P6T_rectangle_4t_8.setAutoDraw(True)
        
        # *P7T_rectangle_4t_8* updates
        if P7T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P7T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P7T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7T_rectangle_4t_8.started')
            P7T_rectangle_4t_8.setAutoDraw(True)
        
        # *P12T_rectangle_4t_8* updates
        if P12T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P12T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P12T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P12T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P12T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P12T_rectangle_4t_8.started')
            P12T_rectangle_4t_8.setAutoDraw(True)
        
        # *P13T_rectangle_4t_8* updates
        if P13T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P13T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P13T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P13T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P13T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P13T_rectangle_4t_8.started')
            P13T_rectangle_4t_8.setAutoDraw(True)
        
        # *P14T_rectangle_4t_8* updates
        if P14T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P14T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P14T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P14T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P14T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P14T_rectangle_4t_8.started')
            P14T_rectangle_4t_8.setAutoDraw(True)
        
        # *P15T_rectangle_4t_8* updates
        if P15T_rectangle_4t_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P15T_rectangle_4t_8.frameNStart = frameN  # exact frame index
            P15T_rectangle_4t_8.tStart = t  # local t and not account for scr refresh
            P15T_rectangle_4t_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P15T_rectangle_4t_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P15T_rectangle_4t_8.started')
            P15T_rectangle_4t_8.setAutoDraw(True)
        
        # *P1T_1t_12* updates
        if P1T_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_12.frameNStart = frameN  # exact frame index
            P1T_1t_12.tStart = t  # local t and not account for scr refresh
            P1T_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_12.started')
            P1T_1t_12.setAutoDraw(True)
        
        # *P2T_1t_12* updates
        if P2T_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_12.frameNStart = frameN  # exact frame index
            P2T_1t_12.tStart = t  # local t and not account for scr refresh
            P2T_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_12.started')
            P2T_1t_12.setAutoDraw(True)
        
        # *P3T_1t_12* updates
        if P3T_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_12.frameNStart = frameN  # exact frame index
            P3T_1t_12.tStart = t  # local t and not account for scr refresh
            P3T_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_12.started')
            P3T_1t_12.setAutoDraw(True)
        
        # *P4T_1t_12* updates
        if P4T_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_12.frameNStart = frameN  # exact frame index
            P4T_1t_12.tStart = t  # local t and not account for scr refresh
            P4T_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_12.started')
            P4T_1t_12.setAutoDraw(True)
        
        # *P5T_1t_12* updates
        if P5T_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_12.frameNStart = frameN  # exact frame index
            P5T_1t_12.tStart = t  # local t and not account for scr refresh
            P5T_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_12.started')
            P5T_1t_12.setAutoDraw(True)
        
        # *P6T_1t_12* updates
        if P6T_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_12.frameNStart = frameN  # exact frame index
            P6T_1t_12.tStart = t  # local t and not account for scr refresh
            P6T_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_12.started')
            P6T_1t_12.setAutoDraw(True)
        
        # *P7t_1t_12* updates
        if P7t_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_12.frameNStart = frameN  # exact frame index
            P7t_1t_12.tStart = t  # local t and not account for scr refresh
            P7t_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_12.started')
            P7t_1t_12.setAutoDraw(True)
        
        # *P8t_1t_12* updates
        if P8t_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_12.frameNStart = frameN  # exact frame index
            P8t_1t_12.tStart = t  # local t and not account for scr refresh
            P8t_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_12.started')
            P8t_1t_12.setAutoDraw(True)
        
        # *P9t_1t_12* updates
        if P9t_1t_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_12.frameNStart = frameN  # exact frame index
            P9t_1t_12.tStart = t  # local t and not account for scr refresh
            P9t_1t_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_12.started')
            P9t_1t_12.setAutoDraw(True)
        
        # *P10t_1t_9* updates
        if P10t_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10t_1t_9.frameNStart = frameN  # exact frame index
            P10t_1t_9.tStart = t  # local t and not account for scr refresh
            P10t_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10t_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10t_1t_9.started')
            P10t_1t_9.setAutoDraw(True)
        
        # *P11_1t_9* updates
        if P11_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11_1t_9.frameNStart = frameN  # exact frame index
            P11_1t_9.tStart = t  # local t and not account for scr refresh
            P11_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11_1t_9.started')
            P11_1t_9.setAutoDraw(True)
        
        # *P12_1t* updates
        if P12_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P12_1t.frameNStart = frameN  # exact frame index
            P12_1t.tStart = t  # local t and not account for scr refresh
            P12_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P12_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P12_1t.started')
            P12_1t.setAutoDraw(True)
        
        # *P13_1t* updates
        if P13_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P13_1t.frameNStart = frameN  # exact frame index
            P13_1t.tStart = t  # local t and not account for scr refresh
            P13_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P13_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P13_1t.started')
            P13_1t.setAutoDraw(True)
        
        # *P14_1t* updates
        if P14_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P14_1t.frameNStart = frameN  # exact frame index
            P14_1t.tStart = t  # local t and not account for scr refresh
            P14_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P14_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P14_1t.started')
            P14_1t.setAutoDraw(True)
        
        # *P15_1t* updates
        if P15_1t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P15_1t.frameNStart = frameN  # exact frame index
            P15_1t.tStart = t  # local t and not account for scr refresh
            P15_1t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P15_1t, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P15_1t.started')
            P15_1t.setAutoDraw(True)
        
        # *finish_13* updates
        if finish_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_13.frameNStart = frameN  # exact frame index
            finish_13.tStart = t  # local t and not account for scr refresh
            finish_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_13.started')
            finish_13.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_4target_8objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_4target_8objects" ---
    for thisComponent in mng_test_4target_8objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_17
    #print(ClickCount1)
    ClickCount1 = 0
    
    P2T_rectangle_4t_8.lineColor = 'white'
    P3T_rectangle_4t_8.lineColor = 'white'
    P6T_rectangle_4t_8.lineColor = 'white'
    P7T_rectangle_4t_8.lineColor = 'white'
    P12T_rectangle_4t_8.lineColor = 'white'
    P13T_rectangle_4t_8.lineColor = 'white'
    P14T_rectangle_4t_8.lineColor = 'white'
    P15T_rectangle_4t_8.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects == 8:
        if ((float(corr_p2) == float(P2T_rectangle_color)) & (float(corr_p3) == float(P3T_rectangle_color)) & (float(corr_p6) == float(P6T_rectangle_color)) & (float(corr_p7) == float(P7T_rectangle_color)) & (float(corr_p12) == float(P12T_rectangle_color)) & (float(corr_p13) == float(P13T_rectangle_color)) & (float(corr_p14) == float(P14T_rectangle_color)) & (float(corr_p15) == float(P15T_rectangle_color))):
            mng_exptrials_t4.addData('accuracy_t4_o8', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t4.addData('accuracy_t4_o8', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)        
    elif meanb2 < 66:
            continueRoutine=False
            thisExp.addData("presented", 0)
    elif meanb3 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t4 (TrialHandler)
    # the Routine "mng_test_4target_8objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "mng_test_4target_10objects" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_18
    if objects < 5:
        continueRoutine=False
    #beginning_trial = globalClock.getTime()
    
    incorr = 1
    ClickCount1 = 0
    startTime = globalClock.getTime()
    end_trial = 0
    
    clicked1 = 0
    clicked2 = 0
    clicked3 = 0
    clicked4 = 0
    clicked5 = 0
    clicked6 = 0
    clicked6 = 0
    clicked7 = 0
    clicked8 = 0
    clicked9 = 0
    clicked10 = 0
    clicked11 = 0
    clicked12 = 0
    clicked13 = 0
    clicked14 = 0
    clicked15 = 0
    clicked16 = 0
    clicked17 = 0
    clicked18 = 0
    clicked19 = 0
    clicked20 = 0
    
    lineColor = 'white'
    msg = 'Incorrect'
    
    P1T_rectangle_color = 0
    P2T_rectangle_color = 0
    P3T_rectangle_color = 0
    P4T_rectangle_color = 0
    P5T_rectangle_color = 0
    P6T_rectangle_color = 0
    P7T_rectangle_color = 0
    P8T_rectangle_color = 0
    P9T_rectangle_color = 0
    P10T_rectangle_color = 0
    P11T_rectangle_color = 0
    P12T_rectangle_color = 0
    P13T_rectangle_color = 0
    P14T_rectangle_color = 0
    P15T_rectangle_color = 0
    P16T_rectangle_color = 0
    P17T_rectangle_color = 0
    P18T_rectangle_color = 0
    P19T_rectangle_color = 0
    P20T_rectangle_color = 0
    
    
    # setup some python lists for storing info about the mouse_14
    gotValidClick = False  # until a click is received
    P1T_1t_13.setImage(test_p1)
    P2T_1t_13.setImage(test_p2)
    P3T_1t_13.setImage(test_p3)
    P4T_1t_13.setImage(test_p4)
    P5T_1t_13.setImage(test_p5)
    P6T_1t_13.setImage(test_p6)
    P7t_1t_13.setImage(test_p7)
    P8t_1t_13.setImage(test_p8)
    P9t_1t_13.setImage(test_p9)
    P10t_1t_10.setImage(test_p10)
    P11_1t_10.setImage(test_p11)
    P12_1t_9.setImage(test_p12)
    P13_1t_9.setImage(test_p13)
    P14_1t_9.setImage(test_p14)
    P15_1t_9.setImage(test_p15)
    P16_1t_9.setImage(test_p16)
    P17_1t_9.setImage(test_p17)
    P18_1t_9.setImage(test_p18)
    P19_1t_9.setImage(test_p19)
    P20_1t_9.setImage(test_p20)
    # keep track of which components have finished
    mng_test_4target_10objectsComponents = [mouse_14, P1T_rectangle_4t_10, P4T_rectangle_4t_10, P5T_rectangle_4t_10, P8T_rectangle_4t_10, P9T_rectangle_4t_10, P16T_rectangle_4t_10, P17T_rectangle_4t_10, P18T_rectangle_4t_10, P19T_rectangle_4t_10, P20T_rectangle_4t_10, P1T_1t_13, P2T_1t_13, P3T_1t_13, P4T_1t_13, P5T_1t_13, P6T_1t_13, P7t_1t_13, P8t_1t_13, P9t_1t_13, P10t_1t_10, P11_1t_10, P12_1t_9, P13_1t_9, P14_1t_9, P15_1t_9, P16_1t_9, P17_1t_9, P18_1t_9, P19_1t_9, P20_1t_9, finish_14]
    for thisComponent in mng_test_4target_10objectsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mng_test_4target_10objects" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_18
        if meanb1 < acc_thr:
                continueRoutine=False
        
        if meanb2 < acc_thr:
                continueRoutine=False
        
        if meanb3 < acc_thr:
                continueRoutine=False
        
        if mouse_14.isPressedIn(P1T_rectangle_4t_10):
            if clicked1 == 0:
                clicked1 = 1
                if lineColor == 'white':
                    P1T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    P1T_rectangle_color = 1
                    thisExp.addData('P1T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P1T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    P1T_rectangle_color = 0
                    thisExp.addData('P1T_rectangle', 0)
        elif clicked1 == 1:
            clicked1 = 0
        
        if mouse_14.isPressedIn(P4T_rectangle_4t_10):
            if clicked4 == 0:
                clicked4 = 1
                if lineColor == 'white':
                    P4T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    P4T_rectangle_color = 1
                    thisExp.addData('P4T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P4T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    P4T_rectangle_color = 0
                    thisExp.addData('P4T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked4 == 1:
            clicked4 = 0
        
        if mouse_14.isPressedIn(P5T_rectangle_4t_10):
            if clicked5 == 0:
                clicked5 = 1
                if lineColor == 'white':
                    P5T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    P5T_rectangle_color = 1
                    thisExp.addData('P5T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P5T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    P5T_rectangle_color = 0
                    thisExp.addData('P5T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked5 == 1:
            clicked5 = 0
            
        if mouse_14.isPressedIn(P8T_rectangle_4t_10):
            if clicked8 == 0:
                clicked8 = 1
                if lineColor == 'white':
                    P8T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    P8T_rectangle_color = 1
                    thisExp.addData('P8T_rectangle', 1) #OR exp.addData('letter', letter)
                elif lineColor == 'black':
                    P8T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    P8T_rectangle_color = 0
                    thisExp.addData('P8T_rectangle', 0) #OR exp.addData('letter', letter)
        elif clicked8 == 1:
            clicked8 = 0
        
        if mouse_14.isPressedIn(P9T_rectangle_4t_10):
            if clicked9 == 0:
                clicked9 = 1
                if lineColor == 'white':
                    P9T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P9T_rectangle', 1) #OR exp.addData('letter', letter)
                    P9T_rectangle_color = 1
                elif lineColor == 'black':
                    P9T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P9T_rectangle', 0) #OR exp.addData('letter', letter)
                    P9T_rectangle_color = 0
        elif clicked9 == 1:
            clicked9 = 0
            
        if mouse_14.isPressedIn(P16T_rectangle_4t_10):
            if clicked16 == 0:
                clicked16 = 1
                if lineColor == 'white':
                    P16T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P16T_rectangle', 1) #OR exp.addData('letter', letter)
                    P13T_rectangle_color = 1
                elif lineColor == 'black':
                    P16T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P16T_rectangle', 0) #OR exp.addData('letter', letter)
                    P16T_rectangle_color = 0
        elif clicked16 == 1:
            clicked16 = 0
        
        if mouse_14.isPressedIn(P17T_rectangle_4t_10):
            if clicked17 == 0:
                clicked17 = 1
                if lineColor == 'white':
                    P17T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P17T_rectangle', 1) #OR exp.addData('letter', letter)
                    P17T_rectangle_color = 1
                elif lineColor == 'black':
                    P17T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P17T_rectangle', 0) #OR exp.addData('letter', letter)
                    P17T_rectangle_color = 0
        elif clicked17 == 1:
            clicked17 = 0
            
        if mouse_14.isPressedIn(P18T_rectangle_4t_10):
            if clicked18 == 0:
                clicked18 = 1
                if lineColor == 'white':
                    P18T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P18T_rectangle', 1) #OR exp.addData('letter', letter)
                    P18T_rectangle_color = 1
                elif lineColor == 'black':
                    P18T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P18T_rectangle', 0) #OR exp.addData('letter', letter)
                    P18T_rectangle_color = 0
        elif clicked18 == 1:
            clicked18 = 0
            
        if mouse_14.isPressedIn(P19T_rectangle_4t_10):
            if clicked19 == 0:
                clicked19 = 1
                if lineColor == 'white':
                    P19T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P19T_rectangle', 1) #OR exp.addData('letter', letter)
                    P19T_rectangle_color = 1
                elif lineColor == 'black':
                    P19T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P19T_rectangle', 0) #OR exp.addData('letter', letter)
                    P19T_rectangle_color = 0
        elif clicked19 == 1:
            clicked19 = 0
            
        if mouse_14.isPressedIn(P20T_rectangle_4t_10):
            if clicked20 == 0:
                clicked20 = 1
                if lineColor == 'white':
                    P20T_rectangle_4t_10.lineColor = 'black'
                    lineColor = 'black'
                    thisExp.addData('P20T_rectangle', 1) #OR exp.addData('letter', letter)
                    P20T_rectangle_color = 1
                elif lineColor == 'black':
                    P20T_rectangle_4t_10.lineColor = 'white'
                    lineColor = 'white'
                    thisExp.addData('P20T_rectangle', 0) #OR exp.addData('letter', letter)
                    P20T_rectangle_color = 0
        elif clicked20 == 1:
            clicked20 = 0
            
        if mouse_14.isPressedIn(finish_14):
            continueRoutine = False
            end_trial = globalClock.getTime();
            thisExp.addData("end", end_trial);
            time_exp = (end_trial - beginning_trial)
            thisExp.addData("rt", time_exp);
        else:
            time_exp = 0;
            thisExp.addData("rt", time_exp);
        # *mouse_14* updates
        if mouse_14.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_14.frameNStart = frameN  # exact frame index
            mouse_14.tStart = t  # local t and not account for scr refresh
            mouse_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_14.started', t)
            mouse_14.status = STARTED
            mouse_14.mouseClock.reset()
            prevButtonState = mouse_14.getPressed()  # if button is down already this ISN'T a new click
        
        # *P1T_rectangle_4t_10* updates
        if P1T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P1T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P1T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_rectangle_4t_10.started')
            P1T_rectangle_4t_10.setAutoDraw(True)
        
        # *P4T_rectangle_4t_10* updates
        if P4T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P4T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P4T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_rectangle_4t_10.started')
            P4T_rectangle_4t_10.setAutoDraw(True)
        
        # *P5T_rectangle_4t_10* updates
        if P5T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P5T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P5T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_rectangle_4t_10.started')
            P5T_rectangle_4t_10.setAutoDraw(True)
        
        # *P8T_rectangle_4t_10* updates
        if P8T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P8T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P8T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8T_rectangle_4t_10.started')
            P8T_rectangle_4t_10.setAutoDraw(True)
        
        # *P9T_rectangle_4t_10* updates
        if P9T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P9T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P9T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9T_rectangle_4t_10.started')
            P9T_rectangle_4t_10.setAutoDraw(True)
        
        # *P16T_rectangle_4t_10* updates
        if P16T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P16T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P16T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P16T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P16T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P16T_rectangle_4t_10.started')
            P16T_rectangle_4t_10.setAutoDraw(True)
        
        # *P17T_rectangle_4t_10* updates
        if P17T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P17T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P17T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P17T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P17T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P17T_rectangle_4t_10.started')
            P17T_rectangle_4t_10.setAutoDraw(True)
        
        # *P18T_rectangle_4t_10* updates
        if P18T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P18T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P18T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P18T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P18T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P18T_rectangle_4t_10.started')
            P18T_rectangle_4t_10.setAutoDraw(True)
        
        # *P19T_rectangle_4t_10* updates
        if P19T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P19T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P19T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P19T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P19T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P19T_rectangle_4t_10.started')
            P19T_rectangle_4t_10.setAutoDraw(True)
        
        # *P20T_rectangle_4t_10* updates
        if P20T_rectangle_4t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P20T_rectangle_4t_10.frameNStart = frameN  # exact frame index
            P20T_rectangle_4t_10.tStart = t  # local t and not account for scr refresh
            P20T_rectangle_4t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P20T_rectangle_4t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P20T_rectangle_4t_10.started')
            P20T_rectangle_4t_10.setAutoDraw(True)
        
        # *P1T_1t_13* updates
        if P1T_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1T_1t_13.frameNStart = frameN  # exact frame index
            P1T_1t_13.tStart = t  # local t and not account for scr refresh
            P1T_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1T_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1T_1t_13.started')
            P1T_1t_13.setAutoDraw(True)
        
        # *P2T_1t_13* updates
        if P2T_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2T_1t_13.frameNStart = frameN  # exact frame index
            P2T_1t_13.tStart = t  # local t and not account for scr refresh
            P2T_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2T_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2T_1t_13.started')
            P2T_1t_13.setAutoDraw(True)
        
        # *P3T_1t_13* updates
        if P3T_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_1t_13.frameNStart = frameN  # exact frame index
            P3T_1t_13.tStart = t  # local t and not account for scr refresh
            P3T_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_1t_13.started')
            P3T_1t_13.setAutoDraw(True)
        
        # *P4T_1t_13* updates
        if P4T_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_1t_13.frameNStart = frameN  # exact frame index
            P4T_1t_13.tStart = t  # local t and not account for scr refresh
            P4T_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_1t_13.started')
            P4T_1t_13.setAutoDraw(True)
        
        # *P5T_1t_13* updates
        if P5T_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_1t_13.frameNStart = frameN  # exact frame index
            P5T_1t_13.tStart = t  # local t and not account for scr refresh
            P5T_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_1t_13.started')
            P5T_1t_13.setAutoDraw(True)
        
        # *P6T_1t_13* updates
        if P6T_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_1t_13.frameNStart = frameN  # exact frame index
            P6T_1t_13.tStart = t  # local t and not account for scr refresh
            P6T_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_1t_13.started')
            P6T_1t_13.setAutoDraw(True)
        
        # *P7t_1t_13* updates
        if P7t_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P7t_1t_13.frameNStart = frameN  # exact frame index
            P7t_1t_13.tStart = t  # local t and not account for scr refresh
            P7t_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P7t_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P7t_1t_13.started')
            P7t_1t_13.setAutoDraw(True)
        
        # *P8t_1t_13* updates
        if P8t_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P8t_1t_13.frameNStart = frameN  # exact frame index
            P8t_1t_13.tStart = t  # local t and not account for scr refresh
            P8t_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P8t_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P8t_1t_13.started')
            P8t_1t_13.setAutoDraw(True)
        
        # *P9t_1t_13* updates
        if P9t_1t_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P9t_1t_13.frameNStart = frameN  # exact frame index
            P9t_1t_13.tStart = t  # local t and not account for scr refresh
            P9t_1t_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P9t_1t_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P9t_1t_13.started')
            P9t_1t_13.setAutoDraw(True)
        
        # *P10t_1t_10* updates
        if P10t_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P10t_1t_10.frameNStart = frameN  # exact frame index
            P10t_1t_10.tStart = t  # local t and not account for scr refresh
            P10t_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P10t_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P10t_1t_10.started')
            P10t_1t_10.setAutoDraw(True)
        
        # *P11_1t_10* updates
        if P11_1t_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P11_1t_10.frameNStart = frameN  # exact frame index
            P11_1t_10.tStart = t  # local t and not account for scr refresh
            P11_1t_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P11_1t_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P11_1t_10.started')
            P11_1t_10.setAutoDraw(True)
        
        # *P12_1t_9* updates
        if P12_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P12_1t_9.frameNStart = frameN  # exact frame index
            P12_1t_9.tStart = t  # local t and not account for scr refresh
            P12_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P12_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P12_1t_9.started')
            P12_1t_9.setAutoDraw(True)
        
        # *P13_1t_9* updates
        if P13_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P13_1t_9.frameNStart = frameN  # exact frame index
            P13_1t_9.tStart = t  # local t and not account for scr refresh
            P13_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P13_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P13_1t_9.started')
            P13_1t_9.setAutoDraw(True)
        
        # *P14_1t_9* updates
        if P14_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P14_1t_9.frameNStart = frameN  # exact frame index
            P14_1t_9.tStart = t  # local t and not account for scr refresh
            P14_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P14_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P14_1t_9.started')
            P14_1t_9.setAutoDraw(True)
        
        # *P15_1t_9* updates
        if P15_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P15_1t_9.frameNStart = frameN  # exact frame index
            P15_1t_9.tStart = t  # local t and not account for scr refresh
            P15_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P15_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P15_1t_9.started')
            P15_1t_9.setAutoDraw(True)
        
        # *P16_1t_9* updates
        if P16_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P16_1t_9.frameNStart = frameN  # exact frame index
            P16_1t_9.tStart = t  # local t and not account for scr refresh
            P16_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P16_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P16_1t_9.started')
            P16_1t_9.setAutoDraw(True)
        
        # *P17_1t_9* updates
        if P17_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P17_1t_9.frameNStart = frameN  # exact frame index
            P17_1t_9.tStart = t  # local t and not account for scr refresh
            P17_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P17_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P17_1t_9.started')
            P17_1t_9.setAutoDraw(True)
        
        # *P18_1t_9* updates
        if P18_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P18_1t_9.frameNStart = frameN  # exact frame index
            P18_1t_9.tStart = t  # local t and not account for scr refresh
            P18_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P18_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P18_1t_9.started')
            P18_1t_9.setAutoDraw(True)
        
        # *P19_1t_9* updates
        if P19_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P19_1t_9.frameNStart = frameN  # exact frame index
            P19_1t_9.tStart = t  # local t and not account for scr refresh
            P19_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P19_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P19_1t_9.started')
            P19_1t_9.setAutoDraw(True)
        
        # *P20_1t_9* updates
        if P20_1t_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P20_1t_9.frameNStart = frameN  # exact frame index
            P20_1t_9.tStart = t  # local t and not account for scr refresh
            P20_1t_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P20_1t_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P20_1t_9.started')
            P20_1t_9.setAutoDraw(True)
        
        # *finish_14* updates
        if finish_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_14.frameNStart = frameN  # exact frame index
            finish_14.tStart = t  # local t and not account for scr refresh
            finish_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finish_14.started')
            finish_14.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_test_4target_10objectsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test_4target_10objects" ---
    for thisComponent in mng_test_4target_10objectsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_18
    #print(ClickCount1)
    ClickCount1 = 0
    
    P1T_rectangle_4t_10.lineColor = 'white'
    P4T_rectangle_4t_10.lineColor = 'white'
    P5T_rectangle_4t_10.lineColor = 'white'
    P8T_rectangle_4t_10.lineColor = 'white'
    P9T_rectangle_4t_10.lineColor = 'white'
    P16T_rectangle_4t_10.lineColor = 'white'
    P17T_rectangle_4t_10.lineColor = 'white'
    P18T_rectangle_4t_10.lineColor = 'white'
    P19T_rectangle_4t_10.lineColor = 'white'
    P20T_rectangle_4t_10.lineColor = 'white'
    
    
    print("finish")
    print(float(P2T_rectangle_color))
    print(float(corr_p2))
    
    if objects == 10:
        if ((float(corr_p1) == float(P1T_rectangle_color)) & (float(corr_p4) == float(P4T_rectangle_color)) & (float(corr_p5) == float(P5T_rectangle_color)) & (float(corr_p8) == float(P8T_rectangle_color)) & (float(corr_p9) == float(P9T_rectangle_color)) & (float(corr_p16) == float(P16T_rectangle_color)) & (float(corr_p17) == float(P17T_rectangle_color)) & (float(corr_p18) == float(P18T_rectangle_color)) & (float(corr_p19) == float(P19T_rectangle_color)) & (float(corr_p20) == float(P20T_rectangle_color))):
            mng_exptrials_t4.addData('accuracy_t4_o10', 1) #OR exp.addData('letter', letter)
            msg = "Correct"
            incorr = 0
        else:
            msg = "Incorrect"
            incorr = 1
            mng_exptrials_t4.addData('accuracy_t4_o10', 0) #OR exp.addData('letter', letter)
            print("value incorr")
            print(incorr)
            
    #beginning_trial = globalClock.getTime()
    #end_trial = globalClock.getTime();
    #time_exp = (end_trial - beginning_trial)
    #thisExp.addData("rt", time_exp);
    
    if meanb1 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)        
    elif meanb2 < 66:
            continueRoutine=False
            thisExp.addData("presented", 0)
    elif meanb3 < acc_thr:
            continueRoutine=False
            thisExp.addData("presented", 0)
    else:
        thisExp.addData("presented", 1)
    # store data for mng_exptrials_t4 (TrialHandler)
    # the Routine "mng_test_4target_10objects" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mng_exptrials_t4'


# --- Prepare to start Routine "mng_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
mng_endComponents = [text_4, key_resp_13]
for thisComponent in mng_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "mng_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_13.started')
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mng_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mng_end" ---
for thisComponent in mng_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# Run 'End Routine' code from code_42
end_exp = globalClock.getTime();
time_exp = (end_exp - beginning_exp)
print(time_exp)
thisExp.addData("totaltime_exp", time_exp);
# the Routine "mng_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
