CREATE TABLE `like` (
    id int(11) NOT NULL AUTO_INCREMENT,
    user_id int(11) NOT NULL,
    property_id int(11) NOT NULL,
    is_active tinyint(1) NOT NULL,
    liked_at datetime(6) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (property_id) REFERENCES property(id)
);
