from typing import Optional
from sqlalchemy.orm import Session

from src.models.user import User
from src.core import tracing_tools


@tracing_tools.trace_it('Utils', 'Verifying user email')
async def verify_email_exists(email: str, db_session: Session) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()

