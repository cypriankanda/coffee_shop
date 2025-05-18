# Coffee Shop Domain Model

## Overview

This project models a Coffee Shop domain using Python and object-oriented programming principles.  
It consists of three main entities: `Customer`, `Coffee`, and `Order`, and their relationships.

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.
- `Customer` and `Coffee` have a many-to-many relationship through `Order`.

## Features

- Class definitions for Customer, Coffee, and Order with input validation.
- Methods to manage relationships and aggregate data:
  - Customers can create orders.
  - Retrieve orders and coffees per customer.
  - Retrieve orders, customers, number of orders, and average price per coffee.
  - Find the customer who spent the most on a specific coffee.
- Comprehensive unit tests using `pytest`.

## Installation and Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/cypriankanda/coffee_shop.git
   cd coffee_shop
