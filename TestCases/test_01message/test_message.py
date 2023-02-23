from PageObjects.message_cen.message_cen_bs import MessageBS


class TestMessage:
    def test_message(self, access_web):
        MessageBS(access_web).messageSelect()
        MessageBS(access_web).messageReceiveSet()
        MessageBS(access_web).messagePublish()
        MessageBS(access_web).messageDel()
