@router.post("/update-avatar")
async def update_avatar(user_id: int, file: UploadFile = File(...)):
