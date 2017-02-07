-- Database diff generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.0-alpha1
-- PostgreSQL version: 9.6

-- [ Diff summary ]
-- Dropped objects: 43
-- Created objects: 1
-- Changed objects: 0
-- Truncated tables: 0

SET search_path=public,pg_catalog;
-- ddl-end --


-- [ Dropped objects ] --
ALTER TABLE public.abastece_itemcontrolado DROP CONSTRAINT IF EXISTS abastece_itemcontrolado_posto_id_c9abb2ca_fk_abastece_posto_id CASCADE;
-- ddl-end --
ALTER TABLE public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_user_id_c564eba6_fk_auth_user_id CASCADE;
-- ddl-end --
ALTER TABLE public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_content_type_id_c4bce8eb_fk_django_content_type_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_user_user_permissions DROP CONSTRAINT IF EXISTS auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_user_user_permissions DROP CONSTRAINT IF EXISTS auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_user_groups DROP CONSTRAINT IF EXISTS auth_user_groups_group_id_97559544_fk_auth_group_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_user_groups DROP CONSTRAINT IF EXISTS auth_user_groups_user_id_6a12ed8b_fk_auth_user_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_b120cbf9_fk_auth_group_id CASCADE;
-- ddl-end --
ALTER TABLE public.auth_permission DROP CONSTRAINT IF EXISTS auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.abastece_itemcontrolado_6e6afa60 CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.django_session_session_key_c0390e0f_like CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.django_session_de54fa62 CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.django_session CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_user_username_6821ab7c_like CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.django_admin_log_e8701ad4 CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.django_admin_log_417f1b1c CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.django_admin_log CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.django_admin_log_id_seq CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_user_user_permissions_8373b171 CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_user_user_permissions_e8701ad4 CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_user_groups_0e939a4f CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_user_groups_e8701ad4 CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_group_permissions_8373b171 CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_group_permissions_0e939a4f CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_group_name_a6ea08ec_like CASCADE;
-- ddl-end --
DROP INDEX IF EXISTS public.auth_permission_417f1b1c CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.auth_user_user_permissions CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.auth_user_user_permissions_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.auth_user_groups CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.auth_user_groups_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.auth_user CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.auth_user_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.auth_group_permissions CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.auth_group_permissions_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.auth_group CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.auth_group_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.auth_permission CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.auth_permission_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.django_content_type CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.django_content_type_id_seq CASCADE;
-- ddl-end --
DROP TABLE IF EXISTS public.django_migrations CASCADE;
-- ddl-end --
DROP SEQUENCE IF EXISTS public.django_migrations_id_seq CASCADE;
-- ddl-end --
ALTER TABLE public.abastece_itemcontrolado DROP COLUMN IF EXISTS posto_id CASCADE;
-- ddl-end --


-- [ Created objects ] --
-- object: public.abastece_tipoevento_id_seq | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public.abastece_tipoevento_id_seq CASCADE;
CREATE SEQUENCE public.abastece_tipoevento_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
ALTER SEQUENCE public.abastece_tipoevento_id_seq OWNER TO temos;
-- ddl-end --

