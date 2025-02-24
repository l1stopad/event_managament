from rest_framework.viewsets import ModelViewSet
from .models import Event, EventRegistration
from .serializers import EventSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django_filters import rest_framework as filters


# class EventViewSet(ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     filterset_class = EventFilter


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User created successfully",
            "user_id": user.id
        }, status=status.HTTP_201_CREATED)


class RegisterToEventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"detail": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        already_registered = EventRegistration.objects.filter(user=request.user, event=event).exists()
        if already_registered:
            return Response({"detail": "Already registered"}, status=status.HTTP_400_BAD_REQUEST)

        EventRegistration.objects.create(user=request.user, event=event)

        subject = f"Registration for {event.title}"
        message = (
            f"Hi {request.user.username},\n\n"
            f"You have successfully registered for the event '{event.title}'.\n"
            "Thank you for your interest!"
        )

        from_email = None
        recipient_list = [request.user.email]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )

        return Response(
            {"detail": f"User {request.user.username} registered for event {event.title}"},
            status=status.HTTP_201_CREATED
        )


class MyRegistrationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        registrations = EventRegistration.objects.filter(user=request.user)
        data = []
        for reg in registrations:
            data.append({
                "event_id": reg.event.id,
                "title": reg.event.title,
                "registered_at": reg.registered_at,
            })
        return Response(data, status=status.HTTP_200_OK)


class EventFilter(filters.FilterSet):

    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Пошук за назвою (частковий збіг)'
    )
    date_after = filters.DateFilter(
        field_name='date',
        lookup_expr='gte',
    )
    date_before = filters.DateFilter(
        field_name='date',
        lookup_expr='lte',

    )
    organizer_username = filters.CharFilter(
        field_name='organizer__username',
        lookup_expr='icontains',

    )

    class Meta:
        model = Event
        fields = [
            'title',
            'date_after',
            'date_before',
            'organizer_username'
        ]


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter
