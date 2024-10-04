from datetime import date
from enum import Enum


class StatusOrder(Enum):
    RECEIVE = "RECEIVE"
    ON_PROGRESS = "ON_PROGRESS"
    PARTS_WAIT = "PARTS_WAIT"
    DELIVERY = "DELIVERY"


class Problem(Enum):
    BROKEN_DISPLAY = "BROKEN_DISPLAY"
    SOFTWARE_PROBLEM = "SOFTWARE_PROBLEM"
    BATTERY_CHANGE = "BATTERY_CHANGE"

class Persona:
    def __init__(self, rut, firstname, lastname, email, phone):
        self.rut = rut
        self.firstName = firstname
        self.lastName = lastname
        self.email = email
        self.phone = phone


class Tech(Persona):
    def __int__(self, rut, firstname, lastname, email, phone, kind):
        super().__int__(rut, firstname, lastname, email, phone)
        self.kind = kind


class Client(Persona):
    def __int__(self, rut, firstname, lastname, email, phone):
        super().__int__(rut, firstname, lastname, email, phone)
        self.devices = []

    def register_device(self, device):
        self.devices.append(device)


class Device:
    def __init__(self, brand, model, problem):
        self.brand = brand
        self.model = model
        self.problem = problem


class WorkOrder:
    def __init__(self, tech, device, diagnosis):
        self.tech = tech
        self.device = device
        self.diagnosis = None
        self.startDate = date.today()
        self.endDate = None
        self.status = StatusOrder.RECEIVE

    def change_status(self, status):
        self.status = status

    def do_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis


class WorkShop:
    def __init__(self):
        self.clients = []
        self.techs = []
        self.workOrders = []

    def register_client(self, client):
        self.clients.append()

    def register_techs(self, tech):
        self.techs.append(tech)

    def register_order(self, order):
        self.workOrders.append(order)

    def get_report(self, _type):
        
