-- creates a trigger to decrease quantity
CREATE TRIGGER new_trigger
AFTER INSERT ON orders
FROM EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
