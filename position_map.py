from screeninfo import get_monitors
from move import moveAndClick, moveTo
from utils import getImagePosition, get_int, exists, delay, get_screen_resolution
from close import check_if_ok

import pyautogui
import constants as C

class Position_Map:
    res = get_monitors()[0]
    _center = [get_int(res.width / 2), get_int(res.height / 2)]

    @staticmethod
    def center_map(times = 2):
        if(times == 0): return [-1]

        artifact = Position_Map._get_artifact_pos()
        if exists(artifact): moveAndClick([artifact[0], artifact[1] - 20])
        else: 
            print('Cannot move the map since there is no point of reference')
            # try again.
            delay(1)
            check_if_ok()
            return Position_Map.center_map(times - 1)
        
        if Position_Map._is_centered(artifact): return artifact

        Position_Map._drag_map(artifact, Position_Map._center)
        return artifact

    @staticmethod
    def drag_map_to_the_top():
        artifact = Position_Map.center_map()
        if not exists(artifact): return artifact
        print('move to top')
        next_pos = [artifact[0], artifact[1] - 300]
        delay(1)
        Position_Map._drag_map(artifact, next_pos)
        delay(.5)

    @staticmethod
    def drag_map_to_the_bottom():
        artifact = Position_Map.center_map()
        if not exists(artifact): return artifact
        print('move to bottom')
        next_pos = [artifact[0], artifact[1] + 300]
        delay(1)
        Position_Map._drag_map(artifact, next_pos)
        delay(.5)
    
    @staticmethod
    def drag_map_to_the_right():
        artifact = Position_Map.center_map()
        if not exists(artifact): return artifact
        print('move to right')
        next_pos = [artifact[0] + 500, artifact[1]]
        delay(1)
        Position_Map._drag_map(artifact, next_pos)
        delay(.5)

    @staticmethod
    def drag_map_to_the_left():
        artifact = Position_Map.center_map()
        if not exists(artifact): return artifact
        print('move to left')
        next_pos = [artifact[0] - 500, artifact[1]]
        delay(1)
        Position_Map._drag_map(artifact, next_pos)
        delay(.5)
        return next_pos
    
    @staticmethod
    def _get_artifact_pos():
        screen_pos = get_screen_resolution()
        art_path = C.get_path(f'{C._BASE_UTILS}{screen_pos}')

        try: return getImagePosition(art_path, 1, .8)
        except: return getImagePosition(C.UTILS_ARTIFACT, 1, .8)
    
    @staticmethod
    def _is_centered(artifact):
        return artifact[0] == Position_Map._center[0] and artifact[1] == Position_Map._center[1]

    @staticmethod
    def _drag_map(artifact, next = [800, 450]):
        pyautogui.moveTo(*artifact, 0)
        # double mouse down to make sure the action is working.
        pyautogui.mouseDown()
        pyautogui.mouseDown()
        pyautogui.moveTo(*next, 0)
        
        delay(0.1)
        pyautogui.mouseUp()