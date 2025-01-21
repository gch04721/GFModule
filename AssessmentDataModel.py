from google_form.GFResponseDataModel import *

@dataclass
class CompanyInfo(GFSectionDataModel):
    name                : str = field(default="")
    address             : str = field(default="")
    contactPersonEmail  : str = field(default="")
    contactPersonPhone  : str = field(default="")

@dataclass
class ProductInfo(GFSectionDataModel):
    HSCODE             : str = field(default="")
    tradeName          : str = field(default="")
    scientificName     : str = field(default="")

@dataclass
class AssociationInfo(GFSectionDataModel):
    name                : str = field(default="")
    country             : str = field(default="")
    female              : int = field(default=-1)

@dataclass
class PostProductInfo(GFSectionDataModel):
    processingFacilities        : str = field(default="")
    processingFacilitiesLoc     : str = field(default="")
    loadCapacity                : str = field(default="")
    storageFacilitiesLoc        : str = field(default="")
    transportation              : str = field(default="")

# Final Form
@dataclass
class AssessmentResponse(GFSectionDataModel):
    companyInfo: CompanyInfo = field(default = CompanyInfo.create_empty())
    productInfo: ProductInfo = field(default = ProductInfo.create_empty())
    associationInfo: AssociationInfo = field(default = AssociationInfo.create_empty())
    postProductInfo: PostProductInfo = field(default = PostProductInfo.create_empty())
