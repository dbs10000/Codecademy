CREATE TABLE "sunlight_profiles" (
  "id" integer PRIMARY KEY,
  "sunlight_hours" varchar(20),
  "sun_position" varchar(10)
);

CREATE TABLE "rooms" (
  "id" integer PRIMARY KEY,
  "name" varchar(50),
  "sunlight_id" integer
);

CREATE TABLE "plants" (
  "id" integer PRIMARY KEY,
  "nickname" varchar(50),
  "species" varchar(100),
  "pot_size" varchar(20),
  "watering_method" varchar(20),
  "watering_instructions" text,
  "room_id" integer
);

CREATE TABLE "days_of_week" (
  "id" integer PRIMARY KEY,
  "day_name" varchar(10)
);

CREATE TABLE "plant_watering_schedules" (
  "plant_id" integer,
  "day_id" integer,
  PRIMARY KEY ("plant_id", "day_id")
);

ALTER TABLE "rooms" ADD FOREIGN KEY ("sunlight_id") REFERENCES "sunlight_profiles" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "plants" ADD FOREIGN KEY ("room_id") REFERENCES "rooms" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "plant_watering_schedules" ADD FOREIGN KEY ("plant_id") REFERENCES "plants" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "plant_watering_schedules" ADD FOREIGN KEY ("day_id") REFERENCES "days_of_week" ("id") DEFERRABLE INITIALLY IMMEDIATE;
