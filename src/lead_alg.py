from zipfile import ZipFile
from io import BytesIO
import dill
import os
from tempfile import NamedTemporaryFile
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
                if not filename.endswith(".txt") or filename.startswith("__"):
                    continue
                texts.append((os.path.basename(filename), zipped_texts.open(filename).read()))
        else:
            texts.append(("", target_file.decode()))

        with open(PIPELINES[text_type], "rb") as pipeline_file:
            results = {}
            pipeline = dill.load(pipeline_file)
            for filename, text in texts:
                with open("./temp.txt", "wb") as temp_text:
                    temp_text.write(text)
                    temp_text.write(b"\n")
                    temp_text.flush()

                os.system("cat %s" % "./temp.txt")
                results[filename] = pipeline.predict_proba(["./temp.txt"])[0][-1] * 100
                os.remove("./temp.txt")

            return results
