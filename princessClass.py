#沒有破防的角色
class Character:
    def __init__(self,level):
        self.level = level
        self.skillHit = 0 #技能破防狀態
        self.ubHit = 0 #ub破防狀態
        self.skillHitRemainTime = 0 #技能破防剩餘時間
        self.ubHitRemainTime = 0 #ub破防剩餘時間
        self.skillHitPower = 0 #技能破防力
        self.ubHitPower = 0 #ub破放力

    def checkSkill(self,skill):
        return 0
    def checkSkillHit(self):
        if self.skillHit:
            self.skillHitRemainTime -= 1
            if self.skillHitRemainTime > 0:
                return 0
            else:
                self.skillHit = 0
                return self.skillHitPower
        else:
            return 0
    def checkUbHit(self):
        if self.ubHit:
            self.ubHitRemainTime -= 1
            if self.ubHitRemainTime > 0:
                return 0
            else:
                self.ubHit = 0
                return self.ubHitPower
        else:
            return 0
class Special(Character):
    def __init__(self,level,skillComponent,skillHitTime,upSkillComponent,upSkillHitTime,defenseSkill,ubComponent,ubHitTime):
        super().__init__(level)
        self.skillComponent = skillComponent #技能係數
        self.skillHitTime = skillHitTime #技能破防時間

        self.upSkillComponent = upSkillComponent #升級技能係數
        self.upSkillHitTime = upSkillHitTime #升級技能破防時間

        self.defenseSkill = defenseSkill #破防技能名稱
        self.ubComponent = ubComponent #ub係數
        self.ubHitTime = ubHitTime #ub破防時間

        self.skillHitPower = skillComponent + skillComponent * self.level #技能破防力
        self.ubHitPower = ubComponent + ubComponent * self.level #ub破防力

        self.upSkillHitPower = upSkillComponent + upSkillComponent * self.level #升級技能破防力

        self.totalHitPower = 0 #破防量
        self.skillHit = 0 #技能破防狀態
        self.ubHit = 0 #ub破防狀態
        self.skillHitRemainTime = 0 #技能破防剩餘時間
        self.ubHitRemainTime = 0 #ub破防剩餘時間
    def checkSkill(self,skill):
        if skill == self.defenseSkill: #技能
            return self.skillUp()
        else:
            if skill == '0' or skill == 0:
                return 0
            else:
                if skill[-2:] == 'UB':
                    if skill[0] == 'U':
                        return self.ubUp() #ub
                    else:
                        return self.skillUp() + self.ubUp() #ub + 技能
                else:
                    return 0
    def skillUp(self):
        if self.skillHit:
            return 0
        else:
            self.skillHit = 1
            if self.ubHit:
                self.skillHitRemainTime = self.upSkillHitTime #有ub效果
                return self.upSkillHitPower
            else:
                self.skillHitRemainTime = self.skillHitTime #沒有ub效果
                return self.skillHitPower
    def ubUp(self):
        if self.ubHit:
            return 0
        else:
            self.ubHit = 1
            self.ubHitRemainTime = self.ubHitTime
            return self.ubHitPower
    
class General(Character):
    def __init__(self,level,skillComponent,skillHitTime,defenseSkill,ubComponent,ubHitTime):
        super().__init__(level)
        self.skillComponent = skillComponent #技能係數
        self.skillHitTime = skillHitTime #技能破防時間
        self.defenseSkill = defenseSkill #破防技能名稱
        self.ubComponent = ubComponent #ub係數
        self.ubHitTime = ubHitTime #ub破防時間

        self.skillHitPower = skillComponent + skillComponent * self.level #技能破防力
        self.ubHitPower = ubComponent + ubComponent * self.level #ub破放力
        self.skillHit = 0 #技能破防狀態
        self.ubHit = 0 #ub破防狀態
        self.skillHitRemainTime = 0 #技能破防剩餘時間
        self.ubHitRemainTime = 0 #ub破防剩餘時間
    def checkSkill(self,skill):
        if skill == self.defenseSkill: #技能
            return self.skillUp()
        else:
            if skill == '0' or skill == 0:
                return 0
            else:
                if skill[-2:] == 'UB':
                    if skill[0] == 'U':
                        return self.ubUp() #ub
                    else:
                        return self.skillUp() + self.ubUp() #ub + 技能
                else:
                    return 0
    def skillUp(self):
        if self.skillHit:
            return 0
        else:
            self.skillHit = 1
            self.skillHitRemainTime = self.skillHitTime
            return self.skillHitPower
    def ubUp(self):
        if self.ubHit:
            return 0
        else:
            self.ubHit = 1
            self.ubHitRemainTime = self.ubHitTime
            return self.ubHitPower