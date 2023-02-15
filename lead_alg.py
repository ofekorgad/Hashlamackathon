from enum import Enum


class Strictness(Enum):
    NONE = 0,
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3


class TextType(Enum):
    Essay = 1,
    SocialMedia = 2,
    Generic = 3


class LeadAlg:
    @staticmethod
    def init():
        pass

    @staticmethod
    def run(text, strict=Strictness.NONE, text_type=TextType.Generic):
        # return alg.run(text)
        return 100
