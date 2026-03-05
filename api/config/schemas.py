from pydantic import BaseModel, ConfigDict


class ErrorMSG(BaseModel):
    result: bool = False
    error_type: str
    error_message: str

    model_config = ConfigDict(from_attributes=True)


class MSG(BaseModel):
    result: str
    model_config = ConfigDict(from_attributes=True)