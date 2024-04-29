
-- Es una solucion para jugar un poco con tables y luego poder hacer algo de analita si se quisiese 
-- Una URL para probar puede ser https://sqliteonline.com/

CREATE TABLE Products (
    Code VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10, 2)
);

CREATE TABLE PricingRules (
    ProductCode VARCHAR(10),
    Type VARCHAR(10), -- 'discount' or 'normal'
    DiscountType VARCHAR(20), -- '2-for-1' or 'bulk'
    MinCount INT, -- For bulk discounts
    DiscountedPrice DECIMAL(10, 2), -- For bulk discounts
    Price DECIMAL(10, 2), -- For normal pricing
    FOREIGN KEY (ProductCode) REFERENCES Products(Code)
);

-- Insertar datos en la tabla PricingRules
INSERT INTO PricingRules (productcode, type, discounttype, mincount, discountedprice, price)
VALUES
    ('VOUCHER','discount' ,'2-for-1', NULL, NULL, 5),
    ('TSHIRT','discount' , 'bulk', 3, 19.00, NULL),
    ('PANTS','no-discount' , null, null, null, NULL);


-- Insertar datos en la tabla Products
INSERT INTO Products (code, name, price)
VALUES
    ('VOUCHER', 'Gift Card', 5.00),
    ('TSHIRT', 'Summer T-Shirt', 20.00),
    ('PANTS', 'Summer Pants', 7.50);
    
    
-- Crear una tabla temporal para almacenar los productos escaneados junto con su cantidad
drop TABLE if exists ScannedItems;
CREATE TEMPORARY TABLE ScannedItems (
    Code VARCHAR(10),
    Quantity INT,
    Sale_id INT
);

-- Insertar los productos escaneados en la tabla temporal
INSERT INTO ScannedItems (Code, Quantity, sale_id)
VALUES 
('VOUCHER', 4, 1), ('TSHIRT', 7,1), ('PANTS', 1, 1),
('VOUCHER', 2, 2), ('TSHIRT', 1,2), ('PANTS', 0, 2),
('VOUCHER', 1, 3), ('TSHIRT', 1,3), ('PANTS', 1, 3),
('VOUCHER', 3, 4), ('TSHIRT', 3,4), ('PANTS', 1, 4);

select * from ScannedItems

-- Calcular el total basado en las reglas de precios
SELECT s.Sale_id,
    SUM(CASE WHEN pr.Type = 'discount' THEN 
        
                CASE 
                    WHEN pr.DiscountType = '2-for-1' THEN (s.Quantity / 2 + s.Quantity % 2) * pd.Price 
                    WHEN pr.DiscountType = 'bulk' AND s.Quantity >= pr.MinCount THEN  s.Quantity * pr.DiscountedPrice 
                    ELSE 
                        s.Quantity * pd.Price 
                END 
            ELSE 
                s.Quantity * pd.Price 
        END) AS Total

FROM 
    ScannedItems s
JOIN 
    PricingRules pr ON s.Code = pr.ProductCode
join 
	Products pd on s.Code = pd.Code
GROUP by s.Sale_id

