import dill
from enums.text_types import TextType
from enums.strictness import Strictness


PIPELINES = {
    TextType.Generic.value: "pipelines/generic"
}


class LeadAlg:
    @staticmethod
    def init():
        pass

    @staticmethod
    def run(text, strict=Strictness.NONE, text_type=TextType.Generic):
        texts = [text.decode()]
        with open(PIPELINES[text_type], "rb") as pipeline_file:
            pipeline = dill.load(pipeline_file)
            try:
                for text_result in pipeline.predict_proba(texts):
                    return round(text_result[-1] * 100)
            except Exception as e:
                print(e)
                return 0
