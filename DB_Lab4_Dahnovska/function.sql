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
