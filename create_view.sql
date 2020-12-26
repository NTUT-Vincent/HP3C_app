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