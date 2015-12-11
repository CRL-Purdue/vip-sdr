#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Dec 10 14:41:59 2015
##################################################

# Call XInitThreads as the _very_ first thing.
# After some Qt import, it's too late
import ctypes
import sys
if sys.platform.startswith('linux'):
    try:
        x11 = ctypes.cdll.LoadLibrary('libX11.so')
        x11.XInitThreads()
    except:
        print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys

from distutils.version import StrictVersion
class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000
        self.repeat = repeat = samp_rate/80

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.blocks_unpacked_to_packed_xx_1 = blocks.unpacked_to_packed_bb(8, gr.GR_MSB_FIRST)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_uchar_to_float_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_char_0 = blocks.short_to_char(1)
        self.blocks_rms_xx_0_0 = blocks.rms_ff(1)
        self.blocks_rms_xx_0 = blocks.rms_ff(1)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, repeat)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vss((256, ))
        self.blocks_integrate_xx_1 = blocks.integrate_ff(repeat)
        self.blocks_integrate_xx_0_1 = blocks.integrate_ff(repeat)
        self.blocks_integrate_xx_0_0 = blocks.integrate_ff(repeat)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(repeat)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*1, "/home/sidekiq/Documents/Documentation_SDR/sdr.in", True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, "/home/sidekiq/Documents/Documentation_SDR/text_output", False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.blocks_abs_xx_0_2 = blocks.abs_ff(1)
        self.blocks_abs_xx_0_1 = blocks.abs_ff(1)
        self.blocks_abs_xx_0_0 = blocks.abs_ff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=1,
        		bits_per_symbol=1,
        		preamble="11111000",
        		access_code="11111111",
        		pad_for_usrp=False,
        	),
        	payload_length=1,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code="",
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.audio_sink_1 = audio.sink(16000, "", True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1330, 1, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1330, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 2720, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 2720, 1, 0)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(100)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_2, 0))    
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_unpacked_to_packed_xx_1, 0))    
        self.connect((self.blks2_packet_encoder_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))    
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_abs_xx_0_0, 0), (self.blocks_add_xx_0_0, 0))    
        self.connect((self.blocks_abs_xx_0_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_abs_xx_0_2, 0), (self.blocks_add_xx_0_0, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.analog_frequency_modulator_fc_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_rms_xx_0, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_rms_xx_0_0, 0))    
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_short_to_float_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.audio_sink_1, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_1, 1))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_2, 1))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blks2_packet_decoder_0, 0))    
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_abs_xx_0_2, 0))    
        self.connect((self.blocks_integrate_xx_0_0, 0), (self.blocks_abs_xx_0, 0))    
        self.connect((self.blocks_integrate_xx_0_1, 0), (self.blocks_abs_xx_0_0, 0))    
        self.connect((self.blocks_integrate_xx_1, 0), (self.blocks_abs_xx_0_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_short_to_char_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_integrate_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_integrate_xx_1, 0))    
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_integrate_xx_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_integrate_xx_0_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blks2_packet_encoder_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_uchar_to_float_0_0_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_argmax_xx_0, 1))    
        self.connect((self.blocks_rms_xx_0_0, 0), (self.blocks_argmax_xx_0, 0))    
        self.connect((self.blocks_short_to_char_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_uchar_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_uchar_to_float_0, 0))    
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_uchar_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_unpacked_to_packed_xx_1, 0), (self.blocks_file_sink_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_repeat(self.samp_rate/80)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_repeat(self):
        return self.repeat

    def set_repeat(self, repeat):
        self.repeat = repeat

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
