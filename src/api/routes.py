from fastapi import APIRouter
from src.ingestion.repo_loader import RepositoryLoader
from src.agents.logic_agent import LogicFlawAgent

router = APIRouter()

@router.post("/scan")
def scan_repository(repo_path: str):

    loader = RepositoryLoader(repo_path)

    files = loader.load_repository()

    agent = LogicFlawAgent()

    findings = agent.analyze(files)

    return {
        "findings": findings
    }
