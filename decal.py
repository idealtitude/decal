#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import wx

import gettext


class DeCal(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_bpm = wx.StaticText(self, wx.ID_ANY, _("bpm"))
        self.spin_ctrl_bpm = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=300)
        self.button_execute = wx.Button(self, wx.ID_OK, "", style=wx.BU_EXACTFIT)
        self.button_toggle_results = wx.ToggleButton(self, wx.ID_ANY, _("*"))
        self.bitmap_3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./img/blanche.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./img/noire.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./img/croche.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./img/double_croche.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./img/binaire_symbol.png", wx.BITMAP_TYPE_ANY))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.bitmap_2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./img/ternaire_symbol.png", wx.BITMAP_TYPE_ANY))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_7 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_8 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_exit = wx.Button(self, wx.ID_EXIT, "")
        self.button_save_results = wx.Button(self, wx.ID_SAVE, "")
        self.button_print = wx.Button(self, wx.ID_PRINT, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.get_results, self.button_execute)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_results, self.button_toggle_results)
        self.Bind(wx.EVT_BUTTON, self.decal_exit, self.button_exit)
        self.Bind(wx.EVT_BUTTON, self.save_results, self.button_save_results)
        self.Bind(wx.EVT_BUTTON, self.print_results, self.button_print)

    def __set_properties(self):
        self.SetTitle(_("DeCal"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("./img/binaire_symbol.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((431, 229))
        self.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.label_bpm.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.label_bpm.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_execute.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.button_execute.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_toggle_results.SetMinSize((24, 24))
        self.button_toggle_results.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.button_toggle_results.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_exit.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.button_exit.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_save_results.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.button_save_results.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_print.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.button_print.SetForegroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        subsizer1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_buttons = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_results = wx.GridSizer(3, 5, 0, 0)
        sizer_bpm = wx.BoxSizer(wx.HORIZONTAL)
        sizer_bpm.Add(self.label_bpm, 0, wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        sizer_bpm.Add(self.spin_ctrl_bpm, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 5)
        sizer_bpm.Add(self.button_execute, 0, wx.ADJUST_MINSIZE | wx.FIXED_MINSIZE, 0)
        subsizer1.Add(sizer_bpm, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_results.Add(self.button_toggle_results, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_results.Add(self.bitmap_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.bitmap_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.bitmap_5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.bitmap_6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.bitmap_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.bitmap_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        grid_sizer_results.Add(self.text_ctrl_8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ADJUST_MINSIZE, 0)
        subsizer1.Add(grid_sizer_results, 10, wx.LEFT | wx.RIGHT, 0)
        grid_sizer_buttons.Add(self.button_exit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_buttons.Add(self.button_save_results, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_buttons.Add(self.button_print, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        subsizer1.Add(grid_sizer_buttons, 10, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_main.Add(subsizer1, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_main)
        self.Layout()

    def get_results(self, event):
       bpm = self.spin_ctrl_bpm.GetValue()
       nbpm = 60000 / bpm

       binaire = {'blanche': nbpm * 2, 'noire': nbpm, 'croche': nbpm / 2, 'dcroche': nbpm / 4}
       ternaire = {'blanche': nbpm * 4 / 3, 'noire': nbpm * 2 / 3, 'croche': nbpm / 3, 'dcroche': nbpm / 6}

       self.text_ctrl_1.SetValue(str(binaire['blanche']))
       self.text_ctrl_2.SetValue(str(binaire['noire']))
       self.text_ctrl_3.SetValue(str(binaire['croche']))
       self.text_ctrl_4.SetValue(str(binaire['dcroche']))

       self.text_ctrl_5.SetValue(str(ternaire['blanche']))
       self.text_ctrl_6.SetValue(str(ternaire['noire']))
       self.text_ctrl_7.SetValue(str(ternaire['croche']))
       self.text_ctrl_8.SetValue(str(ternaire['dcroche']))

    def toggle_results(self, event):
        print "Event handler 'toggle_results' not implemented!"
        event.Skip()

    def decal_exit(self, event):
        self.Close()

    def save_results(self, event):
        print "Event handler 'save_results' not implemented!"
        event.Skip()

    def print_results(self, event):
        print "Event handler 'print_results' not implemented!"
        event.Skip()


if __name__ == "__main__":
    gettext.install("app")

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_main = DeCal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_main)
    frame_main.Show()
    app.MainLoop()
    
