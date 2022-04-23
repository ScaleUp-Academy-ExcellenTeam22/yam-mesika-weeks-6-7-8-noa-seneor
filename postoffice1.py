class PostOffice:
    """A Post Office class. Allows users to message each other.

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

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.

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

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'seen': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
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
            if not user_box[i]['seen']:
                message_list.append(user_box[i])
                user_box[i]['seen'] = True
        return message_list

    def search_inbox(self, receiver, search_string):
        """
        :param receiver:
        :param search_string: string
        :return: all messages that contains the string in their body
        """
        user_box = self.boxes[receiver]
        message_list = []
        for i in range(len(user_box)-1, -1, -1):
            if search_string in user_box[i]['body'] or search_string in user_box[i]['title']:
                message_list.append(user_box[i])
                user_box[i]['seen'] = True
        return message_list


