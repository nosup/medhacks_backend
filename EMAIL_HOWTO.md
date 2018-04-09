# Postfix
[Postfix](http://www.postfix.org/) is an open-source mail transfer agent. It is currently installed on the MedHacks server and can be used in combination with other server-side programs to automate email communications.

Although Postfix can technically be configured as a stand-alone email server, such a configuration is complex. Without full access to the medhacks.org domain, such a configuration is likely impossible. Instead, Postfix is configured as a email client, similar to Mozilla Thunderbird or Microsoft Outlook, but able to be operated from a command-line interface, allowing for email automation. The Postfix client on the MedHacks server relays emails via [STMP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) to a Gmail account. That particular email account is medhacks.noreply@gmail.com

By knowing how to use the Postfix server to automate email delivery, we can avoid having to pay commercial email services. Furthermore, the command-line interface of the Postfix server enables complex automation. To automate our email responses, we need to know how to send an email from the command line.

## Sending an email from the command line

### 1. Using 'echo' to send a short message

```echo "<body>" | mail -s "<subject>" <recipent>```

### 2. Using 'cat' to send a message read from a text file

```cat "<body-file>" | mail -s "<subject>" <recipent>```

### 3. Using a here string to send a message read from a text file

```mail -s "<subject>" <recipent> <<< "<body-file>"```

## Future development

When we obtain full control of the medhacks.org domain, it may be possible to send mail from noreply@medhacks.org .

Dennis Aldea

2018-04-08
