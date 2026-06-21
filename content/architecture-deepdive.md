import os
import json
import time
import hashlib
import subprocess
import traceback

ROOT="starship_eternal"
LEDGER=f"{ROOT}/eternal_ledger.jsonl"
STATE=f"{ROOT}/state.json"

os.makedirs(ROOT, exist_ok=True)


def hash_event(data):
    return hashlib.sha256(
        json.dumps(data).encode()
    ).hexdigest()


def log(event, payload):

    record={
        "timestamp":time.time(),
        "event":event,
        "payload":payload
    }

    record["hash"]=hash_event(record)

    with open(LEDGER,"a") as f:
        f.write(json.dumps(record)+"\n")

    print("📜",event)



def save_state(cycle):

    with open(STATE,"w") as f:
        json.dump(
            {
             "cycle":cycle,
             "status":"ALIVE",
             "last_seen":time.time()
            },
            f,
            indent=2
        )



def run_module(name,cmd):

    print("⚙️",name)

    result=subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode==0:

        log(
          "MODULE_SUCCESS",
          {"module":name}
        )

        return True

    else:

        log(
          "MODULE_FAILURE",
          {
           "module":name,
           "error":result.stderr
          }
        )

        return False



def eternal_loop():

    cycle=0

    log(
        "STARSHIP_ETERNAL_ONLINE",
        {}
    )


    while True:

        try:

            cycle+=1

            print(
             f"""
========================
🚀 STARSHIP CYCLE {cycle}
========================
"""
            )


            save_state(cycle)


            systems=[

             (
              "CYBERNETIC_FACTORY",
              [
               "python",
               "starship_core.py"
              ]
             ),

             (
              "LAW_SWARM",
              [
               "python",
               "law_swarm.py"
              ]
             ),

             (
              "VALIDATION_GATE",
              [
               "./mock_starship_ctl.sh",
               "engage"
              ]
             )

            ]


            for name,cmd in systems:

                run_module(
                    name,
                    cmd
                )


            log(
             "CYCLE_COMPLETE",
             {"cycle":cycle}
            )


            time.sleep(30)


        except KeyboardInterrupt:

            log(
             "OPERATOR_SHUTDOWN",
             {}
            )

            break


        except Exception as e:

            log(
              "SELF_REPAIR_TRIGGER",
              {
               "error":str(e),
               "trace":
               traceback.format_exc()
              }
            )

            time.sleep(10)



if __name__=="__main__":

    eternal_loop()

import os
import json
import time
import hashlib
import subprocess

ROOT="starship_factory"
SKILLS=f"{ROOT}/skills"
LEDGER=f"{ROOT}/ledger.jsonl"

os.makedirs(SKILLS,exist_ok=True)


def event(t,data):
    record={
        "time":time.time(),
        "type":t,
        "data":data
    }

    raw=json.dumps(record)
    record["hash"]=hashlib.sha256(
        raw.encode()
    ).hexdigest()

    with open(LEDGER,"a") as f:
        f.write(json.dumps(record)+"\n")

    print("📜",t)


def build_skill(name):

    print("🧠 Designing:",name)

    code=f'''
class AgentSkill:

    name="{name}"

    def run(self,input):
        return {{
          "agent":self.name,
          "result":"completed",
          "input":input
        }}
'''

    path=f"{SKILLS}/{name}.py"

    with open(path,"w") as f:
        f.write(code)

    event(
      "SKILL_CREATED",
      {"skill":name}
    )

    return path



def validate():

    print("🧪 Running validation")

    result=subprocess.run(
        [
          "./mock_starship_ctl.sh",
          "engage"
        ]
    )

    return result.returncode==0



def cybernetic_loop():

    objectives=[
        "memory_agent",
        "planner_agent",
        "builder_agent",
        "repair_agent",
        "deployment_agent"
    ]

    for obj in objectives:

        build_skill(obj)

        if validate():
            event(
              "SKILL_APPROVED",
              {"skill":obj}
            )

            print(
              "✅ integrated:",
              obj
            )

        else:
            event(
              "ROLLBACK",
              {"skill":obj}
            )

            print(
              "❌ rejected:",
              obj
            )


if __name__=="__main__":

    print(
    """
🚀 STARSHIP CYBERNETIC CORE ONLINE
    """
    )

    cybernetic_loop()

