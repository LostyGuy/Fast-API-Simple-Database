from pydantic import BaseModel

# class TagBase(BaseModel):
#     name: str
# class TagCreate(TagBase):
#     pass
# class Tag(TagBase):
#     id: int
#     class Config:
#         from_attributes = True
        
# class PlatformBase(BaseModel):
#     name: str
# class PlatformCreate(PlatformBase):
#     pass
# class Platform(PlatformBase):
#     id: int
#     class Config:
#         from_attributes = True
        
# class PublisherBase(BaseModel):
#     name: str
# class PublisherCreate(PublisherBase):
#     pass
# class Publisher(PublisherBase):
#     id: int
#     class Config:
#         from_attributes = True
        
# class DeveloperBase(BaseModel):
#     name: str
# class DeveloperCreate(DeveloperBase):
#     pass
# class Developer(DeveloperBase):
#     id: int
#     class Config:
#         from_attributes = True
            
# class GameBase(BaseModel):
#     name: str
#     developer: int
#     publisher: int
#     tag: int
#     platform: int
# class GameCreate(GameBase):
#     pass
# class Game(GameBase):
#     id: int
#     class Config:
#         from_attributes = True

class GamesBase(BaseModel):
    title: str
    developer: str
    publisher: str
    tag: str
    platform: str
class GamesCreate(GamesBase):
    pass
class Games(GamesBase):
    game_id: int
    class Config:
        from_attributes = True