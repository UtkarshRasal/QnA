from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from base.pagination import SmallResultsSetPagination
import logging, json

class BaseViewSet(ModelViewSet):
    pagination_class   = SmallResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]
    logging.basicConfig(filename='QnA.log', filemode='a', level=logging.INFO)


    def create(self, request, *args, **kwargs):
        assert self.model_class is not None

        import pdb;pdb.set_trace()
        category = request.data['category_type']

        if type(category) is str:
            _category = json.loads(category) # convert string to dictionary

        else:
            _category = category
        
        category = []

        # convert uppercase tags to lowercase
        for i in range(len(_category)):
            category.append({k: v.lower() for k, v in _category[i].items()})

        serializer = self.get_serializer(data={**{'ques_sender':request.user.pk,
                                                  'question':request.data['question'],
                                                  'category_type':category,
                                                  'question_type':request.data['question_type']
                                                  }})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #logging
        logging.info(f"{self.instance_name} created successfully")

        return Response(data={
            'status':True,
            'message':f"{self.instance_name} created successfully",
            'data':serializer.data
        })

        # return Response(data={
        #     'status':False,
        #     'message':f"{self.instance_name} creation failed",
        #     'data':serializer.errors
        # })