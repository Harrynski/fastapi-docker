from fastapi import FastAPI
from sql_functions import run_query, run_query_to_dataframe


app = FastAPI()
db_path = r'app\sample.db3'


@app.get("/")
async def root():
    return {"message": "Hello World"}


#@app.get("/items/{query_to_df}")
#async def execute_query(query: str):
#    df = run_query_to_dataframe(query, path_to_data_base=db_path)
#    return df.to_dict(orient="records")

@app.get("/items/{Run_Script}")
async def execute_script(query: str):
    script = run_query(query, path_to_data_base=db_path)
    return script
