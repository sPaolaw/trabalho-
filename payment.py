"""Gateway de pagamento desacoplado.

O sistema só depende da interface PaymentGateway. Trocar o mock por um provedor real
(Mercado Pago, Stripe etc.) exige apenas uma nova implementação, sem tocar nos serviços.
"""
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass


class GatewayTimeout(Exception):
    """Provedor não respondeu a tempo: o resultado da cobrança é desconhecido."""


@dataclass
class GatewayResult:
    approved: bool
    provider_ref: str


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, order_id: int, amount: float, method: str, token: str) -> GatewayResult: ...


class MockPaymentGateway(PaymentGateway):
    """tok_approved* aprova | tok_timeout* simula indisponibilidade | qualquer outro token é recusado."""

    def charge(self, order_id: int, amount: float, method: str, token: str) -> GatewayResult:
        if token.startswith("tok_timeout"):
            raise GatewayTimeout()
        ref = f"mock_{uuid.uuid4().hex[:12]}"
        return GatewayResult(approved=token.startswith("tok_approved"), provider_ref=ref)


def get_gateway() -> PaymentGateway:
    return MockPaymentGateway()
