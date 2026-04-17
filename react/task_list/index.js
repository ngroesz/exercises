import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class TodoList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            expandedGroup: undefined
        };
    }

    handleExpandGroup = (groupName) => {
        this.setState({
            expandedGroup: groupName
        });
    }

    render() {
        let tasksByGroup = {};
        for(const task of this.props.tasks) {
            tasksByGroup[task['group']] || (tasksByGroup[task['group']] = []);
            tasksByGroup[task['group']].push(task);
        }

        let contents = null;
        if (this.state.expandedGroup ) {
            contents =
                <TaskGroup
                   key={this.state.expandedGroup}
                   name={this.state.expandedGroup}
                   tasks={tasksByGroup[this.state.expandedGroup]}
                   onClick={this.handleExpandGroup}
                   expanded
                />;

        } else {
            contents =
                <React.Fragment>
                    <div className="heading">Things To Do</div>
                    <br style={{clear: 'left'}} />
                    <ul>
                        {Object.keys(tasksByGroup).map((taskGroupName) => {
                            return <TaskGroup
                                key={taskGroupName}
                                name={taskGroupName}
                                tasks={tasksByGroup[taskGroupName]}
                                onClick={this.handleExpandGroup}
                            />
                        })}
                    </ul>
                </React.Fragment>;
        }
        return (
            <div className="todo">
              {contents}
            </div>
        );
    }
}

class TaskGroup extends React.Component {
    static defaultProps = {
        expanded: false
    }

    handleExpandGroup = () => {
        this.props.onClick(this.props.name);
    }

    handleCloseGroup = () => {
        this.props.onClick(undefined);
    }

    handleClickTask = (taskId) => {
        let task = this.props.tasks.find(function(task) {
            return task.id === taskId;
        });
        if (task.completedAt) {
            task.completedAt = null;
        } else {
            task.completedAt = new Date();
        }
        this.setState({state: this.state});
    }

    render() {
        const name = this.props.name;
        if (this.props.expanded) {
            function dependentAndIncompleteTasks(task) {
                return this.dependencyIds.indexOf(task.id) !== -1 && task.completedAt === null;
            }

            let tasks = [];
            for(const task of this.props.tasks) {
                const unfinishedTasks = this.props.tasks.filter(dependentAndIncompleteTasks, task);
                let taskStatus = 'locked';
                if (unfinishedTasks.length === 0) {
                    if (task.completedAt) {
                        taskStatus = 'complete';
                    } else {
                        taskStatus = 'incomplete';
                    }
                }
                tasks.push(
                    <Task
                        key={task.task}
                        id={task.id}
                        name={task.task}
                        taskStatus={taskStatus}
                        onClick={this.handleClickTask}
                    />
                );
            }
            return (
                <div>
                    <div className="heading">{name}</div>
                    <a href="#" style={{float: 'right'}} onClick={this.handleCloseGroup}>All Groups</a>
                    <br style={{clear: 'left'}} />
                    <ul>
                        {tasks}
                    </ul>
                </div>
            );
        } else {
            const completedTaskCount = this.props.tasks.filter(function(task) { return task.completedAt } ).length;
            const totalTaskCount = this.props.tasks.length;
            return (
                <li className="group" onClick={this.handleExpandGroup}>
                    <div>{name}</div>
                    <div>{completedTaskCount} of {totalTaskCount} tasks complete</div>
                </li>
            );
        }
    }
}

class Task extends React.Component {
    handleClickTask = () => {
        this.props.onClick(this.props.id);
    }

    render() {
        let taskName = this.props.taskStatus === 'locked' ? 'Locked Task' : this.props.name;
        let className = this.props.taskStatus;
        let onClick = this.props.taskStatus === 'locked' ? null : this.handleClickTask;

        return (
            <li className={className} onClick={onClick}>
                {taskName}
            </li>
        );
    }
}

const TASKS = [
  {
    id: 1,
    group: "Purchases",
    task: "Go to the bank",
    dependencyIds: [],
    completedAt: null,
  },
  {
    id: 2,
    group: "Purchases",
    task: "Buy hammer",
    dependencyIds: [1],
    completedAt: null,
  },
  {
    id: 3,
    group: "Purchases",
    task: "Buy wood",
    dependencyIds: [1],
    completedAt: null,
  },
  {
    id: 4,
    group: "Purchases",
    task: "Buy nails",
    dependencyIds: [1],
    completedAt: null,
  },
  {
    id: 5,
    group: "Purchases",
    task: "Buy paint",
    dependencyIds: [1],
    completedAt: null,
  },
  {
    id: 6,
    group: "Build Airplane",
    task: "Hammer nails into wood",
    dependencyIds: [2, 3, 4],
    completedAt: null,
  },
  {
    id: 7,
    group: "Build Airplane",
    task: "Paint wings",
    dependencyIds: [5, 6],
    completedAt: null,
  },
  {
    id: 8,
    group: "Build Airplane",
    task: "Have a snack",
    dependencyIds: [],
    completedAt: null,
  }
];

ReactDOM.render(<TodoList tasks={TASKS}/>, document.getElementById('root'));
