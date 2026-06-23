from pathlib import Path
import uuid


UPLOAD_FOLDER = Path("uploaded_docs")
UPLOAD_FOLDER.mkdir(exist_ok=True)


class UploadService:

    @staticmethod
    def save_file(file_name: str, file_content: bytes):

        unique_name = f"{uuid.uuid4()}_{file_name}"

        file_path = UPLOAD_FOLDER / unique_name

        with open(file_path, "wb") as f:
            f.write(file_content)

        return str(file_path)
