SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE '% DIAB1%'   -- DIAB1 is preceded by a space
   OR conditions LIKE 'DIAB1%'     -- DIAB1 is at the beginning
