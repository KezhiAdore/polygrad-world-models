from .debug import base, args_to_watch, logbase

params = {
        'diffusion_method': 'autoregressive',
        'suite':'gym',
        'horizon': 2, # train on sequences of two states
        'rollout_steps': 100, # how far to rollout autoregressively
}
base.update(params)