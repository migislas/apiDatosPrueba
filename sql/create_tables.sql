
-- -- Creation of product table
-- CREATE TABLE IF NOT EXISTS product (
--   product_id INT NOT NULL,
--   name varchar(250) NOT NULL,
--   PRIMARY KEY (product_id)
-- );


-- CREATE FUNCTION sum_n_product(IN x int,IN y int, OUT sum int, OUT prod int) AS $$
-- BEGIN
--     sum := x + y;
--     prod := x * y;
-- END;
-- $$ LANGUAGE plpgsql;
-- Creation of Metrobus Information table
-- id INT,
--       date_updated DATE,
--       vehicle_id INT,
--       vehicle_current_status INT,
--       position_latitude numeric,
--       position_longitude numeric,
--       name varchar(250),
--       position_speed numeric,
--       position_odometer numeric,
--       trip_schedule_relationship numeric,
--       trip_id INT,
--       trip_start_date varchar(250),
--       trip_route_id INT
--       );


CREATE TABLE IF NOT EXISTS informacion (
      idMetrobus varchar(250),
      date_updated varchar(250),
      vehicle_id varchar(250),
      vehicle_label varchar(250),
      vehicle_current_status varchar(250),
      position_latitude varchar(250),
      position_longitude varchar(250),
      posicionPunto varchar(250),
      position_speed varchar(250),
      position_odometer varchar(250),
      trip_schedule_relationship varchar(250),
      trip_id varchar(250),
      tstartDate varchar(250),
      trip_route_id varchar(250)
      );
-- SLECT trip_start_date, geographic_point FROM refcursor
-- WHERE ID = 'VARIABLE'
  -- Procedure that returns a single result set (cursor)

CREATE OR REPLACE FUNCTION idFUNCION()  RETURNS TABLE(id varchar(250)) AS $$
  BEGIN
    RETURN QUERY
    SELECT DISTINCT vehicle_id  FROM informacion
    ORDER BY vehicle_id;   
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION idBusqueda(IN metrobusLabel varchar(250))  
              RETURNS TABLE(  fecha varchar(250),posicionPunto varchar(250)) AS $$
  #variable_conflict use_column
  BEGIN
    RETURN QUERY
    SELECT  tstartDate, posicionPunto  FROM informacion
    WHERE vehicle_id = metrobusLabel;   
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION posicion()  
              RETURNS TABLE(  Posiciones varchar(250),vehicle_id varchar(250)) AS $$
                                                
  #variable_conflict use_column
  BEGIN
    RETURN QUERY
    SELECT  posicionPunto,vehicle_id  FROM informacion;  
END;
$$ LANGUAGE plpgsql;