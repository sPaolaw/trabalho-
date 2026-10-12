from decimal import Decimal

# Perfis
CUSTOMER, ATTENDANT, MANAGER, ADMIN = "CUSTOMER", "ATTENDANT", "MANAGER", "ADMIN"

# Canais: cliente usa APP/PICKUP; equipe da loja registra BALCAO/TOTEM
CHANNELS_CUSTOMER = {"APP", "PICKUP"}
CHANNELS_STAFF = {"BALCAO", "TOTEM"}

# Status do pedido
CREATED, PAID, PREPARING, READY, DELIVERED = "CREATED", "PAID", "PREPARING", "READY", "DELIVERED"
CANCELLED, PAYMENT_FAILED = "CANCELLED", "PAYMENT_FAILED"

# Avanço manual feito pela equipe (PAID só via pagamento; CANCELLED só via /cancel)
STAFF_TRANSITIONS = {PAID: PREPARING, PREPARING: READY, READY: DELIVERED}
CANCELLABLE_BY_STAFF = {CREATED, PAID, PREPARING}
REVENUE_STATUSES = (PAID, PREPARING, READY, DELIVERED)

# Fidelização
POINTS_PER_REAIS = 10                 # 1 ponto a cada R$ 10 pagos
POINT_VALUE = Decimal("0.10")         # 1 ponto = R$ 0,10 de desconto no resgate
TIERS = [("OURO", 500, 10), ("PRATA", 200, 5), ("BRONZE", 0, 0)]  # (nome, pontos acumulados, % desconto)
