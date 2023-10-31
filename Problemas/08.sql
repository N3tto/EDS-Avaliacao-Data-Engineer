SELECT 
 AVG(COUNT(DISTINCT Diagnostico)) as Media_Diagnosticos
FROM Atendimento
WHERE Tipo_Atendimento = 'U'
