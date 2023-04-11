from panda3d.core import loadPrcFileData
loadPrcFileData('', 'textures-power-2 up')
loadPrcFileData('', 'show-frame-rate-meter f')
loadPrcFileData('', 'win-size 800 600')
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.task import Task
from direct.showbase.DirectObject import DirectObject
import sys
class Game(DirectObject):
    def __init__(self):
        base = ShowBase()
        base.useTrackball()
        base.trackball.node().setPos(-7.55,0,6)
       # base.setBackgroundColor(1,1,1)
        self.image = self.loadImageAsPlane('NewTestamentPsalmsImages/NewTestament' + str(1) + '.JPG')
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(1.6)
        # labels
        ntlabel = OnscreenText(text='New Testament', pos=(-1.1, 0.92), scale=0.05)
        psalabel = OnscreenText(text='Psalms', pos=(1.2, 0.92), scale=0.05)
        # load menus
        self.LoadNTMenu()        
        self.LoadPSAMenu()
    def LoadNTMenu(self):
        self.NTListFrame = DirectScrolledFrame(canvasSize=(0, 0, -7, 50), frameSize=(-.1, .2, -1.5, 1.5))
        self.NTListFrame.setPos(-1.2, 0, -0)
        self.NTListFrame.setScale(0.6)
        zoffset = 49.9         
        for x in range(403):
            if x != 0:
                l = DirectButton(text=str(x), scale=.1, command=self.LoadNewTestamentImage,extraArgs=[x])
                l.setZ(zoffset)
                zoffset = zoffset -0.13
                l.setX(0.1)
                l.reparentTo(self.NTListFrame.getCanvas())
    def LoadPSAMenu(self):
        self.PSAListFrame = DirectScrolledFrame(canvasSize=(0, 0, -10, 10), frameSize=(-.1, .2, -1.5, 1.5))
        self.PSAListFrame.setPos(1.2, 0, -0)
        self.PSAListFrame.setScale(0.6)
        zoffset = 9.9         
        for x in range(109):
            if x != 0:
                l = DirectButton(text=str(x), scale=.1, command=self.LoadPsalmsImage,extraArgs=[x])
                l.setZ(zoffset)
                zoffset = zoffset -0.13
                l.setX(0.1)
                l.reparentTo(self.PSAListFrame.getCanvas())
    def LoadNewTestamentImage(self,imagenum):
        base.trackball.node().setPos(-7.55,0,6)
        self.image.removeNode();
        self.image = self.loadImageAsPlane('NewTestamentPsalmsImages/NewTestament' + str(imagenum) + '.JPG')
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(1.7)
    def LoadPsalmsImage(self,imagenum):
        base.trackball.node().setPos(-7.55,0,6)
        self.image.removeNode();
        self.image = self.loadImageAsPlane('NewTestamentPsalmsImages/Psalms' + str(imagenum) + '.JPG')
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(1.7)
    def loadImageAsPlane(self, filepath, yresolution = 600):
        tex = loader.loadTexture(filepath)
        tex.setBorderColor(Vec4(0,0,0,0))
        tex.setWrapU(Texture.WMBorderColor)
        tex.setWrapV(Texture.WMBorderColor)
        cm = CardMaker(filepath + ' card')
        cm.setFrame(-tex.getOrigFileXSize(), tex.getOrigFileXSize(), -tex.getOrigFileYSize(), tex.getOrigFileYSize())
        card = NodePath(cm.generate())
        card.setTexture(tex)
        card.setScale(card.getScale()/ yresolution)
        card.flattenLight()
        return card
fgame = Game()
base.run()