from rackio_AI import RackioAI, RackioEDA


class Wrangler(RackioEDA):
    """
    Documentation here
    """
    app = RackioAI

    def __init__(self, **kwargs):
        """
        Documentation here
        """
        super(Wrangler, self).__init__(**kwargs)

    def save(self, filename):
        """
        Documentation here
        """
        self.app.save(self.app.data, filename)
