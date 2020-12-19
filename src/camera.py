from point import P
from settings import *

class Camera:
    """ Class to draw different camera angles """

    def __init__(self, cx, cy, mode='default'):
        '''
        Initializes the game camera

        The game camera has 3 modes:

        - default: Follows the ball while showing surrounding players
        - zoomed: Follows the ball closely
        - full: Displays the entire field

        Attributes:
            cx (float): Camera's x coordinate
            cy (float): Camera's y coordinate
            mode (str): The camera mode
        '''
        self.c = P(cx,cy)
        set_mode(mode)

    @staticmethod
    def params(self):
        ''' Helper  method to reduce code redundancy '''
        if self.mode == 'default':
            return {'pt': CAM_DEF, 'fact': DEF_FACTOR}
        else:
            return {'pt': CAM_ZOOM, 'fact': ZOOM_FACTOR}

    def set_mode(self, mode):
        ''' Set the camera's mode. Mode must be one of ['full', 'default', 'zoomed'] '''
        mode = mode.lower()
        if mode not in ['default', 'zoomed', 'full']:
            raise Exception(f'Camera mode {mode} not recognized')

        self.mode = mode

    def move(self, bx, by):
        self.c.x = max(min(bx, self.params['pt'].x//2), W - self.params['pt'].x//2)
        self.c.x = max(min(by, self.params['pt'].y//2), W - self.params['pt'].y//2)

    def pt(self, p):
        return p if self.mode == 'full' else self.params['pt']*(p-P(self.c.x, self.c.y))

    def rect_intersect(self, r1):
        r2 = (0,0,W,H)
        if mode != 'full':
            r2 = (self.c.x - self.params['pt'].x//2, self.c.y - self.params['pt'].y//2,
                self.params['pt'].x, self.params['pt'].y)

        lx = max(r1[0], r2[0])
        rx = min(r1[0] + r1[2], r2[0] + r2[2])
        ty = max(r1[1], r2[1])
        by = min(r1[1] +  r1[3], r2[1] + r2[3])

        return True if lx < rx and ty < by else False

    def rect(self, win, col, coords, width=0):
        if self.mode == 'full':
            pygame.draw.rect(win, col, coords, width)
        elif rect_interset(coords):
            x,y,w,h = coords
            new_pt = pt(P(x,y))
            pygame.draw.rect(win, col, (new_pt.x, new_pt.y, w*self.params['fact'], h*self.params['fact']), width)

    def blit(self, win, path, pt):
        if self.mode == 'full':
            win.blit(path, pt)
        else:
            x,y = coords
            new_pt = pt(P(x,y))
            win.blit(path, pt)
