# Service Registry

> **Single source of truth** cho danh sách service. KHÔNG sửa bảng tay — sửa `services` trong
> `template.config.json` rồi chạy `pwsh scripts/apply-template.ps1`. Mọi doc khác tham chiếu file này.

## Services (theo tier)

Chưa có service; khai báo trong manifest khi chốt stack.

<!-- BEGIN gen:services-registry -->
| Key | Service | Tier | Stack | Repo | Base URL env |
|-----|---------|------|-------|------|--------------|
<!-- END gen:services-registry -->

## Tier — ý nghĩa

| Tier | Vai trò |
|------|---------|
| `frontend` | Web/mobile app người dùng cuối |
| `bff` | Backend-for-frontend / API gateway / edge |
| `gateway` | Reverse proxy / ingress (nếu tách khỏi bff) |
| `domain` | Service nghiệp vụ (mỗi bounded context 1 service) |
| `integration` | Adapter hệ ngoài (bank, SOAP, message protocol…) |
| `infra` | CI/CD, observability, shared contracts (proto/OpenAPI) |

## Env theo tier

Xem [server-config.example.md](../server-config.example.md) (khối `gen:env`) — danh sách biến môi trường gom theo tier, cũng sinh từ cùng manifest.
