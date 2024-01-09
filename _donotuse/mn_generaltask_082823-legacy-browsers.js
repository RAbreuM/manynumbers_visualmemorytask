/****************************** 
 * Mn_Generaltask_082823 Test *
 ******************************/


// store info about the experiment session:
let expName = 'mn_generaltask_082823';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from response_code
var timer_wcst = '';
var beginning_wcst = '';
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(mng_welcomeRoutineBegin());
flowScheduler.add(mng_welcomeRoutineEachFrame());
flowScheduler.add(mng_welcomeRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'colored PNG/PICTURE_67.png', 'path': 'colored PNG/PICTURE_67.png'},
    {'name': 'colored PNG/PICTURE_69.png', 'path': 'colored PNG/PICTURE_69.png'},
    {'name': 'mn_generaltask_4items_test.csv', 'path': 'mn_generaltask_4items_test.csv'},
    {'name': 'What Pics.wav', 'path': 'What Pics.wav'},
    {'name': 'colored PNG/PICTURE_75.png', 'path': 'colored PNG/PICTURE_75.png'},
    {'name': 'colored PNG/PICTURE_1.png', 'path': 'colored PNG/PICTURE_1.png'},
    {'name': 'colored PNG/PICTURE_90.png', 'path': 'colored PNG/PICTURE_90.png'},
    {'name': 'colored PNG/PICTURE_122.png', 'path': 'colored PNG/PICTURE_122.png'},
    {'name': 'Look At These 2.wav', 'path': 'Look At These 2.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var mng_welcomeClock;
var text;
var key_resp_2;
var mng_blankClock;
var blank_box;
var mng_probeClock;
var sound_1;
var P1;
var P2;
var P3;
var P4;
var key_resp;
var mng_testClock;
var P1T;
var P2T;
var P3T;
var P4T;
var mouse;
var sound_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "mng_welcome"
  mng_welcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mng_blank"
  mng_blankClock = new util.Clock();
  blank_box = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_box',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "mng_probe"
  mng_probeClock = new util.Clock();
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'Look At These 2.wav',
    secs: 2,
    });
  sound_1.setVolume(1.0);
  P1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  P2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  P3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  P4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "mng_test"
  mng_testClock = new util.Clock();
  P1T = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P1T', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.1, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  P2T = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P2T', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.1), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  P3T = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P3T', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.3, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  P4T = new visual.ImageStim({
    win : psychoJS.window,
    name : 'P4T', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.3), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  sound_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'What Pics.wav',
    secs: (- 1),
    });
  sound_2.setVolume(1.0);
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_2_allKeys;
var mng_welcomeComponents;
function mng_welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mng_welcome' ---
    t = 0;
    mng_welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    mng_welcomeComponents = [];
    mng_welcomeComponents.push(text);
    mng_welcomeComponents.push(key_resp_2);
    
    mng_welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function mng_welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mng_welcome' ---
    // get current time
    t = mng_welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mng_welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mng_welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mng_welcome' ---
    mng_welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "mng_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'mn_generaltask_4items_test.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(mng_blankRoutineBegin(snapshot));
      trialsLoopScheduler.add(mng_blankRoutineEachFrame());
      trialsLoopScheduler.add(mng_blankRoutineEnd(snapshot));
      trialsLoopScheduler.add(mng_probeRoutineBegin(snapshot));
      trialsLoopScheduler.add(mng_probeRoutineEachFrame());
      trialsLoopScheduler.add(mng_probeRoutineEnd(snapshot));
      trialsLoopScheduler.add(mng_testRoutineBegin(snapshot));
      trialsLoopScheduler.add(mng_testRoutineEachFrame());
      trialsLoopScheduler.add(mng_testRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var mng_blankComponents;
function mng_blankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mng_blank' ---
    t = 0;
    mng_blankClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    mng_blankComponents = [];
    mng_blankComponents.push(blank_box);
    
    mng_blankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function mng_blankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mng_blank' ---
    // get current time
    t = mng_blankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_box* updates
    if (t >= 0.0 && blank_box.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_box.tStart = t;  // (not accounting for frame time here)
      blank_box.frameNStart = frameN;  // exact frame index
      
      blank_box.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank_box.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_box.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mng_blankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mng_blankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mng_blank' ---
    mng_blankComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var mng_probeComponents;
function mng_probeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mng_probe' ---
    t = 0;
    mng_probeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_1.secs=2;
    sound_1.setVolume(1.0);
    P1.setImage(probe_p1);
    P2.setImage(probe_p2);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    mng_probeComponents = [];
    mng_probeComponents.push(sound_1);
    mng_probeComponents.push(P1);
    mng_probeComponents.push(P2);
    mng_probeComponents.push(P3);
    mng_probeComponents.push(P4);
    mng_probeComponents.push(key_resp);
    
    mng_probeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function mng_probeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mng_probe' ---
    // get current time
    t = mng_probeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_1
    if (t >= 0.0 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (2 > 0.5) {
        sound_1.stop();  // stop the sound (if longer than duration)
      }
      sound_1.status = PsychoJS.Status.FINISHED;
    }
    
    // *P1* updates
    if (t >= 0.0 && P1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P1.tStart = t;  // (not accounting for frame time here)
      P1.frameNStart = frameN;  // exact frame index
      
      P1.setAutoDraw(true);
    }

    
    // *P2* updates
    if (t >= 0.0 && P2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P2.tStart = t;  // (not accounting for frame time here)
      P2.frameNStart = frameN;  // exact frame index
      
      P2.setAutoDraw(true);
    }

    
    // *P3* updates
    if (t >= 0.0 && P3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P3.tStart = t;  // (not accounting for frame time here)
      P3.frameNStart = frameN;  // exact frame index
      
      P3.setAutoDraw(true);
    }

    
    // *P4* updates
    if (t >= 0.0 && P4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P4.tStart = t;  // (not accounting for frame time here)
      P4.frameNStart = frameN;  // exact frame index
      
      P4.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mng_probeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mng_probeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mng_probe' ---
    mng_probeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    sound_1.stop();  // ensure sound has stopped at end of routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "mng_probe" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var corr;
var timer_wcst;
var beginning_wcst;
var gotValidClick;
var mng_testComponents;
function mng_testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mng_test' ---
    t = 0;
    mng_testClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from response_code
    corr = 0;
    timer_wcst = new util.Clock();
    beginning_wcst = timer_wcst.getTime();
    
    var click_counter = 0;
    P1T.setImage(test_p1);
    P2T.setImage(test_p2);
    P3T.setImage(test_p3);
    P4T.setImage(test_p4);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    sound_2.secs=2.5;
    sound_2.setVolume(1.0);
    // keep track of which components have finished
    mng_testComponents = [];
    mng_testComponents.push(P1T);
    mng_testComponents.push(P2T);
    mng_testComponents.push(P3T);
    mng_testComponents.push(P4T);
    mng_testComponents.push(mouse);
    mng_testComponents.push(sound_2);
    
    mng_testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function mng_testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mng_test' ---
    // get current time
    t = mng_testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from response_code
    var current_wcst = timer_wcst.getTime();
    var allow_wcst = (current_wcst - beginning_wcst);
    console.log(allow_wcst)
    
    if(allow_wcst < 1.5){
        continueRoutine = true;
        } else {
            for (var stimulus, _pj_c = 0, _pj_a = [P1T, P2T, P3T, P4T], _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
                stimulus = _pj_a[_pj_c];
                if (mouse.isPressedIn(stimulus)) {
                    //var corrAnsMaybe = 'images/' + stimulus.name + '.jpg';
                    //console.log(stimulus.name, corrAns, corrAnsMaybe === corrAns);
                    //if ((corrAnsMaybe === corrAns)) {
                    //    corr = 1;
                    //    }
                    var end_wcst = timer_wcst.getTime();
                    var time_wcst_trial = (end_wcst - beginning_wcst);
                    //psychoJS.experiment.addData("wcst_rt", time_wcst_trial);
                    //psychoJS.experiment.addData("correct", corr);
                    //continueRoutine = false;
        }
    }
    }
    
    
    
    // *P1T* updates
    if (t >= 0.0 && P1T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P1T.tStart = t;  // (not accounting for frame time here)
      P1T.frameNStart = frameN;  // exact frame index
      
      P1T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (P1T.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      P1T.setAutoDraw(false);
    }
    
    // *P2T* updates
    if (t >= 0.0 && P2T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P2T.tStart = t;  // (not accounting for frame time here)
      P2T.frameNStart = frameN;  // exact frame index
      
      P2T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (P2T.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      P2T.setAutoDraw(false);
    }
    
    // *P3T* updates
    if (t >= 0.0 && P3T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P3T.tStart = t;  // (not accounting for frame time here)
      P3T.frameNStart = frameN;  // exact frame index
      
      P3T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (P3T.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      P3T.setAutoDraw(false);
    }
    
    // *P4T* updates
    if (t >= 0.0 && P4T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P4T.tStart = t;  // (not accounting for frame time here)
      P4T.frameNStart = frameN;  // exact frame index
      
      P4T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (P4T.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      P4T.setAutoDraw(false);
    }
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse.status = PsychoJS.Status.FINISHED;
  }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [P1T, P2T, P3T, P4T]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
        }
      }
    }
    // start/stop sound_2
    if (t >= 0.0 && sound_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_2.tStart = t;  // (not accounting for frame time here)
      sound_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_2.play(); });  // screen flip
      sound_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (2.5 > 0.5) {
        sound_2.stop();  // stop the sound (if longer than duration)
      }
      sound_2.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mng_testComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mng_testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mng_test' ---
    mng_testComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    sound_2.stop();  // ensure sound has stopped at end of routine
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
