'''import requests


url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


def p0_simulator():
    user = 'tester'
    problem = 0
    count = 2

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'ENTER', 'call_ids': [2, 3]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [0, 1]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'EXIT', 'call_ids': [2]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [1]}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'EXIT', 'call_ids': [3]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [4]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [0, 4]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [5]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [5]}, {'elevator_id': 1, 'command': 'STOP'}])


if __name__ == '__main__':
    p0_simulator()'''







'''import requests, json
import time
from pprint import pprint

url = "http://localhost:8000"
state = {
    "token": "",
    "timestamp": 0,
    "elevators": [],
    "is_end": False
}
calls = []
picked = []
requestCount = 0


def start(problem_id, number_of_elevators):
    global state
    res = requests.post(url + f"/start/tester/{problem_id}/{number_of_elevators}")
    state = res.json()
    print("TOKEN : ", state["token"])


def onCalls():
    global state
    global calls
    headers = {"X-Auth-Token": state["token"]}
    res = requests.get(url + "/oncalls", headers=headers)
    state = res.json()
    calls = state["calls"]


def action(commands):
    global state
    headers = {"X-Auth-Token": state["token"], "Content-Type": "application/json"}
    res = requests.post(url + "/action", headers=headers, data=json.dumps({"commands": commands}))
    state = res.json()
    onCalls()
    global requestCount
    requestCount += 2
    pprint(commands)
    print(f"Picked : {len(picked)}  Timestamp : {state['timestamp']}")
    # calls 를 다 처리했는데도 안끝나길래 추가한 디버깅용 print
    if len(picked) == 200 or len(picked) == 500:
        print("PASSENGERS : ", tuple([a["passengers"] for a in state["elevators"]]))
        print("CALLS : ", calls)
    # 몽키패치
    isPassengersEmpty = all(len(el["passengers"]) == 0 for el in state["elevators"])
    if isPassengersEmpty and (problem == "JayZ Building" and len(picked) == 200) or (
            problem == "Lion Tower" and len(picked) == 500):
        picked.clear()


def makeCommand(elevator_id, command, ids=None):
    ret = {"elevator_id": elevator_id, "command": command}
    if ids:
        ret["call_ids"] = ids
    return ret


class Elevator:
    def __init__(self, elevator_id, topFloor, bottomFloor, capacity):
        self.elevator_id = elevator_id
        self.topFloor = topFloor
        self.bottomFloor = bottomFloor
        self.capacity = capacity
        self.toUp = True
        self.el = None
        self.renewElevatorState()

    def renewElevatorState(self):
        global state
        self.el = state["elevators"][self.elevator_id]

    def getNextActions(self):
        self.renewElevatorState()
        ret = []

        # 내릴사람
        getOff_ids = []
        for passenger in self.el["passengers"]:
            if passenger["end"] == self.el["floor"]:
                getOff_ids.append(passenger["id"])

        # 탈사람
        getIn_ids = []
        global calls
        global picked
        for call in calls:
            if call["start"] == self.el["floor"] and call["id"] not in picked:
                getIn_ids.append(call["id"])

        # 내리고 태우기
        if len(getIn_ids) > 0 or len(getOff_ids) > 0:
            ret.append(["STOP", None])
            ret.append(["OPEN", None])

            if len(getOff_ids) > 0:
                ret.append(["EXIT", getOff_ids])

            left = self.capacity - len(self.el["passengers"]) + len(getOff_ids)
            if len(getIn_ids) > 0 and left > 0:
                ret.append(["ENTER", getIn_ids[:left]])
                picked += getIn_ids[:left]

            ret.append(["CLOSE", None])

        # 후처리
        if self.el["floor"] == self.topFloor:
            ret.append(["STOP", None])
            self.toUp = False
        if self.el["floor"] == self.bottomFloor:
            ret.append(["STOP", None])
            self.toUp = True

        direction = "UP" if self.toUp else "DOWN"
        ret.append([direction, None])
        return ret


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 0번문제 어피치맨션 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
problem = "Apeach Mansion"
start(0, 1)
elevators = []
elevators.append(Elevator(elevator_id=0, bottomFloor=1, topFloor=5, capacity=8))
actionQ = [[]]
while not state["is_end"]:
    if requestCount > 0 and requestCount % 40 == 0:  # 1초에 40번 이상의 요청은 에러뜸
        time.sleep(1)

    commands = []
    for el, q in zip(elevators, actionQ):
        if len(q) == 0:
            q += el.getNextActions()
        command, ids = q.pop(0)
        commands.append(makeCommand(el.elevator_id, command, ids))

    action(commands)

print("어피치맨션 완료")

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 1번문제 제이지빌딩 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
problem = "JayZ Building"
start(1, 4)
elevators = []
elevators.append(Elevator(elevator_id=0, bottomFloor=1, topFloor=25, capacity=8))
elevators.append(Elevator(elevator_id=1, bottomFloor=1, topFloor=25, capacity=8))
elevators.append(Elevator(elevator_id=2, bottomFloor=1, topFloor=25, capacity=8))
elevators.append(Elevator(elevator_id=3, bottomFloor=1, topFloor=25, capacity=8))
actionQ = [[], [["STOP", None] for a in range(6)], [["STOP", None] for a in range(12)],
           [["STOP", None] for a in range(18)]]

while not state["is_end"]:
    if requestCount > 0 and requestCount % 40 == 0:
        time.sleep(1)

    commands = []
    for el, q in zip(elevators, actionQ):
        if len(q) == 0:
            q += el.getNextActions()
        command, ids = q.pop(0)
        commands.append(makeCommand(el.elevator_id, command, ids))

    action(commands)

print("제이지빌딩 완료")

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 2번문제 라이언타워 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
problem = "Lion Tower"
start(2, 4)
elevators = []
elevators.append(Elevator(elevator_id=0, bottomFloor=1, topFloor=25, capacity=8))
elevators.append(Elevator(elevator_id=1, bottomFloor=1, topFloor=25, capacity=8))
elevators.append(Elevator(elevator_id=2, bottomFloor=1, topFloor=25, capacity=8))
elevators.append(Elevator(elevator_id=3, bottomFloor=1, topFloor=25, capacity=8))
actionQ = [[], [["UP", None] for a in range(6)], [["UP", None] for a in range(12)], [["UP", None] for a in range(18)]]

while not state["is_end"]:
    if requestCount > 0 and requestCount % 40 == 0:
        time.sleep(1)

    commands = []
    for el, q in zip(elevators, actionQ):
        if len(q) == 0:
            q += el.getNextActions()
        command, ids = q.pop(0)
        commands.append(makeCommand(el.elevator_id, command, ids))

    action(commands)

print("라이언타워 완료")'''

import requests, json
import time
from pprint import pprint

url = 'http://localhost:8000'
request_count = 0

core = {
    "token" : "",
    "timestamp" : 0,
    "elevators" : [],
    "is_end": False
}


# Get started!!
def start(user_key,problem_id,number_of_elevators):
    global core
    global request_count
    uri = url + '/start' + '/' + user_key + '/' + str(problem_id) + '/' + str(number_of_elevators)
    request_count +=2
    core = requests.post(uri).json()
    return core

#숙제 확인용(그 초의)
def onCalls():
    global request_count
    request_count += 2
    uri = url + "/oncalls"
    bigcore = requests.get(uri,headers={'X-Auth-Token': core["token"]}).json()
    return bigcore

#엘베를 움직이게 하는 함수
def action(commands):
    global request_count
    global core
    uri = url +'/action'
    request_count += 2
    core = requests.post(uri,headers={'X-Auth-Token': core["token"],'Content-Type':'application/json'},data=json.dumps({"commands": [commands]})).json()
    return core

#커맨드 생성 함수
def make_command(el_id,command,call_ids=[]):
    if call_ids != []:
        return {
            "elevator_id": el_id,
            'command' : command,
            'call_ids': call_ids
                }
    else:
        return {
            "elevator_id": el_id,
            'command': command
                }

# 엘리베이터
# {
#   "id": 0,
#   "floor": 1,
#   "passengers": [],
#   "status": "STOPPED"
# }

# Call
# {
#   "id": 0,
#   "timestamp": 0,
#   "start": 1,
#   "end": 2
# }

# Command
# {
#   "elevator_id": 0,
#   "command": "ENTER",
#   "call_ids": [0]
# }


#어피치 타워

def Apeach_Tower():
    global request_count
    start("tester",1,1)
    #엘베를 이용한 사람들
    print(core)
    picked = []
    direction = "up"
    while not core["is_end"]:
        print("Asd")
        #숙제확인!(누적)
        homework = onCalls()
        calls = homework["calls"]
        get_in = []
        get_out = []
        # if request_count > 40:
        #     time.sleep(1)
        #     request_count = 0

        # 지금 초에서 탈사람 확인!
        for call in calls:
            if call['start'] == core["elevators"][0]['floor']:
                # 탈 사람
                get_in.append(call['id'])

        # 지금 초에서 내릴사람 확인!
        for call in core["elevators"][0]['passengers']:
            if call['end'] == core["elevators"][0]['floor'] :
                # 내릴 사람
                get_out.append(call['id'])


        #멈추고 열고!
        action(make_command(0,"STOP",[]))
        action(make_command(0,"OPEN",[]))

        #내릴 사람은 내려라!
        if get_out != []:
            print("내릴사람",make_command(0,'EXIT',get_out))
            action(make_command(0,'EXIT',get_out))

        # 탈 사람은 타라!
        if get_in != []:
            print("탈사람", make_command(0, 'ENTER', get_in))
            action(make_command(0,'ENTER',get_in))

        #닫어!
        action(make_command(0,'CLOSE',[]))

        #계속 나아가자!
        if core["elevators"][0]['floor'] == 1:
            action(make_command(0, 'UP',[]))
            direction = "up"

        elif core["elevators"][0]['floor'] == 5:
            action(make_command(0, 'DOWN',[]))
            direction = "down"

        else:
            if direction == "up":
                action(make_command(0,'UP',[]))
            elif direction == 'down':
                action(make_command(0,'DOWN',[]))

    print(request_count)
    print("어피치 완료")

Apeach_Tower()
