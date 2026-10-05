# Add an in-stock-only filter to the product catalog

## User story
As a store application user, I want to hide unavailable products so that I can focus on items that can be ordered now.

## Expected behavior
- `GET /products` continues to return every product.
- `GET /products?in_stock_only=true` returns only products where `in_stock` is `true`.
- `GET /products?in_stock_only=false` behaves like the current endpoint and returns every product.
- Product order and response fields remain unchanged.

## Acceptance criteria
- Existing clients that send no query parameter are unaffected.
- Tests cover default, `true`, and explicit `false` behavior.
- Lint and security checks pass.
- The changelog and API notes are updated.
