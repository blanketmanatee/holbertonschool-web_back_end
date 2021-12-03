--script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
--script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |
CREATE procedure ComputeAverageWeightedScoreForUser(
    user_id INT)
BEGIN
    UPDATE users AS U,
        (SELECT U.id, SUM(score * weight) / SUM(weight) AS w_avg
        FROM users AS U
        JOIN corrections as C ON U.id=C.user_id
        JOIN projects as P on C.project_id=P.id
        GROUP BY U.id)
    AS WA
    SET U.average_score = WA.w_avg
    WHERE U.id=WA.id;
END;
|