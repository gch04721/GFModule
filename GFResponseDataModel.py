"""
 구글폼 데이터의 형태에 대해서 정리된 파일

 GFDataModel        :  JSON을 통해 받은 답변 리스트를 정리하기 위한 형태
                       기본적으로 FORM_FIELDS, 전체 질문 수, 섹션 이름 형태로 구성
                       상속받은 클래스에서 질문의 종류, 수, 섹션 이름을 상세하게 정리.

 GFJSONDataMOdel    : POST method를 통해 전달받은 전체 JSON 데이터의 형태
                      FastAPI를 통해 GooglForm 데이터를 전달받았을 때, 형식에 맞춰 저장하기 위한 모델
"""
from dataclasses import dataclass, field, fields, asdict
from typing import Optional, Union, List
from abc import ABC
from pydantic import BaseModel

@dataclass
class GFSectionDataModel(ABC):
    def __post_init__(self):
        self.FORM_FIELDS = tuple(f.name for f in fields(self) if f.init) # 전체 질문 제목
        self.questionNum = len(self.FORM_FIELDS) # 전체 질문 수 
        self.sectionName = self.__class__.__name__ # 섹션 이름.
        #print("called")

    @classmethod
    def from_list(cls,result: List):
        """
        List 형태로 전달된 데이터를 통해 데이터 클래스 객체를 생성
        """
        try:
            instance = cls()
            field_values = {}
            for idx, field_name in enumerate(instance.FORM_FIELDS):
                if idx < len(result):
                    field_values[field_name] = result[idx]

            return cls(**field_values)
        except IndexError as e:
            print(f"데이터의 형식이 예상과 다릅니다: {e}")
            return cls()
        
    @classmethod
    def create_empty(cls):
        instance = cls()
        return instance
        
    @classmethod
    def create_document_data(cls, instance):
        if isinstance(instance, cls):
            return asdict(instance)
        else:
            raise ValueError("Provided instanace is not of type DataFrom")
        
    def getDictionaryData(cls):
        return asdict(cls)
        
class GFJSONDataModel(BaseModel):
    formId : str
    formTitle : str
    email : Optional[str] = None
    results: List['GFJSONDataModel._GFUserResponseModel']

    class _GFUserResponseModel(BaseModel): 
        id : int
        type : str
        title : str
        response: Union[str, int, List[Union[int, str]]]

if __name__ == "__main__":
    pass