{
    "name": "Instrument Field Service Register",
    "summary": "PCR installation register and field service maintenance task tracking",
    "version": "19.0.1.0.6",
    "category": "Services/Field Service",
    "license": "LGPL-3",
    "depends": ["industry_fsm", "product", "project"],
    "data": [
        "security/ir.model.access.csv",
        "views/instrument_register_views.xml",
        "views/project_task_views.xml",
    ],
    "application": False,
    "installable": True,
}
