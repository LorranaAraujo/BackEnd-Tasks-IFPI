from pydantic import BaseModel

class Tasks(BaseModel):
    id:str | None
    descricao : str
    responsavel: str | None
    nivel : int
    situacao  : str | None
    prioridade : int

    class Config:
        orm_mode = True

    @classmethod
    def fromDict(cls, task):
        usuario_ = Tasks(id=str(task['_id']),descricao=task['descricao'],
                     responsavel=task['responsavel'],nivel=task['nivel'],
                    situacao=task['situacao'],prioridade=task['prioridade'])

        return usuario_

    def toDict(self):
        return{
            "descricao": self.descricao,
            "responsavel":self.responsavel,
            "nivel":self.nivel,
            "situacao":self.situacao,
            "prioridade":self.prioridade,
        }

        

