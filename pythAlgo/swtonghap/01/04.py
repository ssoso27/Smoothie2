SELECT DISTINCT PROFESSOR.NAME, COURSE.NAME
    FROM PROFESSOR
        INNER JOIN SCHEDULE
        ON PROFESSOR.ID = SCHEDULE.PROFESSOR_ID
        INNER JOIN COURSE
        ON SCHEDULE.COURSE_ID = COURSE.ID
    WHERE
        PROFESSOR.DEPARTMENT_ID != COURSE.DEPARTMENT_ID;