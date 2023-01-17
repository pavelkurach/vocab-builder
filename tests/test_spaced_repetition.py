import pytest
from spaced_repetition import SpacedRepetition

states = {'Forgot': SpacedRepetition.states[0],
          'OK': SpacedRepetition.states[1],
          'Recalled easily': SpacedRepetition.states[2]}

last_bucket_number = list(SpacedRepetition.buckets.keys())[-1]

penultimate_bucket_number = list(SpacedRepetition.buckets.keys())[-2]


@pytest.mark.parametrize('bucket, state, new_bucket', [
    (0, states['Forgot'], 0),
    (3, states['Forgot'], 0),
    (0, states['OK'], 1),
    (1, states['OK'], 2),
    (last_bucket_number, states['OK'], last_bucket_number),
    (1, states['Recalled easily'], 3),
    (last_bucket_number, states['Recalled easily'], last_bucket_number),
    (penultimate_bucket_number, states['Recalled easily'],
     last_bucket_number),
])
def test_spaced_repetition_scheduler(bucket, state, new_bucket):
    assert SpacedRepetition.spaced_repetition_scheduler(bucket=bucket, state=state) == new_bucket


def test_spaced_repetition_scheduler_exceptions():
    with pytest.raises(ValueError):
        SpacedRepetition.spaced_repetition_scheduler(bucket=-1, state='OK')

    with pytest.raises(ValueError):
        SpacedRepetition.spaced_repetition_scheduler(bucket=0, state='SomeNonsense')

