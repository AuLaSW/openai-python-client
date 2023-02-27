# openai-python-client

A python GUI application that communicates with OpenAI through their openai-python API. Works with OpenAI Text Completion endpoint.

## Purpose

I began developing this program in January of 2023 as a tool for people in my circle to interact with different ChatGPT models. The goal was to use the OpenAI API to develop an application that could run on the desktop and communicate with the ChatGPT servers. 

Accessing the servers needed to be general use so they could fit the tool to their needs. It also needed to be easy to use, so no needing to download and build from source. It needed to be as general-purpose and accessible as possible.

Though those aspects are not yet developed/ready, in the future the application will have a GUI and have a binary release for Windows (with releases for other OS's coming as fast as I can get them).

This project is still a work in progress, though I am working on it frequently right now.

## Installing

To install, head over to the [releases](https://github.com/AuLaSW/openai-python-client/releases) tab to find the latest release and install from there, either that or clone this repository into a folder. You'll need to set up the correct paths to be able to run the application.

Currently there is no binary build and the project runs in a venv. Currently the application runs through `app.py`, though that will be updated to a better file name soon. When the application runs, it will ask you to either input your API key or use the test API. This has to be done at each instantiation until the code is fixed.

### Requirements

[Requirements for running the application can be found here.](requirements.txt)

## TODO

- [ ] Create documentation for the code.
- [ ] Extend to more endpoints.
  - [ ] Edit endpoint.
  - [ ] Codex endpoint.
  - [ ] Embedding endpoint.
- [ ] API key retrieval and saving.
- [ ] Better interaction UI for the models.
- [ ] Help center for how to best work with the models.

## Current Work

Currently, the project is moving the model package over to a set of abstract factories working together to build the requests and responses. This will allow for easier extension to accomodate different endpoints.

## Contributing

If you would like to contribute, please fork the repository and make a [pull request](https://github.com/AuLaSW/openai-python-client/compare)! Contributions are welcome; however, I can be slow to looking at them and getting back with you, so I may not immediately look at/comment on/merge them.

## Contributors

AuLaSW

## License

