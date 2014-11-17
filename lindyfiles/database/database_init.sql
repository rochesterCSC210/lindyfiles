
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    username    VARCHAR(100),
    password    VARCHAR(100),
    fname       VARCHAR(100),
    email       VARCHAR(200),
    picture     VARCHAR(100),
    leader      BOOLEAN,
    follower    BOOLEAN,
    sessid      VARCHAR(100),
    PRIMARY KEY (email)
);

DROP TABLE IF EXISTS pros;
CREATE TABLE pros (
    fname       VARCHAR(100),
    lname       VARCHAR(100),
    picture     VARCHAR(100),
    leader      BOOLEAN,
    follower    BOOLEAN,
    teacher     BOOLEAN,
    website     VARCHAR(100),
    organization VARCHAR(100),
    organization_website     VARCHAR(100),
    PRIMARY KEY (fname, lname)
);

.separator ,
.import Pro_Dancers.csv

DROP TABLE IF EXISTS events;
CREATE TABLE events (
    id              MEDIUMINT NOT NULL AUTO_INCREMENT,
    name            VARCHAR(100) NOT NULL,
    start_date		DATE,
    end_date		DATE,
    social_dance    BOOLEAN,
    workshop        BOOLEAN,
    competition     BOOLEAN,
    starting_price	SMALLMONEY,
    city            VARCHAR(100),
    state           VARCHAR(100),
    host			VARCHAR(100),
    website         VARCHAR(100),
    PRIMARY KEY  (name, start_date)
);     

.separator ,
.import Swing_Dance_Events.csv