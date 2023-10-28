# %%
from gf_utils2.gamedata.gamedata import GameData

ZEROS = ["0", 0, ""]


def indent(string: str):
    return "\n".join("    " + s for s in string.split("\n"))[:-4]


# %%
class TableBase:
    __tablename__ = None

    class TableBase:
        def __init__(self, data: dict, gamedata: "Inspector") -> None:
            self.gamedata = gamedata
            self.data = data

        def inspect(self):
            attr_repr = ", ".join(
                [f"{k}={repr(v)}" for k, v in self.data.items() if v not in ZEROS]
            )
            string = f"{self.__class__.__name__}({attr_repr})\n"
            return string

    __itemclass__ = TableBase

    def __init__(self, gamedata: "Inspector") -> None:
        self.gamedata = gamedata

    def __getitem__(self, key):
        if key in self.gamedata[self.__tablename__]:
            return self.__itemclass__(
                self.gamedata[self.__tablename__][key], self.gamedata
            )
        else:
            return TableBase.TableBase({}, self.gamedata)


class BattleActionConfig(TableBase):
    __tablename__ = "battle_action_config"

    class BattleActionConfig(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if (self.data["creation_order"]) != "":
                order = [int(i) for i in self.data["creation_order"].split(",")]
                delay = [int(i) for i in self.data["creation_delay"].split(",")]
                if (f := len(order) - len(delay)) > 0:
                    delay.extend([-1] * f)
                for o, d in zip(order, delay):
                    if o == 0:
                        continue
                    string += f"创造物 {o} 延迟 {d}\n"
                    rep = self.gamedata.BattleCreation[o].inspect()
                    string += indent(rep)
            return string

    __itemclass__ = BattleActionConfig


class BattleBuff(TableBase):
    __tablename__ = "battle_buff"

    class BattleBuff(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if (skl := int(self.data["forced_skill"])) != 0:
                string += f"触发技能 {skl}\n"
                string += indent(
                    self.gamedata.BattleSkillConfig[skl * 100 + 1].inspect()
                )
            if (watch := int(self.data["watch_id"])) != 0:
                string += f"添加监视 {watch}\n"
                string += indent(self.gamedata.BattleWatch[watch].inspect())
            return string

    __itemclass__ = BattleBuff

    def __getitem__(self, key: int | str):
        if isinstance(key, str):
            if key.isdigit():
                key = int(key)
            else:
                key = int(key[1:])
                return self.gamedata.BattleFormula[key]
        if key > 1000000:
            return self.gamedata.BattleFormula[key % 1000000]
        else:
            return self.__itemclass__(
                self.gamedata[self.__tablename__][key], self.gamedata
            )


class BattleCreation(TableBase):
    __tablename__ = "battle_creation"

    class BattleCreation(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if self.data["buff_id"] != "0":
                for buff_id in self.data["buff_id"].split(","):
                    string += f"地面buff {buff_id}\n"
                    if ":" in buff_id:
                        buff_id, buff_tier = buff_id.split(":")
                        buff_tier = int(buff_tier)
                        if buff_tier > 1e6:
                            string += indent(
                                self.gamedata.BattleFormula[buff_tier % 1e6].inspect()
                            )
                    string += indent(self.gamedata.BattleBuff[buff_id].inspect())
            if self.data["hurt_id"] != "0":
                hurt_id = int(self.data["hurt_id"])
                string += f"伤害 {hurt_id}\n"
                string += indent(self.gamedata.BattleHurtConfig[hurt_id].inspect())
            if self.data["trigger_creation_id"] != "":
                order = [int(i) for i in self.data["trigger_creation_id"].split(",")]
                delay = [int(i) for i in self.data["trigger_creation_delay"].split(",")]
                if (f := len(order) - len(delay)) > 0:
                    delay.extend([-1] * f)
                for o, d in zip(order, delay):
                    string += f"衍生创造物 {o} 延迟 {d}\n"
                    rep = self.gamedata.BattleCreation[o].inspect()
                    string += indent(rep)
            return string

    __itemclass__ = BattleCreation


class BattleFormula(TableBase):
    __tablename__ = "battle_formula"

    class BattleFormula(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            return string

    __itemclass__ = BattleFormula


class BattleHurtConfig(TableBase):
    __tablename__ = "battle_hurt_config"

    class BattleHurtConfig(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if self.data["buff_id_target"] != "0":
                for buff_id, buff_tier in [
                    i.split(":") for i in self.data["buff_id_target"].split(",")
                ]:
                    string += f"目标buff {buff_id}: {buff_tier}\n"
                    string += indent(self.gamedata.BattleBuff[buff_id].inspect())
                    buff_tier = int(buff_tier)
                    if buff_tier > 1e6:
                        string += indent(
                            self.gamedata.BattleFormula[buff_tier % 1e6].inspect()
                        )
            return string

    __itemclass__ = BattleHurtConfig


class BattleSkillConfig(TableBase):
    __tablename__ = "battle_skill_config"

    class BattleSkillConfig(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            for pool in [
                "data_pool_1",
                "data_pool_2",
                "night_data_pool_1",
                "night_data_pool_2",
                "sp_data_pool_1",
                "sp_data_pool_2",
            ]:
                for s in self.data[pool].split(","):
                    if s.startswith("*"):
                        string += indent(
                            self.gamedata.BattleFormula[int(s[1:])].inspect()
                        )
            if self.data["trigger_id"] != "0":
                for i in self.data["trigger_id"].split(","):
                    i = int(i)
                    string += f"触发条件 {i}\n"
                    string += indent(self.gamedata.BattleTrigger[i].inspect())
            if self.data["sppool_trigger_id"] != "":
                for i in self.data["sppool_trigger_id"].split(","):
                    i = int(i)
                    string += f"SP参数触发条件 {i}\n"
                    string += indent(self.gamedata.BattleTrigger[i].inspect())
            if (i := self.data["target_select_ai"]) != 0:
                string += f"技能目标 {i}\n"
                string += indent(self.gamedata.BattleTargetSelectAi[i].inspect())
            if (i := self.data["action_id"]) != 0:
                string += f"动作 {i}\n"
                string += indent(self.gamedata.BattleActionConfig[i].inspect())
            if self.data["buff_id_self"] != "0":
                for buff_id, buff_tier in [
                    i.split(":") for i in self.data["buff_id_self"].split(",")
                ]:
                    string += f"自身buff {buff_id}: {buff_tier}\n"
                    string += indent(self.gamedata.BattleBuff[buff_id].inspect())
                    if buff_tier == "*":
                        continue
                    buff_tier = int(buff_tier)
                    if buff_tier > 1e6:
                        string += indent(
                            self.gamedata.BattleFormula[buff_tier % 1e6].inspect()
                        )
            if self.data["buff_id_target"] != "0":
                for buff_id, buff_tier in [
                    i.split(":") for i in self.data["buff_id_target"].split(",")
                ]:
                    string += f"目标buff {buff_id}: {buff_tier}\n"
                    string += indent(self.gamedata.BattleBuff[buff_id].inspect())
                    buff_tier = int(buff_tier)
                    if buff_tier > 1e6:
                        string += indent(
                            self.gamedata.BattleFormula[buff_tier % 1e6].inspect()
                        )
            return string

    __itemclass__ = BattleSkillConfig


class BattleSkillTypeConfig(TableBase):
    __tablename__ = "battle_skill_type_config"


class BattleTargetSelectAi(TableBase):
    __tablename__ = "battle_target_select_ai"


class BattleTrigger(TableBase):
    __tablename__ = "battle_trigger"

    class BattleTrigger(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            return string

    __itemclass__ = BattleTrigger


class BattleWatch(TableBase):
    __tablename__ = "battle_watch"

    class BattleWatch(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if (s := self.data["watch_sp_trigger"]) not in ZEROS:
                for i in [int(a) for a in s.split(",")]:
                    string += f"特殊条件 {i}\n"
                    string += indent(self.gamedata.BattleTrigger[i].inspect())
            if (i := self.data["activation_watch_trigger"]) != 0:
                string += f"监视触发器 {i}\n"
                string += indent(self.gamedata.BattleWatchTrigger[i].inspect())
            if (s := self.data["activation_skills"]) not in ZEROS:
                for i in [int(a) for a in s.split(",")]:
                    string += f"触发技能 {i}\n"
                    string += indent(
                        self.gamedata.BattleSkillConfig[i * 100 + 1].inspect()
                    )
            return string

    __itemclass__ = BattleWatch


class BattleWatchTrigger(TableBase):
    __tablename__ = "battle_watch_trigger"

    class BattleWatchTrigger(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if (i := self.data["buff_judge"]) not in ZEROS:
                string += indent(self.gamedata.BattleFormula[i % 1e6].inspect())
            return string

    __itemclass__ = BattleWatchTrigger


class BattleMovementInfo(TableBase):
    __tablename__ = "battle_movement_info"


class Gun(TableBase):
    __tablename__ = "gun"

    class Gun(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if i := self.data["normal_attack"]:
                string += f"普攻 {i}\n"
                string += indent(self.gamedata.BattleSkillConfig[i * 100 + 1].inspect())
            if i := self.data["skill1"]:
                string += f"一技能 {i}\n"
                string += indent(
                    self.gamedata.BattleSkillConfig[i * 100 + 10].inspect()
                )
            if i := self.data["skill2"]:
                string += f"二技能 {i}\n"
                string += indent(
                    self.gamedata.BattleSkillConfig[i * 100 + 10].inspect()
                )

            if s := self.data["passive_skill"]:
                for i in s.split(","):
                    i = int(i)
                    string += f"被动技能 {i}\n"
                    string += indent(
                        self.gamedata.BattleSkillConfig[i * 100 + 1].inspect()
                    )
            if s := self.data["dynamic_passive_skill"]:
                for i in s.split(","):
                    i = int(i)
                    string += f"动态被动技能 {i}\n"
                    string += indent(
                        self.gamedata.BattleSkillConfig[i * 100 + 10].inspect()
                    )

            return string

    __itemclass__ = Gun


class Sangvis(TableBase):
    __tablename__ = "sangvis"

    class Sangvis(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if i := self.data["normal_attack"]:
                string += f"普攻 {i}\n"
                string += indent(self.gamedata.BattleSkillConfig[i * 100 + 1].inspect())
            if i := self.data["skill1"]:
                string += f"一技能 {i}\n"
                string += indent(
                    self.gamedata.BattleSkillConfig[i * 100 + 10].inspect()
                )
            if self.data["skill2_type"] == 1 and (i := self.data["skill2"]):
                string += f"二技能 {i}\n"
                string += indent(
                    self.gamedata.BattleSkillConfig[i * 100 + 10].inspect()
                )
            if i := self.data["skill3"]:
                string += f"三技能 {i}\n"
                string += indent(self.gamedata.BattleSkillConfig[i * 100 + 5].inspect())

            if i := self.data["skill_advance"]:
                string += f"四技能 {i}\n"
                string += indent(self.gamedata.BattleSkillConfig[i * 100 + 5].inspect())

            if s := self.data["passive_skill2"]:
                for i in s.split(","):
                    i = int(i)
                    string += f"被动技能 {i}\n"
                    string += indent(
                        self.gamedata.BattleSkillConfig[i * 100 + 1].inspect()
                    )
            if s := self.data["dynamic_passive_skill"]:
                for i in s.split(","):
                    i = int(i)
                    string += f"动态被动技能 {i}\n"
                    try:
                        string += indent(
                            self.gamedata.BattleSkillConfig[i * 100 + 10].inspect()
                        )
                    except KeyError:
                        string += indent(
                            self.gamedata.BattleSkillConfig[i * 100 + 5].inspect()
                        )

            return string

    __itemclass__ = Sangvis


class EnemyCharacterType(TableBase):
    __tablename__ = "enemy_character_type"

    class EnemyCharacterType(TableBase.TableBase):
        def inspect(self):
            string = super().inspect()
            if i := self.data["normal_attack"]:
                string += f"普攻 {i}\n"
                string += indent(self.gamedata.BattleSkillConfig[i * 100 + 1].inspect())

            if s := self.data["passive_skill"]:
                for i in s.split(","):
                    i = int(i)
                    string += f"被动技能 {i}\n"
                    string += indent(
                        self.gamedata.BattleSkillConfig[i * 100 + 1].inspect()
                    )

            return string

    __itemclass__ = EnemyCharacterType


class Inspector(GameData):
    def __init__(self, stc_dir, table_dir=None, to_dict=True, ext="json") -> None:
        super().__init__(stc_dir, table_dir, to_dict, ext)
        self.BattleActionConfig = BattleActionConfig(self)
        self.BattleBuff = BattleBuff(self)
        self.BattleCreation = BattleCreation(self)
        self.BattleFormula = BattleFormula(self)
        self.BattleHurtConfig = BattleHurtConfig(self)
        self.BattleSkillConfig = BattleSkillConfig(self)
        self.BattleSkillTypeConfig = BattleSkillTypeConfig(self)
        self.BattleTargetSelectAi = BattleTargetSelectAi(self)
        self.BattleTrigger = BattleTrigger(self)
        self.BattleWatch = BattleWatch(self)
        self.BattleWatchTrigger = BattleWatchTrigger(self)
        self.BattleMovementInfo = BattleMovementInfo(self)
        self.EnemyCharacterType = EnemyCharacterType(self)
        self.Gun = Gun(self)
        self.Sangvis = Sangvis(self)


# %%
if __name__ == "__main__":
    # %%
    table_dir = R"D:\Workspace\gfline\GF_Data_Tools\data\ch\asset\table"
    stc_dir = R"D:\Workspace\gfline\GF_Data_Tools\data\ch\stc"
    catch_dir = R"D:\Workspace\gfline\GF_Data_Tools\data\ch\catchdata"
    inspector = Inspector([stc_dir, catch_dir], table_dir)
    # %%
    print(inspector.Gun[392].inspect())

# %%
