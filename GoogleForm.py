from google_form.GFResponseDataModel import GFJSONDataModel
from google_form.GFResponseProcess import GFResponseProcessing
from . import *

import json
from dataclasses import asdict

# Final Google Form data model, other class will use this form only
"""
 구글폼 모델은 우리가 구글 폼 데이터를 받아왔을 때 수행해야 하는 역할과 데이터 구성에 대해서 정의됨.

 1. POST Request를 통해 받은 JSON 데이터 정리
 2. 정리된 데이터를 저장 / 전송

 결과적으로 전달받은 JSON 데이터는 GFModel을 상속받은 클래스에 의해 관리됨.
 즉, GFResponseProcess, GFResponseDataModel은 호출단에선 신경 쓸 필요 x
"""
class GFModel:
    @classmethod
    def from_GFJSONModel(cls, req: GFJSONDataModel, type, FB=True):
        instance = cls()
        instance.__initialize(req, type, FB)
        
        return instance

    @classmethod
    def from_jsonFile(cls, req: str, type, FB=True):
        instance = cls()
        with open(req, "r") as f:
            tmpData = json.load(f)
        req = GFJSONDataModel(**tmpData)
        instance.__initialize(req, type, FB)
        
        return instance
    
    @property
    def sectionData(self):
        return self.__processor.result
    
    @property
    def formId(self):
        return self.__processor.formId
    
    @property
    def email(self):
        return self.__processor.email
    
    @property
    def formTitle(self):
        return self.__processor.email
    
    def __init__(self):
        # Google Form data parser
        self.__processor = None

    def __initialize(self, req, type = ASSESSMENT, FB=True):
        if type == ASSESSMENT:
            # self.processor = AssessmentProcessing(req)
            result: AssessmentResponse = AssessmentResponse.create_empty()
            self.__processor = GFResponseProcessing(req, result)
        else: 
            pass