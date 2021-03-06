# Copyright (c) Facebook, Inc. and its affiliates.
# 
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from ctrl.strategies.task_creation_strategy import TaskCreationStrategy


class IncrementalStrategy(TaskCreationStrategy):
    def __init__(self, new_classes_per_task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_classes_per_task = new_classes_per_task

    def new_task(self, concepts, transformations, previous_tasks, n_samples_per_class):
        if not previous_tasks:
            return self._create_new_task(concepts, transformations)

        prev_task = previous_tasks[-1]
        new_concepts = concepts.get_compatible_concepts(self.new_classes_per_task, prev_task.concepts, True)
        concepts = prev_task.src_concepts + [[c] for c in new_concepts]
        return concepts, prev_task.attributes, prev_task.transformation
