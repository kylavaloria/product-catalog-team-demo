# Product Catalog API

## `GET /products`
Returns all products in catalog order. The optional `in_stock_only` query parameter
filters the response to products with `in_stock: true` when set to `true`. When
omitted or set to `false`, all products are returned. Product fields and catalog
order are unchanged.
