# A Login System Written in Vue and Python

## How to Setup

### 1. Install and run Frontend
```
npm install
```

```
npm run serve
```

## 2. Execute Backend

```
python backend/backend.py
```

## 3. Run Database

### Login to root
```
mysql -uroot -p
```

### Create Database

```
create database debug_database
```

### Use Database

```
use debug_database
```

### Create Table

```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);
```

### Add Unique Constraint (Selective)

```
ALTER TABLE users
ADD CONSTRAINT unique_username UNIQUE (username);

ALTER TABLE users
ADD CONSTRAINT unique_email UNIQUE (email);
```

##