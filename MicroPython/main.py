"""
   An example script for stepper motors, using CW drivers
   written by Jake@circuitspecialists.com
   licensed as GPLv3
"""

import _thread


class STEPPER_MOTOR():
    def __init__(self):
        self.startHTTP()

    def startHTTP(self):
        try:
            from microWebSrv import MicroWebSrv
            self.mws = MicroWebSrv()      # TCP port 80 and files in /flash/www
            self.mws.Start(threaded=True)  # Starts server in a new thread
        except:
            print("HTTP Server failed to start")

    @mws.route('/start')
    def _httpHandlerFileGet(self, httpClient, httpResponse):
        gc.mem_free()
        httpResponse.WriteResponseOk(headers=({
            'Cache-Control': 'no-cache'
        }),
            contentType='text/event-stream',
            contentCharset='UTF-8',
            content='data: {0}'.format())

    def _acceptWebSocketCallback(self, webSocket, httpClient):
        print("WS ACCEPT")
        webSocket.RecvTextCallback = _recvTextCallback
        webSocket.RecvBinaryCallback = _recvBinaryCallback
        webSocket.ClosedCallback = _closedCallback

    def _recvTextCallback(self, webSocket, msg):
        print("WS RECV TEXT : %s" % msg)
        webSocket.SendText("Reply for %s" % msg)

    def _recvBinaryCallback(self, webSocket, data):
        print("WS RECV DATA : %s" % data)

    def _closedCallback(self, webSocket):
        print("WS CLOSED")
