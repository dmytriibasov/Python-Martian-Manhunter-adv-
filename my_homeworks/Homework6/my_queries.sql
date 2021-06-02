USE my_items;

### Task 1

CREATE TABLE phones (id INT NOT NULL AUTO_INCREMENT, phone_name CHAR(255), company_id INT NOT NULL, user_id INT NOT NULL, PRIMARY KEY(id));

CREATE TABLE phone_companies (id INT NOT NULL AUTO_INCREMENT, name (CHAR 255), PRIMARY KEY(id));

INSERT INTO phones (phone_name, company_id, user_id)
VALUES ("Xiaomi Redmi Note 8", 1, 1), ("iPhone 12", 2, 2), ("Samsung Galaxy S21", 3, 2),
	("Xiaomi Mi 9T", 1, 3), ("Xiaomi Mi 10", 1, 6), ("iPhone 11 Pro", 2, 4);
	
INSERT INTO phone_companies (name) VALUES ("Xiaomi Company"), ("Apple Inc."), ("Samsung Inc.");

SELECT phone_name FROM phones WHERE company_id = (SELECT id FROM phone_companies WHERE name LIKE "Xiaomi%");


### TASK 2 (extended)

SELECT users.first_name, users.last_name, phones.phone_name, phone_companies.name FROM ((phones INNER JOIN phone_companies ON phones.company_id=phone_companies.id) INNER JOIN users ON phones.user_id=users.id);

