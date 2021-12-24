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
