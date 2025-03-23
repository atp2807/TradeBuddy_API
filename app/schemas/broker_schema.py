from pydantic import BaseModel

class BrokerBase(BaseModel):
    country: str
    alias: str
    sms_number: str
    kakao_channel_name: str

class BrokerOut(BrokerBase):
    id: int

    class Config:
        orm_mode = True
