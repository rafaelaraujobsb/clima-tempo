from scrapper_clima_tempo.config import envs


enable_utc = True
timezone = "America/Sao_Paulo"

broker_url = envs.BROKER

task_acks_late = True

imports = ["scrapper_clima_tempo"]
include = ["scrapper_clima_tempo.modulos.scrapper", "scrapper_clima_tempo.modulos.schedule"]

task_routes = {
    "scrapper.task_buscar_clima": {"queue": "climatempo_buscar_clima"},
}

beat_schedule = {
    f"buscar-clima-{envs.TS_SCHEDULE}m": {
        "task": "schedule.task_scheduler",
        "schedule": envs.TS_SCHEDULE*60,
        "options": {
            "queue": "climatempo_scheduler"
        }
    },
}
