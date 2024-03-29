PGDMP      "                |            otopark    14.5 (Debian 14.5-1.pgdg110+1)     16.2 (Ubuntu 16.2-1.pgdg20.04+1)     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    51970    otopark    DATABASE     r   CREATE DATABASE otopark WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE otopark;
                postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false                       0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    4            �            1259    51976    abone    TABLE     �   CREATE TABLE public.abone (
    abone_id bigint NOT NULL,
    abone_name "char" NOT NULL,
    abone_plate bigint NOT NULL,
    abone_car bigint NOT NULL,
    abone_date date NOT NULL,
    abone_park bigint NOT NULL
);
    DROP TABLE public.abone;
       public         heap    postgres    false    4            �            1259    51986    camera    TABLE     w   CREATE TABLE public.camera (
    camera_id bigint NOT NULL,
    camera_coordinate "char",
    camera_active boolean
);
    DROP TABLE public.camera;
       public         heap    postgres    false    4            �            1259    51991    park    TABLE     �   CREATE TABLE public.park (
    park_id bigint NOT NULL,
    park_car "char",
    park_plate "char",
    park_door1 boolean,
    park_door2 boolean,
    park_input date,
    park_output date
);
    DROP TABLE public.park;
       public         heap    postgres    false    4            �            1259    51981    plate    TABLE     �   CREATE TABLE public.plate (
    plate_id bigint NOT NULL,
    plate_name "char" NOT NULL,
    plate_abone boolean,
    plate_situation boolean,
    plate_park boolean
);
    DROP TABLE public.plate;
       public         heap    postgres    false    4            �            1259    51971    users    TABLE     �   CREATE TABLE public.users (
    user_id bigint NOT NULL,
    user_name "char" NOT NULL,
    user_passw "char" NOT NULL,
    user_abone boolean,
    user_plate boolean,
    user_car boolean
);
    DROP TABLE public.users;
       public         heap    postgres    false    4                      0    51976    abone 
   TABLE DATA           e   COPY public.abone (abone_id, abone_name, abone_plate, abone_car, abone_date, abone_park) FROM stdin;
    public          postgres    false    210   �                 0    51986    camera 
   TABLE DATA           M   COPY public.camera (camera_id, camera_coordinate, camera_active) FROM stdin;
    public          postgres    false    212                    0    51991    park 
   TABLE DATA           n   COPY public.park (park_id, park_car, park_plate, park_door1, park_door2, park_input, park_output) FROM stdin;
    public          postgres    false    213   7                 0    51981    plate 
   TABLE DATA           _   COPY public.plate (plate_id, plate_name, plate_abone, plate_situation, plate_park) FROM stdin;
    public          postgres    false    211   T                 0    51971    users 
   TABLE DATA           a   COPY public.users (user_id, user_name, user_passw, user_abone, user_plate, user_car) FROM stdin;
    public          postgres    false    209   q       q           2606    51980    abone abone_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.abone
    ADD CONSTRAINT abone_pkey PRIMARY KEY (abone_id);
 :   ALTER TABLE ONLY public.abone DROP CONSTRAINT abone_pkey;
       public            postgres    false    210            u           2606    51990    camera camera_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.camera
    ADD CONSTRAINT camera_pkey PRIMARY KEY (camera_id);
 <   ALTER TABLE ONLY public.camera DROP CONSTRAINT camera_pkey;
       public            postgres    false    212            w           2606    51995    park park_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.park
    ADD CONSTRAINT park_pkey PRIMARY KEY (park_id);
 8   ALTER TABLE ONLY public.park DROP CONSTRAINT park_pkey;
       public            postgres    false    213            s           2606    51985    plate plate_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.plate
    ADD CONSTRAINT plate_pkey PRIMARY KEY (plate_id);
 :   ALTER TABLE ONLY public.plate DROP CONSTRAINT plate_pkey;
       public            postgres    false    211            o           2606    51975    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    209                  x������ � �            x������ � �            x������ � �            x������ � �            x������ � �     