'''
Implementation of the game's camera
'''

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
        self.set_mode(mode)

    @property
    def params(self):
        ''' Helper  method to reduce code redundancy '''
        if self.mode == 'full':
            return {'pt': P(0,0), 'fact': 1}
        elif self.mode == 'default':
            return {'pt': CAM_DEF, 'fact': DEF_FACTOR}
        else:
            return {'pt': CAM_ZOOM, 'fact': ZOOM_FACTOR}

    def set_mode(self, mode):
        ''' Set the camera's mode. Mode must be one of ['full', 'default', 'zoomed'] '''
        mode = mode.lower()
        if mode not in ['default', 'zoomed', 'full']:
            raise Exception(f'Camera mode {mode} not recognized')

        self.mode = mode

    def move(self, bx, by, alpha=P(0.9,0.9)):
        '''
        Move the camera to the given coordinates (Camera can't go over the field boundary)

        Uses exponential smoothing to minimize jittering
        '''
        new_c = P(0,0)
        new_c.x = min(max(bx, self.params['pt'].x//4), W - self.params['pt'].x//4)
        new_c.y = min(max(by, self.params['pt'].y//4), H - self.params['pt'].y//4)

        self.c = alpha*self.c + (P(1,1)-alpha)*new_c

    def pt(self, p):
        ''' Transform any 2-D point with respect to the camera'''
        p = P(p)
        return p if self.mode == 'full' else P(W/2,H/2) + P(self.params['fact'],self.params['fact'])*(p-self.c)

    def rect_in_view(self, r1):
        ''' Check if given rectangle is within the camera's view '''
        r2 = (0,0,W,H)
        if self.mode != 'full':
            r2 = (self.c.x - self.params['pt'].x//2, self.c.y - self.params['pt'].y//2,
                self.params['pt'].x, self.params['pt'].y)

        lx = max(r1[0], r2[0])
        rx = min(r1[0] + r1[2], r2[0] + r2[2])
        ty = max(r1[1], r2[1])
        by = min(r1[1] +  r1[3], r2[1] + r2[3])

        return True if lx < rx and ty < by else False

    def circle_in_view(self, x, y, rad):
        ''' Check if given circle is within the camera's view '''
        r = (0,0,W,H)
        if self.mode != 'full':
            r = (self.c.x - self.params['pt'].x//2, self.c.y - self.params['pt'].y//2,
                self.params['pt'].x, self.params['pt'].y)

        cx = abs(x - (r[0]-r[2]/2))
        cy = abs(y - (r[1]-r[3]/2))

        if x > r[2]/2 + rad or y > r[3]/2 + rad:
            return False

        if x <= r[2]/2 or y <= r[3]/2:
            return True

        cornerDistance_sq = (x - r[2]/2)**2 + (y - r[3]/2)**2

        return cornerDistance_sq <= rad**2

    def rect(self, win, col, coords, width=0):
        ''' Draw a rectangle according to the cameras mode (attributes are same as ```pygame.draw.rect```)'''
        if self.mode == 'full':
            pygame.draw.rect(win, col, coords, width)
        elif self.rect_in_view(coords):
            x,y,w,h = coords
            new_pt = self.pt(P(x,y))
            pygame.draw.rect(win, col, (new_pt.x, new_pt.y, w*self.params['fact'], h*self.params['fact']), width)

    def circle(self, win, col, p, r, width=0):
        ''' Draw a circle according to the cameras mode (attributes are same as ```pygame.draw.cirlce```)'''
        if self.mode == 'full':
            pygame.draw.circle(win, col, p, r, width)
        #elif self.circle_in_view(p[0], p[1], r):
        else:
            new_pt = self.pt(p)
            pygame.draw.circle(win, col, new_pt.val, round(r*self.params['fact']), width)

    def polygon(self, win, col, pts):
        ''' Draw a polygon according to the cameras mode (attributes are same as ```pygame.draw.polygon```)'''
        if self.mode == 'full':
            pygame.draw.polygon(win, col, pts)
        else:
            new_pts = []
            for p in pts:
                new_pts.append(self.pt(P(p)).val)
            pygame.draw.polygon(win, col, new_pts)

    def blit(self, win, path, pt, size):
        '''
        Blit a given sprite to the surface according to the cameras mode

        Attributes:
            win (pygame.Window): window for drawing
            path (pygame.Image): path to the sprite
            pt (P): center of the sprite
            size (P): size of the sprite
        '''
        x,y = pt
        size = P(self.params['fact'],self.params['fact'])*P(size)

        if self.mode == 'full':
            win.blit(path[self.mode], (P(x,y)-P(0.5,0.5)*size).val)
        elif self.rect_in_view((x-size.x//2, y-size.y//2, size.x, size.y)):
                new_pt = self.pt(P(x,y))
                win.blit(path[self.mode], (new_pt-P(0.5,0.5)*size).val)
