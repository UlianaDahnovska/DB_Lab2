DROP TABLE IF EXISTS Changes_Furniture;
CREATE TABLE Changes_Furniture(
	ID SERIAL PRIMARY KEY,
	UPDATED_AT TIMESTAMP,
	OLD_FURNITURE_NAME VARCHAR(50) NOT NULL,
	NEW_FURNITURE_NAME VARCHAR(50) NOT NULL
);

CREATE OR REPLACE FUNCTION Update_Furniture_Details() RETURNS trigger AS
$$
BEGIN
 	IF NEW.FURNITURE_NAME <> OLD.FURNITURE_NAME THEN
		INSERT INTO Changes_Furniture(UPDATED_AT, OLD_FURNITURE_NAME, NEW_FURNITURE_NAME)
		VALUES(NOW(), OLD.FURNITURE_NAME, NEW.FURNITURE_NAME);
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER Show_Update_Furniture_Name 
BEFORE UPDATE ON Furniture
FOR EACH ROW EXECUTE FUNCTION Update_Furniture_Details();

UPDATE Furniture
SET FURNITURE_NAME = 'Door' WHERE FURNITURE_NAME = 'Table';

UPDATE Furniture
SET FURNITURE_NAME = 'Chair' WHERE FURNITURE_NAME = 'Armchair';

SELECT * FROM Changes_Furniture; 



CREATE OR REPLACE PROCEDURE Create_Table_Furniture(Furniture_Category varchar(40))
LANGUAGE 'plpgsql'
AS $$
BEGIN
	DROP TABLE IF EXISTS Furniture_By_Category;
	CREATE TABLE Furniture_By_Category
	AS
	(SELECT FURNITURE_ID, FURNITURE_NAME, FURNITURE_CATEGORY_NAME FROM Furniture  
	 JOIN Category ON Furniture.FURNITURE_CATEGORY_ID = Category.FURNITURE_CATEGORY_ID
	 WHERE FURNITURE_CATEGORY_NAME = Furniture_Category);
END;
$$;

CALL Create_Table_Furniture('Doors');
select * from Furniture_By_Category



CREATE OR REPLACE FUNCTION Get_Cost_In_Bulk(furniture_price int, furniture_count int)
RETURNS int
LANGUAGE 'plpgsql'
AS $$
DECLARE cost_wholesale INT;

BEGIN
	cost_wholesale = furniture_price * furniture_count;
	RETURN cost_wholesale;
END;
$$;

SELECT Get_Cost_In_Bulk(1000,10); 