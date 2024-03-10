from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.db.models import Count
from django.utils import timezone

from datetime import datetime, timedelta

from ..models import Admin, Artwork, ArtworkVisits, Visitor, Section

class GetDashboardSerializer(serializers.Serializer):
  admin_id = serializers.IntegerField(required=True)

  def validate(self, data):
    admin_id = data.get('admin_id')

    try:
      admin = Admin.objects.get(user__id=admin_id)
      twenty_four_hours_ago = timezone.now() - timedelta(hours=24)

      # Get All artworks in this particular museum
      all_artworks = Artwork.objects.all().filter(
        section_id__museum_id=admin.museum_id, 
        is_deleted=False
      )

      # Get the top three popular artworks from the all_artworks in the past 24 hours
      top_artworks = ArtworkVisits.objects.filter(
        art_id__in=all_artworks,
        art_visited_on__gte=twenty_four_hours_ago,
      ).values('art_id').annotate(visit_count=Count('art_id')).order_by('-visit_count')[:3]
      
      # Get the information of the popular artworks
      popular_artworks = []
      for art in top_artworks:
        artwork = Artwork.objects.get(art_id=art['art_id'])
        popular_artworks.append(artwork)

      # Count the number of visitors in the last 24 hours for a specific museum
      number_of_visitors = Visitor.objects.filter(
          visited_on__gte=twenty_four_hours_ago,
          museum_id=admin.museum_id
      ).count()

      # Get the most popular sections
      top_sections = ArtworkVisits.objects.filter(
        art_visited_on__gte=twenty_four_hours_ago,
        art_id__in=all_artworks
      ).values('art_id__section_id').annotate(
        visit_count=Count('art_id')
      ).order_by('-visit_count')[:3]
      
      # Get information per section
      popular_sections = []
      for art in top_sections:
        section = Section.objects.get(section_id=art['art_id__section_id'])
        popular_sections.append(section)

      # Append to serializer data
      data["artworks_count"] = len(all_artworks)
      data["popular_artworks"] = popular_artworks
      data["visitors_count"] = number_of_visitors
      data["popular_sections"] = popular_sections

    except ObjectDoesNotExist:
      raise ObjectDoesNotExist("Admin does not exist.")
      
    # data['museum'] = museum
    return data