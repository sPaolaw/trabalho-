from sqlalchemy.orm import Session

from app.models import AuditLog


def log(db: Session, user_id: int | None, action: str, entity: str,
        entity_id: int | None = None, details: str | None = None) -> None:
    """Registra operação sensível. Não faz commit: entra na mesma transação da operação auditada.
    Regra LGPD: `details` nunca deve conter nome, e-mail ou CPF."""
    db.add(AuditLog(user_id=user_id, action=action, entity=entity, entity_id=entity_id, details=details))
