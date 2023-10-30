SELECT 
 (COUNT(DISTINCT Diagnostico) / COUNT(Diagnostico)) as Media_Diagnosticos
FROM Atendimento
WHERE Tipo_Atendimento = 'U'
