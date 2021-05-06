from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.validators import ValidationError
from base.pagination import SmallResultsSetPagination
from base.response import return_response
import logging, json

class CategoryViewSet(ModelViewSet):
    logging.basicConfig(filename='QnA.log', filemode='a', level=logging.INFO)

    def list(self, request, *args, **kwargs):
        queryset = self.model_class.objects.all()
        serializer = self.get_serializer(queryset, many=True)

        #logging
        logging.info(f"{self.instance_name} listed successfully")


        return return_response(True, f"{self.instance_name} listed successfully", serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        _category = request.data

        category = {}

        # convert uppercase tags to lowercase
        for i in range(len(_category)):
            category = dict((k, v.lower()) for k, v in _category.items())

        serializers = self.serializer_class(data=category)
        if serializers.is_valid():
            serializers.save()

            #logging
            logging.info(f"{self.instance_name} created successfully")


            return return_response(True, f"{self.instance_name} created successfully", serializers.data, status.HTTP_201_CREATED)
        
        return return_response(False, f"{self.instance_name} creation failed", serializers.errors, status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk, *args, **kwargs):
        assert self.model_class is not None

        instance = self.model_class.objects.get(id=pk)
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()

            #logging
            logging.info(f"Partially updated {self.instance_name} '{pk}'")

            return return_response(True, f"{self.instance_name} updated successfully", serializer.data, status.HTTP_201_CREATED)
        
        return return_response(False, f"{self.instance_name} updation failed", serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
    
    def destroy(self, request, pk, *args, **kwargs):
        assert self.model_class is not None
        instance = self.model_class.objects.filter(id=pk)
        instance.delete()

        #logging
        logging.info(f"Deleted {self.instance_name} '{pk}'")
        
        return return_response(True, f"{self.instance_name} deleted successfully", None, status.HTTP_201_CREATED)



class QuestionViewSet(ModelViewSet):
    pagination_class   = SmallResultsSetPagination
    logging.basicConfig(filename='QnA.log', filemode='a', level=logging.INFO)

    def list(self, request, *args, **kwargs):
        instance = self.model_class.objects.filter(ques_sender=request.user.pk)

        page = self.paginate_queryset(instance)
        serializer = self.get_paginated_response(self.get_serializer(page, many=True).data)

         #logging
        logging.info(f"{self.instance_name} listed successfully")

        return return_response(True, f"{self.instance_name} listed successfully", serializer.data, status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        assert self.model_class is not None

        if request.data.get('question_type') != 'Subjective' and request.data.get('question_type') != 'Objective':
            raise ValidationError("The qeustion_type should be Objective or Subjective")
    
        serializer = self.get_serializer(data={**{'ques_sender':request.user.pk,
                                                  }, **request.data})
        if serializer.is_valid():
            serializer.save()

            #logging
            logging.info(f"{self.instance_name} created successfully")

            return return_response(True, f"{self.instance_name} created successfully", serializer.data, status.HTTP_201_CREATED)
        
        return return_response(False, f"{self.instance_name} creation failed", serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk, *args, **kwargs):
        assert self.model_class is not None

        instance = self.model_class.objects.get(id=pk)
        serializer = self.get_serializer(instance=instance, data={**{'ques_sender':request.user.pk,
                                                                        }, **request.data})
        if serializer.is_valid():
            serializer.save()

            #logging
            logging.info(f"Partially updated {self.instance_name} '{pk}'")

            return return_response(True, f"{self.instance_name} updated successfully", serializer.data, status.HTTP_201_CREATED)
        
        return return_response(False, f"{self.instance_name} updation failed", serializer.errors, status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk, *args, **kwargs):
        assert self.serializer_class is not None
        assert self.model_class is not None

        instance = self.model_class.objects.get(id=pk)

        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            #logging
            logging.info(f"Partially updated {self.instance_name} '{pk}'")
        
            return return_response(True, f"{self.instance_name} updated successfully", serializer.data, status.HTTP_201_CREATED)
        
        return return_response(False, f"{self.instance_name} updation failed", serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        assert self.serializer_class is not None
        assert self.model_class is not None

        if not self.model_class.objects.filter(id=pk).exists():
            return return_response(False, f"No such {self.instance_name} found", None, status.HTTP_400_BAD_REQUEST)

        instance = self.model_class.objects.get(id=pk)
        serializer = self.get_serializer(instance=instance)
        
        #logging
        logging.info(f"Retrieved {self.instance_name} '{serializer.data['id']}'")

        return return_response(True, f"{self.instance_name} retrieved successfully", serializer.data, status.HTTP_200_OK)

    def destroy(self, request, pk, *args, **kwargs):
        assert self.model_class is not None
        instance = self.model_class.objects.filter(id=pk)
        instance.delete()

        #logging
        logging.info(f"Deleted {self.instance_name} '{pk}'")
        
        return return_response(True, f"{self.instance_name} deleted successfully", None,status.HTTP_201_CREATED)