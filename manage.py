from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import subprocess as subp
import os
from  urllib.parse import urlparse
import json

instance = None
bindTo = ('localhost', 8000)
loc = bindTo[0] + str(bindTo[1])
class Instance():
    def __init__(self, s):
        inp = s
        lines = inp.split("\n")
        n = int(lines[0].split()[0])
        firm_pref = lines[1:n+1]
        m = int(lines[n+1].split()[0])
        workers_pref = lines[n+2:n+2+m]
        caps = list(map(int, [line.split()[0] for line in lines[n+2+m:n+2+m+n]]))

        self.n, self.m = n,m
        self.firms_pref, self.workers_pref = [], []
        for f in firm_pref:
            raw = list(map(int, f.split()))
            raw.extend([-1]*(m - len(raw)))
            self.firms_pref.append(raw)
        for w in workers_pref:
            raw = list(map(int, w.split()))
            raw.extend([-1]*(n-len(raw)))
            self.workers_pref.append(raw)
        self.worker_pref = workers_pref
        self.caps = caps
    
    def printRaw(self):
        s = []
        s.append(str(self.n) + " " + str(self.m))
        s.extend([" ".join(map(str, line)) for line in self.firms_pref])
        s.append(str(self.m))
        s.extend([" ".join(map(str,line)) for line in self.workers_pref])
        s.append(" ".join(map(str, self.caps)))

        with open("instance_raw.txt", "w") as f:
            for line in s:
                f.write(line)
                f.write("\n")
        
        with open("capacities.html", "w") as f:
            f.write("""
            <!DOCTYPE html>
                <html>
                <head>
                <style>
                table { width:100%;border: 1px solid black; border-collapse:collapse }html, body { width:100%; height:100%; margin:0; }
                td, th { text-align: center; font-size:20pt; }
                th { background-color:black; color:white; }
                </style>
                </head>
            """)
            f.write("\n")

            incButtons = ""
            decButtons = ""
            firms = ""
            caps = ""
            for i in range(self.n):
                incButtons += f"""
                    <td><button id="{i+1}" onClick="addCap(this.id)"> + </button></td> 
                """
            for i in range(self.n):
                decButtons += f"""
                    <td><button id="{i+1}" onClick="delCap(this.id)"> -  </button></td> 
                """
            for i in range(self.n):
                firms += f"""
                    <td> Firm {i+1}</td>
                """
            for i in range(self.n):
                caps += f"""
                    <td id> {self.caps[i]}</td>
                """

            f.write(f"""
                <body>
                <table>
                    <tr id="capacities">
                        {firms}
                    </tr>
                    <tr id="incButtons">
                        {incButtons}
                    </tr>
                    <tr id="capacities">
                        {caps}
                    </tr>
                    <tr id="decButtons">
                        {decButtons}
                    </tr>
                </table>
            """)
            f.write("""

            <script type="text/javascript"> 

                  function delCap(id) {
                        var host = window.location.origin;
                        fetch(host, {
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        method: "POST",
                        body: JSON.stringify({
                            "method": "POST",
                            "id": id,
                            "change": -1
                        })
                        }).then((resp) => {
                        console.log(resp);
                        window.top.location.reload();
                        })
                    }
                    function addCap(id) {
                        var host = window.location.origin;
                        fetch(host, {
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        method: "POST",
                        body: JSON.stringify({
                            "method": "POST",
                            "id": id,
                            "change": 1
                        })
                        }).then((resp) => {
                        console.log(resp);
                        window.top.location.reload();
                        })
                    }


            </script> 
            </body>
            """)

    def addSeats(self, i, d):
        self.caps[i-1] += d
    
    def compile(self):
        instance.printRaw()
        subp.run("../gen.sh", shell=True)


class RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        global instance, bindTo
        length = int(self.headers['content-length'])
        field_data = self.rfile.read(length)
        data = json.loads(field_data.decode("utf-8"))

        instance.addSeats(int(data["id"]), int(data["change"]))
        instance.compile()
        
        self.send_response(200, "OK")
        self.send_header("Content-type", "text/html")
        self.end_headers()




if __name__ == "__main__":
    lines = None
    os.chdir("./result")
    with open("../instance.txt", "r") as f:
        lines = f.readlines()
    instance = Instance("".join(lines))
    instance.printRaw()
    subp.run("../gen.sh", shell=True)

    server = HTTPServer(('localhost', 8000), RequestHandler)
    server.serve_forever()
    server.close()

    # while(True):
    #     s = input()
    #     s = s.split()
    #     if(s[0] == 'i'):
    #         i = int(s[1])
    #         d = 1
    #         if(len(s) > 2):
    #             d = int(s[2])
    #         instance.addSeats(i,d)
    #         instance.printRaw()
    #         subp.run("../gen.sh", shell=True)

    #     elif(s[0] == 'd'):
    #         i = int(s[1])
    #         i = int(s[1])
    #         d = 1
    #         if(len(s) > 2):
    #             d = int(s[2])
    #         instance.addSeats(i,-d)
    #         instance.printRaw()
    #         subp.run("../gen.sh", shell=True)
    #     else:   
    #         break