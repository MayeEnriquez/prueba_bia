Prueba tecnica: Mayerly Enriquez.

============
Instalación
============ 
Se debe instalar el módulo "prueba_bia" el cual tiene como dependencia 2 módulos, crm y projects, los cuales se instalaran automaticamente al
instalar el módulo.

Cuando se instalen estaran disponibles las siguientes opciones: 

============
En project.task
============

1. Se realiza una herencia al modelo project.task, donde se agrega un nuevo campo llamado service_id, en este campo service id se almacenará
la información que retorne el endpoint creado, como no se me proporciono un endpoint cree uno en un sitio web el cual siempre retorna
un json con el id del servicio.

Se realiza en el mismo modelo una herencia a project.task, donde al guardar cualquier tarea se ejecuta el endpoint y se asigna el service id al 
campo creado

============
En Crm.lead
============

1. se creo un page al lado derecho de informacion adicional con el nombre "Tareas relacionadas" el cual contiene las tareas asignadas a un partner o un cliente, por medio de un campo One2many computado, se realiza un search y se buscan las tareas relacionadas a ese cliente

2. En el mismo page de las tareas relacionadas, por cada tarea que tiene el cliente se puede ejecutar un boton que permite llamar al web service
el cual asigna el ID de la tarea.


============
Endpoint creado: update_partner
============

Se creo un endpoint con route update_partner el cual recibe 2 parametros en el body
partner_id <- Debe ser un partner que existe en la base de datos
name <- Seria el valor que necesitamos actualizar en el partner

Si todo es correcto se retornara un mensaje de exitoso
