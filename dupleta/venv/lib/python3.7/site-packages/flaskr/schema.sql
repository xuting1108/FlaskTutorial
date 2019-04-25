DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

-- not null = torna a informação obrigatória
-- unique = a informação será unica
-- autoincrement = sempre +1

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT, --chave primaria
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id) --chave estrangeira
);