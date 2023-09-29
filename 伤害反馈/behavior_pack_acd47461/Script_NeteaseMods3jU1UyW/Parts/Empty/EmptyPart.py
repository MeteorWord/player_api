# -*- coding: utf-8 -*-
from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass


@registerGenericClass("EmptyPart")
class EmptyPart(PartBase):
	def __init__(self):
		PartBase.__init__(self)
		# 零件名称
		self.name = "反馈零件"
		self.vhurt = 0

	def InitClient(self):#监听服务端发来的自定义事件
		import mod.client.extraClientApi as clientApi
		self.ListenSelfEvent("damageClient", self, self.creit)

	def UiInitFinished(self, args):#ui初始化完成时注册ui
		import mod.client.extraClientApi as clientApi
		clientApi.RegisterUI("yuguo", "ui0", "Script_NeteaseMods3jU1UyW.uiScript.NeteaseScreenNode.NeteaseScreenNode", "ui0.main")

	def DamageEvent(self, args):#监听实体受伤事件
		data = self.CreateEventData()
		data["id"] = args["entityId"]
		data["pid"] = args["srcId"]
		data["hurt"] = args["damage"]
		if args["srcId"] == self.GetParent().GetEntityId():
			self.NotifyToClient(self.GetParent().GetEntityId(), "damageClient", data)

	def creit(self, args):#自定义事件回调函数
		import mod.client.extraClientApi as clientApi
		self.vhurt = args["hurt"]
		clientApi.CreateUI("yuguo", "ui0", {"isHud": 1, "bindEntityId": args["id"], "autoScale": 0})

	def getvh(self):#供ui脚本文件获取伤害值
		return self.vhurt

	def DestroyClient(self):#反监听自定义事件
		self.UnListenSelfEvent("damageClient", self, self.creit)

