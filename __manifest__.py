{
    "name": "Instrument Field Service Register",
    "summary": "Instrument delivery, installation, SSO training, and calibration register",

    "version": "19.0.1.0.3",
    "category": "Services/Field Service",
    "license": "LGPL-3",
    "depends": ["industry_fsm"],

    "version": "19.0.1.0.5",
    "category": "Services/Field Service",
    "license": "LGPL-3",
    "depends": ["industry_fsm", "product"],

    "data": [
        "security/ir.model.access.csv",
        "views/instrument_register_views.xml",
    ],
    "application": False,
    "installable": True,
}
