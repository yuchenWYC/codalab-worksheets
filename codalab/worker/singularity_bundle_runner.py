from codalab.worker.bundle_runner import BundleRunner, DEFAULT_RUNTIME


class SingularityBundleRunner(BundleRunner):

    def __init__(self):
        self.f = 1

    def run(self,
            path,
            uuid,
            dependencies,
            command,
            image_spec,
            network=None,
            cpuset=None,
            gpuset=None,
            memory_bytes=0,
            detach=True,
            tty=False,
            runtime=DEFAULT_RUNTIME):
        pass