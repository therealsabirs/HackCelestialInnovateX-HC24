PGDMP      (    
            |            SSIH    16.4    16.4 T    U           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            V           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            W           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            X           1262    16969    SSIH    DATABASE     y   CREATE DATABASE "SSIH" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE "SSIH";
                postgres    false            �            1259    16970    alumni    TABLE     x  CREATE TABLE public.alumni (
    alumni_id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    contact_number character varying(20),
    password character varying(255) NOT NULL,
    passout_year integer,
    company character varying(100),
    role character varying(100),
    linkedin_profile character varying(255)
);
    DROP TABLE public.alumni;
       public         heap    postgres    false            �            1259    16975    alumni_alumni_id_seq    SEQUENCE     �   CREATE SEQUENCE public.alumni_alumni_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.alumni_alumni_id_seq;
       public          postgres    false    215            Y           0    0    alumni_alumni_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.alumni_alumni_id_seq OWNED BY public.alumni.alumni_id;
          public          postgres    false    216            �            1259    16976    answers    TABLE     �   CREATE TABLE public.answers (
    answer_id integer NOT NULL,
    question_id integer,
    alumni_id integer,
    answer_text text NOT NULL,
    answer_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.answers;
       public         heap    postgres    false            �            1259    16982    answers_answer_id_seq    SEQUENCE     �   CREATE SEQUENCE public.answers_answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.answers_answer_id_seq;
       public          postgres    false    217            Z           0    0    answers_answer_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.answers_answer_id_seq OWNED BY public.answers.answer_id;
          public          postgres    false    218            �            1259    17167    comments    TABLE     �  CREATE TABLE public.comments (
    comment_id integer NOT NULL,
    thread_id integer,
    user_id integer NOT NULL,
    user_type character varying(10) NOT NULL,
    comment_text text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT comments_user_type_check CHECK (((user_type)::text = ANY ((ARRAY['student'::character varying, 'faculty'::character varying, 'alumni'::character varying])::text[])))
);
    DROP TABLE public.comments;
       public         heap    postgres    false            �            1259    17166    comments_comment_id_seq    SEQUENCE     �   CREATE SEQUENCE public.comments_comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.comments_comment_id_seq;
       public          postgres    false    234            [           0    0    comments_comment_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.comments_comment_id_seq OWNED BY public.comments.comment_id;
          public          postgres    false    233            �            1259    16990    faculty    TABLE     �   CREATE TABLE public.faculty (
    faculty_id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255) NOT NULL
);
    DROP TABLE public.faculty;
       public         heap    postgres    false            �            1259    16993    faculty_faculty_id_seq    SEQUENCE     �   CREATE SEQUENCE public.faculty_faculty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.faculty_faculty_id_seq;
       public          postgres    false    219            \           0    0    faculty_faculty_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.faculty_faculty_id_seq OWNED BY public.faculty.faculty_id;
          public          postgres    false    220            �            1259    16994    jobs    TABLE     A  CREATE TABLE public.jobs (
    job_id integer NOT NULL,
    title character varying(100) NOT NULL,
    role character varying(100) NOT NULL,
    company character varying(100) NOT NULL,
    number_of_positions integer NOT NULL,
    location character varying(100) NOT NULL,
    application_link character varying(255)
);
    DROP TABLE public.jobs;
       public         heap    postgres    false            �            1259    16999    jobs_job_id_seq    SEQUENCE     �   CREATE SEQUENCE public.jobs_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.jobs_job_id_seq;
       public          postgres    false    221            ]           0    0    jobs_job_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.jobs_job_id_seq OWNED BY public.jobs.job_id;
          public          postgres    false    222            �            1259    17138    mentor_sessions    TABLE     �  CREATE TABLE public.mentor_sessions (
    session_id integer NOT NULL,
    alumni_id integer,
    session_title character varying(255) NOT NULL,
    session_date date NOT NULL,
    session_time time without time zone NOT NULL,
    session_link text NOT NULL,
    session_topic character varying(255),
    session_description text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
 #   DROP TABLE public.mentor_sessions;
       public         heap    postgres    false            �            1259    17137    mentor_sessions_session_id_seq    SEQUENCE     �   CREATE SEQUENCE public.mentor_sessions_session_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.mentor_sessions_session_id_seq;
       public          postgres    false    230            ^           0    0    mentor_sessions_session_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.mentor_sessions_session_id_seq OWNED BY public.mentor_sessions.session_id;
          public          postgres    false    229            �            1259    17000    question    TABLE     �   CREATE TABLE public.question (
    question_id integer NOT NULL,
    student_id integer,
    query_text text NOT NULL,
    query_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    answer_text text,
    alumni_id integer
);
    DROP TABLE public.question;
       public         heap    postgres    false            �            1259    17006    question_question_id_seq    SEQUENCE     �   CREATE SEQUENCE public.question_question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.question_question_id_seq;
       public          postgres    false    223            _           0    0    question_question_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.question_question_id_seq OWNED BY public.question.question_id;
          public          postgres    false    224            �            1259    17007    student    TABLE     
  CREATE TABLE public.student (
    student_id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    contact_number character varying(20),
    password character varying(255) NOT NULL,
    admission_year integer
);
    DROP TABLE public.student;
       public         heap    postgres    false            �            1259    17010    student_student_id_seq    SEQUENCE     �   CREATE SEQUENCE public.student_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.student_student_id_seq;
       public          postgres    false    225            `           0    0    student_student_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.student_student_id_seq OWNED BY public.student.student_id;
          public          postgres    false    226            �            1259    17154    threads    TABLE     �  CREATE TABLE public.threads (
    thread_id integer NOT NULL,
    user_id integer NOT NULL,
    user_type character varying(10) NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT threads_user_type_check CHECK (((user_type)::text = ANY ((ARRAY['student'::character varying, 'faculty'::character varying, 'alumni'::character varying])::text[])))
);
    DROP TABLE public.threads;
       public         heap    postgres    false            �            1259    17153    threads_thread_id_seq    SEQUENCE     �   CREATE SEQUENCE public.threads_thread_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.threads_thread_id_seq;
       public          postgres    false    232            a           0    0    threads_thread_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.threads_thread_id_seq OWNED BY public.threads.thread_id;
          public          postgres    false    231            �            1259    17018    viewperformance    TABLE     �   CREATE TABLE public.viewperformance (
    performance_id integer NOT NULL,
    student_id integer,
    semester character varying(20) NOT NULL,
    subject character varying(100) NOT NULL,
    grade character varying(10),
    feedback text
);
 #   DROP TABLE public.viewperformance;
       public         heap    postgres    false            �            1259    17023 "   viewperformance_performance_id_seq    SEQUENCE     �   CREATE SEQUENCE public.viewperformance_performance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.viewperformance_performance_id_seq;
       public          postgres    false    227            b           0    0 "   viewperformance_performance_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.viewperformance_performance_id_seq OWNED BY public.viewperformance.performance_id;
          public          postgres    false    228            }           2604    17024    alumni alumni_id    DEFAULT     t   ALTER TABLE ONLY public.alumni ALTER COLUMN alumni_id SET DEFAULT nextval('public.alumni_alumni_id_seq'::regclass);
 ?   ALTER TABLE public.alumni ALTER COLUMN alumni_id DROP DEFAULT;
       public          postgres    false    216    215            ~           2604    17025    answers answer_id    DEFAULT     v   ALTER TABLE ONLY public.answers ALTER COLUMN answer_id SET DEFAULT nextval('public.answers_answer_id_seq'::regclass);
 @   ALTER TABLE public.answers ALTER COLUMN answer_id DROP DEFAULT;
       public          postgres    false    218    217            �           2604    17170    comments comment_id    DEFAULT     z   ALTER TABLE ONLY public.comments ALTER COLUMN comment_id SET DEFAULT nextval('public.comments_comment_id_seq'::regclass);
 B   ALTER TABLE public.comments ALTER COLUMN comment_id DROP DEFAULT;
       public          postgres    false    234    233    234            �           2604    17027    faculty faculty_id    DEFAULT     x   ALTER TABLE ONLY public.faculty ALTER COLUMN faculty_id SET DEFAULT nextval('public.faculty_faculty_id_seq'::regclass);
 A   ALTER TABLE public.faculty ALTER COLUMN faculty_id DROP DEFAULT;
       public          postgres    false    220    219            �           2604    17028    jobs job_id    DEFAULT     j   ALTER TABLE ONLY public.jobs ALTER COLUMN job_id SET DEFAULT nextval('public.jobs_job_id_seq'::regclass);
 :   ALTER TABLE public.jobs ALTER COLUMN job_id DROP DEFAULT;
       public          postgres    false    222    221            �           2604    17141    mentor_sessions session_id    DEFAULT     �   ALTER TABLE ONLY public.mentor_sessions ALTER COLUMN session_id SET DEFAULT nextval('public.mentor_sessions_session_id_seq'::regclass);
 I   ALTER TABLE public.mentor_sessions ALTER COLUMN session_id DROP DEFAULT;
       public          postgres    false    230    229    230            �           2604    17029    question question_id    DEFAULT     |   ALTER TABLE ONLY public.question ALTER COLUMN question_id SET DEFAULT nextval('public.question_question_id_seq'::regclass);
 C   ALTER TABLE public.question ALTER COLUMN question_id DROP DEFAULT;
       public          postgres    false    224    223            �           2604    17030    student student_id    DEFAULT     x   ALTER TABLE ONLY public.student ALTER COLUMN student_id SET DEFAULT nextval('public.student_student_id_seq'::regclass);
 A   ALTER TABLE public.student ALTER COLUMN student_id DROP DEFAULT;
       public          postgres    false    226    225            �           2604    17157    threads thread_id    DEFAULT     v   ALTER TABLE ONLY public.threads ALTER COLUMN thread_id SET DEFAULT nextval('public.threads_thread_id_seq'::regclass);
 @   ALTER TABLE public.threads ALTER COLUMN thread_id DROP DEFAULT;
       public          postgres    false    232    231    232            �           2604    17032    viewperformance performance_id    DEFAULT     �   ALTER TABLE ONLY public.viewperformance ALTER COLUMN performance_id SET DEFAULT nextval('public.viewperformance_performance_id_seq'::regclass);
 M   ALTER TABLE public.viewperformance ALTER COLUMN performance_id DROP DEFAULT;
       public          postgres    false    228    227            ?          0    16970    alumni 
   TABLE DATA           �   COPY public.alumni (alumni_id, name, email, contact_number, password, passout_year, company, role, linkedin_profile) FROM stdin;
    public          postgres    false    215   �h       A          0    16976    answers 
   TABLE DATA           ^   COPY public.answers (answer_id, question_id, alumni_id, answer_text, answer_date) FROM stdin;
    public          postgres    false    217   _i       R          0    17167    comments 
   TABLE DATA           g   COPY public.comments (comment_id, thread_id, user_id, user_type, comment_text, created_at) FROM stdin;
    public          postgres    false    234   �l       C          0    16990    faculty 
   TABLE DATA           D   COPY public.faculty (faculty_id, name, email, password) FROM stdin;
    public          postgres    false    219   m       E          0    16994    jobs 
   TABLE DATA           m   COPY public.jobs (job_id, title, role, company, number_of_positions, location, application_link) FROM stdin;
    public          postgres    false    221   Km       N          0    17138    mentor_sessions 
   TABLE DATA           �   COPY public.mentor_sessions (session_id, alumni_id, session_title, session_date, session_time, session_link, session_topic, session_description, created_at, updated_at) FROM stdin;
    public          postgres    false    230   �m       G          0    17000    question 
   TABLE DATA           k   COPY public.question (question_id, student_id, query_text, query_date, answer_text, alumni_id) FROM stdin;
    public          postgres    false    223   bn       I          0    17007    student 
   TABLE DATA           d   COPY public.student (student_id, name, email, contact_number, password, admission_year) FROM stdin;
    public          postgres    false    225   �p       P          0    17154    threads 
   TABLE DATA           U   COPY public.threads (thread_id, user_id, user_type, content, created_at) FROM stdin;
    public          postgres    false    232   Hq       K          0    17018    viewperformance 
   TABLE DATA           i   COPY public.viewperformance (performance_id, student_id, semester, subject, grade, feedback) FROM stdin;
    public          postgres    false    227   �q       c           0    0    alumni_alumni_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.alumni_alumni_id_seq', 2, true);
          public          postgres    false    216            d           0    0    answers_answer_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.answers_answer_id_seq', 16, true);
          public          postgres    false    218            e           0    0    comments_comment_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.comments_comment_id_seq', 2, true);
          public          postgres    false    233            f           0    0    faculty_faculty_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.faculty_faculty_id_seq', 1, true);
          public          postgres    false    220            g           0    0    jobs_job_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.jobs_job_id_seq', 3, true);
          public          postgres    false    222            h           0    0    mentor_sessions_session_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.mentor_sessions_session_id_seq', 1, true);
          public          postgres    false    229            i           0    0    question_question_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.question_question_id_seq', 17, true);
          public          postgres    false    224            j           0    0    student_student_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.student_student_id_seq', 7, true);
          public          postgres    false    226            k           0    0    threads_thread_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.threads_thread_id_seq', 1, true);
          public          postgres    false    231            l           0    0 "   viewperformance_performance_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.viewperformance_performance_id_seq', 3, true);
          public          postgres    false    228            �           2606    17034    alumni alumni_email_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.alumni
    ADD CONSTRAINT alumni_email_key UNIQUE (email);
 A   ALTER TABLE ONLY public.alumni DROP CONSTRAINT alumni_email_key;
       public            postgres    false    215            �           2606    17036    alumni alumni_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.alumni
    ADD CONSTRAINT alumni_pkey PRIMARY KEY (alumni_id);
 <   ALTER TABLE ONLY public.alumni DROP CONSTRAINT alumni_pkey;
       public            postgres    false    215            �           2606    17038    answers answers_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (answer_id);
 >   ALTER TABLE ONLY public.answers DROP CONSTRAINT answers_pkey;
       public            postgres    false    217            �           2606    17176    comments comments_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (comment_id);
 @   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_pkey;
       public            postgres    false    234            �           2606    17042    faculty faculty_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_email_key UNIQUE (email);
 C   ALTER TABLE ONLY public.faculty DROP CONSTRAINT faculty_email_key;
       public            postgres    false    219            �           2606    17044    faculty faculty_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (faculty_id);
 >   ALTER TABLE ONLY public.faculty DROP CONSTRAINT faculty_pkey;
       public            postgres    false    219            �           2606    17046    jobs jobs_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_pkey PRIMARY KEY (job_id);
 8   ALTER TABLE ONLY public.jobs DROP CONSTRAINT jobs_pkey;
       public            postgres    false    221            �           2606    17147 $   mentor_sessions mentor_sessions_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.mentor_sessions
    ADD CONSTRAINT mentor_sessions_pkey PRIMARY KEY (session_id);
 N   ALTER TABLE ONLY public.mentor_sessions DROP CONSTRAINT mentor_sessions_pkey;
       public            postgres    false    230            �           2606    17048    question question_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (question_id);
 @   ALTER TABLE ONLY public.question DROP CONSTRAINT question_pkey;
       public            postgres    false    223            �           2606    17050    student student_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_email_key UNIQUE (email);
 C   ALTER TABLE ONLY public.student DROP CONSTRAINT student_email_key;
       public            postgres    false    225            �           2606    17052    student student_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (student_id);
 >   ALTER TABLE ONLY public.student DROP CONSTRAINT student_pkey;
       public            postgres    false    225            �           2606    17163    threads threads_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.threads
    ADD CONSTRAINT threads_pkey PRIMARY KEY (thread_id);
 >   ALTER TABLE ONLY public.threads DROP CONSTRAINT threads_pkey;
       public            postgres    false    232            �           2606    17056 $   viewperformance viewperformance_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.viewperformance
    ADD CONSTRAINT viewperformance_pkey PRIMARY KEY (performance_id);
 N   ALTER TABLE ONLY public.viewperformance DROP CONSTRAINT viewperformance_pkey;
       public            postgres    false    227            �           2606    17057    answers answers_alumni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_alumni_id_fkey FOREIGN KEY (alumni_id) REFERENCES public.alumni(alumni_id) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.answers DROP CONSTRAINT answers_alumni_id_fkey;
       public          postgres    false    217    215    4754            �           2606    17062     answers answers_question_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.question(question_id) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.answers DROP CONSTRAINT answers_question_id_fkey;
       public          postgres    false    223    217    4764            �           2606    17177     comments comments_thread_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_thread_id_fkey FOREIGN KEY (thread_id) REFERENCES public.threads(thread_id) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_thread_id_fkey;
       public          postgres    false    232    234    4774            �           2606    17148 .   mentor_sessions mentor_sessions_alumni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.mentor_sessions
    ADD CONSTRAINT mentor_sessions_alumni_id_fkey FOREIGN KEY (alumni_id) REFERENCES public.alumni(alumni_id) ON DELETE CASCADE;
 X   ALTER TABLE ONLY public.mentor_sessions DROP CONSTRAINT mentor_sessions_alumni_id_fkey;
       public          postgres    false    215    4754    230            �           2606    17087     question question_alumni_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_alumni_id_fkey FOREIGN KEY (alumni_id) REFERENCES public.alumni(alumni_id) ON DELETE SET NULL;
 J   ALTER TABLE ONLY public.question DROP CONSTRAINT question_alumni_id_fkey;
       public          postgres    false    215    4754    223            �           2606    17092 !   question question_student_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(student_id) ON DELETE CASCADE;
 K   ALTER TABLE ONLY public.question DROP CONSTRAINT question_student_id_fkey;
       public          postgres    false    223    4768    225            �           2606    17112 /   viewperformance viewperformance_student_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.viewperformance
    ADD CONSTRAINT viewperformance_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(student_id) ON DELETE CASCADE;
 Y   ALTER TABLE ONLY public.viewperformance DROP CONSTRAINT viewperformance_student_id_fkey;
       public          postgres    false    225    4768    227            ?   �   x�M���0����)x�0u%j�Nl�eB��H���+�1nN���Jh�s!k-9o�c'�ća"7��1AY�7�]�z)�V����������`-I�<y����ĺF��|�1�%=Ñ�g�3��	s ���E1:��;YuϕRo�5      A   ,  x�mTK��8>'��N����Iw�6bi`@H q��'�NL;�`;ݛOU�GRV\��Q�}���?E��v m���@@�y'ef��?��1 ��1����w� �W�d���+>U���ӈ��Cgm{��wj�|�l?�}#���h�Ej��0���y	�ޫ���:=��9����k�Z7�Z�:����'{i��t� �W7V��s���ĵE�C�,g4����`ׯ�;	�+*L`��kp�vps�grG�0�ӄ����;��0������8�~0�*�z`�T���_D���ؼ��o���6M�K�M�)�q�E��]+�/X��ǻgY����i��ʢ��<�+ɺ����H4�6��~Гg5���<h��<�2Y�i[�av�S���:\�4Wf�{��~SE��ȥp�x���D�ƅŵl�[�i2Zp
�[�q�f�����Ӵ��ݮ��"�7B� N2�<�#�8C�y�I��A�tG"A� y^T wa��Ί����qtOB�D^M�_���(6��.Ͳ'�?L�e�*�4�<�pD�����>Nh���y�X� ���/��G�Gym0�s1
�<+wٞ�(#�X�Od.W��{�Q�;���ټu�e��p�����t��$���K
7ld"*�D����G�cA]7� ��䨛��/��;��8��f�X�U	ٷn^e�N��'��q���s�eS�n�ͫ}̾��Y��n�<-���b���$<����MU5e�n��:ʷ�0� �9�.4��򁭚f�2<�!�7ٶ)viY��jߧq�T��i      R   X   x�U˫�  P�L�pI
�3���������`�zZW��4u�B�-e+l(��K`�o��Q���xu����B�9�I.���MW      C   8   x�3�NL�,�LKL.�)�4tH�M���K���442�2��M�(́I�I��qqq ��/      E   s   x�3�t�a�����`N#N��ܤ�L�?.#NGN����#��;��g@i^*gFFIA���~z~~zN�^r~.�1���/+������q:&'�敔�r��Ţ1F��� x':      N   �   x�}�;! ��)���|�5��	lm�%���@��ngg2�L2���gz��P:H.w?r1k�7`)�z[k��*�)���b��#���b�ss�u]2?���\i5k�g��BN�2B��-V      G     x��R9��@��x]*c��f%E��R�J�8��01̳�����a�H��6���e���p`Ϫ�-4zp��gF��(z/�����I�tKG~ً��Iՠt�3�op؈�)H��m�r�D���U���,�$_���Q�/��{io�JC��9�̯$��wYw+�p���H�+�*V�qg�݉���^�ɾ�a6FT��݌\ќ�����g-bK��ysA++��F�fA�y��E��]~�zT�@��|2&탲���*��$I�2�+KH�-7]�>��xʹ��({ j��%1
կ5X$j�\�GQ�[�����ry�ɧD�y��#A�	D3����˭h���Qפ�zz�W	Y�1�:c���h�`k%u-wt{rW�"^�e9�WE�}�+4�Y�`�^T��� ^��:Vn"���jo���<�y��_��UR���E�n/���w���g�Z�Ҹ^b=JJ��{a��kt N�J�9ۤH�"�c���قW;����,^�<��L��C��l�u�:�      I   �   x�U�;�0��9'@$Nle�PUBb��D�"(B�}I�T�l��lK8Vf*+h)+�'�ڑ����A�b�9*�����;.D$C(�lǠ0d[�oD��ѫ�M$S�����s���I�X*Ա^��1�#�9o��#��m��t�����i��+��j濇V�H��S�{ w�J�      P   T   x����  �7��@(��3�~�4Ї}�#�L����=�M�q�|�V���ؤ6,|e-h����B?��?:(�	 ��`      K   \   x�3�4�4�w�t�K-�Tp��O�2
�q�$�$*+$g��%�rU��%��*����&E����M8�KK2�K2���ƀM����� s�c     