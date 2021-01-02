CREATE VIEW PRODUCT_CPU
AS SELECT * FROM PRODUCT JOIN CPU on type_id = product_ptr_id;
CREATE VIEW PRODUCT_GPU
AS SELECT * FROM PRODUCT JOIN GPU on type_id = product_ptr_id;
CREATE VIEW PRODUCT_MB
AS SELECT * FROM PRODUCT JOIN MB on type_id = product_ptr_id;
CREATE VIEW PRODUCT_SSD
AS SELECT * FROM PRODUCT JOIN SSD on type_id = product_ptr_id;
CREATE VIEW PRODUCT_RAM
AS SELECT * FROM PRODUCT JOIN RAM on type_id = product_ptr_id;

CREATE VIEW ORDER_WITH_PRICE AS
SELECT O.*, sum(P.price * L.quantity * C.disc_value) AS price
FROM PURCHASE_ORDER O JOIN LINE_ITEM L ON O.order_id = L.order_id
JOIN PRODUCT P ON L.type_id = P.type_id
JOIN COUPON C ON O.coupon_code_id = C.pcode
GROUP BY O.order_id