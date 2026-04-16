create table kss_references
(domain_name      varchar(32)	not null
,item_value       varchar(24)	not null
,group_value      varchar(24)
,meaning          varchar(64)
,mean_label       varchar(64) 
,order_val        numeric(7,3)
);
alter table kss_references
add	constraint pk_kssref
	primary key (domain_name,item_value,group_value) using index tablespace sleindex;
    
COMMENT ON TABLE kss_references
    IS 'INFORMACION DE REFERENCIA';
COMMENT ON COLUMN kss_references.domain_name
    IS 'Dominio o nombre de información';
COMMENT ON COLUMN kss_references.item_value
    IS 'Identificador elemento o valor ';
COMMENT ON COLUMN kss_references.meaning
    IS 'Nombre o descripción de elemento';
COMMENT ON COLUMN kss_references.meaning
    IS 'Nombre o descripción de elemento';
     
create table kss_company
(id				varchar(10)		not null
,instance		numeric(10)		not null
,name       	varchar(64)  	not null
,shortening		varchar(32)		not null
,lic_key		varchar(20)		not null
,tin			varchar(20)		not null
,country_id		varchar(4)		not null
,nationality	varchar(24)
,natural_code	varchar(3)
,foreign_code	varchar(3)
,email_cfg_file	varchar(64)
,gen_employee_n numeric(1)		default 0	not null
,len_employee_n numeric(2)		default 0	not null
,lookat_job_sal	numeric(1)		default 0	not null
,start_fy		numeric(2)		default 1   not null
,audit_user     varchar(64)
,audit_dte      date
,audit_track    numeric(10)      default 0
,kinder_age     numeric(2)
,kinder_minwage numeric(2)
,kinder_pct     numeric(5,2)
,kinder_payitem_id numeric(4)
,lookat_dep_job numeric(1) default 0 not null
,lookat_job_quota varchar(24) default 'na' not null
,filename_logo varchar(128)
);
alter table kss_company
add	constraint pk_ksscompany
	primary key (id) using index tablespace sleindex;

COMMENT ON TABLE kss_company
    IS 'DEFINICION DE EMPRESAS';
COMMENT ON COLUMN kss_company.name
    IS 'Nombre de empresa';
COMMENT ON COLUMN kss_company.shortening
    IS 'Nombre abreviado o corto';
COMMENT ON COLUMN kss_company.lic_key
    IS 'Número de licencia o clave de acceso';
COMMENT ON COLUMN kss_company.tin
    IS 'Numero de indenficación tributaria';
COMMENT ON COLUMN kss_company.country_id
    IS 'País donde funciona la empresa';
COMMENT ON COLUMN kss_company.nationality
    IS 'Nacionalidad natural del país donde funciona la empresa';
COMMENT ON COLUMN kss_company.natural_code
    IS 'Código de la nacionalidad,si la persona es de la nacionalidad de la empresa';
COMMENT ON COLUMN kss_company.foreign_code
    IS 'Código de la nacionalidad,si la persona no es de la nacionalidad de la empresa';
COMMENT ON COLUMN kss_company.email_cfg_file
    IS 'Nombre de archivo de configuración de correos o emails';
COMMENT ON COLUMN kss_company.gen_employee_n
    IS 'Generar el número de empleado  de forma autmatica e incremantar (1=Sí)';
COMMENT ON COLUMN kss_company.lookat_job_sal
    IS 'Considerar el salario inicial (nivel 1) del cargo al ingreso (1=Sí)';
COMMENT ON COLUMN kss_company.start_fy
    IS 'Mes de inicial del año fiscal';
COMMENT ON COLUMN kss_company.kinder_payitem_id
    IS 'Concepto para calculo de guarderia';
COMMENT ON COLUMN kss_company.lookat_dep_job
    IS 'Validar si el Cargo es permitido según Departamento (1=Sí)';
COMMENT ON COLUMN kss_company.lookat_job_quota
    IS 'Validar cupo de cargos (na=No aplica, dep=Departamento, loc=Ubicación)';
COMMENT ON COLUMN kss_company.filename_logo
    IS 'Ruta y nombre de archivo imagen del logo de la empresa';


insert into kss_company
(ID
,INSTANCE
,NAME
,SHORTENING
,LIC_KEY
,TIN
,COUNTRY_ID
,GEN_EMPLOYEE_N
,LEN_EMPLOYEE_N
,LOOKAT_JOB_SAL
,START_FY
)
values
('1000'
,0
,'DEMOSTRACION, C.A.'
,'DEMO, C.A.'
,'J54S1JS.125QY0W.1W0D'
,'J299167304'
,'VEN'
,0
,0
,0
,01
);


create table krp_partners
(id			   		numeric(20)  	not null
,instance			numeric(10)		default 0 not null
,name      			varchar(128)  	not null
,tin	       		varchar(20)     not null
,partner_type		varchar(24)		not null
,is_tax_exempt numeric(1) default 0 not null
,economy_sector    	varchar(24)  	not null
,website      		varchar(64)
,e_mail       		varchar(64)
,contract_d date
,empl_size numeric(5)
,phone1 varchar(15)
,phone2 varchar(15)
,pub_note varchar(255)
,pri_note varchar(255)
); 
comment on table krp_partners
 is 'ALIADOS';
comment on column krp_partners.id
 is 'Identificador o código';
comment on column krp_partners.partner_type
is 'Tipo de aliado (domain=partnerType)'
comment on column krp_partners.economy_sector
is 'Clasificación según Sector Economico (domain=economySec)'
comment on column krp_partners.pub_note
is 'Nota o comentario publico'
comment on column krp_partners.pri_note
is 'Nota o comentario privado'

Emplos de busqueda en kss_references 
select item_value, meaning from kss_references where domain_name = 'partnerType' order by order_val
select item_value, meaning kss_references where domain_name = 'economySec' order by order_val


create krp_partner_address
(id numeric(20) not null
,client_id numeric(20) not null
,address_type varchar(24) not null
,address_lines varchar(120)  
,ref_address	varchar(64)
,country_id   	varchar(4) 
,state_id    	varchar(4)
,city      		varchar(64)
,municipality	varchar(64)
,parish		   	varchar(64)
,postal_code  	varchar(10)
);
comment on table krp_partner_address
 is 'DIRECCION DE ALIADOS';
comment on column krp_partner_address.address_type
is 'Tipo de aliado (domain=addressType)'
comment on column krp_partner_address.ref_address
is 'Referencia para encontrar dirección'
comment on column krp_partner_address.country_id
is 'País donde esta establecido el aliado o  cliente'
comment on column krp_partner_address.state_id
is 'Estado o Provincia del país donde se encuentra el cliente  o aliado'

 
create table krp_partner_contacts
(id	numeric(20) not null
,partner_id numeric(20) not null
,firstname  varchar(17) not null
,middlename varchar(15)
,lastname1	varchar(17) not null 	
,lastname2 	varchar(15)
,position	varchar(64)	not null
,phone      varchar(15)
,phone_ext	varchar(6)  	
,mobile		varchar(15)
,e_mail	    varchar(60)
,in_invoice  numeric(1) default 0 not null
);
comment on table krp_partner_contacts
 is 'CONTACTOS DE ALIADOS';
comment on column krp_partner_contacts.firstname
 is 'Primer nombre de persona contacto';
comment on column krp_partner_contacts.middlename
 is 'Segundo nombre de persona contacto';
comment on column krp_partner_contacts.lastname1
 is 'Primer apellido de persona contacto';
comment on column krp_partner_contacts.lastname2
 is 'Segundo nombre de persona contacto';
comment on column krp_partner_contacts.position
is 'Posición o Cargo en el ampresaTipo de aliado (domain=addressType)'
comment on column krp_partner_contacts.position
 is 'Posición, cargo  o función de la persona contacto';
comment on column krp_partner_contacts.phone
 is 'Número de teléfono';
comment on column krp_partner_contacts.phone_ext
 is 'Extensión del número de teléfono';
comment on column krp_partner_contacts.mobile
 is 'Número de celular o teléfono movil';
comment on column krp_partner_contacts.e_mail
 is 'Correo electrónico o email';
comment on column krp_partner_contacts.in_invoice
is 'Indica si el contacto debe mostrarse en la factura (1=Sí)'


create table krp_products
(id	numeric(20) not null
,company_id varchar(10) not null
,name varchar(64) not null
,price varchar(15,2) not null 	
,vat_rate numeric(5,2) not null
,default_qty numeric(5) not null
,currency_id varchar(4) not null
,is_tax_exempt numeric(1) default 0 not null
,note varchar(255)
);
comment on table krp_products
 is 'PRODUCTOS O SERVICIOS';
comment on column krp_products.vat_rate
 is 'Tasa de impuesto valor agregado';
comment on column krp_products.currency_id
 is 'Tipo de moneda expresado el precio';

create table krp_invoices
(id	numeric(20) not null
,company_id varchar(10) not null
,partner_id numeric(20) not null
,invoice_n  numeric(7) not null
,invoice_d date
,invoice_c varchar(7) not null
,discount numeric(15,2) default 0 not null
,currency_id varchar(4)
,pub_note varchar(255)
,pri_note varchar(255) 
);
comment on table krp_invoices
 is 'FACTURAS';
comment on column krp_invoices.invoice_n
 is 'Número de factura';
comment on column krp_invoices.invoice_d
 is 'Fecha de factura';
comment on column krp_invoices.invoice_c
 is 'Número de control de facturación';
comment on column krp_invoices.currency_id
 is 'Tipo de moneda de la factura en general';


create table krp_invoice_transactions
(id	numeric(20) not null
,invoice_id numeric(20) not null
,product_id  numeric(20) not null
,price 	varchar(15,2) not null 
,qty numeric(5) not null
,amount numeric(15,2)
,vat_rate numeric(5,2) not null
,currency_id varchar(4) not null
,curr_rate numeric(9,5) default 0
,note varchar(255)
);
comment on table krp_invoice_transactions
 is 'PRUDUCTOS POR FACTURA';
comment on column krp_invoices.price
 is 'Precio por unidad';
comment on column krp_invoices.qty
 is 'Unidades o cantidad del producto a facturar';
comment on column krp_invoices.vat_rate
 is 'Porcentaje de impuesto valor agregado';



