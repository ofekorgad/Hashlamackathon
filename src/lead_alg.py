from zipfile import ZipFile
from io import BytesIO
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
    def run(target_file, strict=Strictness.NONE, text_type=TextType.Generic, is_zip=False):

        texts = []

        if is_zip:
            zipped_texts = ZipFile(BytesIO(target_file))
            for filename in zipped_texts.namelist():
                if not filename.endswith(".txt"):
                    continue
                texts.append((filename, zipped_texts.open(filename).read()))
        else:
            texts.append(('', target_file.decode()))

        with open(PIPELINES[text_type], "rb") as pipeline_file:
            results = {}
            pipeline = dill.load(pipeline_file)
            for filename, text in texts:
                results[filename] = pipeline.predict_proba([text])[0][-1] * 100

            return results
