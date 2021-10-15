


CREATE TABLE IF NOT EXISTS informacion (
      id int,
      date_updated varchar(250),
      vehicle_id varchar(250),
      vehicle_label varchar(250),
      vehicle_current_status varchar(250),
      position_latitude varchar(250),
      position_longitude varchar(250),
      geographic_point geometry,
      position_speed varchar(250),
      position_odometer varchar(250),
      trip_schedule_relationship varchar(250),
      trip_id varchar(250),
      trip_start_date varchar(250),
      trip_route_id varchar(250)
      );

CREATE TABLE IF NOT EXISTS alcaldias (
      idAlcaldia int,
      nombreAlcaldia varchar(250),
      geometryAlcaldia geometry
      );


CREATE OR REPLACE FUNCTION idFUNCION()  RETURNS TABLE(id varchar(250)) AS $$
  BEGIN
    RETURN QUERY
    SELECT DISTINCT vehicle_id  FROM informacion
    ORDER BY vehicle_id;   
END;
$$ LANGUAGE plpgsql;

      
CREATE OR REPLACE FUNCTION idBusqueda(IN metrobus_id int)  
              RETURNS TABLE(  fecha varchar(250),lat varchar(250), long varchar(250)) AS $$
  #variable_conflict use_column
  BEGIN
    RETURN QUERY
    SELECT  trip_start_date, position_latitude, position_longitude FROM informacion
    WHERE vehicle_id::integer = metrobus_id;   
END;
$$ LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION AlcaldiasconMetrobus()  
              RETURNS TABLE(  alcaldia varchar(250)) AS $$
                                                
  #variable_conflict use_column
  BEGIN
    RETURN QUERY
    SELECT  DISTINCT  al.nombreAlcaldia 
    FROM alcaldias AS al, informacion AS inf
    WHERE ST_Contains(al.geometryAlcaldia, inf.geographic_point) 
    ORDER BY al.nombreAlcaldia;  
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION alcaldiaBusquedaUnidades(IN idAlcaldiainput int)  RETURNS TABLE(vehicle_label varchar(250)) AS $$
  BEGIN
    RETURN QUERY
    SELECT    inf.vehicle_label 
    FROM alcaldias AS al, informacion AS inf
    WHERE ST_Contains(al.geometryAlcaldia, inf.geographic_point) and al.idAlcaldia::integer = idAlcaldiainput;
       
END;
$$ LANGUAGE plpgsql;