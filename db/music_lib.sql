DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
-- artist is created first since we can't reference something not yet created in albums as a foreign key
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id) ON DELETE CASCADE
                                                    -- ^ if artists is deleted then albums is deleted as consequence or in cascade
);
