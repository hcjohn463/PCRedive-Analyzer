class Characters():
    def __init__(self,level,characterList = [0,0,0,0,0,0,0,0,0]):
        self.level = level
        self.skill1 = characterList[0]
        self.skill1Coef = characterList[1]
        self.skill1HitTime = characterList[2]
        self.skill2 = characterList[3]
        self.skill2Coef = characterList[4]
        self.skill2HitTime = characterList[5]
        self.ub = characterList[6]
        self.ubCoef = characterList[7]
        self.ubHitTime = characterList[8]

        self.skill1Hit = 0 #技能1破防狀態
        self.skill2Hit = 0 #技能2破防狀態
        self.ubHit = 0 #ub破防狀態
        self.skill1HitRemainTime = 0 #技能1破防剩餘時間
        self.skill2HitRemainTime = 0 #技能2破防剩餘時間
        self.ubHitRemainTime = 0 #ub破防剩餘時間
        
    def checkHit(self):
        needDelete = 0
        if self.skill1Hit:
            self.skill1HitRemainTime -= 1
            if self.skill1HitRemainTime == 0:
                self.skill1Hit = 0
                needDelete += float(self.skill1Coef) + float(self.skill1Coef) * float(self.level) #技能1破防力
        if self.skill2Hit:
            self.skill2HitRemainTime -= 1
            if self.skill2HitRemainTime == 0:
                self.skill2Hit = 0
                needDelete += float(self.skill2Coef) + float(self.skill2Coef) * float(self.level) #技能2破防力
        if self.ubHit:
            self.ubHitRemainTime -= 1
            if self.ubHitRemainTime == 0:
                self.ubHit = 0
                needDelete += float(self.ubCoef) + float(self.ubCoef) * float(self.level) #ub破防力
        return needDelete
    def checkSkill(self,skill):
        if skill == '技能1':
            if int(self.skill1) == 0:
                return 0
            else:
                return self.skill1Up()
        elif skill == '技能2':
            if self.skill2 == 0:
                return 0
            else:
                return self.skill2Up()
        elif skill == 'UB':
            if int(self.ub) == 0:
                return 0
            else:
                return self.ubUp()
        else:
            return 0

    def skill1Up(self):
        if self.skill1Hit:
            return 0
        else:
            self.skill1Hit = 1
            if 'or' in str(self.skill1Coef):
                if self.ubHit == 1:
                    self.skill1Coef = float(self.skill1Coef.split('or')[0][:-1])
                else:
                    self.skill1Coef = float(self.skill1Coef.split('or')[1][1:])
            if 'or' in str(self.skill1HitTime):
                if self.ubHit == 1:
                    self.skill1HitTime = float(self.skill1HitTime.split('or')[0][:-1])
                else:
                    self.skill1HitTime = float(self.skill1HitTime.split('or')[1][1:])
            self.skill1HitRemainTime = float(self.skill1HitTime)
            return float(self.skill1Coef) + float(self.skill1Coef) * float(self.level) #技能1破防力
    def skill2Up(self):
        if self.skill2Hit:
            return 0
        else:
            self.skill2Hit = 1
            if 'or' in str(self.skill2Coef):
                if self.ubHit == 1:
                    self.skill2Coef = float(self.skill2Coef.split('or')[0][:-1])
                else:
                    self.skill2Coef = float(self.skill2Coef.split('or')[1][1:])
            if 'or' in str(self.skill2HitTime):
                if self.ubHit == 1:
                    self.skill2HitTime = float(self.skill2HitTime.split('or')[0][:-1])
                else:
                    self.skill2HitTime = float(self.skill2HitTime.split('or')[1][1:])
            self.skill2HitRemainTime = float(self.skill2HitTime)
            return float(self.skill2Coef) + float(self.skill2Coef) * float(self.level) #技能2破防力
    def ubUp(self):
        if self.ubHit:
            return 0
        else:
            self.ubHit = 1
            self.ubHitRemainTime = float(self.ubHitTime)
            return float(self.ubCoef) + float(self.ubCoef) * float(self.level) #ub破防力