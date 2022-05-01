class Message:
    
    """
    
    Class representing a message
    Parameters
    ----------
    sender : str
        The message sender's username.
     message_body : str
        The body of the message.
    title: str
        title of the message
    message_id : int
        Incremental id of the last message sent.

    Attributes
    ----------
    sender : str
        The message sender's username.
    message_body : str
        The body of the message.
    title: str
        title of the message
    message_id : int
        Incremental id of the last message sent.
    seen : bool
        message already seen or not
    """
    def __init__(self, sender, id, title, body):
        
        """
        Initiation
        """
        self.id = id
        self.title = title
        self.body = body
        self.sender = sender
        self.seen = False

    def __str__(self):
        
        """
        :return: return the presentation of the message
        """
        s = '{' + f'id: {self.id}, title: {self.title}, body: {self.body}, sender: {self.sender},' \
                  f' seen: {self.seen}' + '}'
        return s

    def __repr__(self):
        
        """
        Magic Function to use __str__
        :return: __str__()
        """
        return self.__str__()

    def len(self):
        
        """
        :return: message length
        """
        return len(self.body)


class PostOffice:
    
    """
    A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, title, urgent=False):
        
        """
        Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 messege in the
        inbox.

        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        msg = Message(sender, self.message_id, title, message_body)
        if urgent:
            user_box.insert(0, msg)
        else:
            user_box.append(msg)
        return self.message_id

    def read_inbox(self, receiver, N):
        
        """
        :param receiver:
        :param N: number of message to return
        :return: N (if less then all) unseen messages in the receiver box
        """
        user_box = self.boxes[receiver]
        message_list = []
        for i in range(len(user_box)-1, -1, -1):
            if len(message_list) == N:
                break
            if not user_box[i].seen:
                message_list.append(user_box[i])
                user_box[i].seen = True
        return message_list

    def search_inbox(self, receiver, search_string):
        
        """
        :param receiver:
        :param search_string: string
        :return: all messages that contains the string in their body
        """
        user_box = self.boxes[receiver]
        message_list = []
        for i in range(len(user_box) - 1, -1, -1):
            if search_string in user_box[i].body or search_string in user_box[i].title:
                message_list.append(user_box[i])
                user_box[i].seen = True
        return message_list


