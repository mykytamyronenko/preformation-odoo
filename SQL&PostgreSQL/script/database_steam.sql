-- \c postgres

-- DROP DATABASE IF EXISTS pfo_games WITH (FORCE)
-- CREATE DATABASE pfo_games

-- \c pfo_games

-- Besoin de ligne de commande
-- psql -U postgres -f ./scripts/pfo_games_database.sql
-- alt + shift + f

DROP TABLE IF EXISTS users, profile, publisher, games, review, users_games;

create table users(
    id INT GENERATED ALWAYS AS IDENTITY,
    username varchar(100) not null,
    email varchar(320) not null,
    country varchar(50),
    created_at TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT uk_username UNIQUE (username),
    CONSTRAINT uk_email UNIQUE (email),

    CONSTRAINT ck_users_username_length CHECK (LENGTH(username) >= 3),
    CONSTRAINT ck_users_email_format CHECK (email ~* '^[A-Z0-9._+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$')
);


create table profile(
    id INT GENERATED ALWAYS AS IDENTITY,
    bio text,
    avatar VARCHAR(100),
    dob date not null,

    users_id int not null,

    CONSTRAINT pk_profile PRIMARY KEY(id),
    CONSTRAINT fk_profile_users FOREIGN KEY (users_id)
        REFERENCES users (id) on delete cascade on update cascade
);

CREATE table publisher(
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(100) not null,
    country VARCHAR(100) not null,


    CONSTRAINT pk_publisher PRIMARY KEY(id)
);

CREATE TABLE games(
    id INT GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(200) not null,
    price MONEY not null,
    release_date date not null,

    publisher_id int not null,

    CONSTRAINT pk_games PRIMARY KEY(id),
    CONSTRAINT uk_title unique (title),
    CONSTRAINT ck_price CHECK (price >= 0::MONEY),
    CONSTRAINT fk_games_publisher FOREIGN KEY (publisher_id)
        REFERENCES publisher (id)
);

create TABLE review(
    id INT GENERATED ALWAYS AS IDENTITY,
    rating smallint not null,
    comment TEXT not null,
    creation_date TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,

    users_id int not null,
    game_id int not null,

    CONSTRAINT pk_review PRIMARY KEY (id),
    CONSTRAINT fk_review_users FOREIGN KEY (users_id)
        references users (id) on delete cascade,
    CONSTRAINT fk_review_games FOREIGN KEY (game_id)
        references games (id) on delete cascade,
    CONSTRAINT ck_rating CHECK (rating BETWEEN 0 and 5)
);

create table users_games(
    users_id int not null,
    game_id int not null,
    hours_played int not null,
    purchase_date date not null,


    CONSTRAINT pk_users_games PRIMARY key (users_id, game_id),
    CONSTRAINT fk_users_games_users FOREIGN KEY (users_id)
        REFERENCES users (id) on delete cascade,
    CONSTRAINT fk_users_games_games FOREIGN KEY (game_id)
        REFERENCES games (id) on delete cascade,
    CONSTRAINT ck_hours_played CHECK (hours_played >= 0)
);

--
-- Peuplement de la base de données
--

INSERT INTO users (username, email, country) VALUES
('Davit', 'davit@test.com', 'Belgium'),
('Sarah', 'sarah@test.com', 'France'),
('Lucas', 'lucas@test.com', 'Belgium'),
('Emma', 'emma@test.com', 'Canada'),
('Noah', 'noah@test.com', 'Germany'),
('Lina', 'lina@test.com', 'Belgium'),
('Tom', 'tom@test.com', 'USA'),
('Julie', 'julie@test.com', 'France'),
('Alex', 'alex@test.com', 'USA'),
('Mike', 'mike@test.com', 'UK');

INSERT INTO profile (users_id, bio, avatar, dob) VALUES
(1, 'Metalhead and Souls fan', 'avatar1.png', '2002-03-02'),
(2, 'Competitive FPS player', 'avatar2.png', '1998-07-10'),
(3, 'Indie games lover', 'avatar3.png', '2001-11-15'),
(4, 'Streamer and content creator', 'avatar4.png', '1999-01-20'),
(5, 'Hardcore RPG gamer', 'avatar5.png', '1995-05-05');

INSERT INTO publisher (name, country) VALUES
('FromSoftware', 'Japan'),
('CD Projekt', 'Poland'),
('Valve', 'USA'),
('Rockstar Games', 'USA'),
('Riot Games', 'USA'),
('Activision', 'USA'),
('Naughty Dog', 'USA'),
('Mojang', 'Sweden'),
('Epic Games', 'USA');

INSERT INTO games (title, price, release_date, publisher_id) VALUES
('Elden Ring', 59.99, '2022-02-25', 1),
('Dark Souls 3', 39.99, '2016-04-12', 1),
('Cyberpunk 2077', 49.99, '2020-12-10', 2),
('Counter Strike 2', 0.00, '2023-09-27', 3),
('GTA V', 29.99, '2013-09-17', 4),
('League of Legends', 0.00, '2009-10-27', 5),
('Call of Duty MW3', 79.99, '2023-11-10', 6),
('The Last of Us', 69.99, '2022-09-02', 7),
('Minecraft', 26.95, '2011-11-18', 8),
('Fortnite', 0.00, '2017-07-21', 9),
('Red Dead Redemption 2', 59.99, '2018-10-26', 4);

INSERT INTO users_games (users_id, game_id, hours_played, purchase_date) VALUES
(1, 1, 220, '2024-01-10'),
(1, 4, 450, '2023-11-01'),
(1, 5, 180, '2022-08-20'),

(2, 3, 95, '2024-03-15'),
(2, 6, 800, '2020-06-01'),
(2, 7, 120, '2024-01-20'),

(3, 2, 140, '2023-07-22'),
(3, 9, 300, '2022-12-05'),

(4, 8, 40, '2024-04-18'),
(4, 11, 110, '2024-01-03'),

(5, 1, 350, '2024-02-11'),
(5, 8, 70, '2024-03-10'),

(6, 10, 500, '2021-07-14'),
(6, 6, 1000, '2019-09-09'),

(7, 4, 1300, '2021-06-01'),

(8, 3, 35, '2024-05-02'),

(9, 5, 220, '2022-10-10'),

(10, 9, 600, '2020-05-05');

INSERT INTO review (users_id, game_id, rating, comment) VALUES
(1, 1, 5, 'Absolute masterpiece'),
(2, 6, 4, 'Still addictive after years'),
(3, 2, 5, 'Amazing boss fights'),
(4, 11, 5, 'Best story ever'),
(5, 1, 5, 'Fantastic exploration'),
(6, 10, 4, 'Very fun with friends'),
(7, 4, 5, 'Competitive and intense'),
(8, 3, 3, 'Good but buggy'),
(9, 5, 5, 'Classic game'),
(10, 9, 5, 'Infinite creativity');

INSERT INTO users (username, email, country) VALUES
('Nina', 'nina@test.com', 'Belgium'),
('Oscar', 'oscar@test.com', 'Spain'),
('Yuki', 'yuki@test.com', 'Japan'),
('Maya', 'maya@test.com', 'USA'),
('Chris', 'chris@test.com', 'UK');

INSERT INTO profile (users_id, bio, avatar, dob) VALUES
(11, NULL, NULL, '2000-06-12'),
(12, 'Casual gamer', NULL, '1997-09-30'),
(13, 'JRPG and Souls enjoyer', 'avatar13.png', '1996-02-14');

INSERT INTO publisher (name, country) VALUES
('Ubisoft', 'France');

INSERT INTO games (title, price, release_date, publisher_id) VALUES
('Bloodborne', 19.99, '2015-03-24', 1),
('Sekiro', 59.99, '2019-03-22', 1),
('Bully', 14.99, '2006-10-17', 4),
('Valorant', 0.00, '2020-06-02', 5),
('Warzone', 0.00, '2020-03-10', 6),
('Uncharted 4', 39.99, '2016-05-10', 7),
('Hades', 24.99, '2020-09-17', 3),
('Portal 2', 9.99, '2011-04-19', 3);

INSERT INTO users_games (users_id, game_id, hours_played, purchase_date) VALUES

(1, 6, 120, '2020-01-12'),
(1, 7, 240, '2024-02-01'),
(1, 9, 90, '2021-04-10'),
(1, 12, 160, '2022-02-02'),
(1, 15, 80, '2023-04-04'),

(2, 4, 300, '2023-09-28'),
(2, 10, 900, '2018-08-08'),
(2, 15, 450, '2022-07-07'),
(2, 16, 700, '2021-02-02'),

(3, 4, 150, '2023-10-01'),
(3, 6, 500, '2020-03-03'),
(3, 10, 250, '2018-01-01'),
(3, 15, 200, '2021-01-01'),
(3, 16, 100, '2022-05-05'),

(4, 18, 60, '2020-11-11'),

(5, 12, 400, '2022-06-06'),
(5, 13, 180, '2023-03-03'),

(6, 4, 700, '2023-11-11'),
(6, 16, 350, '2022-10-10'),
(6, 17, 40, '2024-04-04'),

(7, 6, 1200, '2019-09-09'),
(7, 16, 850, '2020-04-04'),

(8, 11, 100, '2023-08-08'),
(8, 14, 40, '2023-01-01'),

(9, 1, 150, '2024-01-01'),
(9, 3, 90, '2024-02-02'),
(9, 4, 300, '2024-03-03'),
(9, 6, 600, '2024-04-04'),
(9, 7, 80, '2024-05-05'),

(12, 17, 25, '2024-06-06'),

(13, 1, 500, '2024-01-01'),
(13, 2, 350, '2024-01-02'),
(13, 12, 250, '2024-01-03'),
(13, 13, 300, '2024-01-04'),

(14, 5, 70, '2024-02-02'),
(14, 8, 30, '2024-03-03'),

(15, 18, 10, '2024-05-05');

INSERT INTO review (users_id, game_id, rating, comment) VALUES
(1, 7, 4, 'Fun but sweaty'),
(1, 9, 5, 'Blocky perfection'),
(2, 4, 5, 'Best competitive FPS'),
(2, 10, 4, 'Chaotic but fun'),
(3, 6, 4, 'Still toxic but addictive'),
(4, 18, 5, 'Beautiful adventure'),
(5, 12, 5, 'Gothic masterpiece'),
(5, 13, 5, 'Parry god simulator'),
(6, 17, 5, 'Insane roguelike'),
(7, 16, 4, 'Battle royale classic'),
(8, 14, 4, 'Old but gold'),
(9, 3, 4, 'Much better now'),
(9, 7, 2, 'Too expensive for what it is'),
(12, 17, 5, 'Perfect indie game'),
(13, 1, 5, 'Peak fantasy RPG'),
(14, 5, 5, 'Still iconic'),
(15, 6, 1, 'Not my thing');


-- EXERCICES
-- SQL Exercises — Gaming Platform

-- 1.
-- Display all users.
Select * From users;
---

-- 2.
-- Display only the usernames and countries of all users.
select username, country from users;
---

-- 3.
-- Display all games.
select * from games;
---

-- 4.
-- Display only the title and price of all games.
select title, price from games;
---

-- 5.
-- Display all games that cost more than 40€.
select * from games where price > 40::money;
---

-- 6.
-- Display all games that cost less than 50€.
select * from games where price < 50::money;
---

-- 7.
-- Display all free games.
select * from games where price = 0::money;
---

-- 8.
-- Display all users coming from Belgium.
select * from users where country = 'Belgium';
---

-- 9.
-- Display all users who are not from Belgium.
select * from users where country != 'Belgium';
---

-- 10.
-- Display all publishers from the USA.
select * from publisher where country = 'USA';
---

-- 11.
-- Display all games released after 2020.
select * from games where release_date > '2020-12-31';
---

-- 12.
-- Display all games released before 2020.
select * from games where release_date < '2020-01-01';
---

-- 13.
-- Display all games ordered by price in descending order.
select * from games ORDER BY price desc;
---

-- 14.
-- Display all games ordered by release date from newest to oldest.
select * from games ORDER BY release_date desc;
---

-- 15.
-- Display all usernames ordered alphabetically.
select username from users ORDER BY username;
---

-- 16.
-- Display all games whose title contains "Dark".
select * from games where title ILIKE '%DARK%';
---

-- 17.
-- Display all games whose title starts with "C".
select * from games where title ILIKE 'C%';
---

-- 18.
-- Display all users whose username contains the letter "a".
select * from users where username ILIKE '%a%';
---

-- 19.
-- Display all reviews with a rating of 5.
select * from review where rating = 5;
---

-- 20.
-- Display all reviews created after `2024-01-01`.
select * from review where creation_date > '2024-01-01';
---

-- 21.
-- Display all games with a price between 20€ and 60€.
select * from games where price between 20::money and 60::money;
---

-- 22.
-- Display all users coming from Belgium or France.
select * from users where country = 'Belgium' or country = 'France';
select * from users where country IN ('Belgium', 'France');
---

-- 23.
-- Display all games that are not free.
select * from games where price > 0::money;
---

-- 24.
-- Display all games ordered alphabetically by title.
select * from games ORDER BY title;
---

-- 25.
-- Display all publishers ordered alphabetically.
select * from publisher ORDER BY name;
---

-- 26.
-- Display all games where the title ends with "2".
select * from games where title LIKE '%2';
---

-- 27.
-- Display all users created after a specific date.
select * from users where created_at > '2026-10-09 12:01:30';
---

-- 28.
-- Display all games released between 2015 and 2022.
select * from games where release_date between '2015-01-01' and '2022-12-31';
---

-- 29.
-- Display all reviews where the comment contains the word "best".
select * from review where comment ilike '%best%';
---

-- 30.
-- Display all games whose price is exactly 59.99€.
select * from games where price = 59.99::money;



-- # SQL Exercises — Gaming Platform
-- ## Functions, Aggregations, GROUP BY / HAVING

-- 1. Display all usernames in uppercase.

select UPPER(username) from users;

-- 2. Display each username with its length.

select username,char_length(username) "username_length" from users;
select username,length(username) "username_length" from users;

-- 3. Display each game with its release year.

select title, release_date from games;
select title, extract(year from release_date) from games;

-- 4. Display profiles and replace NULL bio with 'No bio yet'.

select id, coalesce(bio, 'No bio yet') as "bio", avatar, dob, users_id from profile;

SELECT
    id,
    users_id,
    case
        when bio is null then 'no bio yet'
        else bio
    end "bio"
from profile;

-- 5. Display each game with a price label: Free or Paid.

select *,
case price
    when 0::money then 'Free'
    else 'Paid'
end as "price_label"
from games;

select 
    title,
    release_date,
    price,
    case price
        when 0::money then 'Free'
        else 'Paid'
    end as "price_label"
from games;

-- 6. Display the total number of users.

select count(id) from users;

-- 7. Display the total number of games.

select count(id) from games;

-- 8. Display the average game price.

select avg(price::NUMERIC) as "average_price" from games;
select round(avg(price::NUMERIC),2) as "average_price" from games;

-- 9. Display the total number of hours played.

select sum(hours_played) as "total_hours_played" from users_games;

-- 10. Display the highest and lowest rating.

select max(rating) as "best_rating", min(rating) as "worst_rating" from review;

select
    min(rating) as "lowest",
    max(rating) as "highest"
from review;

-- 11. Display the number of users per country.

select country, count(id) "number_users_country"
from users
GROUP BY country
order by country;

-- 12. Display the number of games per publisher_id.

select  publisher_id, count(id) "number_game_publisher"
from games
GROUP BY publisher_id
ORDER BY publisher_id;

-- 13. Display the average game price per publisher_id.

select publisher_id, round(avg(price::NUMERIC),2) "average_game_price"
from games
GROUP BY publisher_id
ORDER BY publisher_id;

-- 14. Display the total hours played per user_id.

select users_id, sum(hours_played) "total_hours_played"
from users_games
GROUP BY users_id
having sum(hours_played) > 50 -- l'alias ne fonctionne pas ici, car having se fait avant le select
ORDER BY "total_hours_played" desc; -- l'alias fonctionne ici

-- 15. Display the average hours played per user_id.

select users_id, round(AVG(hours_played),2) "average_hours_played"
from users_games
GROUP BY users_id
ORDER BY "average_hours_played" desc;

-- 16. Display the total hours played per game_id.

select game_id, sum(hours_played)
from users_games
GROUP BY game_id
ORDER BY game_id;

-- 17. Display the average rating per game_id.

SELECT game_id, round(avg(rating))
from review
GROUP BY game_id
ORDER BY avg(rating) desc;

-- 18. Display the number of purchases per year.

SELECT extract(year from purchase_date) as "year", count(game_id) "game_purchased"
from users_games
GROUP BY extract(year from purchase_date)
ORDER BY extract(year from purchase_date);

SELECT extract(year from purchase_date) as "year", count(*) "game_purchased"
from users_games
GROUP BY extract(year from purchase_date);

-- 19. Display the number of games released per year.

select extract(year from release_date) "year", count(id) "game_released"
from games
GROUP BY EXTRACT(year from release_date)
ORDER BY EXTRACT(year from release_date);

select extract(year from release_date) "year", count(id) "count_game_released"
from games
GROUP BY EXTRACT(year from release_date)
ORDER BY year desc;

-- 20. Display the number of games per price category:
-- - Free if price = 0
-- - Cheap if price < 30
-- - Standard if price between 30 and 60
-- - Expensive if price > 60

SELECT
CASE
    when price = 0::money then 'Free'
    when price < 30::money then 'Cheap'
    when price BETWEEN 30::money and 60::money then 'Standard'
    when price > 60::money then 'way too much'
end as price_category,
count(id) as "Number_of_games"
from games
GROUP BY price_category;

SELECT
CASE
    when price = 0::money then 'Free'
    when price < 30::money then 'Cheap'
    when price <= 60::money then 'Standard'
    else 'way too much'
end as "price_category",
count(price) as "Number_of_games"
from games
GROUP BY "price_category";

SELECT
CASE
    when price = 0::money then 'Free'
    when price < 30::money then 'Cheap'
    when price <= 60::money then 'Standard'
    else 'way too much'
end as "price_category",
count(price) as "Number_of_games"
from games
GROUP BY CASE
        when price = 0::money then 'Free'
        when price < 30::money then 'Cheap'
        when price <= 60::money then 'Standard'
        else 'way too much'
    end;

-- 21. Display the number of paid games per publisher_id.

select publisher_id, count(id) as "number_of_free_games"
from games
where price != 0::money
group by publisher_id;

select publisher_id, count(id) as "number_of_free_games"
from games
where price > 0::money
group by publisher_id;

select publisher_id,
    sum(
        case
            when price = 0::money then 0
            else 1
        end
    ) as "count_paid_games"
from games
GROUP BY publisher_id;

select publisher_id, count(NULLIF(price, 0::money)) "count_paid_games"
from games
GROUP BY publisher_id;

-- 22. Display the average price per publisher_id for games released after '2015-01-01'.

SELECT publisher_id, round(avg(price::NUMERIC),2) "average_price"
from games
where release_date > '2015-01-01'
GROUP BY publisher_id;

-- 23. Display only countries that have more than 1 user.

select country, count(id) as "count"
from users
GROUP BY country
having count(id) > 1;

-- 24. Display only user_id values with more than 300 total hours played.

select users_id, sum(hours_played) as "total_hours_played"
from users_games
GROUP BY users_id
having sum(hours_played) >= 300;

-- 25. Display only game_id values with an average rating >= 4.5.

select game_id, round(avg(rating), 1) as "average_rating"
from review
GROUP BY game_id
having avg(rating) >= 4.5
ORDER BY game_id;






-- # SQL Exercises — Gaming Platform

-- ## JOINs and Advanced SELECT

-- ## Level 1 — Fundamentals


-- ### 1. Games and publishers

-- Display every game with its publisher.

-- Expected columns:

-- * `game_title`
-- * `publisher_name`

SELECT
    g.title "game_title",
    p.name "publisher"
from games g
    join publisher p on p.id = g.publisher_id;

-- ---

-- ### 2. Owned games

-- Display every game owned by a user.

-- Expected columns:

-- * `username`
-- * `game_title`
-- * `hours_played`

select
    u.username,
    g.title,
    ug.hours_played
from users_games ug
    join users u on u.id = ug.users_id
    join games g ON g.id = ug.game_id

-- ---

-- ### 3. Users and profiles

-- Display all users with their profile information.

-- Users without a profile must still appear.

-- Expected columns:

-- * `username`
-- * `bio`
-- * `avatar_url`

SELECT
    u.username,
    p.bio,
    p.avatar
from users u
    left join profile p on p.users_id = u.id;

-- ---

-- ### 4. Reviews

-- Display every review with the user and game information.

-- Expected columns:

-- * `username`
-- * `game_title`
-- * `rating`
-- * `comment`

SELECT
    u.username,
    g.title,
    r.rating,
    r.comment
from review r
    join users u ON u.id = r.users_id
    join games g ON g.id = r.game_id;

-- ---

-- ### 5. Publishers and games

-- Display all publishers with their games.

-- Publishers without games must still appear.

-- Expected columns:

-- * `publisher_name`
-- * `game_title`

SELECT
    p.name,
    g.title
from publisher p
    left join games g ON g.publisher_id = p.id;

-- ---

-- ### 6. Users without games

-- Display all users who have never bought a game.

-- Expected columns:

-- * `username`

SELECT
    u.username
from users u
    left join users_games ug ON ug.users_id = u.id
    where ug.purchase_date is null;



select username from users
except
select username from users u, users_games ug where u.id = ug.users_id;

-- ---

-- ### 7. Game purchases

-- Display all users with the games they own and the corresponding purchase date.

-- Expected columns:

-- * `username`
-- * `game_title`
-- * `purchase_date`

SELECT
    users.username,
    games.title,
    users_games.purchase_date
from users_games
    join users ON users.id = users_games.users_id
    join games ON games.id = users_games.game_id;

-- ---

-- ### 8. Games without purchases

-- Display all games that have never been purchased.

-- Expected columns:

-- * `game_title`

SELECT
    games.title
from games
    left join users_games ON users_games.game_id = games.id
    where users_games.purchase_date is null;

-- ---

-- ### 9. Number of players per game

-- Display every game with its total number of players.

-- Games without players must still appear.

-- Expected columns:

-- * `game_title`
-- * `total_players`

SELECT
    games.title,
    count(users_games.users_id) "total_players"
from games
    left join users_games ON users_games.game_id = games.id
    GROUP BY games.title;

-- ---

-- ### 10. Average rating per game

-- Display every reviewed game with its average rating.

-- Expected columns:

-- * `game_title`
-- * `average_rating`

SELECT
    games.title,
    round(avg(review.rating),1)
from games
    join review ON review.game_id = games.id
    GROUP BY games.title;

-- ---

-- ## Level 2 — Intermediate

-- ### 11. User activity summary

-- Display all users with the number of games they own and their total number of hours played.

-- Users without games must still appear.

-- Expected columns:

-- * `username`
-- * `games_owned`
-- * `total_hours_played`

select
    u.username,
    count(ug.game_id) "number_of_game",
    coalesce(sum(ug.hours_played), 0) "number_hours_played"
from users u
    left join users_games ug on ug.users_id = u.id
    group by u.id;

-- ---

-- ### 12. Publishers with several games

-- Display publishers that have published more than one game.

-- Expected columns:

-- * `publisher_name`
-- * `total_games`

select
    p.name "publisher",
    count(g.id) "number_of_games"
from games g
    join publisher p on p.id = g.publisher_id
    group by p.id
    having(count(g.id) > 1);

-- ---

-- ### 13. Highly played games

-- Display games for which the total number of hours played exceeds 500.

-- Expected columns:

-- * `game_title`
-- * `total_hours_played`

select
    g.title,
    sum(ug.hours_played)
from games g
    join users_games ug on ug.game_id = g.id
    group by g.title
    having sum(ug.hours_played) > 500; 

-- ---

-- ### 14. Active reviewers

-- Display users who have written more than one review.

-- Expected columns:

-- * `username`
-- * `reviews_written`

select
    u.username,
    count(r.users_id) "reviews_written"
from users u
    join review r on r.users_id = u.id
    group by u.username
    having(count(r.users_id) > 1);

-- ---

-- ### 15. Most-played games

-- Display the five games with the highest total number of hours played.

-- Expected columns:

-- * `game_title`
-- * `total_hours_played`

-- The most-played game must appear first.

select
    g.title,
    sum(ug.hours_played) total_hours_played
from games g
    join users_games ug on ug.game_id = g.id
    group by g.title
    order by total_hours_played desc
    limit 5;

-- ---

-- ## Level 3 — Advanced

-- ### 16. Detailed game review statistics

-- Display all games with their publisher and review statistics.

-- Games without reviews must still appear.

-- Expected columns:

-- * `game_title`
-- * `publisher_name`
-- * `total_reviews`
-- * `average_rating`

-- Order the result by average rating from highest to lowest.

select
    g.title "game_title",
    p.name "publisher_name",
    count(r.id) "total_reviews",
    round(avg(r.rating),1) "average_rating"
from games g
    join publisher p on p.id = g.publisher_id
    left join review r on r.game_id = g.id -- left s'applique sur publisher ET games
    group by g.title, p.name
    order by "average_rating" desc nulls last;

-- ---

-- ### 17. Complete user activity

-- Display all users with the number of games they own and the numbe
-- of reviews they have written.

-- Users without games or reviews must still appear.

-- Expected columns:

-- * `username`
-- * `games_owned`
-- * `reviews_written`

-- Be careful not to count the same game or review several times.

select
    u.username,
    count(distinct ug.game_id) "games_owned",
    count(distinct r.id) "reviews_written"
from users u
    left join users_games ug on ug.users_id = u.id
    left join review r on r.users_id = u.id
    group by u.username;

-- ---

-- ### 18. Users loyal to a publisher

-- Display every user who owns at least two games from the same publisher.

-- Expected columns:

-- * `username`
-- * `publisher_name`
-- * `games_owned_from_publisher`

select
    u.username,
    p.name "publisher_name",
    count(ug.game_id) "games_owned_from_publisher"
from users u
    join users_games ug on ug.users_id = u.id
    join games g on g.id = ug.game_id
    join publisher p on p.id = g.publisher_id
    group by u.username, p.name
    having count(ug.game_id) >= 2;

select
    u.username,
    p.name "publisher_name",
    count(p.id) "games_owned_from_publisher"
from users u
    join users_games ug on ug.users_id = u.id
    join games g on g.id = ug.game_id
    join publisher p on p.id = g.publisher_id
    group by u.id, p.name
    having count(p.id) >= 2;

-- ---

-- ### 19. Local publisher audiences

-- For each publisher, display the number of distinct players who come
-- from the same country as the publisher.

-- Publishers without matching players must still appear.

-- Expected columns:

-- * `publisher_name`
-- * `publisher_country`
-- * `local_players`

select
    p.name "publisher_name",
    p.country "publisher_country",
    count(distinct u.id) "local_players"
from publisher p
    left join games g on g.publisher_id = p.id
    left join users_games ug on ug.game_id = g.id
    left join users u on u.id = ug.users_id and u.country = p.country -- cool
    group by p.name, p.country;

-- ---

-- ### 20. Publishers ranked by playtime

-- Display all publishers with the total number of hours played across all their games.

-- Publishers whose games have never been played must still appear.

-- Expected columns:

-- * `publisher_name`
-- * `total_hours_played`

-- Order the result from the highest total playtime to the lowest.

select
    p.name publisher_name,
    sum(coalesce(ug.hours_played, 0)) "total_hours_played"
from publisher p
    left join games g on p.id = g.publisher_id
    left join users_games ug on ug.game_id = g.id
    group by p.name
    order by "total_hours_played" desc;


-- # SQL Exercises — Gaming Platform

-- ## Subqueries

-- A **subquery** is a `SELECT` written inside another query, between parentheses.
-- It can be used in the `WHERE`, `HAVING`, `SELECT` and `FROM` clauses.

-- * **Single value** subquery (one row, one column) → compare with `=`, `<`, `>`, …
-- * **List** subquery (one column, several rows) → use `IN`, `NOT IN`, `ANY`, `ALL`
-- * **Table** subquery (in the `FROM`) → must have an alias, or be written with `WITH` (CTE)
-- * **Correlated** subquery → references the outer query and is evaluated for each row
-- * `EXISTS` / `NOT EXISTS` → checks whether the subquery returns at least one row

-- The "Expected rows" line lets you check your result.

-- ---

-- ## Level 1 — Subqueries in `WHERE` (single value)

-- ### 1. Above-average games

-- Display all games that cost more than the average game price.

-- Expected columns:

-- * `title`
-- * `price`

-- Expected rows: 8

select title, price
from games
where price::numeric > (select avg(price::numeric) from games)
order by price desc;

-- ---

-- ### 2. Most expensive game

-- Display the most expensive game(s).

-- Expected columns:

-- * `title`
-- * `price`

-- Do not use `ORDER BY` + `LIMIT`: your query must still work if several games
-- share the highest price.

-- Expected rows: 1

select title, price
from games
where price = (select max(price) from games);

-- ---

-- ### 3. Same publisher as Elden Ring

-- Display all games published by the same publisher as "Elden Ring", except Elden Ring itself.

-- You only know the title of the game, not the publisher's id or name.

-- Expected columns:

-- * `title`
-- * `release_date`

-- Expected rows: 3

select title, release_date
from games
where publisher_id = (
    select publisher.id
    from publisher
    join games on games.publisher_id = publisher.id
    where games.title = 'Elden Ring' and publisher.id = games.publisher_id
) and title <> 'Elden Ring';

-- ---

-- ### 4. Lucas's compatriots

-- Display all users who come from the same country as Lucas, except Lucas himself.

-- Expected columns:

-- * `username`
-- * `country`

-- Expected rows: 3

select username, country
from users
where country = (
    select country
    from users
    where username = 'Lucas'
) and username <> 'Lucas';

-- ---

-- ### 5. Long gaming sessions

-- Display every owned game whose number of hours played is higher
-- than the average number of hours played
-- (across all purchases).

-- Expected columns:

-- * `username`
-- * `game_title`
-- * `hours_played`

-- Order the result from the highest number of hours played to the lowest.

-- Expected rows: 19

select
    u.username,
    g.title "game_title",
    ug.hours_played
from games g
join users_games ug on ug.game_id = g.id
join users u on u.id = ug.users_id
where ug.hours_played > (
    select avg(hours_played)
    from users_games
);

-- ---

-- ## Level 1 — Subqueries with `IN` / `NOT IN`

-- ### 6. Reviewers

-- Display all users who have written at least one review.

-- **No JOIN allowed.**

-- Expected columns:

-- * `username`

-- Expected rows: 14

select username
from users
where id in (
    select users_id
    from review
);

-- ---

-- ### 7. Games without reviews

-- Display all games that have never been reviewed.

-- **No JOIN allowed.**

-- Expected columns:

-- * `title`

-- Expected rows: 3

select title
from games
where id not in (
    select game_id
    from review
);

-- ---

-- ### 8. FromSoftware players

-- Display all users who own at least one game published by FromSoftware.

-- **No JOIN allowed:** you will need to nest several subqueries.

-- Expected columns:

-- * `username`

-- Expected rows: 5

select username
from users
where id in (
    select users_id
    from users_games
    where game_id in (
        select id
        from games
        where publisher_id in (
            select id
            from publisher
            where name = 'FromSoftware'
        )
    )
);

-- ---

-- ### 9. Users without a profile

-- Display all users who don't have a profile.

-- **No JOIN allowed.**

-- Expected columns:

-- * `username`

-- Expected rows: 7

select username
from users
where id not in (
    select users_id
    from profile
);

-- ---

-- ### 10. Publishers with local users

-- Display all publishers based in a country where at least one user lives.

-- Expected columns:

-- * `publisher_name`
-- * `country`

-- Expected rows: 8

select name "publisher_name", country
from publisher
where country in (
    select distinct country -- distinct préférable dans les IN ou NOT IN, pour l'opti
    from users
);

-- ---

-- ## Level 2 — Subqueries in `HAVING`, `SELECT` and `FROM`

-- ### 11. Premium publishers

-- Display publishers whose average game price is higher than the average price of all games.

-- Expected columns:

-- * `publisher_name`
-- * `average_price` (rounded to 2 decimals)

-- Expected rows: 5

select p.name "publisher_name", round(avg(g.price::numeric),2)
from publisher p
join games g on g.publisher_id = p.id
where g.price::numeric > (
    select avg(price::numeric)
    from games
) group by p.name;

-- ---

-- ### 12. Bigger communities than France

-- Display the countries that have more users than France.

-- Expected columns:

-- * `country`
-- * `total_users`

-- Expected rows: 2

select country, count(id) "total_users"
from users
group by country
having count(id) > (
    select count(id)
    from users
    where country = 'France'
    group by country
);

-- ---

-- ### 13. Price compared to the average

-- Display every game with its price, the average price of all games and the difference
-- between both.

-- Expected columns:

-- * `title`
-- * `price`
-- * `average_price` (rounded to 2 decimals)
-- * `price_difference` (rounded to 2 decimals, negative if the game is cheaper than the average)

-- Order the result from the highest difference to the lowest.

-- Expected rows: 19

select title, price,
(select round(avg(price::numeric),2) from games) "average_price",
price::numeric - (
    SELECT
    round(avg(price::numeric),2)
    from games
) "price_difference"
from games;

-- ---

-- ### 14. Library size without JOIN

-- Display every user with the number of games they own.

-- Users without games must still appear with `0`.

-- **No JOIN allowed:** use a subquery in the `SELECT`.

-- Expected columns:

-- * `username`
-- * `games_owned`

-- Expected rows: 15

SELECT username,
(select count(game_id)
from users_games
where users_id = id
) "games_owned"
from users order by games_owned desc;

-- ---

-- ### 15. Average library size

-- Display the average number of games owned per user.

-- Only users who own at least one game are taken into account.

-- Expected columns:

-- * ` ` (rounded to 2 decimals)

-- Write it twice: once with a subquery in the `FROM`, once with a CTE (`WITH`).

-- Expected rows: 1

select round(avg(count),2) "average_games_per_user"
from (SELECT users_id, count(game_id)
from users_games
where users_id in (SELECT
id from users)
group by users_id);

select round(avg(count),2) "average_games_per_user"
from (SELECT users_id, count(game_id)
from users_games
group by users_id);


with table_cte
as (
    SELECT users_id, count(game_id)
    from users_games
    where users_id in (SELECT
    id from users)
    group by users_id
)
select round(avg(count),2) "average_games_per_user" from table_cte;

-- ---

-- ### 16. Heavy players

-- Display users whose total number of hours played is higher than the **average total**
-- number of hours played per user.

-- Careful: this is not the same as the average of `hours_played`!

-- Expected columns:

-- * `username`
-- * `total_hours_played`

-- Order the result from the highest total to the lowest.

-- Expected rows: 7

with table_cte
as (
select username, sum(users_games.hours_played) "total_hours_played"
from users
join users_games ON users_games.users_id = users.id
where id in (SELECT users_id
from users_games)
GROUP BY username
)
select username, total_hours_played from table_cte where total_hours_played > (
    select avg(total_hours_played) "total_hours_played" from table_cte
)
order by total_hours_played desc;

-- ---

-- ## Level 3 — Correlated subqueries, `EXISTS`, `ANY` / `ALL`

-- ### 17. Flagship game of each publisher

-- Display the most expensive game(s) of each publisher.

-- If several games of the same publisher share the highest price, all of them must appear.

-- Expected columns:

-- * `publisher_name`
-- * `game_title`
-- * `price`

-- Expected rows: 11

select p.name "publisher_name", g.title "game_title", g.price
from games g
    join publisher p on p.id = g.publisher_id
where g.price >= all (
    select g2.price
    from games g2
    where g2.publisher_id = p.id
);

-- ---

-- ### 18. Favorite game of each user

-- Display, for each user, the game(s) they played the most.

-- Expected columns:

-- * `username`
-- * `game_title`
-- * `hours_played`

-- Expected rows: 14

select username, title, hours_played
from users u
join users_games ug on ug.users_id = u.id
join games g on g.id = ug.game_id
where hours_played >= all (select
hours_played
from users_games
where users_games.users_id = u.id)
order by username;

-- ---

-- ### 19. Better than the average player

-- Display every owned game where the user played more than the average number of hours played
-- **on that same game**.

-- Expected columns:

-- * `username`
-- * `game_title`
-- * `hours_played`
-- * `game_average_hours` (rounded to 2 decimals)

-- Expected rows: 24

select username,
title,
hours_played, 
(select
round(avg(hours_played),2)
from users_games where users_games.game_id = ug.game_id) "game_average_hours"
from users u
join users_games ug on ug.users_id = u.id
join games g on g.id = ug.game_id
where hours_played > (select avg(hours_played)
from users_games where users_games.game_id = ug.game_id
);

-- ---

-- ### 20. Publishers with recent games

-- Display publishers that have released at least one game after `2020-01-01`.

-- Use `EXISTS`.

-- Expected columns:

-- * `publisher_name`

-- Expected rows: 6

select name "publihser_name" from publisher p
where exists (select 1 from games g
where g.publisher_id = p.id and g.release_date > '2020-01-01');

-- ---

-- ### 21. Inactive users

-- Display users who have never bought a game.

-- Use `NOT EXISTS`.

-- Expected columns:

-- * `username`
-- * `country`

-- Expected rows: 1

select username, country
from users u
where not exists(select 1 from users_games ug where ug.users_id = u.id);

-- ---

-- ### 22. More expensive than every Valve game

-- Display games that cost more than **every** game published by Valve.

-- Use `ALL`.

-- Expected columns:

-- * `title`
-- * `price`

-- Expected rows: 10

select title, price
from games
where price > all (select price
from games
where publisher_id = (select id from publisher where name = 'Valve')
);

-- ---

-- ### 23. Cheaper than a FromSoftware game

-- Display games, **not** published by FromSoftware, that are cheaper than **at least one**
-- FromSoftware game.

-- Use `ANY`.

-- Expected columns:

-- * `title`
-- * `price`

-- Expected rows: 12

select title, price from games
where publisher_id <> (select id from publisher where name = 'FromSoftware')
and
price < any (select price from games where publisher_id = (select
id from publisher where name = 'FromSoftware'));

-- ---

-- ### 24. Completionists

-- Display users who own at least one game **and** have reviewed **every** game they own.

-- Hint: "every game they own is reviewed" means "there is no owned game without a review".

-- Expected columns:

-- * `username`

-- Expected rows: 2

select
u.username
from users u
where exists (
    select 1
    from users_games ug
    where ug.users_id = u.id
)
and not exists (
    select 1
    from users_games ug
    where ug.users_id = u.id
    and not exists (
        select 1
        from review r
        where r.users_id = u.id
            and r.game_id = ug.game_id
    )
);

-- ---

-- ### 25. Publishers above the average playtime

-- Using a CTE (`WITH`), display publishers whose total number of hours played
-- (across all their games)
-- is higher than the average total number of hours played per publisher.

-- Publishers whose games have never been played count as `0` in the average.

-- Expected columns:

-- * `publisher_name`
-- * `total_hours_played`

-- Order the result from the highest total playtime to the lowest.

-- Expected rows: 4

with publishers_hours as (
    select
        p.name publisher_name,
        coalesce(sum(ug.hours_played), 0) total_hours_played
    from publisher p
        join games g on g.publisher_id = p.id
        left join users_games ug on ug.game_id = g.id
    group by p.name
)

select 
    publisher_name,
    total_hours_played
from publishers_hours
where total_hours_played > (
    select avg(total_hours_played)
    from publishers_hours
)
order by total_hours_played desc;




-- # SQL Exercises — Gaming Platform

-- ## DML — INSERT, UPDATE, DELETE

-- ## How to work

-- Every exercise must be written **inside a transaction** and **cancelled at the end**,
-- so the data stays identical for the next exercise:

-- ```sql
-- BEGIN;

-- -- your INSERT / UPDATE / DELETE

-- -- a SELECT to check the result

-- ROLLBACK;
-- ```

-- Rules:

-- * Always check your modification with a `SELECT` **before** the `ROLLBACK`.
-- * If a statement fails, the transaction is aborted: every following statement
-- is refused until you run `ROLLBACK`.
-- * No hard-coded `id`: find the ids with a subquery
-- (`(SELECT id FROM users WHERE username = 'Davit')`).
-- * `RETURNING` displays the rows affected by an `INSERT`, `UPDATE` or `DELETE`:

-- ```sql
-- UPDATE games
-- SET price = 0
-- WHERE title = 'Minecraft'
-- RETURNING title, price;
-- ```

-- The "Expected" line gives the number of rows affected.

-- ---

-- ## Level 1 — INSERT

-- ### 1. New user

-- Add the user `Zelda` (`zelda@test.com`, Belgium).

-- Check that she exists, then cancel. Check again after the `ROLLBACK`.

-- Expected: 1 row inserted, 0 rows after the `ROLLBACK`.

-- ---

begin;
select * from users;

insert into users (username, email, country)
values ('Zelda', 'zelda@test.com', 'Belgium') returning *;

rollback;

-- ### 2. Several users at once

-- Add these 3 users **in a single statement**, and display their generated `id`,
-- `username` and `created_at`:

-- | username | email           | country |
-- | -------- | --------------- | ------- |
-- | Link     | link@test.com   | Japan   |
-- | Samus    | samus@test.com  | USA     |
-- | Kratos   | kratos@test.com | Greece  |

-- Question: run the exercise twice. Are the generated `id` values the same? Why?

-- Expected: 3 rows inserted.

begin;
select * from users;

insert into users (username, email, country)
values ('Link', 'link@test.com', 'Japan'),
        ('Samus', 'samus@test.com', 'USA'),
        ('Kratos', 'kratos@test.com', 'Greece') RETURNING *;

select * from users;
rollback;
-- id incrémenté malgré le rollback



-- ---

-- ### 3. New publisher and its first game

-- In the same transaction:

-- 1. add the publisher `Supergiant Games` (USA)
-- 2. add its game `Hades II` (29.99€, released on `2025-09-25`)

-- Display the game with the name and country of its publisher.

-- Expected: 1 + 1 rows inserted.

begin;
select * from publisher;
select * from games;

insert into publisher (name, country)
    values ('Supergiant Games', 'USA') returning *;

insert into games (title, price, release_date, publisher_id)
    values ('Hades II', 29.99, '2025-09-25',
    (select id from publisher where name = 'Supergiant Games')
    ) returning *;

select * from publisher;
select * from games;

select g.title, g.price, p.country, p.name
from games g
    join publisher p on g.publisher_id = p.id
where g.title = 'Hades II';

rollback;

-- ---

-- ### 4. A profile for Tom

-- Tom has no profile. Create one with the bio `Counter Strike addict`
-- and the birth date `1999-12-24`.

-- Constraint: use `INSERT ... SELECT` (no `VALUES`).

-- Expected: 1 row inserted.

BEGIN;
select * from profile;
insert into profile (bio, dob, users_id)
select 'Counter Strike addict', '1999-12-24', id from users where username = 'Tom' returning *;
select * from profile;

select
    u.username,
    p.bio,
    p.avatar,
    p.dob
from users u
    join profile p on u.id = p.users_id
where u.username = 'Tom';

ROLLBACK;

-- ---

-- ### 5. Breaking the constraints

-- Each insertion below **must fail**. For each one,
-- run it in its own transaction and explain which constraint blocks it.

-- a) A user named `Al`
-- b) A user with the email `albert.test.com`
-- c) A second user named `Davit`
-- d) A game that costs -10€
-- e) A review with a rating of 6
-- f) A purchase for the user with `id` 999
-- g) A user inserted with the `id` 100
-- h) Davit buys Elden Ring (again)
-- i) A review with the comment `Wow`

-- Question: why one transaction per insertion?

-- a) A user named `Al`
begin;
insert into users (username, email)
values ('Al', 'alb@alb.com') returning *;
ROLLBACK; -- contraintre username Longueur >= 3

-- b) A user with the email `albert.test.com`
begin;
insert into users (username, email, country)
values ('Albert', 'albert.test.com', 'Belgium') returning *;
ROLLBACK; -- format email

-- c) A second user named `Davit`
BEGIN;
INSERT INTO users (username, email, country)
VALUES ('Davit', 'davit@test.com', 'Belgium'); -- Unique constraint
ROLLBACK;

-- d) A game that costs -10€
BEGIN;
INSERT INTO games (title, price, publisher_id, release_date)
VALUES ('Severed steel', -10, 1, '2020-01-01'); -- check price
ROLLBACK;

-- e) A review with a rating of 6
BEGIN;
INSERT INTO review (users_id, game_id, rating, comment)
VALUES (1, 3, 6, 'Super'); -- ck_reviews_rating_range
ROLLBACK;

-- f) A purchase for the user with `id` 999
BEGIN;
INSERT INTO users_games (users_id, game_id, hours_played, purchase_date)
VALUES (999, 1, 0, CURRENT_DATE); -- fk_user_games_users
ROLLBACK;

-- g) A user inserted with the `id` 100
BEGIN;
INSERT INTO users (id, username, email, country)
VALUES (100, 'Quentin', 'quentin@test.com', 'Belgium');
-- DETAIL: Column "id" is an identity column defined as GENERATED ALWAYS.
ROLLBACK;

-- h) Davit buys Elden Ring (again)
BEGIN;
INSERT INTO users_games (users_id, game_id, hours_played, purchase_date)
VALUES (1, 1, 0, CURRENT_DATE);
ROLLBACK;

-- i) A review with the comment `Wow`
BEGIN;
INSERT INTO review(users_id, game_id, rating, comment)
VALUES (1, 1, 5, 'Wow'); -- ck_reviews_comment_length -- perso pas mis
ROLLBACK;

-- ---

-- ## Level 2 — UPDATE

-- ### 6. Mike moves

-- Mike now lives in Ireland.

-- Expected: 1 row updated.

begin;
select * from users;

update users
set country = 'Ireland'
where username = 'Mike'
returning old.*, new.*;

select * from users;
rollback;

-- ---

-- ### 7. FromSoftware sale

-- All FromSoftware games are 20% off. Round the new prices to 2 decimals and display the 
-- itles and new prices.

-- Expected: 4 rows updated.

begin;

update games
set price = round(price::numeric * 0.8, 2)::money
where publisher_id = (select id from publisher where name = 'FromSoftware')
returning title, price;

rollback;

-- ---

-- ### 8. Inflation

-- Games released since 2022 that cost more than 50€ get 10% more expensive
-- (rounded to 2 decimals).

-- Expected: 3 rows updated.

begin;

update games
set price = round(price::numeric * 1.1, 2)::money
where release_date >= '2022-01-01' and price::numeric > 50
returning title, release_date, price "new_price", old.price "old_price";

rollback;

-- ---

-- ### 9. Davit's gaming weekend

-- Davit played 50 more hours on **each** of his games.

-- Display Davit's total hours before and after the update, in the same transaction.

-- Expected: 8 rows updated, total from 1540 to 1940.

begin;

select
sum(hours_played) before_played
from users_games
where users_id = (select id from users where username = 'Davit');

update users_games
set hours_played = hours_played + 50
where users_id = (select id from users where username = 'Davit');

select
sum(hours_played) after_update
from users_games
where users_id = (select id from users where username = 'Davit');

rollback;

-- ---

-- ### 10. Fill the empty profiles

-- In a **single** `UPDATE`:

-- * profiles without bio get `No bio yet`
-- * profiles without avatar get `default.png`

-- The existing values must not change.

-- Expected: 2 rows updated.

begin;

update profile
set
    bio = coalesce(bio, 'no bio yet'),
    avatar = coalesce(avatar, 'default.png')
where bio is null or avatar is null
returning users_id, bio, avatar;

rollback;


-- ---

-- ### 11. New pricing policy

-- For all paid games:

-- * under 30€: +5€
-- * between 30€ and 60€: -10% (rounded to 2 decimals)
-- * above 60€: 59.99€

-- Free games stay free.

-- Constraint: a single `UPDATE`.

-- Expected: 14 rows updated.

BEGIN;

UPDATE games
SET price = CASE
    WHEN price < 30::money THEN price + 5::money
    WHEN price <= 60::money THEN ROUND(price::numeric * 0.9, 2)::money
    ELSE 59.99::money
END
WHERE price > 0::money
RETURNING title, price AS new_price;

ROLLBACK;

-- ---

-- ### 12. Verified owners

-- Add ` (verified owner)` at the end of the comment of every
-- review whose author owns the game **and** played it for at least 100 hours.

-- Expected: 17 rows updated.

-- ---

begin;

update review r
set comment = r.comment || ' (verified owner)'
where exists (
    select 1
    from users_games ug
    where ug.users_id = r.users_id
    and ug.game_id = r.game_id
    and ug.hours_played >= 100
)
returning r.users_id, r.game_id, r.comment;

rollback;

-- ### 13. The forgotten WHERE

-- Run this query, then display the number of users per country:

-- ```sql
-- UPDATE users
-- SET country = 'Belgium';
-- ```

-- What happened? Cancel, then check that the data is intact.
begin;
UPDATE users
SET country = 'Belgium';
select country, count(id) from users group by country;
rollback;
select country, count(id) from users group by country;

-- Expected: 15 rows updated.

-- ---

-- ## Level 3 — DELETE

-- ### 14. Chris's review

-- Delete Chris's review on League of Legends.

-- Expected: 1 row deleted.

begin;

delete from review
where users_id = (select id from users where username = 'Chris')
    and game_id = (select id from games where title = 'League of Legends')
returning *;

rollback;

-- ---

-- ### 15. Reviews from non-owners

-- Delete every review written by a user who does not own the game.

-- Constraint: the query must work for any user and any game (no names, no ids).

-- Expected: 1 row deleted.

begin;

delete from review r
where not exists (
    select 1
    from users_games ug
    where ug.users_id = r.users_id
    and ug.game_id = r.game_id
)
returning *;

rollback;

-- ---

-- ### 16. Lina deletes her account

-- Display the number of rows in `users`, `user_games` and `reviews`.
-- Delete Lina, then display the counts again.

-- What happened to her games and reviews? Which part of the table definitions explains it?

-- Expected: 1 user deleted — `users` 15 → 14, `user_games` 55 → 50, `reviews` 27 → 25.

-- ---

begin;

select
    (select count(*) from users) users,
    (select count(*) from users_games) users_games,
    (select count(*) from review) review;

delete from users
 where username = 'Lina';

select
    (select count(*) from users) users,
    (select count(*) from users_games) users_games,
    (select count(*) from review) review;

rollback;


-- ### 17. Deleting publishers

-- a) Delete Valve. What happens? Why?
-- b) Delete Ubisoft. Why does it work?

-- Expected: a) error, b) 1 row deleted.

-- ---

begin;

delete from publisher where name = 'Valve' returning *;

rollback;


begin;

delete from publisher where name = 'Ubisoft' returning *;

rollback;

-- ### 18. Ghost accounts

-- Delete the users who never bought **nor** reviewed anything.

-- Expected: 1 row deleted.

begin;

delete from users u
where not exists (select 1 from users_games ug where ug.users_id = u.id)
 and not exists (select 1 from review r where r.users_id = u.id)
returning *;

rollback;



begin;

delete from users u
where id not in (
    select users_id from users_games
    union
    select users_id from review
    )
returning *;

rollback;

-- ---

-- ### 19. Games nobody bought

-- Delete the games that have never been purchased.

-- Expected: 1 row deleted.

begin;

delete from games g
where not exists (select 1 from users_games ug where ug.game_id = g.id)
returning *;

rollback;

-- ---

-- ### 20. DELETE vs TRUNCATE

-- Empty the `reviews` table with `TRUNCATE`, count its rows, then cancel.

-- Questions:

-- * What is the difference between `DELETE FROM reviews;` and `TRUNCATE TABLE reviews;`?
-- * Can a `TRUNCATE` be cancelled in PostgreSQL?

begin;
truncate table review;
select count(*) from review;
rollback;
select count(*) from review;

-- ---

-- ## Level 4 — INSERT ... SELECT

-- ### 21. A profile for everyone

-- Create a profile for every user who doesn't have one yet,
-- with the bio `Hello, I am <username>`.

-- Check that no user is left without a profile.

-- Expected: 7 rows inserted.

begin;

insert into profile (users_id, bio, dob)
select id, 'Hello, I am ' || username, CURRENT_DATE
from users
where id not in (select users_id from profile)
returning users_id, bio;

select count(*) from users u
left join profile p on p.users_id = u.id
where p.id is null;

rollback;

-- ---

-- ### 22. Belgian gift

-- Every Belgian user receives `Portal 2` today, with 0 hours played,
-- unless they already own it.

-- Expected: 4 rows inserted.

begin;

insert into users_games (users_id, game_id, hours_played, purchase_date)
select
u.id,
(select id from games where title = 'Portal 2'),
0,
current_date
from users u
where u.country = 'Belgium'
and not exists (
    select 1
    from users_games ug
    join games g on g.id = ug.game_id
    where ug.users_id = u.id
    and g.title = 'Portal 2'
)
returning *;

rollback;

-- ---

-- ### 23. Statistics table

-- In a transaction:

-- 1. create a table `game_stats`
-- (`game_id` as primary key, `title`, `total_players`, `total_hours`, `avg_rating`)
-- 2. fill it with **one** `INSERT ... SELECT` covering all games
-- (`total_hours` = 0 for games never played)
-- 3. display it, sorted by total hours

-- After the `ROLLBACK`, try `SELECT * FROM game_stats;`. What happens?

-- Expected: 19 rows inserted.

begin;
-- création de la table
create table game_stats (
    game_id int,
    title varchar(100),
    total_players int,
    total_hours int,
    avg_rating numeric(3,2),
    constraint pk_game_stats primary key (game_id)
);
-- Insertion des statistiques
insert into game_stats -- toutes les colonnes
select
    g.id,
    g.title,
    (select count(*) from users_games ug where ug.game_id = g.id),
    (select coalesce(sum(ug.hours_played), 0) from users_games ug where ug.game_id = g.id),
    (select round(avg(r.rating), 2) from review r where r.game_id = g.id)
from games g;

select * from game_stats order by total_hours desc;
rollback;

select * from game_stats; -- la table n'existe plus

-- ---

-- ## Level 5 — Transactions

-- ### 24. Nina's first purchase

-- In a single transaction:

-- 1. Nina buys `Hades` today
-- 2. create a `SAVEPOINT`
-- 3. Nina reviews it with a rating of 7 and the comment `Best roguelike ever` → error
-- 4. go back to the `SAVEPOINT`
-- 5. insert the review again with a rating of 5
-- 6. check that Nina has 1 game and 1 review

-- Syntax:

-- ```sql
-- SAVEPOINT savepoint_name;
-- ROLLBACK TO SAVEPOINT savepoint_name;
-- ```

-- Question: without the `SAVEPOINT`, what would happen after the error?

-- ---

-- ### 25. A gift between friends

-- Davit gives his copy of Elden Ring to Nina:

-- * the game now belongs to Nina, with 0 hours played and today's purchase date
-- * Davit's review on Elden Ring is deleted

-- Display all the owners of Elden Ring with their hours and purchase date.

-- Constraint: no `INSERT`.

-- Expected: 1 row updated, 1 row deleted.

-- ---

-- ### 26. Account merge

-- Sarah and Julie are the same person. Merge Julie's account into Sarah's:

-- 1. for the games they **both** own: add Julie's hours to Sarah's
-- 2. Julie's other games are transferred to Sarah
-- 3. Julie's reviews are transferred to Sarah (only for games Sarah has not reviewed yet)
-- 4. Julie's account is deleted

-- Check at the end:

-- | sarah_games | sarah_reviews | cyberpunk_hours | julie |
-- | ----------- | ------------- | --------------- | ----- |
-- | 9           | 5             | 130             | 0     |

-- Question: why is the order of the steps important?
