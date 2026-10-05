# Feature Brief: In-Stock Product Filter

## User Outcome
Store application users can hide unavailable products and focus on items that can be ordered now.

## Acceptance Criteria
- `GET /products` returns every product when the query parameter is omitted.
- `GET /products?in_stock_only=true` returns only products whose `in_stock` value is `true`.
- `GET /products?in_stock_only=false` returns every product.
- Product order and response fields remain unchanged.
- Tests cover the default, explicit `true`, and explicit `false` behaviors.
- Lint and security checks pass, and the changelog and API notes are updated.

## Backward Compatibility
Existing clients that omit the query parameter continue to receive every product, in the existing catalog order and with the existing response fields.

## Affected Behavior
The current `GET /products` handler returns the `PRODUCTS` list without filtering. The requested change adds optional filtering by the existing `in_stock` field; only the explicit `true` value restricts results. The current fixture has both in-stock and out-of-stock products.

## Test Scenarios
- Omit `in_stock_only`: response contains every product in catalog order.
- Set `in_stock_only=true`: response contains only products with `in_stock: true`, retaining their relative catalog order and existing fields.
- Set `in_stock_only=false`: response contains every product in catalog order.

## Open Decision
None identified. Issue #1 specifies the parameter behavior, compatibility expectations, and ordering/field constraints.