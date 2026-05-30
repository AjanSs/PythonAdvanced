from altair import ProjectionType
from fastapi import FastAPI
from setuptools.command.develop import develop
from statsmodels.stats.descriptivestats import describe
from streamlit import title

from model import Developer, Projects

app = FastAPI

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}


@app.post("/projects/")
def create_project(project: Projects):
    return {"message": "Project created successfully", "project": project}

@app.get("/projects/")
def get_projects():
    sample_project = Projects(
        title = "Sample Project",
        description = "This is a sample project",
        language = ["HTML","CSS","JAVASCRIPT"],
        lead_developer = Developer(name="Jon Doe",experience=5)
    )

    return {"projects": [sample_project]}