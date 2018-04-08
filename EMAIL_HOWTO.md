# Postfix Email Server
The Postfix Email Server is an open-source mail server. By knowing how to use the Postfix server to automate email delivery, we can avoid having to pay commercial email services. Furthermore, the command-line interface of the Postfix server enables complex automation.

Postfix is not an email service provider, but rather an email director. Postfix as currently implemented in this project, is a command-line tool to create email messages and direct their delivery through the Gmail service provider. To automate our email responses, we need to know how to send an email from the command line.

## Sending an email from the command line

### 1. Using 'echo' to send a short message

```echo "<body>" | mail -s "<subject>" <recipent>```

### 2. Using 'cat' to send a message read from a text file

```cat "<body-file>" | mail -s "<subject>" <recipent>```

### 3. Using a here string to send a message read from a text file

```mail -s "<subject>" <recipent> <<< "<body-file>"```

Dennis Aldea
2018-04-08
