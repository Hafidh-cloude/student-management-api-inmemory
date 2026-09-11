"""
    === Student Router Module ===

Menyediakan endpoint REST API untuk CRUD
"""

from fastapi import APIRouter, Depends, HTTPException

from app.schemas import StudentCreate, StudentResponse, StudentUpdate

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)

students = []
next_id = 1


# Retrieve all student record
@router.get("/", response_model=list[StudentResponse])
def get_students():
    return students


# Create new student record
@router.post("/", response_model=StudentResponse)
def create_student(student_data: StudentCreate):
    global next_id

    student = {
        "id": next_id,
        "name": student_data.name,
        "major": student_data.major,
        "semester": student_data.semester,
    }

    students.append(student)
    next_id += 1

    return student


# Retrieve student by ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found!",
    )


# Update exsisting student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
):
    for student in students:
        if student["id"] == student_id:
            student["name"] = student_data.name
            student["major"] = student_data.major
            student["semester"] = student_data.semester

            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found!",
    )


# Delete exsisting student
@router.delete("/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully!",
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found!",
    )
