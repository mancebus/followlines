import time

class ControllerPID:

    def __init__(self,whiteValue,blackValue,Tp,Kp=None):
        self.offset = (whiteValue-blackValue)/2.0
        self.Tp = Tp
        self.zero = blackValue
        self.Kp = Kp
        self.initTime = None
        if Kp is None:
            self.Kp = self.Tp/self.offset
        self.logFile = 'data.csv'
        self.__log(mode='w')
            
    def getPower(self,light):
        currentTime = time.time()
        if self.initTime is None:
            self.initTime = currentTime
            self.previousTime = currentTime
            
        deltaTime = currentTime-self.previousTime
        measureTime = currentTime-self.initTime

        self.previousTime = currentTime

        error = light-(self.offset+self.zero)
        turn = self.Kp*error
        powerLeft = self.Tp+turn
        powerRight = self.Tp-turn
        self.__log(measureTime,
                   light,
                   powerLeft,
                   powerRight)
        return int(powerLeft),int(powerRight)

    def __log(self,measureTime=0,light=0,left=0,right=0,mode='a'):
        msg = '%.2f;%d;%d;%d' % (measureTime,                                    
                                light,
                                left,                                
                                right)
        if mode == 'w':
            msg = 'time;light;left;right'

        f = open(self.logFile,mode)
        f.write(msg+'\n')
        f.close()









