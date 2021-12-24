INSERT INTO Category
VALUES  (1,'Beds'),
        (2,'Bar furniture'),
        (3,'Bookcases & shelving units'),
        (4,'Cabinets & cupboards');

		
INSERT INTO Furniture(FURNITURE_NAME,FURNITURE_SHORT_DESCRIPTION,FURNITURE_CATEGORY_ID) 
VALUES  ('BILLY','Bookcase with glass-doors, 80x30x202 cm',4),
        ('KALLVIKEN','Drawer front, 60x26 cm',3),
		('EKET','Wall-mounted cabinet combination, 105x35x120 cm',3),
		('LYCKSELE MURBO','Mattress, 140x188 cm',1),
		('VALLENTUNA','3-seat modular sofa with sofa-bed',1),
		('KULLABERG','Stool',2),
		('NORDVIKEN','Bar stool with backrest, 75 cm',2);

		
		
INSERT INTO Furniture_Price(FURNITURE_PRICE,FURNITURE_ID) 
VALUES  (745,1),
        (136,2),
		(414,3),
		(695,4),
		(4036,5),
		(140,6),
		(275,7);