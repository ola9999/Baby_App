# Create Order API Documentation

## Overview
This API endpoint allows external systems to create orders in the restaurant management system. The API supports creating orders with items, combos, customer information, and various configurations.

## Endpoint
```
POST /api/orders/create
```

## Authentication
- **Required**: Yes
- **Type**: Bearer Token or API Key (specify your authentication method)

## Request Format

### Content-Type
```
application/json
```

### Request Body Structure

```json
{
  "branch_id": integer,
  "customer": {
    "name": "string",
    "phone": "string",
    "dial_code": "string",
    "email": "string",
    "address": {
      "address": "string",
      "city": "string",
      "state": "string",
      "title": "string",
      "block_number": "string",
      "level_number": "string", 
      "door_number": "string",
      "longitude": "decimal",
      "latitude": "decimal"
    }
  },
  "order_type": integer,
  "order_source": integer,
  "payment_method": integer,
  "items": [
    {
      "product_id": integer,
      "quantity": integer,
      "discount_id": integer,
      "options": [
        {
          "modifier_option_id": integer,
          "quantity": integer
        }
      ]
    }
  ],
  "combos": [
    {
      "combo_size_id": integer,
      "quantity": integer,
      "discount_id": integer,
      "products": [
        {
          "product_id": integer,
          "combo_size_id": integer,
          "options": [
            {
              "modifier_option_id": integer,
              "quantity": integer
            }
          ]
        }
      ]
    }
  ],
  "service_charges": [
    {
      "charge_id": integer
    }
  ]
}
```

## Request Fields Description

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `branch_id` | integer | ID of the restaurant branch |
| `order_type` | integer | Type of order (see Order Types) |
| `order_source` | integer | Source of the order (see Order Sources) |
| `payment_method` | integer | Payment method (see Payment Methods) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `customer` | object | Customer information |
| `items` | array | Array of individual items |
| `combos` | array | Array of combo items |
| `service_charges` | array | Array of service charges |

### Customer Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | No | Customer name |
| `phone` | string | Yes* | Customer phone number |
| `dial_code` | string | No | Phone dial code (default: "966") |
| `email` | string | No | Customer email |
| `address` | object | No** | Customer address |

*Required for delivery orders
**Required for delivery orders

### Address Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `address` | string | Yes | Full address |
| `city` | string | No | City name |
| `state` | string | No | State name |
| `title` | string | Yes | Address title |
| `block_number` | string | No | Block number |
| `level_number` | string | No | Level/floor number |
| `door_number` | string | No | Door number |
| `longitude` | decimal | No | GPS longitude |
| `latitude` | decimal | No | GPS latitude |

### Items Array

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `product_id` | integer | Yes | Menu item ID |
| `quantity` | integer | Yes | Quantity of the item |
| `discount_id` | integer | No | Applied discount ID |
| `options` | array | No | Array of modifiers |

### Item Options Array

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `modifier_option_id` | integer | Yes | Modifier option ID |
| `quantity` | integer | Yes | Quantity of the modifier |

### Combos Array

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `combo_size_id` | integer | Yes | Combo size ID |
| `quantity` | integer | Yes | Quantity of the combo |
| `discount_id` | integer | No | Applied discount ID |
| `products` | array | Yes | Array of products in the combo |

### Combo Products Array

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `product_id` | integer | Yes | Product ID within the combo |
| `combo_size_id` | integer | Yes | Combo size ID |
| `options` | array | No | Array of modifiers for the product |

## Enumeration Values

### Order Types
| Value | Name | Description |
|-------|------|-------------|
| 1 | Dine In | Customer dines in the restaurant |
| 2 | Take Away | Customer picks up the order |
| 3 | Delivery | Order delivered to customer |
| 4 | Drive Through | Drive-through order |

### Order Sources
| Value | Name | Description |
|-------|------|-------------|
| 1 | Cashier | Order created by cashier |
| 2 | Web App | Order from web application |
| 3 | Tablet App | Order from tablet application |
| 4 | External Source | Order from external system |
| 5 | Third Party | Order from third-party platform |

### Payment Methods
| Value | Name | Description |
|-------|------|-------------|
| 1 | Cash | Cash payment |
| 2 | Online Payment | Online credit card |
| 3 | Credit Card at Door | Physical credit card |
| 4 | Partial Payment | Partial payment |
| 5 | Transfer | Bank transfer |

### Order Status
| Value | Name | Description |
|-------|------|-------------|
| 1 | Pending | Order is pending |
| 2 | Active | Order is active |
| 3 | Declined | Order declined |
| 4 | Closed | Order completed |
| 5 | Returned | Order returned |
| 6 | Joined | Order joined |
| 7 | Processing | Order in processing |
| 8 | Future | Future order |

### Payment Status
| Value | Name | Description |
|-------|------|-------------|
| 1 | Waiting | Waiting for payment |
| 2 | Canceled | Payment canceled |
| 3 | Completed | Payment completed |
| 4 | Failed | Payment failed |
| 5 | Succeeded | Payment succeeded |

## Response Format

### Success Response (HTTP 201)

```json
{
  "success": true,
  "data": {
    "id": integer,
    "order_number": "string",
    "status": integer,
    "order_type": integer,
    "order_source": integer,
    "payment_method": integer,
    "payment_status": integer,
    "branch": {
      "id": integer,
      "name": "string"
    },
    "customer": {
      "id": integer,
      "name": "string",
      "phone": "string",
      "email": "string",
      "address": {
        "address": "string",
        "city": "string",
        "state": "string",
        "title": "string",
        "longitude": "decimal",
        "latitude": "decimal"
      }
    },
    "items": [
      {
        "id": integer,
        "product": {
          "id": integer,
          "name": "string",
          "category": {
            "id": integer,
            "name": "string"
          }
        },
        "quantity": integer,
        "unit_price": "decimal",
        "price_without_tax": "decimal",
        "taxes_price": "decimal",
        "discount_price": "decimal",
        "taxes": [
          {
            "id": integer,
            "name": "string",
            "rate": "decimal"
          }
        ],
        "options": [
          {
            "modifier_option_id": integer,
            "name": "string",
            "name_ar": "string",
            "name_en": "string",
            "parent_name": "string",
            "parent_name_ar": "string",
            "parent_name_en": "string",
            "quantity": integer,
            "unit_price": "decimal",
            "taxes": [
              {
                "id": integer,
                "name": "string",
                "rate": "decimal"
              }
            ],
            "taxes_price": "decimal"
          }
        ]
      }
    ],
    "combos": [
      {
        "id": integer,
        "combo_size_id": integer,
        "quantity": integer,
        "unit_price": "decimal",
        "price_without_tax": "decimal",
        "taxes_price": "decimal",
        "discount_price": "decimal",
        "products": [
          {
            "product_id": integer,
            "combo_size_id": integer,
            "unit_price": "decimal",
            "taxes": [
              {
                "id": integer,
                "name": "string",
                "rate": "decimal"
              }
            ],
            "options": [
              {
                "modifier_option_id": integer,
                "quantity": integer,
                "unit_price": "decimal",
                "taxes": [
                  {
                    "id": integer,
                    "name": "string",
                    "rate": "decimal"
                  }
                ],
                "taxes_price": "decimal"
              }
            ]
          }
        ]
      }
    ],
    "service_charges": [
      {
        "charge_id": integer,
        "amount": "decimal",
        "charge": {
          "id": integer,
          "name": "string",
          "description": "string"
        },
        "taxes": [
          {
            "id": integer,
            "name": "string",
            "rate": "decimal"
          }
        ]
      }
    ],
    "subtotal": "decimal",
    "tax_amount": "decimal",
    "discount_amount": "decimal",
    "service_charge_amount": "decimal",
    "total_amount": "decimal",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

## Error Responses

### Validation Error (HTTP 400)

```json
{
  "success": false,
  "error": "Validation Error",
  "details": {
    "field_name": [
      "Error message"
    ]
  }
}
```

### Authentication Error (HTTP 401)

```json
{
  "success": false,
  "error": "Authentication failed",
  "message": "Invalid or missing authentication token"
}
```

### Resource Not Found (HTTP 404)

```json
{
  "success": false,
  "error": "Resource not found",
  "message": "Branch with ID 123 not found"
}
```

### Server Error (HTTP 500)

```json
{
  "success": false,
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

## Common Error Scenarios

### 1. Invalid Branch ID
- **HTTP Status**: 404
- **Error**: Branch not found
- **Solution**: Verify the branch ID exists and is active

### 2. Invalid Product ID
- **HTTP Status**: 404
- **Error**: Product not found
- **Solution**: Verify the product ID exists in the menu

### 3. Invalid Modifier Option ID
- **HTTP Status**: 404
- **Error**: Modifier option not found
- **Solution**: Verify the modifier option ID is valid for the product

### 4. Missing Customer Information for Delivery
- **HTTP Status**: 400
- **Error**: Customer information required for delivery orders
- **Solution**: Provide customer name, phone, and address for delivery orders

### 5. Invalid Discount ID
- **HTTP Status**: 404
- **Error**: Discount not found
- **Solution**: Verify the discount ID exists and is applicable to the items

### 6. Invalid Combo Configuration
- **HTTP Status**: 400
- **Error**: Invalid combo configuration
- **Solution**: Ensure all required products are included in the combo

### 7. Branch Closed
- **HTTP Status**: 400
- **Error**: Branch is currently closed
- **Solution**: Check branch opening hours and try again during operating hours

### 8. Invalid Order Type for Branch
- **HTTP Status**: 400
- **Error**: Order type not supported by this branch
- **Solution**: Use a supported order type for the branch

## Business Rules

### Order Types and Customer Requirements
- **Delivery orders** (type 3) require customer information and address
- **Dine-in orders** (type 1) may not require customer information
- **Take-away orders** (type 2) may require customer phone number

### Combo Rules
- Combos must include all required products for the combo size
- Combo products must be valid for the specific combo configuration
- Combo size must be available for the combo

### Discount Rules
- Discounts are optional and must be valid for the specific items
- Multiple discounts cannot be applied to the same item
- Discount eligibility is validated against item categories and restrictions

### Tax Calculation
- Taxes are calculated based on the item's tax group
- Tax rates are applied to the base price before discounts (if taxable=true)
- Tax rates are applied to the discounted price (if taxable=false)

## Example Requests

### Simple Dine-in Order

```json
{
  "branch_id": 1,
  "order_type": 1,
  "order_source": 4,
  "payment_method": 1,
  "items": [
    {
      "product_id": 123,
      "quantity": 2,
      "options": [
        {
          "modifier_option_id": 456,
          "quantity": 1
        }
      ]
    }
  ]
}
```

### Delivery Order with Customer

```json
{
  "branch_id": 1,
  "order_type": 3,
  "order_source": 2,
  "payment_method": 2,
  "customer": {
    "name": "John Doe",
    "phone": "1234567890",
    "dial_code": "966",
    "email": "john@example.com",
    "address": {
      "address": "123 Main Street",
      "city": "Riyadh",
      "state": "Riyadh",
      "title": "Home",
      "block_number": "A",
      "level_number": "2",
      "door_number": "201",
      "longitude": 24.7136,
      "latitude": 46.6753
    }
  },
  "items": [
    {
      "product_id": 123,
      "quantity": 1,
      "discount_id": 789
    }
  ],
  "combos": [
    {
      "combo_size_id": 456,
      "quantity": 1,
      "products": [
        {
          "product_id": 111,
          "combo_size_id": 456,
          "options": [
            {
              "modifier_option_id": 222,
              "quantity": 1
            }
          ]
        },
        {
          "product_id": 333,
          "combo_size_id": 456
        }
      ]
    }
  ]
}
```

## Rate Limiting
- **Limit**: 100 requests per minute per API key
- **Header**: `X-RateLimit-Remaining` indicates remaining requests
- **Reset**: `X-RateLimit-Reset` indicates when the limit resets

## Webhook Notifications
If configured, the system will send webhook notifications for:
- Order status changes
- Payment status updates
- Order cancellations

## Testing
Use the following test endpoints for development:
- **Sandbox**: `https://api-sandbox.example.com/api/orders/create`
- **Production**: `https://api.example.com/api/orders/create`

## Support
For technical support or questions about this API:
- **Email**: api-support@example.com
- **Documentation**: https://docs.example.com/api
- **Status Page**: https://status.example.com

## Changelog
- **v1.0**: Initial API release
- **v1.1**: Added combo support
- **v1.2**: Enhanced customer address fields
- **v1.3**: Added service charges support