from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.custom_json_encoder import PrettyJSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(default_response_class=PrettyJSONResponse)

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"Welcome to Database \n /items/{id}"}

# @app.post("/game/", response_model=schemas.Game)
# def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
#     db_game = models.Game(
#         name=game.name, 
#         developer=game.developer, 
#         publisher=game.publisher,
#         tag=game.tag,
#         platform=game.platform
#     )
#     db.add(db_game)
#     db.commit()
#     db.refresh(db_game)
#     return db_game

# @app.get("/game/", response_model=list[schemas.Game])
# def read_games(db: Session = Depends(get_db)):
#     games = db.query(models.Game).all()
#     return games

# @app.get("/platform/", response_model=list[schemas.Platform])
# def read_platforms(db: Session = Depends(get_db)):
#     platforms = db.query(models.Platform).all()
#     return platforms

# @app.get("/publisher/", response_model=list[schemas.Publisher])
# def read_publishers(db: Session = Depends(get_db)):
#     publishers = db.query(models.Publisher).all()
#     return publishers

# @app.get("/developer/", response_model=list[schemas.Developer])
# def read_developers(db: Session = Depends(get_db)):
#     developers = db.query(models.Developer).all()
#     return developers

# @app.get("/tag/", response_model=list[schemas.Tag])
# def read_tags(db: Session = Depends(get_db)):
#     tags = db.query(models.Tag).all()
#     return tags

@app.get("/games/", response_model=list[schemas.Games])
def read_games(db: Session = Depends(get_db)):
    games = db.query(models.Games).all()
    return games


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )
    
@app.get("/game/{id}", response_model=list[schemas.Games])
async def read_games(request: Request,db: Session = Depends(get_db)):
    games = db.query(models.Games).all()
    return templates.TemplateResponse(
        request=request, name="game.php", context={"id": id, "games": games}
    )