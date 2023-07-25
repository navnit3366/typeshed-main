"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import tensorflow.core.framework.summary_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _WorkerHealth:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkerHealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WorkerHealth.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _WorkerHealth.ValueType  # 0
    """By default a worker is healthy."""
    RECEIVED_SHUTDOWN_SIGNAL: _WorkerHealth.ValueType  # 1
    INTERNAL_ERROR: _WorkerHealth.ValueType  # 2
    SHUTTING_DOWN: _WorkerHealth.ValueType  # 3
    """Worker has been instructed to shutdown after a timeout."""

class WorkerHealth(_WorkerHealth, metaclass=_WorkerHealthEnumTypeWrapper):
    """Worker heartbeat messages.  Support for these operations is currently
    internal and expected to change.

    Current health status of a worker.
    """

OK: WorkerHealth.ValueType  # 0
"""By default a worker is healthy."""
RECEIVED_SHUTDOWN_SIGNAL: WorkerHealth.ValueType  # 1
INTERNAL_ERROR: WorkerHealth.ValueType  # 2
SHUTTING_DOWN: WorkerHealth.ValueType  # 3
"""Worker has been instructed to shutdown after a timeout."""
global___WorkerHealth = WorkerHealth

class _WorkerShutdownMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkerShutdownModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WorkerShutdownMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DEFAULT: _WorkerShutdownMode.ValueType  # 0
    NOT_CONFIGURED: _WorkerShutdownMode.ValueType  # 1
    WAIT_FOR_COORDINATOR: _WorkerShutdownMode.ValueType  # 2
    SHUTDOWN_AFTER_TIMEOUT: _WorkerShutdownMode.ValueType  # 3

class WorkerShutdownMode(_WorkerShutdownMode, metaclass=_WorkerShutdownModeEnumTypeWrapper):
    """Indicates the behavior of the worker when an internal error or shutdown
    signal is received.
    """

DEFAULT: WorkerShutdownMode.ValueType  # 0
NOT_CONFIGURED: WorkerShutdownMode.ValueType  # 1
WAIT_FOR_COORDINATOR: WorkerShutdownMode.ValueType  # 2
SHUTDOWN_AFTER_TIMEOUT: WorkerShutdownMode.ValueType  # 3
global___WorkerShutdownMode = WorkerShutdownMode

@typing_extensions.final
class Event(google.protobuf.message.Message):
    """Protocol buffer representing an event that happened during
    the execution of a Brain model.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WALL_TIME_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    FILE_VERSION_FIELD_NUMBER: builtins.int
    GRAPH_DEF_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    LOG_MESSAGE_FIELD_NUMBER: builtins.int
    SESSION_LOG_FIELD_NUMBER: builtins.int
    TAGGED_RUN_METADATA_FIELD_NUMBER: builtins.int
    META_GRAPH_DEF_FIELD_NUMBER: builtins.int
    wall_time: builtins.float
    """Timestamp of the event."""
    step: builtins.int
    """Global step of the event."""
    file_version: builtins.str
    """An event file was started, with the specified version.
    This is use to identify the contents of the record IO files
    easily.  Current version is "brain.Event:2".  All versions
    start with "brain.Event:".
    """
    graph_def: builtins.bytes
    """An encoded version of a GraphDef."""
    @property
    def summary(self) -> tensorflow.core.framework.summary_pb2.Summary:
        """A summary was generated."""
    @property
    def log_message(self) -> global___LogMessage:
        """The user output a log message. This was theoretically used by the defunct
        tensorboard_logging module, which has since been removed; this field is
        now deprecated and should not be used.
        """
    @property
    def session_log(self) -> global___SessionLog:
        """The state of the session which can be used for restarting after crashes."""
    @property
    def tagged_run_metadata(self) -> global___TaggedRunMetadata:
        """The metadata returned by running a session.run() call."""
    meta_graph_def: builtins.bytes
    """An encoded version of a MetaGraphDef."""
    def __init__(
        self,
        *,
        wall_time: builtins.float | None = ...,
        step: builtins.int | None = ...,
        file_version: builtins.str | None = ...,
        graph_def: builtins.bytes | None = ...,
        summary: tensorflow.core.framework.summary_pb2.Summary | None = ...,
        log_message: global___LogMessage | None = ...,
        session_log: global___SessionLog | None = ...,
        tagged_run_metadata: global___TaggedRunMetadata | None = ...,
        meta_graph_def: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file_version", b"file_version", "graph_def", b"graph_def", "log_message", b"log_message", "meta_graph_def", b"meta_graph_def", "session_log", b"session_log", "summary", b"summary", "tagged_run_metadata", b"tagged_run_metadata", "what", b"what"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_version", b"file_version", "graph_def", b"graph_def", "log_message", b"log_message", "meta_graph_def", b"meta_graph_def", "session_log", b"session_log", "step", b"step", "summary", b"summary", "tagged_run_metadata", b"tagged_run_metadata", "wall_time", b"wall_time", "what", b"what"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["what", b"what"]) -> typing_extensions.Literal["file_version", "graph_def", "summary", "log_message", "session_log", "tagged_run_metadata", "meta_graph_def"] | None: ...

global___Event = Event

@typing_extensions.final
class LogMessage(google.protobuf.message.Message):
    """Protocol buffer used for logging messages to the events file.

    This was theoretically used by the defunct tensorboard_logging module, which
    has been removed; this message is now deprecated and should not be used.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Level:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _LevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LogMessage._Level.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: LogMessage._Level.ValueType  # 0
        DEBUGGING: LogMessage._Level.ValueType  # 10
        """Note: The logging level 10 cannot be named DEBUG. Some software
        projects compile their C/C++ code with -DDEBUG in debug builds. So the
        C++ code generated from this file should not have an identifier named
        DEBUG.
        """
        INFO: LogMessage._Level.ValueType  # 20
        WARN: LogMessage._Level.ValueType  # 30
        ERROR: LogMessage._Level.ValueType  # 40
        FATAL: LogMessage._Level.ValueType  # 50

    class Level(_Level, metaclass=_LevelEnumTypeWrapper): ...
    UNKNOWN: LogMessage.Level.ValueType  # 0
    DEBUGGING: LogMessage.Level.ValueType  # 10
    """Note: The logging level 10 cannot be named DEBUG. Some software
    projects compile their C/C++ code with -DDEBUG in debug builds. So the
    C++ code generated from this file should not have an identifier named
    DEBUG.
    """
    INFO: LogMessage.Level.ValueType  # 20
    WARN: LogMessage.Level.ValueType  # 30
    ERROR: LogMessage.Level.ValueType  # 40
    FATAL: LogMessage.Level.ValueType  # 50

    LEVEL_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    level: global___LogMessage.Level.ValueType
    message: builtins.str
    def __init__(
        self,
        *,
        level: global___LogMessage.Level.ValueType | None = ...,
        message: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["level", b"level", "message", b"message"]) -> None: ...

global___LogMessage = LogMessage

@typing_extensions.final
class SessionLog(google.protobuf.message.Message):
    """Protocol buffer used for logging session state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _SessionStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SessionStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SessionLog._SessionStatus.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: SessionLog._SessionStatus.ValueType  # 0
        START: SessionLog._SessionStatus.ValueType  # 1
        STOP: SessionLog._SessionStatus.ValueType  # 2
        CHECKPOINT: SessionLog._SessionStatus.ValueType  # 3

    class SessionStatus(_SessionStatus, metaclass=_SessionStatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: SessionLog.SessionStatus.ValueType  # 0
    START: SessionLog.SessionStatus.ValueType  # 1
    STOP: SessionLog.SessionStatus.ValueType  # 2
    CHECKPOINT: SessionLog.SessionStatus.ValueType  # 3

    STATUS_FIELD_NUMBER: builtins.int
    CHECKPOINT_PATH_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    status: global___SessionLog.SessionStatus.ValueType
    checkpoint_path: builtins.str
    """This checkpoint_path contains both the path and filename."""
    msg: builtins.str
    def __init__(
        self,
        *,
        status: global___SessionLog.SessionStatus.ValueType | None = ...,
        checkpoint_path: builtins.str | None = ...,
        msg: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["checkpoint_path", b"checkpoint_path", "msg", b"msg", "status", b"status"]) -> None: ...

global___SessionLog = SessionLog

@typing_extensions.final
class TaggedRunMetadata(google.protobuf.message.Message):
    """For logging the metadata output for a single session.run() call."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAG_FIELD_NUMBER: builtins.int
    RUN_METADATA_FIELD_NUMBER: builtins.int
    tag: builtins.str
    """Tag name associated with this metadata."""
    run_metadata: builtins.bytes
    """Byte-encoded version of the `RunMetadata` proto in order to allow lazy
    deserialization.
    """
    def __init__(
        self,
        *,
        tag: builtins.str | None = ...,
        run_metadata: builtins.bytes | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_metadata", b"run_metadata", "tag", b"tag"]) -> None: ...

global___TaggedRunMetadata = TaggedRunMetadata

@typing_extensions.final
class WatchdogConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMEOUT_MS_FIELD_NUMBER: builtins.int
    timeout_ms: builtins.int
    def __init__(
        self,
        *,
        timeout_ms: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["timeout_ms", b"timeout_ms"]) -> None: ...

global___WatchdogConfig = WatchdogConfig

@typing_extensions.final
class RequestedExitCode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXIT_CODE_FIELD_NUMBER: builtins.int
    exit_code: builtins.int
    def __init__(
        self,
        *,
        exit_code: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exit_code", b"exit_code"]) -> None: ...

global___RequestedExitCode = RequestedExitCode

@typing_extensions.final
class WorkerHeartbeatRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHUTDOWN_MODE_FIELD_NUMBER: builtins.int
    WATCHDOG_CONFIG_FIELD_NUMBER: builtins.int
    EXIT_CODE_FIELD_NUMBER: builtins.int
    shutdown_mode: global___WorkerShutdownMode.ValueType
    @property
    def watchdog_config(self) -> global___WatchdogConfig: ...
    @property
    def exit_code(self) -> global___RequestedExitCode: ...
    def __init__(
        self,
        *,
        shutdown_mode: global___WorkerShutdownMode.ValueType | None = ...,
        watchdog_config: global___WatchdogConfig | None = ...,
        exit_code: global___RequestedExitCode | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exit_code", b"exit_code", "watchdog_config", b"watchdog_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exit_code", b"exit_code", "shutdown_mode", b"shutdown_mode", "watchdog_config", b"watchdog_config"]) -> None: ...

global___WorkerHeartbeatRequest = WorkerHeartbeatRequest

@typing_extensions.final
class WorkerHeartbeatResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_STATUS_FIELD_NUMBER: builtins.int
    WORKER_LOG_FIELD_NUMBER: builtins.int
    HOSTNAME_FIELD_NUMBER: builtins.int
    health_status: global___WorkerHealth.ValueType
    @property
    def worker_log(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Event]: ...
    hostname: builtins.str
    def __init__(
        self,
        *,
        health_status: global___WorkerHealth.ValueType | None = ...,
        worker_log: collections.abc.Iterable[global___Event] | None = ...,
        hostname: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["health_status", b"health_status", "hostname", b"hostname", "worker_log", b"worker_log"]) -> None: ...

global___WorkerHeartbeatResponse = WorkerHeartbeatResponse
