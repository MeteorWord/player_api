# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseMods3jU1UyW", version="0.0.1")
class Script_NeteaseMods3jU1UyW(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseMods3jU1UyWServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseMods3jU1UyWServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseMods3jU1UyWClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseMods3jU1UyWClientDestroy(self):
        pass
