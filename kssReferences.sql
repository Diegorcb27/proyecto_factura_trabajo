delete kss_references;
insert into kss_references values('accountType','00','none','Planificada','',0);
insert into kss_references values('accountType','16','none','Presunci�n','',1);
insert into kss_references values('accountType','15','none','Personalizada','',2);
insert into kss_references values('accountType','81','none','M�trica','',3);
insert into kss_references values('accountType','90','none','Extendida','',4);

-- Se incorporaran cuando apliquen en una futura versi�n
--insert into kss_references values('accountType','151','none','Acumulativa','',5);
insert into kss_references values('affinity','spouse','none','C�nyuge','',1);
insert into kss_references values('affinity','parent','none','Padre/Madre','',2);
insert into kss_references values('affinity','children','none','Hijo/Hija','',3);
insert into kss_references values('affinity','brother','none','Hermano/Hermana','',3);
insert into kss_references values('affinity','nephew','none','Sobrino/Sobrina','',3);
insert into kss_references values('affinity','cousin','none','Primo/Prima','',3);
insert into kss_references values('affinity','uncle','none','T�o/T�a','',3);
insert into kss_references values('affinity','grandparent','none','Abuelo/Abuela','',3);
insert into kss_references values('affinity','grandson','none','Nieto/Nieta','',3);
insert into kss_references values('affinity','other','none','Otro','',98);
insert into kss_references values('affinity','titular','none','Titular/Nominal','',99);
insert into kss_references values('columnType','S','none','Caracter','',1);
insert into kss_references values('columnType','N','none','Num�rico','',2);
insert into kss_references values('columnType','D','none','Fecha','',3);
insert into kss_references values('columnType','C','none','Categor�a','',4);
--Plan C
insert into kss_references values('dateType','HireCompany','none','Ingreso','',1);
insert into kss_references values('dateType','HireSet1','none','Ingreso grupo','',2);
insert into kss_references values('dateType','HireSet2','none','Ingreso alterna 2','',3);
insert into kss_references values('dateType','HireSet3','none','Ingreso alterna 3','',4);
insert into kss_references values('dateType','HireSet4','none','Ingreso alterna 4','',5);
insert into kss_references values('dateType','StartPeriod','none','Inicio de periodo','',6.04);
insert into kss_references values('dateType','EndPeriod','none','Fin de periodo','',6.08);
insert into kss_references values('dateType','Birthday','none','Nacimiento','',7);
insert into kss_references values('dateType','StartScenario','none','Inicio escenario','',8.04);
insert into kss_references values('dateType','EndScenario','none','Fin escenario','',8.08);
insert into kss_references values('dateType','SysDate','none','D�a de ejecuci�n','',10);
--- Plan C
insert into kss_references values('anniversaryPlanC','0','none','No aplica','',1);
insert into kss_references values('anniversaryPlanC','1','none','Ingreso','',2);
insert into kss_references values('anniversaryPlanC','2','none','Ingreso grupo','',2.50);
insert into kss_references values('anniversaryPlanC','3','none','Ingreso alterna 2','',3);
insert into kss_references values('anniversaryPlanC','4','none','Ingreso alterna 3','',4);
insert into kss_references values('anniversaryPlanC','5','none','Ingreso alterna 4','',5);
insert into kss_references values('anniversaryPlanC','6','none','Nacimiento','',6);

--Stipendia
insert into kss_references values('dateCalc','_hireCompany','none','Ingreso','',1);
insert into kss_references values('dateCalc','_hireSet1','none','Ingreso grupo','',2);
insert into kss_references values('dateCalc','_hireSet2','none','Ingreso alterna 1','',2.1); 
insert into kss_references values('dateCalc','_hireSet3','none','Ingreso alterna 2','',2.2);
insert into kss_references values('dateCalc','_hireSet4','none','Ingreso alterna 3','',2.3);
insert into kss_references values('dateCalc','_startPeriod','none','Inicio de periodo','',3);
insert into kss_references values('dateCalc','_endPeriod','none','Fin de periodo','',4);
insert into kss_references values('dateCalc','_helperPeriod','none','Auxiliar en periodo','',4.1);
insert into kss_references values('dateCalc','_startMonth','none','Inicio mes per�odo','',4.4);
insert into kss_references values('dateCalc','_endMonth','none','Fin mes per�odo','',4.6);
insert into kss_references values('dateCalc','_startYear','none','Inicio de a�o','',4.70);
insert into kss_references values('dateCalc','_endYear','none','Fin de a�o','',4.71);
insert into kss_references values('dateCalc','_prevEndYear','none','Fin de a�o anterior','',4.75);
insert into kss_references values('dateCalc','_birthday','none','Nacimiento','',5);
insert into kss_references values('dateCalc','_settlement','none','Fin relaci�n laboral','',6);
insert into kss_references values('dateCalc','_vacationOut','none','Salida de vacaci�n','',7);
insert into kss_references values('dateCalc','_vacationBack','none','Regreso de vacaci�n','',8);
insert into kss_references values('dateCalc','_transaction','none','Transacci�n o movimiento','',9);
insert into kss_references values('dateCalc','_startContract','none','Inicio contrato','',10);
insert into kss_references values('dateCalc','_endContract','none','Fin contrato','',10.1);
insert into kss_references values('dateCalc','_startFiscalYear','none','Inicio a�o fiscal','',11);
insert into kss_references values('dateCalc','_endPrevFiscalYear','none','Fin a�o fiscal anterior','',11.1);


--insert into kss_references values('dateType','StartYear','none','Inicio de a�o calendario','',10.04);
--insert into kss_references values('dateType','EndYear','none','Fin de a�o calendario','',10.08);
insert into kss_references values('sleapp','sleplanc','none','Plan C','',1);
insert into kss_references values('sleapp','stipendia','none','STIPENDIA','',2);
insert into kss_references values('sleapp','slesec','none','kSecurity','',3);

--kSec
insert into kss_references values('ksecModule','security','none','SEGURIDAD','',1);

--Plan C
insert into kss_references values('kplancModule','config','none','CONFIGURACION','',2);
insert into kss_references values('kplancModule','compensation','none','COMPENSACION','',4);
insert into kss_references values('kplancModule','accounting','none','CONTABLE','',5);
insert into kss_references values('kplancModule','transfer','none','TRANSFERIR DATOS','',6);

-- Payroll
insert into kss_references values('stipendiaModule','security','none','SEGURIDAD','',1);
insert into kss_references values('stipendiaModule','config','none','CONFIGURACION','',2);
insert into kss_references values('stipendiaModule','compensation','none','COMPENSACION','',3);
insert into kss_references values('stipendiaModule','accounting','none','CONTABLE','',5);
insert into kss_references values('stipendiaModule','report','none','LISTADOS','',6);
insert into kss_references values('stipendiaModule','trainning','none','FORMACION','',7);
insert into kss_references values('stipendiaModule','custom','none','ADAPTACION','',8);

insert into kss_references values('kstipendiaModule','config','none','CONFIGURACION','',2);
insert into kss_references values('kstipendiaModule','compensation','none','COMPENSACION','',3);
insert into kss_references values('kstipendiaModule','accounting','none','CONTABLE','',5);
insert into kss_references values('kstipendiaModule','report','none','LISTADOS','',6);
insert into kss_references values('kstipendiaModule','trainning','none','FORMACION','',7);

insert into kss_references values('khealthModule','health','none','SALUD','',1);

insert into kss_references values('kmailModule','mail','none','CORREOS','',1);

--
insert into kss_references values('plancFunc','001','none','Valor o monto por calendario','',1);
insert into kss_references values('plancFunc','002','none','Cantidad de d�as del mes','',2);
insert into kss_references values('plancFunc','003','none','Valor o monto por Unidad de Negocio','',3);
insert into kss_references values('plancFunc','004','none','Cantidad de a�os de servicios','',4);
insert into kss_references values('reportAccount','AccountSummary','none','Resumen Cuenta','',1);
insert into kss_references values('reportAccount','AccountBU','none','Cuenta Unidad de negocio','',2);
insert into kss_references values('reportAccount','BUSummary','none','Resumen Unidad de negocio','',2.10);
insert into kss_references values('reportAccount','AccountCategory','none','Cuenta Categor�a','',3);
insert into kss_references values('reportAccount','CategorySummary','none','Resumen Categor�a','',3.10);
insert into kss_references values('reportAccount','AccountCategoryWorkforce','none','Categor�a Colaborador','',3.12);
insert into kss_references values('reportAccount','AccountWorkforce','none','Cuenta Colaborador','',4);
insert into kss_references values('reportAccount','WorkforceSummary','none','Resumen Colaborador','',4.10);
insert into kss_references values('reportAccount','AccountWorkforceType','none','Cuenta clasificaci�n fuerza laboral','',4.20);
insert into kss_references values('reportAccount','WorkforceTotal','none','Total Colaboradores','',4.30);
insert into kss_references values('reportAccount','HeadcountBU','none','Headcount -Unidad de negocio','',5);
insert into kss_references values('reportAccount','HeadcountBUJob','none','Headcount -Unidad por Cargo','',5.10);
insert into kss_references values('reportAccount','HeadcountCatBU','none','Headcount -Categoria por unidad ','',5.20);
--
insert into kss_references values('repAccounting','AccountingType','none','Estimaci�n -Cuenta contable por Tipo de costo','',1);
insert into kss_references values('repAccounting','HeadcountSCost','jasper','Headcount -Centro de costo','',2);
insert into kss_references values('repAccounting','HeadcountSCostCat','jasper','Headcount -Centro de costo Categor�a','',2.10);
insert into kss_references values('repAccounting','HeadcountCenterCost','none','Headcount -Unidad por Centro de costo','',2.20);
insert into kss_references values('repAccounting','AccountingInterfaceSTD','jasper','Interfaz contable -Estandar','',3);
insert into kss_references values('repAccounting','LedgerAccountDistByBU','jasper','Interfaz contable -Hyperion','',3.10);
insert into kss_references values('repAccounting','AccountingInterfaceJDE','jasper','Interfaz contable -JDE','',3.20);
--insert into kss_references values('repAccounting','PCAccountingInterface','none','Interfaz contable','',4);
--insert into kss_references values('repAccounting','PCAccountingInterfaceUSD','none','Interfaz contable -USD','',4.10);
insert into kss_references values('repAccounting','WorkforceCostCenters','jasper','Colaboradores -Centros de Costos','',4.10);
insert into kss_references values('repAccounting','AccountingAccount','jasper','Cuentas contables','',4.20);
insert into kss_references values('repAccounting','WorkforceWithoutAccount','jasper','Colaboradores sin Centros de Costos','',5.10);
insert into kss_references values('repAccounting','RelAcctWithoutAccount','jasper','Colaboradores con Centros sin Cuentas','',5.20);

insert into kss_references values('plancCalcReport','AccountSummary','none','Resumen Cuenta','',1);
insert into kss_references values('plancCalcReport','CategorySummary','none','Resumen Categor�a','',1.5);
insert into kss_references values('plancCalcReport','CategoryAccount','none','Categor�as por Cuenta','',2);
insert into kss_references values('plancCalcReport','AccountCategory','none','Cuentas por Categor�a','',2);
insert into kss_references values('plancCalcReport','AccountClassifCategory','none','Cuenta Clasificada -Categor�a','',2.10);
insert into kss_references values('plancCalcReport','WorkforceClassifCategory','none','Colaborador Clasificaci�n Cuenta','',3);
insert into kss_references values('plancCalcReport','WorkforceTotalAccount','none','Total Colaboradores -Cuenta','',3.10);
insert into kss_references values('plancCalcReport','WorkforceColAccount','none','Cuenta Colaborador por Gerencia','',3.20);
insert into kss_references values('plancCalcReport','AccountWorkforce','none','Cuenta por Colaborador','',3.30);
insert into kss_references values('plancCalcReport','AccountWorkforceDetail','none','Detalle Cuenta Colaborador','',3.40);


insert into kss_references values('salaryScheme','worker','none','Colaborador','',1);
insert into kss_references values('salaryScheme','job','none','Cargo','',2);
insert into kss_references values('salaryScheme','tab','none','Tabulador','',3);
insert into kss_references values('salaryScheme','jobTab','none','Cargo Tabulador','',4);
insert into kss_references values('scaleClassif','time','none','Tiempo','',1);
insert into kss_references values('scaleClassif','salary','none','Acumulado','',2);
insert into kss_references values('scaleClassif','novelty','none','Novedades','',3);
insert into kss_references values('scaleClassif','insurance','none','Primas de seguros','',4);
insert into kss_references values('scaleClassif','period','none','Mes o periodo','',5);
insert into kss_references values('sourceCategory','payroll','none','N�mina','',1);
insert into kss_references values('sourceCategory','agreement','none','Convenio','',1.10);
insert into kss_references values('sourceCategory','group','none','Grupo o turno de trabajo','',2);
insert into kss_references values('sourceCategory','paylocation','none','Ubicaci�n de n�mina','',3);
insert into kss_references values('sourceCategory','govClassif','none','Clasificaci�n p�blica','',4);
insert into kss_references values('sourceCategory','category1','none','Categoria 1','',5);
insert into kss_references values('sourceCategory','category2','none','Categoria 2','',6);
insert into kss_references values('sourceCategory','category3','none','Categoria 3','',7);
insert into kss_references values('sourceCategory','positionLevel','none','Nivel de puesto','',8);
insert into kss_references values('sourceCategory','tabulator','none','Tabulador','',9);
insert into kss_references values('sourceCategory','tabulatorAmn','none','Tabulador -Salario','',9.10);
insert into kss_references values('sourceCategory','tabulatorMid','none','Tabulador -Asignaci�n 1','',9.15);
insert into kss_references values('sourceCategory','tabulatorMax','none','Tabulador -Asignaci�n 2','',9.20);
insert into kss_references values('sourceCategory','tabulatorAllow','none','Tabulador -Asignaci�n 3','',9.25);



insert into kss_references values('timeUnit','0','none','No aplica','',0);
insert into kss_references values('timeUnit','2','none','Meses','',1);
insert into kss_references values('timeUnit','1','none','D�as -mes calendario','',2);
insert into kss_references values('timeUnit','4','none','D�as -mes comercial','',3);
insert into kss_references values('timeUnit','3','none','A�os','',4);
insert into kss_references values('timeUnit','5','none','Cuenta meses ','',5);
--Calculado el tiempo de antiguedad total, retorna el valor seg�n unidad indicada
insert into kss_references values('timeUnit','6','none','A�os tiempo calculado','',6);
insert into kss_references values('timeUnit','7','none','Meses tiempo calculado','',7);
insert into kss_references values('timeUnit','8','none','D�as tiempo calculado','',8);

insert into kss_references values('positionType','0','none','Activo','',0);
insert into kss_references values('positionType','1','none','Vacante','',1);
insert into kss_references values('positionType','2','none','Nuevo puesto','',2);
insert into kss_references values('positionType','9','none','Gasto General','',2);


insert into kss_references values('personID','document','none','Cedula','',1);
insert into kss_references values('personID','passport','none','Pasaporte','',2);
insert into kss_references values('personID','security','none','Seguro Social','',3);
insert into kss_references values('personID','tax','none','Identificacion Tributaria','',4);
insert into kss_references values('personID','driver','none','Licencia de conducir','',5);
insert into kss_references values('personID','military','none','Libreta militar','',6);
insert into kss_references values('personID','judicial','none','Certificado judicial','',7);
insert into kss_references values('personID','rrhhID','none','Identificador Unico RRHH','',8);

insert into kss_references values('companyID','tax','none','Identificaci�n fiscal o tributaria','',1);
insert into kss_references values('companyID','security','none','Seguro Social','',2);
insert into kss_references values('companyID','employment','none','Identificaci�n Laboral -NIL','',3);

insert into kss_references values('maritalStatus','single','none','Soltero','',1);
insert into kss_references values('maritalStatus','married','none','Casado','',2);
insert into kss_references values('maritalStatus','divorced','none','Divorciado','',3);
insert into kss_references values('maritalStatus','widowed','none','Viudo','',4);
insert into kss_references values('maritalStatus','concubinage','none','Concubino','',5);
insert into kss_references values('maritalStatus','other','none','Otro','',99);

insert into kss_references values('eduLevel','0','none','No asisti� a la escuela','',0.5);
insert into kss_references values('eduLevel','01','none','Primaria','',1);
insert into kss_references values('eduLevel','02','none','Secundaria','',2);
insert into kss_references values('eduLevel','03','none','Tecnico medio','',3);
insert into kss_references values('eduLevel','04','none','Tecnico superior','',4);
insert into kss_references values('eduLevel','05','none','Universitaria','',5);
insert into kss_references values('eduLevel','06','none','Especializaci�n','',6);
insert into kss_references values('eduLevel','07','none','Maestr�a','',7);
insert into kss_references values('eduLevel','08','none','Postgrado','',8);
insert into kss_references values('eduLevel','09','none','Doctorado','',9);
insert into kss_references values('eduLevel','10','none','Postdoctorado','',10);
insert into kss_references values('eduLevel','other','none','Otro','',99);

insert into kss_references values('partnerType','bank','none','Instituci�n financiera','',1);
insert into kss_references values('partnerType','union','none','Sindicato','',2);
insert into kss_references values('partnerType','health','none','Centro M�dico','',3);
insert into kss_references values('partnerType','kinder','none','Guarder�a','',4);
insert into kss_references values('partnerType','insurance','none','Seguro','',5);
insert into kss_references values('partnerType','educational','none','Entidad Educativa','',6);
insert into kss_references values('partnerType','supplier','none','Proveedor','',6);
insert into kss_references values('partnerType','client','none','Cliente','',6);

insert into kss_references values('partnerType','other','none','Otro','',7);

insert into kss_references values('economySector','extraction','none','Extraci�n','',1);
insert into kss_references values('economySector','service','none','Servicio','',2);
insert into kss_references values('economySector','commercial','none','Comercial','',3);
insert into kss_references values('economySector','agricultural','none','Agropecuario','',4);
insert into kss_references values('economySector','industrial','none','Indutrial','',5);
insert into kss_references values('economySector','transport','none','Transporte','',6);
insert into kss_references values('economySector','financial','none','Financiero','',7);
insert into kss_references values('economySector','construction','none','Construcci�n','',8);
insert into kss_references values('economySector','mining','none','Minero y energ�tico','',9);
insert into kss_references values('economySector','solidary','none','Solidarios o Cooperativas','',10);
insert into kss_references values('economySector','communication','none','Comunicaciones','',11);
insert into kss_references values('economySector','other','none','Otro','',12);

insert into kss_references values('ownerStock','1','none','P�blica','',1);
insert into kss_references values('ownerStock','2','none','Privada','',2);
insert into kss_references values('ownerStock','3','none','Mixta','',3);
insert into kss_references values('ownerStock','9','none','Otra','',4);

insert into kss_references values('kinderType','0','none','No aplica','',1);
insert into kss_references values('kinderType','1','none','Establecida','',2);
insert into kss_references values('kinderType','2','none','Compartida','',3);
insert into kss_references values('kinderType','3','none','No establecida','',4);
insert into kss_references values('kinderType','4','none','Pre-escolar','',5);
insert into kss_references values('kinderType','5','none','Fundaci�n','',6);

insert into kss_references values('paymentMethod','1','none','Efectivo','',2);
insert into kss_references values('paymentMethod','2','none','Transferencia','',3);
insert into kss_references values('paymentMethod','3','none','Cheque','',4);

insert into kss_references values('calcPaymethod','1','none','Efectivo','',1.10);
insert into kss_references values('calcPaymethod','2','none','Transferencia','',1.20);
insert into kss_references values('calcPaymethod','3','none','Cheque','',1.30);
insert into kss_references values('calcPaymethod','blank','none','Omitir n�mero de cuenta','',2);
insert into kss_references values('calcPaymethod','calctType','none','Tipo Calculo','',3.10);
insert into kss_references values('calcPaymethod','fund','none','Fondo','',4.20);
insert into kss_references values('calcPaymethod','fundBen','none','Fondo Beneficiario','',4.30);
insert into kss_references values('calcPaymethod','fundCalc','none','Fondo /Tipo Calculo','',5.20);
insert into kss_references values('calcPaymethod','fundBenCalc','none','Fondo Beneficiario / Tipo Calculo','',5.20);


insert into kss_references values('lookatAccount','cash','none','Efectivo','',1.10);
insert into kss_references values('lookatAccount','paymethod','none','Metodo de pago','',1.20);

insert into kss_references values('classifSettlement','1','none','Despido justificado','',2);
insert into kss_references values('classifSettlement','2','none','Despido injustificado','',3);
insert into kss_references values('classifSettlement','3','none','Renuncia voluntaria','',4);
insert into kss_references values('classifSettlement','4','none','Renuncia involuntaria','',5);
insert into kss_references values('classifSettlement','5','none','Jubilado','',6);
insert into kss_references values('classifSettlement','6','none','Pensionado','',7);
insert into kss_references values('classifSettlement','7','none','Traslado a otra empresa','',8);
insert into kss_references values('classifSettlement','8','none','Fallecimiento','',9);
insert into kss_references values('classifSettlement','9','none','Terminacion de contrato -TD','',10);
insert into kss_references values('classifSettlement','10','none','Reduccion de personal','',11);
insert into kss_references values('classifSettlement','99','none','Patronal -Uso exclusivo','',99);

insert into kss_references values('lookatIndic','na','none','No aplica','',1);
insert into kss_references values('lookatIndic','voluntary','none','Voluntaria','',2);
insert into kss_references values('lookatIndic','involuntary','none','Involuntaria','',3);
insert into kss_references values('rateType','0','none','No aplica','',1);
insert into kss_references values('rateType','1','none','Impuesto','',2);
insert into kss_references values('rateType','2','none','Subsidio','',3);
insert into kss_references values('rateType','3','none','Cr�dito','',4);

insert into kss_references values('taxPeriodicity','0','none','No aplica','',1);
insert into kss_references values('taxPeriodicity','7','none','Semanal','',2);
insert into kss_references values('taxPeriodicity','15','none','Quincinal','',3);
insert into kss_references values('taxPeriodicity','30','none','Mensual','',4);
insert into kss_references values('taxPeriodicity','360','none','Anual','',5);

insert into kss_references values('bankAccountType','saving','none','Ahorro','',1);
insert into kss_references values('bankAccountType','basicChecking','none','Corriente','',2);
insert into kss_references values('bankAccountType','interestChecking','none','Corriente con inter�s','',3);
insert into kss_references values('bankAccountType','moneyMarket','none','Dep�sito de mercado','',4);
insert into kss_references values('bankAccountType','certificate','none','Certificado de dep�sitos','',5);
insert into kss_references values('bankAccountType','trust','none','Fideicomiso','',6);
insert into kss_references values('bankAccountType','electronicCard','none','Tarjeta Electr�nica','',7);
insert into kss_references values('bankAccountType','popularCard','none','Tarjeta popular','',8);
insert into kss_references values('bankAccountType','other','none','Otro','',99);

insert into kss_references values('orgCategory','0','none','No aplica','',1);
insert into kss_references values('orgCategory','01','none','Empresa','',2);
insert into kss_references values('orgCategory','02','none','Establecimiento','',3);
insert into kss_references values('orgCategory','03','none','Unidad de explotaci�n','',4);
insert into kss_references values('orgCategory','04','none','Cooperativa','',5);

insert into kss_references values('weekday','0','none','No aplica','',0);
insert into kss_references values('weekday','1','none','Domingo','',1);
insert into kss_references values('weekday','2','none','Lunes','',2);
insert into kss_references values('weekday','3','none','Martes','',3);
insert into kss_references values('weekday','4','none','Mi�rcoles','',4);
insert into kss_references values('weekday','5','none','Jueves','',5);
insert into kss_references values('weekday','6','none','Viernes','',6);
insert into kss_references values('weekday','7','none','S�bado','',7);

insert into kss_references values('classifAbs','0','none','No Aplica','',1);
insert into kss_references values('classifAbs','1','none','Enfermedad com�n','',3);
insert into kss_references values('classifAbs','2','none','Enfermedad ocupacional','',4);
insert into kss_references values('classifAbs','3','none','Suspensi�n temporal','',5);
insert into kss_references values('classifAbs','4','none','Permiso no remunerado','',6);
insert into kss_references values('classifAbs','5','none','Permiso maternidad','',7);
insert into kss_references values('classifAbs','6','none','Vacaciones','',2);
insert into kss_references values('classifAbs','7','none','Permiso paternidad','',8);
insert into kss_references values('classifAbs','8','none','Permiso remunerado','',9);
insert into kss_references values('classifAbs','9','none','Accidente laboral','',10);
insert into kss_references values('classifAbs','10','none','Accidente com�n','',11);





insert into kss_references values('forDetermine','taxmet01','none','Impuesto -Venezuela','',1.10);
insert into kss_references values('forDetermine','taxpan01','none','Impuesto -Panama','',1.15);
insert into kss_references values('forDetermine','taxpan02','none','Impuesto Gasto Representaci�n -Panama','',1.20);
insert into kss_references values('forDetermine','taxpan03','none','Impuesto XIII -Panama','',1.30);

--insert into kss_references values('forDetermine','taxmet02.1','none','Retenci�n impuesto base -Panama','',1.21);
--insert into kss_references values('forDetermine','taxmet02.2','none','Retenci�n impuesto variable -Panama','',1.22);
--insert into kss_references values('forDetermine','taxmet02.3','none','Retenci�n impuesto proyectado -Panama','',1.23);

--insert into kss_references values('forDetermine','taxmet02.1','none','Retenci�n impuesto XIII -Panama','',1);

insert into kss_references values('forDetermine','pive001','none','C�lculo intereses prestaciones','',8);
insert into kss_references values('forDetermine','pive001a','none','C�lculo intereses prestaciones -saldo final periodo','',8.10);
--insert into kss_references values('forDetermine','pive001a1','none','Intereses/P -Total Abono mes anterior','',8.20);
--insert into kss_references values('forDetermine','pive001a','none','Intereses/P -Capital  mes anterior','',8.30);
insert into kss_references values('forDetermine','pive001b','none','Intereses/P -Capital  mes anterior','',8.30);
--insert into kss_references values('forDetermine','pive001c','none','Intereses sobre prestaciones [-]','',8.40);
--insert into kss_references values('forDetermine','pive001d','none','Intereses/P -Abono mes anterior [-]','',8.50);
--insert into kss_references values('forDetermine','pive001e','none','Intereses/P -Capital mes anterior [-]','',8.60);
insert into kss_references values('forDetermine','pive002','none','Pago intereses prestaciones','',9);
insert into kss_references values('forDetermine','pive028','none','Intereses de mora - Fin relaci�n','',9.10);         

insert into kss_references values('forDetermine','pive003','none','Garant�as prestaciones -Fin relaci�n','',10);
--insert into kss_references values('forDetermine','pive004','none','Garant�as Finiquito diferencia de Abono','',10.10);
--insert into kss_references values('forDetermine','pive005','none','Inter�s Abonos Fideicomiso','',10.20);
insert into kss_references values('forDetermine','pive006','none','Ajuste de Inter�s/Prestaciones -Tasa','',10.30);
insert into kss_references values('forDetermine','pive006a','none','Ajuste de Inter�s/Prestaciones -Capital','',10.50);
insert into kss_references values('forDetermine','pive007','none','Inter�s Prest. en beneficio','',11);
insert into kss_references values('forDetermine','pive007a','none','Inter�s sobre saldo en beneficio','',11.10);
--insert into kss_references values('forDetermine','pive008','none','Aporte de seguro -Trabajador','',12);
--insert into kss_references values('forDetermine','pive008a','none','Aporte de seguro, frecuencia n�mina -Trabajador','',12.10);
--insert into kss_references values('forDetermine','pive008b','none','Aporte de seguro edad inicial -Trabajador','',12.20);
--insert into kss_references values('forDetermine','pive008c','none','Aporte de seguro, edad y frecuencia -Trabajador','',12.30);
--insert into kss_references values('forDetermine','pive008d','none','Aporte de seguro, frecuencia n�mina -Trabajador (Retiro)','',12.40);
--insert into kss_references values('forDetermine','pive008e','none','Aporte de seguro, edad y frecuencia -Trabajador (Retiro)','',12.50);
--insert into kss_references values('forDetermine','pive009','none','Aporte de seguro -Empresa','',12.60);
--insert into kss_references values('forDetermine','pive009a','none','Aporte de seguro, frecuencia n�mina -Empresa','',12.70);
--insert into kss_references values('forDetermine','pive009b','none','Aporte de seguro edad inicial -Empresa','',12.80);
--insert into kss_references values('forDetermine','pive009c','none','Aporte de seguro, edad y frecuencia -Empresa','',12.82);
--insert into kss_references values('forDetermine','pive009d','none','Aporte de seguro, frecuencia n�mina -Empresa (Retiro)','',12.84);
--insert into kss_references values('forDetermine','pive009e','none','Aporte de seguro, edad y frecuencia -Empresa (Retiro)','',12.86);
insert into kss_references values('forDetermine','pive010','none','Provisi�n de vacaci�n','',13);
--insert into kss_references values('forDetermine','pive010a','none','Provisi�n de vacaci�n - cancelada anual','',13.10);
--insert into kss_references values('forDetermine','pive010b','none','Provisi�n de vacaci�n - Saldo total','',13.20);
--insert into kss_references values('forDetermine','pive010c','none','Provisi�n de vacaci�n ajustada','',13.30);
--insert into kss_references values('forDetermine','pive011','none','Guarder�as','',14);
insert into kss_references values('forDetermine','pive013','none','Fecha de pago = movimiento','',15);
insert into kss_references values('forDetermine','pive014','none','Cuotas especiales -prestamos','',16);
insert into kss_references values('forDetermine','pive014a','none','Cuotas especiales -prestamos a�o vac.','',16.10);
--insert into kss_references values('forDetermine','pive015','none','Cantidad -Saldo vacaciones vencidas','',17);
insert into kss_references values('forDetermine','pive016','none','A�os de vacaciones pendientes','',17.10);
insert into kss_references values('forDetermine','pive018','none','Meses de prestaciones acumuladas','',18);
insert into kss_references values('forDetermine','pive019','none','Prestaciones acumuladas entre fechas','',18.10);
--insert into kss_references values('forDetermine','pive020','none','Prestaciones acumuladas de un concepto','',18.20);
--insert into kss_references values('forDetermine','pive021','none','Total de d�as -Art 108, LOT','',18.30);
insert into kss_references values('forDetermine','pive021a','none','Retroactividad superior a 6 meses','',18.34);
insert into kss_references values('forDetermine','pive021a1','none','Retroactividad','',18.36);
insert into kss_references values('forDetermine','pive021b','none','Cantidad por tiempo de servicio','',18.38);
insert into kss_references values('forDetermine','pive021c','none','Cantidad por tiempo de servicio trimestral ','',18.40);
insert into kss_references values('forDetermine','pive022','none','D�as adicionales a pagar -Art 108, LOT','',18.50);
insert into kss_references values('forDetermine','pive023','none','Selecci�n de abonos/prest. como salario','',18.60);
insert into kss_references values('forDetermine','pive024','none','Disponible -Prestaciones sociales','',18.70);
insert into kss_references values('forDetermine','pive025a','none','S�bados de vacaci�n en finiquito','',19);
insert into kss_references values('forDetermine','pive025b','none','Domingos de vacaci�n en finiquito','',19.10);
insert into kss_references values('forDetermine','pive025c','none','Feriados de vacaci�n en finiquito','',19.20);
insert into kss_references values('forDetermine','pive026','none','Abono de Garant�a Trimestral','',18.74);
insert into kss_references values('forDetermine','pive027a','none','Cantidad de D�as de la semana considerando ausencias','',19.30); 
--insert into kss_references values('forDetermine','pive027b','none','D�as en el per�odo, por toda ausencia','',19.40); 
--insert into kss_references values('forDetermine','pive027c','none','D�as en el per�odo, ausencia distinta vacaci�n','',19.50); 
insert into kss_references values('forDetermine','pive029','none','Feriados en vacaciones -sin descanso','',19.52); 
insert into kss_references values('forDetermine','pive029a','none','Feriados en vacaciones -con descanso','',19.53); 
insert into kss_references values('forDetermine','pive030','none','Descasos en vacaciones -sin feriado','',19.60); 
insert into kss_references values('forDetermine','pive030a','none','Descasos en vacaciones -con feriado','',19.65); 

insert into kss_references values('forDetermine','proratePeriod','none','Prorratear d�as - periodo','',20.1);
insert into kss_references values('forDetermine','prorateMonth','none','Prorratear d�as - mes comercial','',20.2);
insert into kss_references values('forDetermine','vacationPaid','none','Vacaci�n pagadas -Provisi�n','',21.2);
insert into kss_references values('forDetermine','pive011','none','Calculo guarder�a','',25);
insert into kss_references values('forDetermine','valSalary','none','Sumar valor a Salario','',26);
insert into kss_references values('forDetermine','picustom','none','Funci�n adaptada o personalizada','',99.50); 

insert into kss_references values('determineElem','0','none','No aplica','',1);
--insert into kss_references values('determineElem','salaryScale','none','Escala de salario','',1); --temporary
--insert into kss_references values('determineElem','timeScale','none','Escala de tiempo','',1); --temporary

insert into kss_references values('determineElem','groupRota','none','Rotaci�n grupo','',2);
--insert into kss_references values('determineElem','calendarMonth','none','Monto por mes calendario','',2.01);
--insert into kss_references values('determineElem','riskCenter','none','Riesgo centro de trabajo','',3);
insert into kss_references values('determineElem','monday','none','Cantidad de d�as lunes en el per�odo','',4);
insert into kss_references values('determineElem','saturday','none','Cantidad de d�as s�bados en el per�odo','',5);
insert into kss_references values('determineElem','sunday','none','Cantidad de d�as domingos en el per�odo','',6);
insert into kss_references values('determineElem','period','none','Cantidad de d�as en el periodo','',7);
insert into kss_references values('determineElem','periodMonth','none','Cantidad de meses calendarios en el periodo','',7.05);
insert into kss_references values('determineElem','periodBiz','none','Cantidad de d�as comercial en el periodo','',7.10);
insert into kss_references values('determineElem','hiringday','none','Cantidad de d�as de ingreso en el periodo','',7.14);
insert into kss_references values('determineElem','holiday','none','Cantidad de d�as feriados en el per�odo','',9);
insert into kss_references values('determineElem','dayoff','none','Cantidad de d�as de descanso en el per�odo','',10);
insert into kss_references values('determineElem','daysMonth','none','Dias del mes en proceso','',10.10);
--insert into kss_references values('determineElem','department','none','Monto por Departamento','',11);
insert into kss_references values('determineElem','job','none','Monto por Cargo','',12);
insert into kss_references values('determineElem','payLocation','none','Ubicaci�n de n�mina','',13);
--insert into kss_references values('determineElem','positionLevel','none','Nivel de puesto','',14);
insert into kss_references values('determineElem','minWage','none','Salario m�nimo','',15);
insert into kss_references values('determineElem','taxUnit','none','Unidad tributaria','',16);
--insert into kss_references values('determineElem','dailyTickets','none','Cantidad de tickets diarios','',16.10);

insert into kss_references values('determineElem','workcenter','none','Riesgo por Centro de Trabajo','',17);
insert into kss_references values('determineElem','dayAbsence','none','D�as ausentes en el periodo','',18);
--insert into kss_references values('determineElem','monAbsence','none','Lunes ausentes en el periodo','',18.10);
insert into kss_references values('determineElem','timeDecimal','none','Convertir tiempo a decimal','',19);
insert into kss_references values('determineElem','accumQty','none','Cantidad acumulada','',20);

--insert into kss_references values('determineElem','vacHoliday','none','D�as feriados en vacaciones','',22.00); 
insert into kss_references values('determineElem','pivePro001','none','Salario promedio a fecha de movimiento','',50.50); 
insert into kss_references values('determineElem','currencyRate','none','Tasa de cambio','',60); 

insert into kss_references values('formulaType','0','none','No aplica','',1);
insert into kss_references values('formulaType','01','none','Salario * Cantidad * Factor','',2);
insert into kss_references values('formulaType','02','none','Cantidad * Valor ','',2.10);
insert into kss_references values('formulaType','03','none','Salario * Factor','',2.20);
insert into kss_references values('formulaType','04','none','Salario * Cantidad * Factor * Valor','',2.30);
insert into kss_references values('formulaType','05','none','Salario * Cantidad * Factor / Valor','',2.34);
insert into kss_references values('formulaType','06','none','Salario * Cantidad / Factor','',2.40);
insert into kss_references values('formulaType','07','none','Cantidad * Valor * Factor','',2.12);
insert into kss_references values('formulaType','08','none','Cantidad * Valor / Factor','',2.14);
insert into kss_references values('formulaType','09','none','Valor * Factor','',2.16);
insert into kss_references values('formulaType','10','none','Salario * Cantidad','',2.16);
insert into kss_references values('formulaType','11','none','Salario * Factor / Valor','',2.22);


insert into kss_references values('purposeAccum','calc','none','C�lculo','',1);
insert into kss_references values('purposeAccum','report','none','Reporte','',2);
insert into kss_references values('purposeAccum','group','none','Agrupador','',3);
insert into kss_references values('purposeAccum','fund','none','Dep�sito en fondo','',4);
insert into kss_references values('purposeAccum','trust','none','Fondo de Garantia','',5);

insert into kss_references values('lookatFund','0','none','No aplica','',1);
insert into kss_references values('lookatFund','1','none','Aporte colaborador','',2);
insert into kss_references values('lookatFund','2','none','Aporte empresa','',3);
insert into kss_references values('lookatFund','3','none','Prestamo','',4);
insert into kss_references values('lookatFund','4','none','Aporte voluntario -Colabarodor','',5);
insert into kss_references values('lookatFund','5','none','Aporte voluntario -Empresa','',6);
insert into kss_references values('lookatFund','6','none','Amortizaci�n','',6);


insert into kss_references values('initialVal','salary','none','Salario base','',1);
insert into kss_references values('initialVal','minWage','none','Salario m�nimo','',1);
insert into kss_references values('initialVal','taxUnit','none','Unidad tributaria','',1);

insert into kss_references values('accumFunc','amount','none','Monto acumulado','',1);
insert into kss_references values('accumFunc','quantity','none','Cantidad acumulada','',2);
insert into kss_references values('accumFunc','daysAccum','none','D�as acumulados','',3);
insert into kss_references values('accumFunc','daysProc','none','D�as en proceso','',4);
insert into kss_references values('accumFunc','daysMonth','none','D�as del mes en proceso','',4.10);
insert into kss_references values('accumFunc','afve001','none','Conceptos en beneficio -Saldo','',5);
insert into kss_references values('accumFunc','afve001b','none','Conceptos en beneficio -Monto','',5.5);
insert into kss_references values('accumFunc','afve001c','none','Conceptos en beneficio -Valor','',5.75);
insert into kss_references values('accumFunc','afve002','none','Conceptos periodo calculado','',6);
insert into kss_references values('accumFunc','afve004','none','Garant�as prestaciones','',6.5);
insert into kss_references values('accumFunc','afve006','none','Periodos SSO -Salario variable','',7);
insert into kss_references values('accumFunc','afve006a','none','Periodos SSO -Salario mixto','',8);
insert into kss_references values('accumFunc','afve006d','none','Hasta fecha de movimiento','',8.4);
insert into kss_references values('accumFunc','afve015','none','Saldo historial de vacaciones','',10.1);
insert into kss_references values('accumFunc','afve011b','none','Hasta semana anterior a aniversario','',10.2);
insert into kss_references values('accumFunc','afve011','none','Hasta semana en aniversario','',10.3);
insert into kss_references values('accumFunc','afve016','none','Fondo de garant�as','',10.4);
insert into kss_references values('accumFunc','afve017','none','Saldo historial beneficio','',11);
insert into kss_references values('accumFunc','afve018','none','Conceptos pagados en el mes','',12);


insert into kss_references values('userGroup','notifier','none','Notificaci�n','',1);

insert into kss_references values('userType','super','none','Super usuario','',1);
insert into kss_references values('userType','admin','none','Administrador','',2);
insert into kss_references values('userType','veri','none','Verificador','',3);
insert into kss_references values('userType','plan','none','Planificador','',4);

insert into kss_references values('subsMaxElem','wage','none','Sueldo o salario','',1);
insert into kss_references values('subsMaxElem','quantity','none','Cantidad','',2);
insert into kss_references values('subsMaxElem','factor','none','Factor','',3);
insert into kss_references values('subsMaxElem','value','none','Valor','',4);
insert into kss_references values('subsMaxElem','amount','none','Monto','',5); 

insert into kss_references values('subsMaxCond','greater','none','Mayor que','',1);
insert into kss_references values('subsMaxCond','greaterDif','none','Mayor que -Diferencia','',1.5);
insert into kss_references values('subsMaxCond','greaterZero','none','Mayor que -Diferencia o cero','',1.8);
insert into kss_references values('subsMaxCond','less','none','Menor que','',2);
insert into kss_references values('subsMaxCond','increase3Months','none','Incremento salario �ltimos 3 meses','',3);
insert into kss_references values('subsMaxCond','seniority1Month','none','Antig�edad menor o igual a 1 mes','',4);
insert into kss_references values('subsMaxCond','lessVac','none','Menor que -Regreso de vacaciones','',5);

insert into kss_references values('salDetermine','0','none','No aplica','',1);
insert into kss_references values('salDetermine','01','none','Salario m�nimo','',2);
insert into kss_references values('salDetermine','02','none','Unidad tributaria','',2);
insert into kss_references values('salDetermine','03','none','Tabulador','',2);
insert into kss_references values('salDetermine','04','none','Cargo tabulador','',2);
insert into kss_references values('salDetermine','05','none','Nivel de tabulador','',2);
insert into kss_references values('salDetermine','06','none','Diferencia nivel tabulador','',2);
insert into kss_references values('salDetermine','71','none','Salario sustitivo -Mayor','',2);
insert into kss_references values('salDetermine','72','none','Salario sustitivo -Menor','',2);
insert into kss_references values('salDetermine','73','none','Salario sustitivo -Aumento <=3 meses','',2);
insert into kss_references values('salDetermine','74','none','Salario sustitivo -Antig�edad <= 1 mes','',2);

insert into kss_references values('nationality','AFG','none','Afgana','',1);
insert into kss_references values('nationality','ALB','none','Albanesa','',2);
insert into kss_references values('nationality','ALE','none','Alemana','',3);
insert into kss_references values('nationality','AND','none','Andorrana','',4);
insert into kss_references values('nationality','AGO','none','Angolesa','',5);
insert into kss_references values('nationality','ATG','none','Antiguana','',6);
insert into kss_references values('nationality','ANT','none','Antillana','',7);
insert into kss_references values('nationality','SAU','none','Arabe','',8);
insert into kss_references values('nationality','DZA','none','Argelina','',9);
insert into kss_references values('nationality','ARG','none','Argentina','',10);
insert into kss_references values('nationality','ABW','none','Arube�a','',11);
insert into kss_references values('nationality','AUS','none','Australiana','',12);
insert into kss_references values('nationality','AUT','none','Austriaca','',13);
insert into kss_references values('nationality','AZE','none','Azer�','',14);
insert into kss_references values('nationality','BHS','none','Bahame�a','',15);
insert into kss_references values('nationality','BHR','none','Bahreinita','',16);
insert into kss_references values('nationality','BGD','none','Bangladesh�','',17);
insert into kss_references values('nationality','BRB','none','Barbadense','',18);
insert into kss_references values('nationality','BEL','none','Belga','',19);
insert into kss_references values('nationality','BLZ','none','Belice�a','',20);
insert into kss_references values('nationality','BEN','none','Beninesa','',21);
insert into kss_references values('nationality','BMU','none','Bermude�a','',22);
insert into kss_references values('nationality','BLR','none','Bielorrusa','',23);
insert into kss_references values('nationality','birmana','none','Birmana','',24);
insert into kss_references values('nationality','BOL','none','Boliviana','',25);
insert into kss_references values('nationality','BIH','none','Bosnia','',26);
insert into kss_references values('nationality','BWA','none','Botsuanesa','',27);
insert into kss_references values('nationality','BRA','none','Brasile�a','',28);
insert into kss_references values('nationality','GBR','none','Brit�nico','',29);
insert into kss_references values('nationality','BRN','none','Bruneana','',30);
insert into kss_references values('nationality','BGR','none','B�lgara','',31);
insert into kss_references values('nationality','BFA','none','Burkinesa','',32);
insert into kss_references values('nationality','BDI','none','Burundesa','',33);
insert into kss_references values('nationality','BHU','none','Butanesa','',34);
insert into kss_references values('nationality','CPV','none','Caboverdiana','',35);
insert into kss_references values('nationality','KHM','none','Camboyana','',36);
insert into kss_references values('nationality','CMR','none','Camerunesa','',37);
insert into kss_references values('nationality','CAN','none','Canadiense','',38);
insert into kss_references values('nationality','ceilandesa','none','Ceilandesa','',39);
insert into kss_references values('nationality','CAF','none','Centroafricana','',29);
insert into kss_references values('nationality','TCD','none','Chadiana','',30);
insert into kss_references values('nationality','CZE','none','Checa','',31);
insert into kss_references values('nationality','CHL','none','Chilena','',32);
insert into kss_references values('nationality','CHN','none','China','',33);
insert into kss_references values('nationality','CYP','none','Chipriota','',34);
insert into kss_references values('nationality','COL','none','Colombiana','',35);
insert into kss_references values('nationality','COM','none','Comorana','',36);
insert into kss_references values('nationality','COG','none','Congole�a','',37);
insert into kss_references values('nationality','CIV','none','Costamarfile�o','',38);
insert into kss_references values('nationality','CRI','none','Costarricense','',39);
insert into kss_references values('nationality','HRV','none','Croata','',40);
insert into kss_references values('nationality','CUB','none','Cubana','',41);
insert into kss_references values('nationality','DNK','none','Danesa','',42);
insert into kss_references values('nationality','SLB','none','De las Islas Salom�n','',1);
insert into kss_references values('nationality','DOM','none','Dominicana','',1);
insert into kss_references values('nationality','ECU','none','Ecuatoriana','',1);
insert into kss_references values('nationality','EGY','none','Egipcia','',1);
insert into kss_references values('nationality','SLV','none','Eritrea','',1);
insert into kss_references values('nationality','SVK','none','Eslovaca','',1);
insert into kss_references values('nationality','SVN','none','Eslovena','',1);
insert into kss_references values('nationality','ESP','none','Espa�ola','',1);
insert into kss_references values('nationality','USA','none','Estadounidense','',1);
insert into kss_references values('nationality','EST','none','Estonia','',1);
insert into kss_references values('nationality','ETH','none','Et�ope','',1);
insert into kss_references values('nationality','PHL','none','Filipina','',1);
insert into kss_references values('nationality','FJI','none','Fiyiana','',1);
insert into kss_references values('nationality','FRA','none','Francesa','',1);
insert into kss_references values('nationality','GAB','none','Gabonesa','',1);
insert into kss_references values('nationality','GMB','none','Gambiana','',1);
insert into kss_references values('nationality','GEO','none','Georgiana','',1);
insert into kss_references values('nationality','GHA','none','Ghanesa','',1);
insert into kss_references values('nationality','GRD','none','Granadina','',1);
insert into kss_references values('nationality','GRC','none','Griega','',1);
insert into kss_references values('nationality','guatemalteca','none','Guatemalteca','',1);
insert into kss_references values('nationality','guineana','none','Guineana','',1);
insert into kss_references values('nationality','guyanesa','none','Guyanesa','',1);
insert into kss_references values('nationality','haitiana','none','Haitiana','',1);
insert into kss_references values('nationality','holandesa','none','Holandesa','',1);
insert into kss_references values('nationality','hondurena','none','Hondure�a','',1);
insert into kss_references values('nationality','hongkonesa','none','Hongkonesa','',1);
insert into kss_references values('nationality','hungara','none','H�ngara','',1);
insert into kss_references values('nationality','india','none','India','',1);
insert into kss_references values('nationality','indonesica','none','Indon�sica','',1);
insert into kss_references values('nationality','irani','none','Iran�','',1);
insert into kss_references values('nationality','iraqui','none','Iraqu�','',1);
insert into kss_references values('nationality','irlandesa','none','Irlandesa','',1);
insert into kss_references values('nationality','islandesa','none','Islandesa','',1);
insert into kss_references values('nationality','israeli','none','Israel�','',1);
insert into kss_references values('nationality','italiana','none','Italiana','',1);
insert into kss_references values('nationality','jamaicana','none','Jamaicana','',1);
insert into kss_references values('nationality','japonesa','none','Japonesa','',1);
insert into kss_references values('nationality','jordana','none','Jordana','',1);
insert into kss_references values('nationality','kazaja','none','Kazaja','',1);
insert into kss_references values('nationality','keniana','none','Keniana','',1);
insert into kss_references values('nationality','kirguizo','none','Kirguizo','',1);
insert into kss_references values('nationality','kuwaiti','none','Kuwait�','',1);
insert into kss_references values('nationality','laosiana','none','Laosiana','',1);
insert into kss_references values('nationality','lesota','none','Lesota','',1);
insert into kss_references values('nationality','letona','none','Letona','',1);
insert into kss_references values('nationality','libanesa','none','Libanesa','',1);
insert into kss_references values('nationality','liberiana','none','Liberiana','',1);
insert into kss_references values('nationality','libia','none','Libia','',1);
insert into kss_references values('nationality','liechtenstein','none','Liechtenstein','',1);
insert into kss_references values('nationality','lituana','none','Lituana','',1);
insert into kss_references values('nationality','luxemburguesa','none','Luxemburguesa','',1);
insert into kss_references values('nationality','macedonia','none','Macedonia','',1);
insert into kss_references values('nationality','malasia','none','Malasia','',1);
insert into kss_references values('nationality','malaui','none','Malaui','',1);
insert into kss_references values('nationality','maldivia','none','Maldivia','',1);
insert into kss_references values('nationality','maldova','none','Maldova','',1);
insert into kss_references values('nationality','malgache','none','Malgache','',1);
insert into kss_references values('nationality','maliensa','none','Maliensa','',1);
insert into kss_references values('nationality','maltesa','none','Maltesa','',1);
insert into kss_references values('nationality','marroqui','none','Marroqu�','',1);
insert into kss_references values('nationality','mauriciana','none','Mauriciana','',1);
insert into kss_references values('nationality','mauritania','none','Mauritania','',1);
insert into kss_references values('nationality','mexicana','none','Mexicana','',1);
insert into kss_references values('nationality','micronesia','none','Micronesia','',1);
insert into kss_references values('nationality','Moldava','none','Moldava','',1);
insert into kss_references values('nationality','Monegasca','none','Monegasca','',1);
insert into kss_references values('nationality','Mongol','none','Mongol','',1);
insert into kss_references values('nationality','Mozambiquena','none','Mozambique�a','',1);
insert into kss_references values('nationality','Namibiana','none','Namibiana','',1);
insert into kss_references values('nationality','Nauruana','none','Nauruana','',1);
insert into kss_references values('nationality','Neozelandesa','none','Neozelandesa','',1);
insert into kss_references values('nationality','Nepalesa','none','Nepalesa','',1);
insert into kss_references values('nationality','Nicarag�ense','none','Nicarag�ense','',1);
insert into kss_references values('nationality','Nigeria','none','Niger�a','',1);
insert into kss_references values('nationality','Nigeriana','none','Nigeriana','',1);
insert into kss_references values('nationality','Norcoreana','none','Norcoreana','',1);
insert into kss_references values('nationality','Noruega','none','Noruega','',1);
insert into kss_references values('nationality','Omani','none','Oman�','',1);
insert into kss_references values('nationality','Otro','none','Otro','',1);
insert into kss_references values('nationality','Pakistani','none','Pakistan�','',1);
insert into kss_references values('nationality','Palao','none','Palao','',1);
insert into kss_references values('nationality','Panamena','none','Paname�a','',1);
insert into kss_references values('nationality','Papu','none','Pap�','',1);
insert into kss_references values('nationality','Paraguaya','none','Paraguaya','',1);
insert into kss_references values('nationality','Peruana','none','Peruana','',1);
insert into kss_references values('nationality','Polaca','none','Polaca','',1);
insert into kss_references values('nationality','Portuguesa','none','Portuguesa','',1);
insert into kss_references values('nationality','Puertorriquena','none','Puertorrique�a','',1);
insert into kss_references values('nationality','Qatariana','none','Qatariana','',1);
insert into kss_references values('nationality','Ruandesa','none','Ruandesa','',1);
insert into kss_references values('nationality','Rumana','none','Rumana','',1);
insert into kss_references values('nationality','Rusa','none','Rusa','',1);
insert into kss_references values('nationality','Salvadorena','none','Salvadore�a','',1);
insert into kss_references values('nationality','Samoana','none','Samoana','',1);
insert into kss_references values('nationality','Sancristobalense','none','Sancristobalense','',1);
insert into kss_references values('nationality','Sanmarinense','none','Sanmarinense','',1);
insert into kss_references values('nationality','Santalucense','none','Santalucense','',1);
insert into kss_references values('nationality','Santomense','none','Santomense','',1);
insert into kss_references values('nationality','Sanvicentina','none','Sanvicentina','',1);
insert into kss_references values('nationality','Saudita','none','Saudita','',1);
insert into kss_references values('nationality','Senegalesa','none','Senegalesa','',1);
insert into kss_references values('nationality','Seychellese','none','Seychellese','',1);
insert into kss_references values('nationality','Sierraleones','none','Sierraleon�s','',1);
insert into kss_references values('nationality','Singapuriana','none','Singapuriana','',1);
insert into kss_references values('nationality','Siria','none','Siria','',1);
insert into kss_references values('nationality','Somali','none','Somal�','',1);
insert into kss_references values('nationality','Suazilandesa','none','Suazilandesa','',1);
insert into kss_references values('nationality','Sudafricana','none','Sudafricana','',1);
insert into kss_references values('nationality','Sudanesa','none','Sudanesa','',1);
insert into kss_references values('nationality','Sueca','none','Sueca','',1);
insert into kss_references values('nationality','Suiza','none','Suiza','',1);
insert into kss_references values('nationality','Surcoreana','none','Surcoreana','',1);
insert into kss_references values('nationality','Surinamesa','none','Surinamesa','',1);
insert into kss_references values('nationality','Tailandesa','none','Tailandesa','',1);
insert into kss_references values('nationality','Taiwanesa','none','Taiwanesa','',1);
insert into kss_references values('nationality','Tanzana','none','Tanzana','',1);
insert into kss_references values('nationality','Tayik','none','Tayik','',1);
insert into kss_references values('nationality','Timorense','none','Timorense','',1);
insert into kss_references values('nationality','Togolesa','none','Togolesa','',1);
insert into kss_references values('nationality','Tongana','none','Tongana','',1);
insert into kss_references values('nationality','Trinitaria','none','Trinitaria','',1);
insert into kss_references values('nationality','Tunecina','none','Tunecina','',1);
insert into kss_references values('nationality','Turca','none','Turca','',1);
insert into kss_references values('nationality','Turcomana','none','Turcomana','',1);
insert into kss_references values('nationality','tuvaluana','none','Tuvaluana','',1);
insert into kss_references values('nationality','ucraniana','none','Ucraniana','',1);
insert into kss_references values('nationality','ugandesa','none','Ugandesa','',1);
insert into kss_references values('nationality','uruguaya','none','Uruguaya','',1);
insert into kss_references values('nationality','uzbeko','none','Uzbeko','',1);
insert into kss_references values('nationality','vanuatense','none','Vanuatense','',185);
insert into kss_references values('nationality','vaticana','none','Vaticana','',186);
insert into kss_references values('nationality','VEN','none','Venezolana','',187);
insert into kss_references values('nationality','vietnamita','none','Vietnamita','',188);
insert into kss_references values('nationality','YEM','none','Yemenita','',189);
insert into kss_references values('nationality','DJI','none','Yibutiense','',190);
insert into kss_references values('nationality','yugoslava','none','Yugoslava','',191);
insert into kss_references values('nationality','zairense','none','Zairense','',192);
insert into kss_references values('nationality','ZMB','none','Zambiana','',193);
insert into kss_references values('nationality','ZWE','none','Zimbabuense','',194);
insert into kss_references values('nationality','OTHER','none','Extranjero','',201);

insert into kss_references values('disabilityCon','01','none','Temporal','',1);
insert into kss_references values('disabilityCon','02','none','Parcial permanente','',2);
insert into kss_references values('disabilityCon','03','none','Total permanente','',3);
insert into kss_references values('disabilityCon','04','none','Absoluta permanente','',4);

insert into kss_references values('disabilityOri','01','none','Congenita','',1);
insert into kss_references values('disabilityOri','02','none','Adquirida','',2);
insert into kss_references values('disabilityOri','03','none','Hereditaria','',3);
insert into kss_references values('disabilityOri','04','none','Accidente com�n','',4);
insert into kss_references values('disabilityOri','05','none','Accidente laboral','',5);
insert into kss_references values('disabilityOri','06','none','Enfermedad com�n','',6);
insert into kss_references values('disabilityOri','07','none','Enfermedad laboral','',7);


insert into kss_references values('disabilityType','hearing','none','Auditiva','',1);
insert into kss_references values('disabilityType','muscle','none','Musculo-esqueletica','',2);
insert into kss_references values('disabilityType','visual','none','Visual','',3);
insert into kss_references values('disabilityType','intellectual','none','Intelectual','',4);
insert into kss_references values('disabilityType','mental','none','Mental','',4.4);
insert into kss_references values('disabilityType','dwarf','none','Talla baja','',5);
insert into kss_references values('disabilityType','other','none','Otra','',99);

insert into kss_references values('laborSit','permanent','none','Fijo','',1);
insert into kss_references values('laborSit','contract','none','Contratado','',2);
insert into kss_references values('laborSit','passant','none','Pasante','',3);
insert into kss_references values('laborSit','trainee','none','Aprendiz','',4);


insert into kss_references values('laborOcc','partner','none','Propietario o socio','',1);
insert into kss_references values('laborOcc','manager','none','Gerente o director','',2);
insert into kss_references values('laborOcc','employee','none','Empleado','',3);
insert into kss_references values('laborOcc','worker','none','Obrero','',4);

insert into kss_references values('durationUnit','hours','none','Horas','',1);
insert into kss_references values('durationUnit','days','none','D�as','',2);

insert into kss_references values('depType','dir','none','Direcci�n','',1);
--insert into kss_references values('depType','staff','none','Staff','',2);
insert into kss_references values('depType','manager','none','Gerencia','',3);
insert into kss_references values('depType','dep','none','Departamento','',4);
--insert into kss_references values('depType','coord','none','Coordinaci�n','',5);
insert into kss_references values('depType','sec','none','Divisi�n','',6);
insert into kss_references values('depType','area','none','Area','',7);
insert into kss_references values('depType','na','none','No aplica','',99);


insert into kss_references values('replaceWhen','beJob','none','Cargo','',1);
insert into kss_references values('replaceWhen','beReason','none','Motivo fin relaci�n','',2);
insert into kss_references values('replaceWhen','bePaylocation','none','Ubicaci�n n�mina','',3);
insert into kss_references values('replaceWhen','beWorkcenter','none','Centro de trabajo','',4);
insert into kss_references values('replaceWhen','beBenefit','none','Beneficio ','',5);
insert into kss_references values('replaceWhen','beBenefitAmount','none','Beneficio -monto','',5.10);
insert into kss_references values('replaceWhen','beBenefitCurrBalance','none','Beneficio -saldo actual','',5.20);
insert into kss_references values('replaceWhen','beBenefitFinalBalance','none','Beneficio -saldo final','',5.30);

insert into kss_references values('replaceWhen','beGroup','none','Grupo','',6);
insert into kss_references values('replaceWhen','bePrevSalary','none','Salario anterior','',7);
insert into kss_references values('replaceWhen','beDifSalary','none','Diferencia salario','',8);


--
insert into kss_references values('officialRep','01','none','Clase de ocupaci�n -MINTRA, Declaraci�n empleo','',1);
insert into kss_references values('officialRep','02','none','Tipo de trabajador TIUNA -IVSS','',2);
insert into kss_references values('officialRep','03','none','Condici�n de trabajador TIUNA -IVSS','',3);
insert into kss_references values('officialRep','04','none','Tipo de trabajador  FAOV -BANAVIH','',4);
insert into kss_references values('officialRep','05','none','Tipo de trabajador -MINTRA, Declaraci�n empleo','',1.50);
--
insert into kss_references values('officialRep','06','none','RNET: Tipo de trabajador -Declaraci�n de empleo','',6);
insert into kss_references values('officialRep','07','none','RNET: Tipo de contrato -Declaraci�n de empleo','',7);
insert into kss_references values('officialRep','08','none','RNET: Tipo de jornada -Declaraci�n de empleo','',8);
insert into kss_references values('officialRep','09','none','RNET: Embarazada? -Declaraci�n de empleo','',9);
insert into kss_references values('officialRep','10','none','RNET: Sindicalizado? -Declaraci�n de empleo','',10);
--insert into kss_references values('officialRep','11','none','RNET: Familiar discapacitado? -Declaraci�n de empleo','',11);
--insert into kss_references values('officialRep','12','none','RNET: Trabaja domingo? -Declaraci�n de empleo','',12);

insert into kss_references values('officialRep','58','none','RNET: Enfermedad ocupacional?','',12);
--insert into kss_references values('officialRep','59','none','RNET: Etnia ind�gena? ','',13);
--insert into kss_references values('officialRep','60','none','RNET: Discapacidad auditiva?','',14);
--insert into kss_references values('officialRep','61','none','RNET: Discapacidad visual?','',15);
--insert into kss_references values('officialRep','62','none','RNET: Discapacidad intelectual?','',16);
--insert into kss_references values('officialRep','63','none','RNET: Discapacidad mental?','',17);
--insert into kss_references values('officialRep','64','none','RNET: Discapacidad musculo-esqueletica?','',18);
--insert into kss_references values('officialRep','65','none','RNET: Discapacidad musculo-esqueletica?','',19);


insert into kss_references values('reasonType','hire','none','Ingreso','',1);
insert into kss_references values('reasonType','settlement','none','Terminaci�n o finiquito','',2);
insert into kss_references values('reasonType','movement','none','Movimiento','',3);
insert into kss_references values('reasonType','other','none','Otro','',4);


insert into kss_references values('officialValVEN','01','none','Valor unidad tributaria','',1);
insert into kss_references values('officialValVEN','02','none','Desgravamen �nico','',3);
insert into kss_references values('officialValVEN','03','none','Rebaja personal','',4);
insert into kss_references values('officialValVEN','04','none','Rebaja c�nyuge','',5);
insert into kss_references values('officialValVEN','05','none','Rebaja familiar','',6);
insert into kss_references values('officialValVEN','06','none','Salario tope mensual -IVSS','',7);
--insert into kss_references values('officialValVEN','07','none','Salario m�nimo -rural','',8);
insert into kss_references values('officialValVEN','08','none','Salario m�nimo nacional','',2);
--insert into kss_references values('officialValVEN','09','none','Cantidad de tickets diarios','',1.10);
insert into kss_references values('officialValVEN','10','none','Cantidad salario minimo -guarder�a','',7);

insert into kss_references values('officialValCOL','08','none','Salario m�nimo nacional','',2);
insert into kss_references values('officialValPAN','08','none','Salario m�nimo nacional','',2);

insert into kss_references values('ethnicity','american','none','Indio Americano o Nativo de Alaska','',1);
insert into kss_references values('ethnicity','asian','none','Asiatico','',2);
insert into kss_references values('ethnicity','black','none','Negro o Afrodescendiente','',3);
insert into kss_references values('ethnicity','hawiian','none','Hawaiano o Islas del p�cifico','',4);
insert into kss_references values('ethnicity','white','none','Blanco','',5);

insert into kss_references values('payFrequency','7','none','Semanal','',1);
insert into kss_references values('payFrequency','15','none','Quincenal','',2);
insert into kss_references values('payFrequency','30','none','Mensual','',3);
insert into kss_references values('payFrequency','14','none','Catorcenal','',4);

-- Clasificaci�n Ente Publico
insert into kss_references values('govClassType','mintra01','none','Clase de ocupaci�n -MINTRA, Declaraci�n empleo','',1);
insert into kss_references values('govClassType','mintra02','none','Tipo de trabajador -MINTRA, Declaraci�n empleo','',1.5);
insert into kss_references values('govClassType','tiuna01','none','TIUNA: Tipo de trabajador -IVSS','',2);
insert into kss_references values('govClassType','tiuna02','none','TIUNA: Condici�n de trabajador -IVSS','',3);
insert into kss_references values('govClassType','banavih01','none','FAOV: Tipo de trabajador -BANAVIH','',4);
--06..12
insert into kss_references values('govClassType','rnet01','none','RNET: Tipo de trabajador','',6);
insert into kss_references values('govClassType','rnet02','none','RNET: Tipo de contrato','',7);
insert into kss_references values('govClassType','rnet03','none','RNET: Tipo de jornada','',8);
insert into kss_references values('govClassType','rnet04','none','RNET: Embarazada?','',9);
insert into kss_references values('govClassType','rnet05','none','RNET: Sindicalizado?','',10);
--insert into kss_references values('govClassType','rnet06','none','RNET: Familiar discapacitado? -Declaraci�n de empleo','',11);
--insert into kss_references values('govClassType','rnet07','none','RNET: Trabaja domingo? -Declaraci�n de empleo','',12);
--58..65
insert into kss_references values('govClassType','rnet08','none','RNET: Enfermedad ocupacional?','',12);
--insert into kss_references values('govClassType','rnet09','none','RNET: Etnia ind�gena? ','',13);
--insert into kss_references values('govClassType','rnet10','none','RNET: Discapacidad auditiva?','',14);
--insert into kss_references values('govClassType','rnet11','none','RNET: Discapacidad visual?','',15);
--insert into kss_references values('govClassType','rnet12','none','RNET: Discapacidad intelectual?','',16);
--insert into kss_references values('govClassType','rnet13','none','RNET: Discapacidad mental?','',17);
--insert into kss_references values('govClassType','rnet14','none','RNET: Discapacidad musculo-esqueletica?','',18);
--
insert into kss_references values('recruitSource','website','none','P�gina o Zona de empleo','',1);
insert into kss_references values('recruitSource','socialNetwork','none','Red social','',2);
insert into kss_references values('recruitSource','newspaper','none','Prensa','',3);
insert into kss_references values('recruitSource','magazine','none','Revista','',4);
insert into kss_references values('recruitSource','advertising','none','Publicidad','',5);
insert into kss_references values('recruitSource','xref','none','Referencia externa','',6.10);
insert into kss_references values('recruitSource','iref','none','Referencia interna','',6.20);
insert into kss_references values('recruitSource','zone','none','Zona de empleo','',7);
insert into kss_references values('recruitSource','iniciative','none','Iniciativa propia','',8);
insert into kss_references values('recruitSource','portal','none','Portal de empleo','',9);
insert into kss_references values('recruitSource','fair','none','Feria de empleo','',9);
insert into kss_references values('recruitSource','other','none','Otra','',99);

insert into kss_references values('calcClassif','payroll','none','N�mina','',1);
insert into kss_references values('calcClassif','vacation','none','Vacaci�n','',2);
insert into kss_references values('calcClassif','settlement','none','Finiquito laboral','',3);
insert into kss_references values('calcClassif','special','none','Especial','',4);
insert into kss_references values('calcClassif','retroactive','none','C�lculo retroactivo','',5);
insert into kss_references values('calcClassif','provacation','none','Provisi�n de vacaci�n','',6);
insert into kss_references values('calcClassif','postClose','none','Post cierre','',7);
insert into kss_references values('calcClassif','kindergarten','none','Guarder�a','',10);


-- T077
--tipo trabajador mintra
insert into kss_references values('govClassVal','1','mintra01','Propietarios/Socios','',1); 
insert into kss_references values('govClassVal','2','mintra01','Trab. Familiares no remunerado','',2); 
insert into kss_references values('govClassVal','3','mintra01','Gerentes y Directores','',3); 
insert into kss_references values('govClassVal','4','mintra01','Empleados','',4); 
insert into kss_references values('govClassVal','5','mintra01','Obreros','',5); 
insert into kss_references values('govClassVal','6','mintra01','Aprendices','',6); 
insert into kss_references values('govClassVal','7','mintra01','Trabajadores adolescentes','',7); 
insert into kss_references values('govClassVal','8','mintra01','Extranjeros','',8); 
insert into kss_references values('govClassVal','9','mintra01','Con discapacidad','',9); 

insert into kss_references values('govClassVal','1','mintra02','Empleado','',1); 
insert into kss_references values('govClassVal','2','mintra02','Obrero','',1); 

--insert into kss_references values('govClassVal','1','tiuna01','Medio tiempo','',7); 
--insert into kss_references values('govClassVal','2','tiuna01','Pasante','',7.10); 
--insert into kss_references values('govClassVal','3','tiuna01','Conserje','',7.14); 
--insert into kss_references values('govClassVal','4','tiuna01','Adolescente y Aprendiz','',7.16); 
--insert into kss_references values('govClassVal','5','tiuna01','Dom�sticos','',7.18); 
--insert into kss_references values('govClassVal','6','tiuna01','Rural','',7.20); 
--insert into kss_references values('govClassVal','7','tiuna01','Urbando','',7.22); 
--insert into kss_references values('govClassVal','8','tiuna01','A Destajo','',7.24); 

insert into kss_references values('govClassVal','0','tiuna01','Rural menor 20','',6); 
insert into kss_references values('govClassVal','1','tiuna01','Rural mayor 20','',7); 
insert into kss_references values('govClassVal','2','tiuna01','Urbano mayor 20','',7.10); 
insert into kss_references values('govClassVal','3','tiuna01','Adolescente y Aprendiz','',7.14); 
insert into kss_references values('govClassVal','4','tiuna01','Urbano menor de 20','',7.16); 
insert into kss_references values('govClassVal','5','tiuna01','Conserje','',7.18); 
insert into kss_references values('govClassVal','6','tiuna01','Medio Tiempo','',7.20); 
insert into kss_references values('govClassVal','7','tiuna01','A Destajo','',7.22); 
insert into kss_references values('govClassVal','8','tiuna01','Pasante','',7.24); 
insert into kss_references values('govClassVal','9','tiuna01','Domesticos','',7.30); 

insert into kss_references values('govClassVal','1','tiuna02','Normal','',8); 
insert into kss_references values('govClassVal','2','tiuna02','Pensionado','',8.10); 
insert into kss_references values('govClassVal','3','tiuna02','Jubilado','',8.12);

insert into kss_references values('govClassVal','1','banavih01','Fijo','',9); 
insert into kss_references values('govClassVal','2','banavih01','Contratado','',9.10); 
insert into kss_references values('govClassVal','3','banavih01','Obrero','',9.12); 
insert into kss_references values('govClassVal','4','banavih01','Pasante','',9.14); 
insert into kss_references values('govClassVal','5','banavih01','Aprendiz','',9.16); 
insert into kss_references values('govClassVal','6','banavih01','Tiempo Parcial','',9.18); 

--Tipo de trabajador 
insert into kss_references values('govClassVal','1','rnet01','De Direccion','',1); 
insert into kss_references values('govClassVal','2','rnet01','De Inspeccion o Vigilancia','',2); 
insert into kss_references values('govClassVal','3','rnet01','Aprendiz INCES','',3); 
insert into kss_references values('govClassVal','4','rnet01','Pasante','',4); 
insert into kss_references values('govClassVal','5','rnet01','Trabajador Calificado','',5); 
insert into kss_references values('govClassVal','6','rnet01','Trabajador no Calificado','',6); 

--Tipo contrato 
insert into kss_references values('govClassVal','TI','rnet02','Tiempo Indeterminado','',1); 
insert into kss_references values('govClassVal','TD','rnet02','Tiempo Determinado','',2); 
insert into kss_references values('govClassVal','OD','rnet02','Obra Determinada','',3); 
--Tipo jornada
insert into kss_references values('govClassVal','D','rnet03','Diurna','',1); 
insert into kss_references values('govClassVal','N','rnet03','Nocturna','',2); 
insert into kss_references values('govClassVal','M','rnet03','Mixta','',3); 
insert into kss_references values('govClassVal','C','rnet03','Continua','',4); 
insert into kss_references values('govClassVal','R','rnet03','Rotativa','',5); 
insert into kss_references values('govClassVal','R2','rnet03','Rotativa 2 Turnos','',6); 
insert into kss_references values('govClassVal','R3','rnet03','Rotativa 3 Turnos','',7); 

--Embarazada
insert into kss_references values('govClassVal','N','rnet04','No','',1); 
insert into kss_references values('govClassVal','S','rnet04','S�','',2); 
--Sindicalizado
insert into kss_references values('govClassVal','N','rnet05','No','',1); 
insert into kss_references values('govClassVal','S','rnet05','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet06','No','',1); 
insert into kss_references values('govClassVal','S','rnet06','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet07','No','',1); 
insert into kss_references values('govClassVal','S','rnet07','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet08','No','',1); 
insert into kss_references values('govClassVal','S','rnet08','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet09','No','',1); 
insert into kss_references values('govClassVal','S','rnet09','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet10','No','',1); 
insert into kss_references values('govClassVal','S','rnet10','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet11','No','',1); 
insert into kss_references values('govClassVal','S','rnet11','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet12','No','',1); 
insert into kss_references values('govClassVal','S','rnet12','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet13','No','',1); 
insert into kss_references values('govClassVal','S','rnet13','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet14','No','',1); 
insert into kss_references values('govClassVal','S','rnet14','S�','',2); 
--
insert into kss_references values('govClassVal','N','rnet15','No','',1); 
insert into kss_references values('govClassVal','S','rnet15','S�','',2); 

--Reporte - Ente P�blico
insert into kss_references values('govRepType','rnet','VEN','RNET -MINTRA','',1); 
insert into kss_references values('govRepType','tiuna','VEN','TIUNA -IVSS','',2); 

insert into kss_references values('payslips','payroll','none','Por defecto','',1);
insert into kss_references values('payslips','Payslip02','none','Vacaci�n','',2);
insert into kss_references values('payslips','Payslip03','none','Fin de relaci�n o finiquito','',3);
insert into kss_references values('payslips','Payslip01','none','Estandar 01','',4);
insert into kss_references values('payslips','Payslip01b','none','Estandar 02','',4.2);
insert into kss_references values('payslips','Payslip01c','none','Estandar 03 -media pagina','',4.3);
--insert into kss_references values('payslips','calcType','none','Adaptado tipo de c�lculo','',6);
insert into kss_references values('payslips','Payslip04','none','Garant�as de prestaciones','',5);
insert into kss_references values('payslips','Payslip05','none','Garant�as y saldo de prestaciones','',6);

insert into kss_references values('authCalcType','0','none','Pre-c�lculo y Cierre','',1);
insert into kss_references values('authCalcType','1','none','Pre-c�lculo','',2);
insert into kss_references values('authCalcType','2','none','Cierre','',3);

insert into kss_references values('orderingType','FW','none','ACH/ABA','',1);
insert into kss_references values('orderingType','IS','none','BIC/SWIFT','',2);
insert into kss_references values('orderingType','/ACCT/','none','Account','',3);

insert into kss_references values('catConstant','0','none','No aplica','',1);
insert into kss_references values('catConstant','1','none','General','',2);
insert into kss_references values('catConstant','2','none','Colaborador','',3);
insert into kss_references values('catConstant','3','none','Competencia','',4);
insert into kss_references values('catConstant','4','none','General-Colaborador','',2.1);

insert into kss_references values('bodilyFunc','0','none','No existe deficiencia','',1);
insert into kss_references values('bodilyFunc','1','none','Deficiencia leve','',2);
insert into kss_references values('bodilyFunc','2','none','Deficiencia moderada','',3);
insert into kss_references values('bodilyFunc','3','none','Deficiencia grave','',4);
insert into kss_references values('bodilyFunc','4','none','Dimensiones completa','',5);
insert into kss_references values('bodilyFunc','8','none','No especificada','',6);
insert into kss_references values('bodilyFunc','9','none','No aplicable','',7);

insert into kss_references values('bodilyStruc','0','none','No hay cambio','',1);
insert into kss_references values('bodilyStruc','1','none','Ausencia total','',2);
insert into kss_references values('bodilyStruc','2','none','Ausencia parcial','',3);
insert into kss_references values('bodilyStruc','3','none','Ausencia adicional','',4);
insert into kss_references values('bodilyStruc','4','none','Dimensiones abrrantes','',5);
insert into kss_references values('bodilyStruc','5','none','Disicontinuidad','',6);
insert into kss_references values('bodilyStruc','6','none','Posici�n desviada','',7);
insert into kss_references values('bodilyStruc','7','none','Cambios cualitativos, incluye acumulaci�n de liquido','',8);
insert into kss_references values('bodilyStruc','8','none','No especificada','',9);
insert into kss_references values('bodilyStruc','9','none','No aplicable','',10);

insert into kss_references values('bodilyActiv','0','none','No hay dificultad','',1);
insert into kss_references values('bodilyActiv','1','none','Difcultad ligera','',2);
insert into kss_references values('bodilyActiv','2','none','Dificultad moderada','',3);
insert into kss_references values('bodilyActiv','3','none','Dificultad grave','',4);
insert into kss_references values('bodilyActiv','4','none','Dificultad completa','',5);
insert into kss_references values('bodilyActiv','8','none','No especificada','',6);
insert into kss_references values('bodilyActiv','9','none','No aplicable','',7);

insert into kss_references values('consultType','preempl','none','Pre-empleo','',1);
insert into kss_references values('consultType','periodic','none','Periodica','',2);
insert into kss_references values('consultType','prevac','none','Pre-vacacional','',3);
insert into kss_references values('consultType','postvac','none','Post-vacacional','',4);
insert into kss_references values('consultType','settle','none','Egreso','',5);
insert into kss_references values('consultType','postrest','none','Post-reposo','',6);
insert into kss_references values('consultType','occcupa','none','Ocupacional','',7);
insert into kss_references values('consultType','survei','none','Vigilancia medica','',8);
insert into kss_references values('consultType','accidentLab','none','Accidente de trabajo','',9);
insert into kss_references values('consultType','accident','none','Accidente comun','',10);
insert into kss_references values('consultType','report','none','Informe medico','',11);
insert into kss_references values('consultType','emergency','none','Emergencia','',12);
insert into kss_references values('consultType','general','none','General','',13);
insert into kss_references values('consultType','promo','none','Promocion','',14);
insert into kss_references values('consultType','telemed','none','Telemedicina','',15);

insert into kss_references values('consultType','other','none','Otra','',99);

insert into kss_references values('bodySystem','muscle','none','Musculo Esqueletico','',1);
insert into kss_references values('bodySystem','circula','none','Circulatorio','',3);
insert into kss_references values('bodySystem','respira','none','Respiratorio','',4);
insert into kss_references values('bodySystem','nervous','none','Nervioso','',5);
insert into kss_references values('bodySystem','gastro','none','Digestivo -Gastrointestina','',5);
insert into kss_references values('bodySystem','genito','none','Genitourinario','',7);
insert into kss_references values('bodySystem','endocrine','none','Endocrino metabolico','',10);
insert into kss_references values('bodySystem','immuno','none','Linfatico e Inmunologico','',11);
insert into kss_references values('bodySystem','skin','none','Tegumentario -Piel y anexos','',13);
insert into kss_references values('bodySystem','otorhino','none','Otorrinolaringologico','',14);
insert into kss_references values('bodySystem','neuro','none','Neurologico','',15);
insert into kss_references values('bodySystem','ophtal','none','Oftalmologico','',16);
insert into kss_references values('bodySystem','hema','none','Hematologico','',17);
insert into kss_references values('bodySystem','psych','none','Mental','',18);


insert into kss_references values('visualAcuity','200','none','20/200','',1);
insert into kss_references values('visualAcuity','100','none','20/100','',2);
insert into kss_references values('visualAcuity','50','none','20/50','',3);
insert into kss_references values('visualAcuity','70','none','20/70','',4);
insert into kss_references values('visualAcuity','40','none','20/40','',5);
insert into kss_references values('visualAcuity','30','none','20/30','',6);
insert into kss_references values('visualAcuity','25','none','20/25','',7);
insert into kss_references values('visualAcuity','20','none','20/20','',8);

insert into kss_references values('disabilityGrade','0','none','No existe','',1);
insert into kss_references values('disabilityGrade','1','none','Leve','',2);
insert into kss_references values('disabilityGrade','2','none','Moderada','',3);
insert into kss_references values('disabilityGrade','3','none','Severa','',4);
insert into kss_references values('disabilityGrade','4','none','Completa','',5);

insert into kss_references values('userProgram','ListWorkforceGen','none','Listado de Informaci�n general','',1);
insert into kss_references values('sectionProgram','salary','ListWorkforceGen','Salario','',1);
insert into kss_references values('sectionProgram','gradeSalary','ListWorkforceGen','Grado Salarial','',2);
insert into kss_references values('sectionProgram','typi','ListWorkforceGen','Tipificaci�n','',2.5);

insert into kss_references values('userProgram','ImportInfoType','none','Importar info type','',2);
insert into kss_references values('sectionProgram','ingreso','ImportInfoType','Igreso','',2);
insert into kss_references values('sectionProgram','salary','ImportInfoType','Salario','',3);
insert into kss_references values('sectionProgram','bankaccount','ImportInfoType','Cuenta banco','',4);
insert into kss_references values('sectionProgram','fund_account','ImportInfoType','Cuenta fondo','',5);
insert into kss_references values('sectionProgram','vac_history','ImportInfoType','Historial de vacaciones','',6);
insert into kss_references values('sectionProgram','movement_wforce','ImportInfoType','Movimiento de colaboradores','',7);
insert into kss_references values('sectionProgram','movement_dep','ImportInfoType','Historial de departamentos','',8);
insert into kss_references values('sectionProgram','movement_job','ImportInfoType','Historial de cargos','',9);
insert into kss_references values('sectionProgram','gov_class','ImportInfoType','Clasificaci�n Entes Publicos','',10);
insert into kss_references values('sectionProgram','identity','ImportInfoType','Identficaiones','',11);
insert into kss_references values('sectionProgram','department','ImportInfoType','Departamentos','',12);
insert into kss_references values('sectionProgram','job','ImportInfoType','Cargos','',1);
insert into kss_references values('sectionProgram','ceco','ImportInfoType','Centros de costos','',13);
insert into kss_references values('sectionProgram','address_contact','ImportInfoType','Direccion contacto','',14);
insert into kss_references values('sectionProgram','people','ImportInfoType','Informaci�n Personal','',15);
insert into kss_references values('sectionProgram','contract','ImportInfoType','Fecha contrato','',16);
insert into kss_references values('sectionProgram','people_relation','ImportInfoType','Tipo relaci�n','',17);

insert into kss_references values('userProgram','workforce','none','Relacion Laboral','',3);
insert into kss_references values('sectionProgram','aditional','workforce','Campos adicionales','',1);
insert into kss_references values('sectionProgram','access','workforce','Control de acceso','',2);
insert into kss_references values('sectionProgram','government','workforce','Clasificaci�n Entes Publicos','',2);
--insert into kss_references values('sectionProgram','dep','workforce','Historial Departamentos','',3);
--insert into kss_references values('sectionProgram','job','workforce','Historial Cargos','',4);
--insert into kss_references values('sectionProgram','salary','workforce','Historial Salario','',5);

insert into kss_references values('peopleRelation','recruit','none','Reclutamiento','',1);
insert into kss_references values('peopleRelation','medical','none','Evaluacion medica','',2);
insert into kss_references values('peopleRelation','training','none','Entrenamiento','',1);
insert into kss_references values('peopleRelation','laboral','none','Laboral','',3);
insert into kss_references values('peopleRelation','interview','none','Entrevista','',3.10);
insert into kss_references values('peopleRelation','apt','none','Elegible','',3.10);
insert into kss_references values('peopleRelation','noapt','none','No elegible','',3.10);

insert into kss_references values('roleType','option','none','Opciones de menu','',1);
insert into kss_references values('roleType','payroll','none','Empresas y Nominas','',2);
insert into kss_references values('roleType','database','none','Base de datos','',3);
insert into kss_references values('roleType','program','none','Programas especiales','',4);
insert into kss_references values('roleType','calctype','none','Tipo de calculo','',5);
insert into kss_references values('roleType','category','none','Categorias','',6);

insert into kss_references values('jobCondition','maternity','none','Maternidad o Paternidad','',3);
insert into kss_references values('jobCondition','delegate','none','Maternidad o Paternidad','',3);
insert into kss_references values('jobCondition','disability','none','Discapacidad','',3);
insert into kss_references values('jobCondition','disabilityChild','none','Hijo con discapacidad','',3);

insert into kss_references values('workflowClass','hire','none','Captaci�n o ingreso','',1);
insert into kss_references values('workflowClass','other','none','Otro','',9);

insert into kss_references values('stepWorkflow','start','none','Inicio','',1);
insert into kss_references values('stepWorkflow','control','none','Control','',2);
insert into kss_references values('stepWorkflow','interview','none','Entrevista','',3);
insert into kss_references values('stepWorkflow','final','none','Fin','',9);


insert into kss_references values('addressType','billing','none','Factura','',1);
insert into kss_references values('addressType','shiping','none','Env�o','',1);

update kss_references set group_value='none' where group_value is null;

