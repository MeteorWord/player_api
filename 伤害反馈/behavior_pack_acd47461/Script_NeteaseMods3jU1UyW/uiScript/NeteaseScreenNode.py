# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
import Preset.Controller.PresetApi as presetApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class NeteaseScreenNode(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.ftext = "/panel/label"

	def Create(self):#实例化文字控件并修改文字
		atext = self.GetBaseUIControl(self.ftext).asLabel()
		fvalue = presetApi.GetPresetByName("Player0").GetPartByName("反馈零件").getvh()
		if fvalue > 0 and fvalue <= 3:
			atext.SetText("§6" + str(fvalue))
		if fvalue >3 and fvalue <= 6:
			atext.SetText("§9" + str(fvalue))
		if fvalue >6:
			atext.SetText("§4" + str(fvalue))
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		comp.AddTimer(0.25, self.removeit)

	def removeit(self):#移除界面
		self.SetRemove()

