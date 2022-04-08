#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

class MediaPlayer:
    def play(self, audioType, fileName):
        pass

class AudioPlayer(MediaPlayer):
    def __init__(self):
        self._mediaAdapter = None
    @property
    def mediaAdapter(self):
        return self._mediaAdapter
    def play(self, audioType, fileName):
        if audioType == 'mp3':
            print("Playing mp3 file. Name: " + fileName)
        elif audioType == 'vlc' or audioType == 'mp4':
            self.mediaAdapter = MediaAdapter(audioType)
            self.mediaAdapter.play(audioType, fileName)
        else:
            print("Invalid media. "+ audioType + " format not supported")


class MediaAdapter(MediaPlayer):
    def __init__(self, audioType):
        if audioType == 'vlc':
            self._advancedMediaPlayer = VlcPlayer()
        elif audioType == 'mp4':
            self._advancedMediaPlayer = Mp4Player()
    @property
    def advancedMediaPlayer(self):
        return self._advancedMediaPlayer
    def play(self, audioType, fileName):
        if audioType == 'vlc':
            self.advancedMediaPlayer.playVlc(fileName)
        elif audioType == 'mp4':
            self.advancedMediaPlayer.playMp4(fileName)

class AdvancedMediaPlayer:
    def playVlc(self, fileName):
        pass
    def playMp4(self, fileName):
        pass

class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self, fileName):
        print("Playing vlc file. Name: "+ fileName)

class Mp4Player(AdvancedMediaPlayer):
    def playMp4(self, fileName):
        print("Playing mp4 file. Name: "+ fileName)

if __name__ == '__main__':
    audioPlayer = AudioPlayer()
 
    audioPlayer.play("mp3", "beyond the horizon.mp3")
    audioPlayer.play("mp4", "alone.mp4")
    audioPlayer.play("vlc", "far far away.vlc")
    audioPlayer.play("avi", "mind me.avi")
