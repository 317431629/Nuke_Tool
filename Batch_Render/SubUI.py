# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Administrator/.nuke/Batch_Render\UI\SubUI.ui'
#
# Created: Sun Jun 16 22:22:58 2019
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Out_Type(object):
    def setupUi(self, Out_Type):
        Out_Type.setObjectName("Out_Type")
        Out_Type.resize(553, 677)
        self.exr_GroupBox = QtWidgets.QGroupBox(Out_Type)
        self.exr_GroupBox.setEnabled(False)
        self.exr_GroupBox.setGeometry(QtCore.QRect(10, 10, 520, 311))
        self.exr_GroupBox.setObjectName("exr_GroupBox")
        self.write_ACES_compliant_EXR = QtWidgets.QCheckBox(self.exr_GroupBox)
        self.write_ACES_compliant_EXR.setGeometry(QtCore.QRect(121, 31, 167, 16))
        self.write_ACES_compliant_EXR.setObjectName("write_ACES_compliant_EXR")
        self.autocrop = QtWidgets.QCheckBox(self.exr_GroupBox)
        self.autocrop.setGeometry(QtCore.QRect(294, 31, 71, 16))
        self.autocrop.setObjectName("autocrop")
        self.datatype_exr = QtWidgets.QComboBox(self.exr_GroupBox)
        self.datatype_exr.setGeometry(QtCore.QRect(120, 55, 69, 20))
        self.datatype_exr.setObjectName("datatype_exr")
        self.datatype_exr.addItem("")
        self.datatype_exr.addItem("")
        self.label_4 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_4.setGeometry(QtCore.QRect(59, 55, 48, 16))
        self.label_4.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_4.setObjectName("label_4")
        self.compression = QtWidgets.QComboBox(self.exr_GroupBox)
        self.compression.setGeometry(QtCore.QRect(120, 85, 93, 20))
        self.compression.setObjectName("compression")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.compression.addItem("")
        self.label_7 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 85, 66, 16))
        self.label_7.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_8.setGeometry(QtCore.QRect(12, 111, 102, 16))
        self.label_8.setObjectName("label_8")
        self.compression_lavel_Slider = QtWidgets.QSlider(self.exr_GroupBox)
        self.compression_lavel_Slider.setGeometry(QtCore.QRect(186, 111, 321, 21))
        self.compression_lavel_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.compression_lavel_Slider.setObjectName("compression_lavel_Slider")
        self.label_9 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_9.setGeometry(QtCore.QRect(61, 145, 48, 16))
        self.label_9.setObjectName("label_9")
        self.heroview = QtWidgets.QComboBox(self.exr_GroupBox)
        self.heroview.setGeometry(QtCore.QRect(120, 145, 69, 20))
        self.heroview.setObjectName("heroview")
        self.heroview.addItem("")
        self.label_10 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_10.setGeometry(QtCore.QRect(61, 171, 48, 16))
        self.label_10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_10.setObjectName("label_10")
        self.metadata = QtWidgets.QComboBox(self.exr_GroupBox)
        self.metadata.setGeometry(QtCore.QRect(120, 171, 141, 21))
        self.metadata.setObjectName("metadata")
        self.metadata.addItem("")
        self.metadata.addItem("")
        self.metadata.addItem("")
        self.metadata.addItem("")
        self.metadata.addItem("")
        self.noprefix = QtWidgets.QCheckBox(self.exr_GroupBox)
        self.noprefix.setGeometry(QtCore.QRect(267, 173, 143, 16))
        self.noprefix.setObjectName("noprefix")
        self.label_11 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_11.setGeometry(QtCore.QRect(50, 195, 60, 16))
        self.label_11.setMaximumSize(QtCore.QSize(60, 20))
        self.label_11.setObjectName("label_11")
        self.interleave = QtWidgets.QComboBox(self.exr_GroupBox)
        self.interleave.setGeometry(QtCore.QRect(120, 195, 181, 21))
        self.interleave.setObjectName("interleave")
        self.interleave.addItem("")
        self.interleave.addItem("")
        self.interleave.addItem("")
        self.label_12 = QtWidgets.QLabel(self.exr_GroupBox)
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QtCore.QRect(50, 220, 60, 16))
        self.label_12.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_12.setObjectName("label_12")
        self.first_part = QtWidgets.QComboBox(self.exr_GroupBox)
        self.first_part.setEnabled(False)
        self.first_part.setGeometry(QtCore.QRect(120, 220, 318, 19))
        self.first_part.setObjectName("first_part")
        self.first_part.addItem("")
        self.standardlayernameformat = QtWidgets.QCheckBox(self.exr_GroupBox)
        self.standardlayernameformat.setGeometry(QtCore.QRect(120, 245, 181, 21))
        self.standardlayernameformat.setChecked(False)
        self.standardlayernameformat.setObjectName("standardlayernameformat")
        self.write_full_layer_names = QtWidgets.QCheckBox(self.exr_GroupBox)
        self.write_full_layer_names.setEnabled(False)
        self.write_full_layer_names.setGeometry(QtCore.QRect(120, 265, 181, 21))
        self.write_full_layer_names.setObjectName("write_full_layer_names")
        self.truncateChannelNames = QtWidgets.QCheckBox(self.exr_GroupBox)
        self.truncateChannelNames.setEnabled(False)
        self.truncateChannelNames.setGeometry(QtCore.QRect(120, 285, 181, 21))
        self.truncateChannelNames.setObjectName("truncateChannelNames")
        self.compression_lavel = QtWidgets.QLineEdit(self.exr_GroupBox)
        self.compression_lavel.setEnabled(False)
        self.compression_lavel.setGeometry(QtCore.QRect(120, 111, 60, 20))
        self.compression_lavel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.compression_lavel.setObjectName("compression_lavel")
        self.jpeg_GroupBox = QtWidgets.QGroupBox(Out_Type)
        self.jpeg_GroupBox.setEnabled(False)
        self.jpeg_GroupBox.setGeometry(QtCore.QRect(10, 320, 520, 81))
        self.jpeg_GroupBox.setObjectName("jpeg_GroupBox")
        self.label_13 = QtWidgets.QLabel(self.jpeg_GroupBox)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 51, 16))
        self.label_13.setObjectName("label_13")
        self.jpeg_quality_Slider = QtWidgets.QSlider(self.jpeg_GroupBox)
        self.jpeg_quality_Slider.setGeometry(QtCore.QRect(160, 20, 361, 21))
        self.jpeg_quality_Slider.setMaximum(100)
        self.jpeg_quality_Slider.setSingleStep(1)
        self.jpeg_quality_Slider.setPageStep(0)
        self.jpeg_quality_Slider.setProperty("value", 75)
        self.jpeg_quality_Slider.setTracking(True)
        self.jpeg_quality_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.jpeg_quality_Slider.setObjectName("jpeg_quality_Slider")
        self.label_14 = QtWidgets.QLabel(self.jpeg_GroupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_14.setObjectName("label_14")
        self._jpeg_sub_sampling = QtWidgets.QComboBox(self.jpeg_GroupBox)
        self._jpeg_sub_sampling.setGeometry(QtCore.QRect(93, 50, 69, 22))
        self._jpeg_sub_sampling.setObjectName("_jpeg_sub_sampling")
        self._jpeg_sub_sampling.addItem("")
        self._jpeg_sub_sampling.addItem("")
        self._jpeg_sub_sampling.addItem("")
        self._jpeg_quality = QtWidgets.QLineEdit(self.jpeg_GroupBox)
        self._jpeg_quality.setGeometry(QtCore.QRect(93, 20, 61, 21))
        self._jpeg_quality.setObjectName("_jpeg_quality")
        self.mov_GroupBox = QtWidgets.QGroupBox(Out_Type)
        self.mov_GroupBox.setEnabled(False)
        self.mov_GroupBox.setGeometry(QtCore.QRect(10, 450, 411, 201))
        self.mov_GroupBox.setObjectName("mov_GroupBox")
        self.label_15 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_15.setGeometry(QtCore.QRect(12, 32, 48, 16))
        self.label_15.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_15.setObjectName("label_15")
        self.meta_codec = QtWidgets.QComboBox(self.mov_GroupBox)
        self.meta_codec.setGeometry(QtCore.QRect(66, 32, 176, 20))
        self.meta_codec.setObjectName("meta_codec")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.meta_codec.addItem("")
        self.label_16 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_16.setEnabled(False)
        self.label_16.setGeometry(QtCore.QRect(248, 32, 42, 16))
        self.label_16.setObjectName("label_16")
        self.meta_encodec = QtWidgets.QComboBox(self.mov_GroupBox)
        self.meta_encodec.setEnabled(False)
        self.meta_encodec.setGeometry(QtCore.QRect(296, 32, 69, 20))
        self.meta_encodec.setObjectName("meta_encodec")
        self.label_17 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_17.setEnabled(False)
        self.label_17.setGeometry(QtCore.QRect(12, 65, 78, 16))
        self.label_17.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_17.setObjectName("label_17")
        self.mov_64_dnxhd_codec_profile = QtWidgets.QComboBox(self.mov_GroupBox)
        self.mov_64_dnxhd_codec_profile.setEnabled(False)
        self.mov_64_dnxhd_codec_profile.setGeometry(QtCore.QRect(99, 65, 143, 19))
        self.mov_64_dnxhd_codec_profile.setObjectName("mov_64_dnxhd_codec_profile")
        self.label_18 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_18.setGeometry(QtCore.QRect(21, 91, 72, 16))
        self.label_18.setObjectName("label_18")
        self.mov32_fps_Slider = QtWidgets.QSlider(self.mov_GroupBox)
        self.mov32_fps_Slider.setGeometry(QtCore.QRect(180, 91, 191, 21))
        self.mov32_fps_Slider.setProperty("value", 24)
        self.mov32_fps_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.mov32_fps_Slider.setObjectName("mov32_fps_Slider")
        self.label_19 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_19.setGeometry(QtCore.QRect(20, 117, 72, 16))
        self.label_19.setObjectName("label_19")
        self.mov32_audiofile = QtWidgets.QLineEdit(self.mov_GroupBox)
        self.mov32_audiofile.setGeometry(QtCore.QRect(99, 115, 271, 21))
        self.mov32_audiofile.setObjectName("mov32_audiofile")
        self.pushButton = QtWidgets.QPushButton(self.mov_GroupBox)
        self.pushButton.setGeometry(QtCore.QRect(375, 114, 25, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_20 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_20.setGeometry(QtCore.QRect(21, 147, 72, 16))
        self.label_20.setObjectName("label_20")
        self.mov32_audio_offset_Slider = QtWidgets.QSlider(self.mov_GroupBox)
        self.mov32_audio_offset_Slider.setGeometry(QtCore.QRect(180, 146, 191, 21))
        self.mov32_audio_offset_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.mov32_audio_offset_Slider.setObjectName("mov32_audio_offset_Slider")
        self.mov32_audio_offset = QtWidgets.QLineEdit(self.mov_GroupBox)
        self.mov32_audio_offset.setGeometry(QtCore.QRect(99, 145, 75, 20))
        self.mov32_audio_offset.setMaximumSize(QtCore.QSize(75, 16777215))
        self.mov32_audio_offset.setObjectName("mov32_audio_offset")
        self.mov32_fps = QtWidgets.QLineEdit(self.mov_GroupBox)
        self.mov32_fps.setGeometry(QtCore.QRect(99, 91, 75, 19))
        self.mov32_fps.setMaximumSize(QtCore.QSize(75, 16777215))
        self.mov32_fps.setObjectName("mov32_fps")
        self.label_21 = QtWidgets.QLabel(self.mov_GroupBox)
        self.label_21.setGeometry(QtCore.QRect(61, 171, 36, 16))
        self.label_21.setObjectName("label_21")
        self.mov32_units = QtWidgets.QComboBox(self.mov_GroupBox)
        self.mov32_units.setGeometry(QtCore.QRect(99, 171, 69, 20))
        self.mov32_units.setObjectName("mov32_units")
        self.mov32_units.addItem("")
        self.mov32_units.addItem("")
        self.mov32_write_timecode = QtWidgets.QCheckBox(self.mov_GroupBox)
        self.mov32_write_timecode.setGeometry(QtCore.QRect(178, 173, 113, 16))
        self.mov32_write_timecode.setObjectName("mov32_write_timecode")
        self.png_GroupBox = QtWidgets.QGroupBox(Out_Type)
        self.png_GroupBox.setEnabled(False)
        self.png_GroupBox.setGeometry(QtCore.QRect(10, 400, 411, 51))
        self.png_GroupBox.setObjectName("png_GroupBox")
        self.label_22 = QtWidgets.QLabel(self.png_GroupBox)
        self.label_22.setGeometry(QtCore.QRect(30, 21, 54, 16))
        self.label_22.setObjectName("label_22")
        self.datatype = QtWidgets.QComboBox(self.png_GroupBox)
        self.datatype.setGeometry(QtCore.QRect(93, 21, 62, 20))
        self.datatype.setObjectName("datatype")
        self.datatype.addItem("")
        self.datatype.addItem("")
        self.Cancel_Button = QtWidgets.QPushButton(Out_Type)
        self.Cancel_Button.setGeometry(QtCore.QRect(450, 620, 75, 31))
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.Confirm_Butotn = QtWidgets.QPushButton(Out_Type)
        self.Confirm_Butotn.setGeometry(QtCore.QRect(450, 580, 75, 31))
        self.Confirm_Butotn.setObjectName("Confirm_Butotn")

        self.retranslateUi(Out_Type)
        self.write_ACES_compliant_EXR.clicked['bool'].connect(self.label_4.setDisabled)
        self.write_ACES_compliant_EXR.clicked['bool'].connect(self.datatype_exr.setDisabled)
        self.write_ACES_compliant_EXR.clicked['bool'].connect(self.label_7.setDisabled)
        self.write_ACES_compliant_EXR.clicked['bool'].connect(self.compression.setDisabled)
        self.Cancel_Button.clicked['bool'].connect(Out_Type.close)
        self.Confirm_Butotn.clicked.connect(Out_Type.close)
        QtCore.QMetaObject.connectSlotsByName(Out_Type)

    def retranslateUi(self, Out_Type):
        _translate = QtCore.QCoreApplication.translate
        Out_Type.setWindowTitle(_translate("Out_Type", "Form"))
        self.exr_GroupBox.setTitle(_translate("Out_Type", "exr"))
        self.write_ACES_compliant_EXR.setText(_translate("Out_Type", "write ACES compliant EXR"))
        self.autocrop.setText(_translate("Out_Type", "autocrop"))
        self.datatype_exr.setItemText(0, _translate("Out_Type", "16 bit half"))
        self.datatype_exr.setItemText(1, _translate("Out_Type", "32 bit half"))
        self.label_4.setText(_translate("Out_Type", "datatype"))
        self.compression.setItemText(0, _translate("Out_Type", "Zip (1 scanline)"))
        self.compression.setItemText(1, _translate("Out_Type", "none"))
        self.compression.setItemText(2, _translate("Out_Type", "Zip (16 scanline)"))
        self.compression.setItemText(3, _translate("Out_Type", "PIZ Wavelet(32 scanlinnes)"))
        self.compression.setItemText(4, _translate("Out_Type", "RLE"))
        self.compression.setItemText(5, _translate("Out_Type", "B44"))
        self.compression.setItemText(6, _translate("Out_Type", "B44A"))
        self.compression.setItemText(7, _translate("Out_Type", "DWAA"))
        self.compression.setItemText(8, _translate("Out_Type", "DWAB"))
        self.label_7.setText(_translate("Out_Type", "compression"))
        self.label_8.setText(_translate("Out_Type", "compression level"))
        self.label_9.setText(_translate("Out_Type", "heroview"))
        self.heroview.setItemText(0, _translate("Out_Type", "main"))
        self.label_10.setText(_translate("Out_Type", "metadata"))
        self.metadata.setItemText(0, _translate("Out_Type", "default metadata"))
        self.metadata.setItemText(1, _translate("Out_Type", "no metadatd"))
        self.metadata.setItemText(2, _translate("Out_Type", "default metadata and exr/*"))
        self.metadata.setItemText(3, _translate("Out_Type", "all metadata except input/*"))
        self.metadata.setItemText(4, _translate("Out_Type", "all metadate"))
        self.noprefix.setText(_translate("Out_Type", "do not attach prefix"))
        self.label_11.setText(_translate("Out_Type", "interleave"))
        self.interleave.setItemText(0, _translate("Out_Type", "channels,layers and views"))
        self.interleave.setItemText(1, _translate("Out_Type", "channels and layers"))
        self.interleave.setItemText(2, _translate("Out_Type", "channels"))
        self.label_12.setText(_translate("Out_Type", "first part"))
        self.first_part.setItemText(0, _translate("Out_Type", "none"))
        self.standardlayernameformat.setText(_translate("Out_Type", "standard layer name format"))
        self.write_full_layer_names.setText(_translate("Out_Type", "write full layer names"))
        self.truncateChannelNames.setText(_translate("Out_Type", "truncate channel names"))
        self.jpeg_GroupBox.setTitle(_translate("Out_Type", "jpeg"))
        self.label_13.setText(_translate("Out_Type", "quality"))
        self.label_14.setText(_translate("Out_Type", "sub-sampling"))
        self._jpeg_sub_sampling.setItemText(0, _translate("Out_Type", "4:1:1"))
        self._jpeg_sub_sampling.setItemText(1, _translate("Out_Type", "4:2:2"))
        self._jpeg_sub_sampling.setItemText(2, _translate("Out_Type", "4:4:4"))
        self._jpeg_quality.setText(_translate("Out_Type", "0.75"))
        self.mov_GroupBox.setTitle(_translate("Out_Type", "mov"))
        self.label_15.setText(_translate("Out_Type", "   codec"))
        self.meta_codec.setItemText(0, _translate("Out_Type", "Apple ProRes 4444"))
        self.meta_codec.setItemText(1, _translate("Out_Type", "Animation"))
        self.meta_codec.setItemText(2, _translate("Out_Type", "Apple ProRes 422"))
        self.meta_codec.setItemText(3, _translate("Out_Type", "Apple ProRes 422 HQ"))
        self.meta_codec.setItemText(4, _translate("Out_Type", "Apple ProRes 422 LT"))
        self.meta_codec.setItemText(5, _translate("Out_Type", "Apple ProRes 422 Proxy"))
        self.meta_codec.setItemText(6, _translate("Out_Type", "Apple ProRes 4444 XQ"))
        self.meta_codec.setItemText(7, _translate("Out_Type", "Avid DNxHD Codec"))
        self.meta_codec.setItemText(8, _translate("Out_Type", "BMP"))
        self.meta_codec.setItemText(9, _translate("Out_Type", "Cinepak"))
        self.meta_codec.setItemText(10, _translate("Out_Type", "Component Video"))
        self.meta_codec.setItemText(11, _translate("Out_Type", "DV_PAL"))
        self.meta_codec.setItemText(12, _translate("Out_Type", "DV/DVCPRO - NTSC"))
        self.meta_codec.setItemText(13, _translate("Out_Type", "DVCPRO - PAL"))
        self.meta_codec.setItemText(14, _translate("Out_Type", "H.261"))
        self.meta_codec.setItemText(15, _translate("Out_Type", "H.263"))
        self.meta_codec.setItemText(16, _translate("Out_Type", "H.264"))
        self.meta_codec.setItemText(17, _translate("Out_Type", "JPEG 2000"))
        self.meta_codec.setItemText(18, _translate("Out_Type", "MPEG-1 Video"))
        self.meta_codec.setItemText(19, _translate("Out_Type", "MPEG-4 Video"))
        self.meta_codec.setItemText(20, _translate("Out_Type", "Motion JPEG A"))
        self.meta_codec.setItemText(21, _translate("Out_Type", "Motion JPEG B"))
        self.meta_codec.setItemText(22, _translate("Out_Type", "PNG"))
        self.meta_codec.setItemText(23, _translate("Out_Type", "Photo - JPEG"))
        self.meta_codec.setItemText(24, _translate("Out_Type", "Planar RGB"))
        self.meta_codec.setItemText(25, _translate("Out_Type", "Sorenson Video"))
        self.meta_codec.setItemText(26, _translate("Out_Type", "Sorenson Video 3"))
        self.meta_codec.setItemText(27, _translate("Out_Type", "TGA"))
        self.meta_codec.setItemText(28, _translate("Out_Type", "TIFF"))
        self.meta_codec.setItemText(29, _translate("Out_Type", "Uncompressed 10-bit 4:2:2"))
        self.meta_codec.setItemText(30, _translate("Out_Type", "Video"))
        self.label_16.setText(_translate("Out_Type", "encoder"))
        self.label_17.setText(_translate("Out_Type", "codec profile"))
        self.label_18.setText(_translate("Out_Type", "         fps"))
        self.label_19.setText(_translate("Out_Type", "  audio file"))
        self.label_20.setText(_translate("Out_Type", "audio offest"))
        self.mov32_audio_offset.setText(_translate("Out_Type", "0"))
        self.mov32_fps.setText(_translate("Out_Type", "24"))
        self.label_21.setText(_translate("Out_Type", "units "))
        self.mov32_units.setItemText(0, _translate("Out_Type", "Seconds"))
        self.mov32_units.setItemText(1, _translate("Out_Type", "Frames"))
        self.mov32_write_timecode.setText(_translate("Out_Type", "write time code"))
        self.png_GroupBox.setTitle(_translate("Out_Type", "png"))
        self.label_22.setText(_translate("Out_Type", "data type"))
        self.datatype.setItemText(0, _translate("Out_Type", "8 bit"))
        self.datatype.setItemText(1, _translate("Out_Type", "16 bit"))
        self.Cancel_Button.setText(_translate("Out_Type", "Cancel"))
        self.Confirm_Butotn.setText(_translate("Out_Type", "Confirm"))
