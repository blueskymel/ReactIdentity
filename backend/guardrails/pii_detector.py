import re


EMAIL_PATTERN = r'\S+@\S+\.\S+'

PHONE_PATTERN = r'\d{10,15}'


class PIIDetector:


    def detect(

        self,

        text: str

    ) -> bool:

        if re.search(
            EMAIL_PATTERN,
            text
        ):
            return True


        if re.search(
            PHONE_PATTERN,
            text
        ):
            return True


        return False