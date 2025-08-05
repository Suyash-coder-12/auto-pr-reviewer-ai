from fastapi import FastAPI, Request
from app.github_client import get_pr_diff
from app.reviewer import review_code

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI PR Reviewer is live!"}

@app.post("/review/")
async def review(request: Request):
    data = await request.json()
    repo = data.get("repo")
    pr_number = data.get("pr_number")
    
    diff = get_pr_diff(repo, pr_number)
    suggestions = review_code(diff)
    
    return {"suggestions": suggestions}
