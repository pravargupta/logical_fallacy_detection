# logical_fallacy_detection
Building a project to detect fault logics in an argument/speech that sound like they make sense but are based off a wrong base overall and are very hard to find out in the heat of the moment.

For now we have speech to text recognition where we play audio from microphone and it outputs to output.txt(using google speech recognition) and then we run it through gemini api because gemini is free for educational use.

The text is then passed through gemini api with the prompt to detect fallacies within that text, this will be updated and made with a way better version in future too.
