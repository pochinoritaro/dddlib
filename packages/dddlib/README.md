# dddlib

`dddlib` is a Python library that provides foundational components for implementing Domain-Driven Design.

This library does not provide application-specific business logic itself. Instead, it aims to provide common concepts that repeatedly appear in DDD design in a type-safe and easy-to-use form.

## Positioning

`dddlib` standardizes the following elements commonly required in the domain layer.

- Value objects
- Entities
- Aggregate roots
- Domain events
- Identifiers
- Domain errors
- Messages

When these are implemented separately for each application, similar constraints, validations, equality comparisons, and reconstruction logic can easily become scattered.
`dddlib` serves as a foundation for reducing that repetition and making it easier to focus on designing the domain model itself.

## Design Policy

`dddlib` is designed based on the following policies.

- Make it easy to handle value storage and immutability based on `dataclass`
- Provide an implementation that works well with type checking by `mypy`
- Keep the code explicit and readable in line with strict `ruff` rules
- Avoid concrete business processing and limit the scope to common domain foundations
- Separate it from `dddlib_cli` to distinguish library usage from CLI usage

For this reason, `dddlib` is intended to be used not as a framework, but as a thin foundational layer for domain models.

## Provided Features

### Value Objects

A value object is an object whose identity is determined by its value rather than by an ID.

In `dddlib`, the following operations, which are often needed when creating value objects, are consolidated.

- Validation at creation time
- Conversion to dictionaries
- Conversion to display strings
- Storage as immutable values

By using `FrozenBase`, behavior equivalent to `dataclass(frozen=True)` can be handled naturally.

### Entities

An entity is an object that has identity through an identifier.

The entity foundation in `dddlib` supports the following operations.

- Creating objects with identifiers
- Internal creation for reconstruction
- Comparison based on identity
- Retrieving identifiers

Unlike value objects, entities have a lifecycle. Therefore, it is important to clearly separate identity determination.

### Aggregate Roots

An aggregate root is the entry point for protecting domain consistency.

The aggregate root in `dddlib` inherits the characteristics of an entity while allowing domain events to be accumulated and retrieved.

- Adding events
- Getting and extracting events
- Adding multiple events together

This makes it easier to safely handle events that occur as a result of domain operations.

### Domain Events

A domain event represents an important event that occurred within the domain.

In `dddlib`, emphasis is placed on handling events not as simple dictionaries or strings, but as typed objects.
By representing event contents as explicit classes, it becomes easier to connect them to event-driven processing, auditing, and notification processing.

### Identifiers

An identifier is a value used to uniquely handle an entity or aggregate.

`dddlib` provides bases mainly for UUID-based identifiers, consolidating value validation and conversion.

This makes it easier to handle IDs as meaningful types instead of scattering raw `str` or `int` values throughout the code.

### Errors and Messages

`dddlib` also standardizes errors and messages handled in the domain layer.

- `DDDError` is the foundation for domain errors that have a code and message
- `Message` handles message body generation and formatting
- `DDDMessage` represents predefined messages with codes

Using this mechanism makes it easier to handle errors consistently across the entire application, rather than confining them to simple exception messages.

## Typical Usage Image

`dddlib` is intended to be used, for example, in the following kind of structure.

- Define domain IDs by deriving them from `UUIDIdentifier`
- Give validation logic to value objects
- Determine entity identity based on IDs
- Publish domain events from aggregate roots
- Explicitly represent business failures with domain errors

This design makes it easier to build models using domain language without pushing too much responsibility into the application layer or infrastructure layer.

## Relationship with the CLI

The main body of `dddlib` is a library.

If you want to support project work using a CLI, refer to the separate package [dddlib_cli](../dddlib_cli/README.md).

## Adoption Approach

When adopting `dddlib`, it is useful to think through the following order.

1. First, decide how to represent domain identifiers
1. Next, extract concepts that should be closed as value objects
1. Then, define entities and aggregate roots
1. Finally, align the representation of events and errors

`dddlib` should be used as a tool for aligning implementation, rather than as something that disrupts this flow.

## Notes

- `dddlib` is not a completed business application, but a common foundation
- The domain cannot be established simply by using it as-is, so each project needs to define concrete models
- CLI details are separated into the [dddlib_cli README](../dddlib_cli/README.md)

## License

For this project, refer to [LICENSE.md](../../LICENSE.md) directly under the repository root.
