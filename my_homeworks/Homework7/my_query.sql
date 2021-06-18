### 3rd task ###

SELECT u. first_name, u.last_name, p.title, c.title, pi.file FROM users u JOIN products p ON u.id=p.user_id JOIN categories_products cp ON p.id=cp.product_id JOIN categories
c ON cp.category_id=c.id JOIN product_images pi ON p.id=pi.product_id;
