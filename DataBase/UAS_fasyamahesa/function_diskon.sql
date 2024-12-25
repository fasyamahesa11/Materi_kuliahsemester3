DELIMITER //
CREATE FUNCTION hitung_diskon(total DECIMAL(10,2)) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE diskon DECIMAL(10,2);
    IF total >= 500000 THEN
        SET diskon = total * 0.1;
    ELSE
        SET diskon = 0;
    END IF;
    RETURN diskon;
END //
DELIMITER ;
