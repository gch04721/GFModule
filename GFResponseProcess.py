from abc import ABC, abstractmethod
from google_form.GFResponseDataModel import GFJSONDataModel, GFSectionDataModel
from dataclasses import fields
"""
 Parsing assessment survey results are saving in the form of ResponseData class 
 and return it's instance
"""
class GFResponseProcessing:
    def __init__(self, modelData, resModel:GFSectionDataModel):
        # initial data
        self.formId = ""
        self.formTitle = ""
        self.email = ""

        # input reqeust data (GFJSONDataModel)
        self.input: GFJSONDataModel = modelData
        # parsed data
        self.result: GFSectionDataModel = resModel

        self._parsingData()

    def _parsingData(self):
        self.formId = self.input.formId
        self.formTitle = self.input.formTitle
        self.formTitle = self.input.formTitle

        if self.input.email == None:
            self.email = ""
        else:
            self.email = self.input.email

        res = {}
        for r in self.input.results:
            res[r.title] = r.response
        
        ans = []
        for k, v in res.items():
            # ------ this seciton used for Assessment Data ------------
            if k == "Is the subject of the assessment a cooperative/association or an individual farm(s)?":
                if v == "Yes, it is a cooperative/association":
                    continue
                elif v == "No, it is one (or more) individual farm(s)":
                    self.result.isAssociation = False
                    for i in range(7):
                        ans.append("None")
                    continue
            # ----------------------------------------------------------
            ans.append(v)

        sNum = 0
        
        for field in fields(self.result):
            tmp = getattr(self.result, field.name)
            if isinstance(tmp, GFSectionDataModel) == False:
                continue
            else:
                step = tmp.questionNum
                setattr(self.result, field.name, tmp.from_list(ans[sNum:sNum+step]))

                if field.name == "postProductInfo":
                    addr = tmp.processingFacilitiesLoc
                    # 주소 맞춰서 데이터 배치.
                sNum = sNum + step

    def _convertGPSCoord(self, origin: str, dest: str):
        pass