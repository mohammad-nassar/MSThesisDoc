-- Start of DDL Script for Table LRT.LRT_EXAM_DETAILS
-- Generated 11-Jun-2020 17:00:03 from LRT@ORCLM

CREATE TABLE lrt_exam_details
    (detail_id                      NUMBER(4,0) ,
    exam_id                        NUMBER(3,0),
    template_id                    NUMBER(2,0),
    id                             NUMBER(10,0),
    word_id                        NUMBER(10,0),
    item                           VARCHAR2(20 BYTE),
    real_answer                    CHAR(1 BYTE),
    student_result                 CHAR(1 BYTE),
    type                           CHAR(20 BYTE),
    attribute_4                    VARCHAR2(20 BYTE),
    attribute_5                    VARCHAR2(20 BYTE))
  SEGMENT CREATION IMMEDIATE
  PCTFREE     10
  INITRANS    1
  MAXTRANS    255
  TABLESPACE  users
  STORAGE   (
    INITIAL     65536
    NEXT        1048576
    MINEXTENTS  1
    MAXEXTENTS  2147483645
  )
  NOCACHE
  MONITORING
  NOPARALLEL
  LOGGING
/





-- Constraints for LRT_EXAM_DETAILS

ALTER TABLE lrt_exam_details
ADD CONSTRAINT lrt_exam_details_con PRIMARY KEY (detail_id)
USING INDEX
  PCTFREE     10
  INITRANS    2
  MAXTRANS    255
  TABLESPACE  users
  STORAGE   (
    INITIAL     65536
    NEXT        1048576
    MINEXTENTS  1
    MAXEXTENTS  2147483645
  )
/


-- Triggers for LRT_EXAM_DETAILS

CREATE OR REPLACE TRIGGER lrt_exam_dt_trg
 BEFORE
  INSERT
 ON lrt_exam_details
REFERENCING NEW AS NEW OLD AS OLD
 FOR EACH ROW
BEGIN
  SELECT lrt_exam_dtl_seq.nextval
  INTO :new.detail_id
  FROM dual;
END;
/


-- End of DDL Script for Table LRT.LRT_EXAM_DETAILS

