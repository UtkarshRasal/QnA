class QnaCategory(BaseModel):
    """
    Qna category model for category and intro video.
    """
    category_name = models.CharField(max_length=255, null=True, blank=True)
    category_img = models.FileField(upload_to='category_img/', null=True, blank=True,
                                    max_length=255)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return str(self.category_name)
    class Meta:
        db_table = 'qna_category'
class Question(BaseModel):
    """Model for QnA."""
    question = models.CharField(max_length=100, null=True, blank=True)
    category_type = models.ForeignKey(QnaCategory, on_delete=models.CASCADE, related_name="question_set_category")
    mandatory_id = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE,
                                     related_name="identity_question",
                                     null=True, blank=True)
    question_type = models.CharField(max_length=100, null=True, blank=True)
    is_mandatory = models.BooleanField(default=False)
    is_ivr = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.question
    class Meta:
        db_table = 'question'
class Choices(BaseModel):
    """
    Choice model for creating choices for mcq questions.
    """
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="choice_set_question")
    choice_1 = models.CharField(max_length=100, null=True, blank=True)
    choice_2 = models.CharField(max_length=100, null=True, blank=True)
    choice_3 = models.CharField(max_length=100, null=True, blank=True)
    choice_4 = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.question.question)
    class Meta:
        db_table = 'choice'
class Answer(BaseModel):
    """Model for answers."""
    ques_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answer_set_user")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer_set_question")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 null=True, blank=True,
                                 related_name="receiver_set_user")
    ques_answer = models.CharField(max_length=100, null=True, blank=True)
    ans_file = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.ques_answer
    class Meta:
        db_table = 'answer'
class MatchAnswer(BaseModel):
    """
    Model for saving match record for IVR.
    """
    answer = models.OneToOneField(Answer, related_name="match_set_answer", blank=True,
                                  null=True, on_delete=models.CASCADE)
    is_match = models.BooleanField(default=False)
    def __str__(self):
        return self.answer.ques_answer
    class Meta:
        db_table = 'answer_match'
class SelectedQna(BaseModel):
    """
    Model for selected qna.
    """
    ques_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="select_qna_set_user")
    question = models.ManyToManyField(Question, related_name="select_set_question", blank=True)
    answer = models.ManyToManyField(Answer, related_name="select_set_question", blank=True)
    verification_needed = models.BooleanField(default=False)
    case = models.ForeignKey(Case, related_name="select_set_case", null=True, blank=True, on_delete=models.CASCADE)
    ques_receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name="select_receiver_set_user",
                                      null=True,
                                      blank=True)
    is_received = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ques_sender.mobile_num)
    class Meta:
        db_table = 'selected_qna'



1) crud on questions and there answer
2) crud on choices for the question