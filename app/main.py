"""
    === Application Entry Point ===

Inisialisasi FastAPI
"""

from fastapi import FastAPI

from app.routers.students import router as student_router

app = FastAPI(
    title="Student Management API",
    description="REST API for managing student data.",
    version="1.0.0",
)

app.include_router(student_router)
