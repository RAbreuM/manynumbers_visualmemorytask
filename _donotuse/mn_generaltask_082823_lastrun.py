#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Tue Sep  5 13:26:27 2023
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'mn_generaltask_082823'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/robertoabreu/Documents/indiana/mn_general_task/mn_generaltask_082823_lastrun.py',
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
    monitor='testMonitor', color='white', colorSpace='rgb',
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
    pos=[0,0], height=0.15, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "mng_blank" ---
blank_box = visual.TextStim(win=win, name='blank_box',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "mng_probe" ---
sound_1 = sound.Sound('Look At These 2.wav', secs=2, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
P1 = visual.ImageStim(
    win=win,
    name='P1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
P2 = visual.ImageStim(
    win=win,
    name='P2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
P3 = visual.ImageStim(
    win=win,
    name='P3', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0.625, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
P4 = visual.ImageStim(
    win=win,
    name='P4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
P5 = visual.ImageStim(
    win=win,
    name='P5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.375, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
P6 = visual.ImageStim(
    win=win,
    name='P6', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0.625, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "mng_test" ---
P1T_rectangle = visual.Rect(
    win=win, name='P1T_rectangle',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
P3T_rectangle = visual.Rect(
    win=win, name='P3T_rectangle',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(0.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
P5T_rectangle = visual.Rect(
    win=win, name='P5T_rectangle',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(0.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
P2T_rectangle = visual.Rect(
    win=win, name='P2T_rectangle',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.125, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
P4T_rectangle = visual.Rect(
    win=win, name='P4T_rectangle',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0.0, pos=(-.375, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
P6T_rectangle = visual.Rect(
    win=win, name='P6T_rectangle',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=(-0.625, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
P1T = visual.ImageStim(
    win=win,
    name='P1T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.125, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
P3T = visual.ImageStim(
    win=win,
    name='P3T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
P5T = visual.ImageStim(
    win=win,
    name='P5T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
P2T = visual.ImageStim(
    win=win,
    name='P2T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.125, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
P4T = visual.ImageStim(
    win=win,
    name='P4T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.375, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
P6T = visual.ImageStim(
    win=win,
    name='P6T', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.625, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
sound_3 = sound.Sound('What Pics.wav', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)

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

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mn_generaltask_4items_test.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mng_blank" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    mng_blankComponents = [blank_box]
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
    while continueRoutine and routineTimer.getTime() < 0.5:
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
        if blank_box.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_box.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_box.tStop = t  # not accounting for scr refresh
                blank_box.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_box.stopped')
                blank_box.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "mng_probe" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sound_1.setSound('Look At These 2.wav', secs=2, hamming=True)
    sound_1.setVolume(1.0, log=False)
    P1.setImage(probe_p1)
    P2.setImage(probe_p3)
    P4.setImage(probe_p2)
    P5.setImage(probe_p4)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    mng_probeComponents = [sound_1, P1, P2, P3, P4, P5, P6, key_resp]
    for thisComponent in mng_probeComponents:
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
    
    # --- Run Routine "mng_probe" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                sound_1.stop()
        
        # *P1* updates
        if P1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P1.frameNStart = frameN  # exact frame index
            P1.tStart = t  # local t and not account for scr refresh
            P1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P1.started')
            P1.setAutoDraw(True)
        if P1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P1.tStop = t  # not accounting for scr refresh
                P1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P1.stopped')
                P1.setAutoDraw(False)
        
        # *P2* updates
        if P2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P2.frameNStart = frameN  # exact frame index
            P2.tStart = t  # local t and not account for scr refresh
            P2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P2.started')
            P2.setAutoDraw(True)
        if P2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P2.tStop = t  # not accounting for scr refresh
                P2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P2.stopped')
                P2.setAutoDraw(False)
        
        # *P3* updates
        if P3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3.frameNStart = frameN  # exact frame index
            P3.tStart = t  # local t and not account for scr refresh
            P3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3.started')
            P3.setAutoDraw(True)
        if P3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P3.tStop = t  # not accounting for scr refresh
                P3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P3.stopped')
                P3.setAutoDraw(False)
        
        # *P4* updates
        if P4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4.frameNStart = frameN  # exact frame index
            P4.tStart = t  # local t and not account for scr refresh
            P4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4.started')
            P4.setAutoDraw(True)
        if P4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P4.tStop = t  # not accounting for scr refresh
                P4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P4.stopped')
                P4.setAutoDraw(False)
        
        # *P5* updates
        if P5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5.frameNStart = frameN  # exact frame index
            P5.tStart = t  # local t and not account for scr refresh
            P5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5.started')
            P5.setAutoDraw(True)
        if P5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P5.tStop = t  # not accounting for scr refresh
                P5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P5.stopped')
                P5.setAutoDraw(False)
        
        # *P6* updates
        if P6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6.frameNStart = frameN  # exact frame index
            P6.tStart = t  # local t and not account for scr refresh
            P6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6.started')
            P6.setAutoDraw(True)
        if P6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > P6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                P6.tStop = t  # not accounting for scr refresh
                P6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'P6.stopped')
                P6.setAutoDraw(False)
        
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
            if tThisFlipGlobal > key_resp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
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
        for thisComponent in mng_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_probe" ---
    for thisComponent in mng_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "mng_test" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    ClickCount1 = 0
    P1T.setImage(test_p1)
    P3T.setImage(test_p3)
    P5T.setImage(test_p5)
    P2T.setImage(test_p2)
    P4T.setImage(test_p4)
    P6T.setImage(test_p6)
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    sound_3.setSound('What Pics.wav', secs=2.5, hamming=True)
    sound_3.setVolume(1.0, log=False)
    # keep track of which components have finished
    mng_testComponents = [P1T_rectangle, P3T_rectangle, P5T_rectangle, P2T_rectangle, P4T_rectangle, P6T_rectangle, P1T, P3T, P5T, P2T, P4T, P6T, mouse, sound_3]
    for thisComponent in mng_testComponents:
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
    
    # --- Run Routine "mng_test" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        #print(ClickCount1)
        if mouse.isPressedIn(P1T_rectangle) and P1T_rectangle.lineColor[0] == 1.0:
            P1T_rectangle.lineColor = 'black'
            ClickCount1 = ClickCount1 + 1
            #print(ClickCount1)
            
        if mouse.isPressedIn(P2T_rectangle) and P2T_rectangle.lineColor[0] == 1.0:
            P2T_rectangle.lineColor = 'black'
            ClickCount1 = ClickCount1 + 1
            #print(ClickCount1)
            
        if mouse.isPressedIn(P3T_rectangle) and P3T_rectangle.lineColor[0] == 1.0:
            P3T_rectangle.lineColor = 'black'
            ClickCount1 = ClickCount1 + 1
            #print(ClickCount1)
            
        if mouse.isPressedIn(P4T_rectangle) and P4T_rectangle.lineColor[0] == 1.0:
            P4T_rectangle.lineColor = 'black'
            ClickCount1 = ClickCount1 + 1
            #print(ClickCount1)
            
        if mouse.isPressedIn(P5T_rectangle) and P5T_rectangle.lineColor[0] == 1.0:
            P5T_rectangle.lineColor = 'black'
            ClickCount1 = ClickCount1 + 1
            #print(ClickCount1)
            
        if mouse.isPressedIn(P6T_rectangle) and P6T_rectangle.lineColor[0] == 1.0:
            P6T_rectangle.lineColor = 'black'
            ClickCount1 = ClickCount1 + 1
            #print(ClickCount1)
            
        if ClickCount1 == clicks:
            print(ClickCount1)
            continueRoutine = False
        
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
        
        # *P3T_rectangle* updates
        if P3T_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T_rectangle.frameNStart = frameN  # exact frame index
            P3T_rectangle.tStart = t  # local t and not account for scr refresh
            P3T_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T_rectangle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T_rectangle.started')
            P3T_rectangle.setAutoDraw(True)
        
        # *P5T_rectangle* updates
        if P5T_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T_rectangle.frameNStart = frameN  # exact frame index
            P5T_rectangle.tStart = t  # local t and not account for scr refresh
            P5T_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T_rectangle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T_rectangle.started')
            P5T_rectangle.setAutoDraw(True)
        
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
        
        # *P4T_rectangle* updates
        if P4T_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T_rectangle.frameNStart = frameN  # exact frame index
            P4T_rectangle.tStart = t  # local t and not account for scr refresh
            P4T_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T_rectangle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T_rectangle.started')
            P4T_rectangle.setAutoDraw(True)
        
        # *P6T_rectangle* updates
        if P6T_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T_rectangle.frameNStart = frameN  # exact frame index
            P6T_rectangle.tStart = t  # local t and not account for scr refresh
            P6T_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T_rectangle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T_rectangle.started')
            P6T_rectangle.setAutoDraw(True)
        
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
        
        # *P3T* updates
        if P3T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P3T.frameNStart = frameN  # exact frame index
            P3T.tStart = t  # local t and not account for scr refresh
            P3T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P3T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P3T.started')
            P3T.setAutoDraw(True)
        
        # *P5T* updates
        if P5T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P5T.frameNStart = frameN  # exact frame index
            P5T.tStart = t  # local t and not account for scr refresh
            P5T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P5T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P5T.started')
            P5T.setAutoDraw(True)
        
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
        
        # *P4T* updates
        if P4T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P4T.frameNStart = frameN  # exact frame index
            P4T.tStart = t  # local t and not account for scr refresh
            P4T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P4T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P4T.started')
            P4T.setAutoDraw(True)
        
        # *P6T* updates
        if P6T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P6T.frameNStart = frameN  # exact frame index
            P6T.tStart = t  # local t and not account for scr refresh
            P6T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P6T, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P6T.started')
            P6T.setAutoDraw(True)
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
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_3.started', tThisFlipGlobal)
            sound_3.play(when=win)  # sync with win flip
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_3.stopped')
                sound_3.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mng_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mng_test" ---
    for thisComponent in mng_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    #print(ClickCount1)
    ClickCount1 = 0
    P1T_rectangle.lineColor = 'white'
    P2T_rectangle.lineColor = 'white'
    P3T_rectangle.lineColor = 'white'
    P4T_rectangle.lineColor = 'white'
    P5T_rectangle.lineColor = 'white'
    P6T_rectangle.lineColor = 'white'
    
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(P1T_rectangle)
            clickableList = P1T_rectangle
        except:
            clickableList = [P1T_rectangle]
        for obj in clickableList:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    trials.addData('mouse.leftButton', buttons[0])
    trials.addData('mouse.midButton', buttons[1])
    trials.addData('mouse.rightButton', buttons[2])
    if len(mouse.clicked_name):
        trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    sound_3.stop()  # ensure sound has stopped at end of routine
    # the Routine "mng_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


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
