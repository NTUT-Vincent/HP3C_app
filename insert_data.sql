DELETE FROM USER;
DELETE FROM PRODUCT;
DELETE FROM CPU;
DELETE FROM MB;
DELETE FROM SSD;
DELETE FROM RAM;
DELETE FROM GPU;
DELETE FROM PURCHASE_ORDER;
DELETE FROM LINE_ITEM;
DELETE FROM MANAGE;
DELETE FROM COUPON;


-- insert USER

INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0001','115台北市南港區研究院路一段99號', 'M', '00000001', 1, 'Kevin');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0002', '115台北市南港區研究院路一段99號', 'M', '00000002', 1, 'James');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0003', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000003', 1, 'Bryant');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0004', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000004', 1, 'Kyle');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0005', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'F', '00000005', 1, 'Annie');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0006', '12, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000006', 1,'Annie');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0007', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000007', 1, 'Lue');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0008', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000008', 1, 'Len');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0009', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000009', 1, 'Bob');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0010', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000010', 1, 'Harden');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0011', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000011', 1, 'Tom');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('costumer0012', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000012', 1, 'George');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0001', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000001', 2, 'Jeff');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0002', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000002', 2, 'Brian');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0003', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000003', 2, 'Jack');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0004', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000004', 2, 'Oscar');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0005', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000005', 2, 'Danny');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0006', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'F', '00000006', 2, 'Jenny');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0007', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'F', '00000007', 2, 'Jessica');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0008', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000008', 2, 'Kyle');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0009', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000009', 2, 'Robert');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0010', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000010', 2, 'Leo');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0011', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000011', 2, 'Paul');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('staff0012', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000012', 2, 'Zack');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('admin0001', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000001', 2, 'Tommy');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('admin0002', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000002', 2, 'Henrry');
INSERT INTO USER(user_id, address, gender, password, user_type, name) VALUES('admin0003', '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', 'M', '00000003', 2, 'George');

-- insert product 
-- CPU
INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Intel Core i7-10700', 'Intel', 20, 10390, 10, 'https://e.ecimg.tw/items/DRAI2NA900ANZQ3/000001_1590980027.jpg');
INSERT INTO CPU(product_ptr_id, socket, cores, clock, cache) VALUES('Intel Core i7-10700', '1200', 8, '2.90-4.80 GHz', '16MB');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Intel Core i5-10500', 'Intel', 20, 6750, 10, 'https://d.ecimg.tw/items/DRAI2NA900ANZPG/000001_1590979514.jpg');
INSERT INTO CPU(product_ptr_id, socket, cores, clock, cache) VALUES('Intel Core i5-10500', '1200', 6, '3.10-4.50 GHz', '12MB');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Intel Core i3-10100', 'Intel', 20, 6750, 10, 'https://d.ecimg.tw/items/DRAI2NA900ANZPG/000001_1590979514.jpg');
INSERT INTO CPU(product_ptr_id, socket, cores, clock, cache) VALUES('Intel Core i3-10100', '1200', 4, '3.60-4.30 GHz', '6MB');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('AMD Ryzen 7-3800X', 'AMD', 20, 12700, 10, 'https://e.ecimg.tw/items/DRAI07A900A4PG1/000001_1562325857.jpg');
INSERT INTO CPU(product_ptr_id, socket, cores, clock, cache) VALUES('AMD Ryzen 7-3800X', 'AM4', 8, '3.90-4.50 GHz', '32MB');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('AMD Ryzen 5-3400G', 'AMD', 20, 4870, 10, 'https://e.ecimg.tw/items/DRAI05A900A4PFX/000001_1562325659.jpg');
INSERT INTO CPU(product_ptr_id, socket, cores, clock, cache) VALUES('AMD Ryzen 5-3400G', 'AM4', 4, '3.70-4.20 GHz', '16MB');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('AMD Ryzen 3-3100', 'AMD', 20, 3270, 10, 'https://f.ecimg.tw/items/DRAI2SA900ANOEN/000001_1590033460.jpg');
INSERT INTO CPU(product_ptr_id, socket, cores, clock, cache) VALUES('AMD Ryzen 3-3100', 'AM4', 4, '3.60-3.90 GHz', '16MB');

-- GPU
INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('GIGABYTE GeForce RTX 3060 Ti', 'GIGABYTE', 20, 13790, 11, 'https://b.ecimg.tw/items/DRAD1KA900B0TR8/000001_1606844781.jpg');
INSERT INTO GPU(product_ptr_id, model, size) VALUES('GIGABYTE GeForce RTX 3060 Ti', 'GeForce RTX 3060 Ti', '8G');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('msi GeForce GTX1660', 'msi', 20, 6090, 11, 'https://d.ecimg.tw/items/DRAD1RA9009V3U6/000001_1599789881.jpg');
INSERT INTO GPU(product_ptr_id, model, size) VALUES('msi GeForce GTX1660', 'GeForce GTX 1660', '6G');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('GIGABYTE Radeon RX 6800 GAMING OC 16G', 'GIGYBYTE', 20, 20590, 11, 'https://f.ecimg.tw/items/DRAD1KA900B10T3/000001_1607011477.jpg');
INSERT INTO GPU(product_ptr_id, model, size) VALUES('GIGABYTE Radeon RX 6800 GAMING OC 16G', 'Radeon RX 6800','16G');

-- mother board
INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('msi MPG Z490 GAMING EDGE WIFI', 'msi', 20, 7090, 12, 'https://f.ecimg.tw/items/DSAJ28A900ANDGR/000001_1589165310.jpg');
INSERT INTO MB(product_ptr_id, chip, size, expansion) VALUES('msi MPG Z490 GAMING EDGE WIFI', '1200', 2, 'unknown');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('ASUS PROART Z490 CREATOR 10G', 'ASUS', 20, 9090, 12, 'https://e.ecimg.tw/items/DSAJ3EA900ANKPQ/000001_1590399233.jpg');
INSERT INTO MB(product_ptr_id, chip, size, expansion) VALUES('ASUS PROART Z490 CREATOR 10G', '1200', 2, 'unknown');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('GIGABYTE Z490 AORUS MASTER', 'GIGABYTE', 20, 12090, 12, 'https://b.ecimg.tw/items/DSAJ3KA900AO01W/000001_1590558965.jpg');
INSERT INTO MB(product_ptr_id, chip, size, expansion) VALUES('GIGABYTE Z490 AORUS MASTER', '1200', 2, 'unknown');

-- RAM
INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Kingston DDR4 2666 8GB', 'Kingston', 20, 989, 13, 'https://e.ecimg.tw/items/DRAL3TA900A5PM8/000001_1581502612.jpg');
INSERT INTO RAM(product_ptr_id, gen, size, speed, channel) VALUES('Kingston DDR4 2666 8GB', 'DDR4', '8GB', '2666MHz', 0);

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('HyperX Impact DDR4 3200 8GB', 'HyperX', 20, 1183, 13, 'https://e.ecimg.tw/items/DRAL1WA9008WIJC/000001_1533522880.jpg');
INSERT INTO RAM(product_ptr_id, gen, size, speed, channel) VALUES('HyperX Impact DDR4 3200 8GB', 'DDR4', '8GB', '3200MHz', 0);

-- ssd
INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Micron Crucial MX500 1TB SATA3', 'Micron', 20, 2999, 14, 'https://e.ecimg.tw/items/DRAH7GA900AHXTO/000001_1607073876.jpg');
INSERT INTO SSD(product_ptr_id, interface, size, speed) VALUES('Micron Crucial MX500 1TB SATA3', 0, '1TB', '560MB/s');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Kingston KC600 SATA-3 512GB SSD', 'Kingston', 20, 2999, 14, 'https://e.ecimg.tw/items/DRAH7GA900AHXTO/000001_1607073876.jpg');
INSERT INTO SSD(product_ptr_id, interface, size, speed) VALUES('Kingston KC600 SATA-3 512GB SSD', 0, '512GB', '550MB/s');

INSERT INTO PRODUCT(type_id, brand, quantity, price, polymorphic_ctype_id, product_picture) VALUES('Transcend PCIe SSD 220S 512GB', 'Transcend', 20, 1900, 14, 'http://www.transcend-info.com/products/images/item/TS512GMTE220S-.png');
INSERT INTO SSD(product_ptr_id, interface, size, speed) VALUES('Transcend PCIe SSD 220S 512GB', 1, '512GB', '3,500MB/s');

-- insert coupon
INSERT INTO COUPON(pcode, disc_value, restrict, type, coupon_staff_id) VALUES('coupon0001', 0.95, 'no restrict', 1, 'staff0001');
INSERT INTO COUPON(pcode, disc_value, restrict, type, coupon_staff_id) VALUES('coupon0002', 0.85, 'no restrict', 2, 'staff0002');
INSERT INTO COUPON(pcode, disc_value, restrict, type, coupon_staff_id) VALUES('coupon0003', 0.95, 'no restrict', 1, 'staff0001');
INSERT INTO COUPON(pcode, disc_value, restrict, type, coupon_staff_id) VALUES('coupon0004', 0.95, 'no restrict', 1, 'staff0010');
INSERT INTO COUPON(pcode, disc_value, restrict, type, coupon_staff_id) VALUES('coupon0005', 0.75, 'no restrict', 3, 'staff0005');
INSERT INTO COUPON(pcode, disc_value, restrict, type, coupon_staff_id) VALUES('coupon0006', 0.55, 'no restrict', 5, 'staff0012');

-- insert ORDER
INSERT INTO PURCHASE_ORDER(order_id, address, delivered_date_time, deliver_type, status, coupon_code_id, order_customer_id, order_staff_id, payment, order_date_time) VALUES(1, '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', '2020-12-01 10:22:00', 'Home delivery', 'delivering', 'coupon0001', 'costumer0001', 'staff0001', 'credit card', '2020-12-01 10:22:00');
INSERT INTO PURCHASE_ORDER(order_id, address, delivered_date_time, deliver_type, status, coupon_code_id, order_customer_id, order_staff_id, payment, order_date_time)  VALUES(2, '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', '2020-12-04 20:12:00', 'Home delivery', 'delivering', 'coupon0002', 'costumer0002', 'staff0001', 'credit card', '2020-11-30 10:15:00');
INSERT INTO PURCHASE_ORDER(order_id, address, delivered_date_time, deliver_type, status, coupon_code_id, order_customer_id, order_staff_id, payment, order_date_time)  VALUES(3 , '1, Sec. 3, Zhongxiao E. Rd., Taipei 10608 Taiwan', '2020-12-05 20:12:00', 'Home delivery', 'delivering', 'coupon0002', 'costumer0003', 'staff0004', 'cash', '2020-11-29 10:15:00');

-- inset line_item
INSERT INTO LINE_ITEM VALUES(1, 1, 1, 'ASUS PROART Z490 CREATOR 10G');
INSERT INTO LINE_ITEM VALUES(2, 1, 1, 'Kingston DDR4 2666 8GB');
INSERT INTO LINE_ITEM VALUES(3, 1, 1, 'Transcend PCIe SSD 220S 512GB');
INSERT INTO LINE_ITEM VALUES(4, 1, 1, 'msi GeForce GTX1660');
INSERT INTO LINE_ITEM VALUES(5, 1, 2, 'Intel Core i7-10700');
INSERT INTO LINE_ITEM VALUES(6, 1, 2, 'GIGABYTE Radeon RX 6800 GAMING OC 16G');
INSERT INTO LINE_ITEM VALUES(7, 1, 2, 'Micron Crucial MX500 1TB SATA3');
INSERT INTO LINE_ITEM VALUES(8, 1, 3, 'ASUS PROART Z490 CREATOR 10G');
INSERT INTO LINE_ITEM VALUES(9, 1, 3, 'Kingston DDR4 2666 8GB');

-- insert manage
INSERT INTO MANAGE(id, Ptype_id, Staff_id) VALUES(1, 'msi GeForce GTX1660', 'staff0001');
INSERT INTO MANAGE(id, Ptype_id, Staff_id) VALUES(2, 'Micron Crucial MX500 1TB SATA3', 'staff0003');
INSERT INTO MANAGE(id, Ptype_id, Staff_id) VALUES(3, 'Intel Core i7-10700', 'admin0003');





