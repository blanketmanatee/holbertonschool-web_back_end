--script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |
CREATE procedure ComputeAverageWeightedScoreForUser(
    user_id INT)
BEGIN
    DECLARE w_avg_score FLOAT;
    SET w_avg_score = (SELECT SUM(score * weight) / SUM(weight)
    FROM users AS U
    JOIN corrections as C ON U.id=C.user_id
    JOIN projects as P on C.project_id=P.id
    WHERE U.id=user_id);
UPDATE users SET average_score = w_avg_score WHERE id=user_id;
END;
|