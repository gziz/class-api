from pydantic import BaseModel


class PredictionRequest(BaseModel):
    fix_acid: float
    vol_acid: float
    cit_acid: float
    res_sugar: float
    chlor: float
    free_sulf: float
    tot_sulf: float
    dens: float
    pH: float
    sulph: float
    alc: float
    qual: float