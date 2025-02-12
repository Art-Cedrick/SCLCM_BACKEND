from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
# router.register('routine_interview', RoutineInterviewViewset, basename='routine_interview')
router.register('careertracking', CareerTrackingViewset, basename='careertracking')
router.register('conferenceform', ConferenceFormViewset, basename='conferenceform')
#router.register('ms_impactevaluation', MS_ImpactEvaluationViewset, basename='ms_impactevaluation')
# router.register('ms_counselingserviceevaluation', MS_CounselingServiceEvaluationViewset, basename='ms_counselingserviceevaluation')
#router.register('guidance_class_evaluation', Guidance_Class_EvaluationViewset, basename='counseling_service_evaluation')
router.register('kinder', KinderViewset, basename='kinder')
router.register('grade_one', Grade_OneViewset, basename='grade_one')
router.register('grade_two', Grade_TwoViewset, basename='grade_two')
router.register('grade_three', Grade_ThreeViewset, basename='grade_three')
router.register('grade_four', Grade_FourViewset, basename='grade_four')
router.register('grade_five', Grade_FiveViewset, basename='grade_five')
router.register('grade_six', Grade_SixViewset, basename='grade_six')
router.register('grade_seven', Grade_SevenViewset, basename='grade_seven')
router.register('grade_eight', Grade_EightViewset, basename='grade_eight')  
router.register('grade_nine', Grade_NineViewset, basename='grade_nine')
router.register('grade_ten', Grade_TenViewset, basename='grade_ten')
router.register('grade_eleven', Grade_ElevenViewset, basename='grade_eleven')
router.register('grade_twelve', Grade_TwelveViewset, basename='grade_twelve')
router.register('first_year', First_YearViewset, basename='first_year')
router.register('second_year', Second_YearViewset, basename='second_year')
router.register('third_year', Third_YearViewset, basename='third_year')
router.register('fourth_year', Fourth_YearViewset, basename='fourth_year')
router.register('resource', ResourceViewSet, basename='resource')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('api/appointment/', AppointmentView.as_view(), name='appointment'),
    path('api/appointment/<int:pk>/', AppointmentView.as_view(), name='appointment-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('api/familyproblem_analytics/', Family_Problem_Analytics.as_view(), name='familyproblem_analytics'),
    path('api/friendsproblem_analytics/', Friends_Problem_Analytics.as_view(), name='friendsproblem_analytics'),
    path('api/healthproblem_analytics/', Health_Problem_Analytics.as_view(), name='healthproblem_analytics'),
    path('api/academicproblem_analytics/', Academic_Problem_Analytics.as_view(), name='academicproblem_analytics'),
    path('api/careerproblem_analytics/', Career_Problem_Analytics.as_view(), name='careerproblem_analytics'),
    path('api/routineinterview_analytics/', RoutineInterview_Analytics.as_view(), name='routineinterview_analytics'),
    path('api/problem_trends/', ProblemTrendAnalysisView.as_view(), name='problem_trends'),
    path('api/students/', StudentListView.as_view(), name='student-list'),
    path('api/search-student/', search_student, name='search_student'),
    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
    path('api/storage/upload/', StorageView.as_view(), name='storage-file-upload'),
    path('api/storage/files/', ListFilesView.as_view(), name='storage-list-files'),
    path('api/storage/download/<str:filename>/', DownloadFileView.as_view(), name='storage-download-file'),
    path('api/counselor/appointment/', CounselorAppointmentView.as_view(), name='counselor-appointment'),
    path('api/counselor/appointment/<int:pk>/', CounselorAppointmentView.as_view(), name='counselor-appointment-detail'),
    path('api/list-counselor/appointment/', ListCounselorAppointmentsView.as_view(), name='list-appointment-detail'),
    path('api/new-resource/', ResourceNewView.as_view(), name='resource-new'),
    path('api/get-resource/<int:pk>/', GetResourceView.as_view(), name='get-resource'),
    path('api/record/', GetRecordView.as_view(), name='get-record'),
    path("ckeditor5/", include("django_ckeditor_5.urls")),   
    path('api/individual_record_form/', IndividualRecordView.as_view(), name='individual-record'),
    path('api/mscounselingservice/', MsCouncelingView.as_view(), name='ms-counceling'),
    path('api/routine_interview/', RoutineInterviewFormView.as_view(), name='routine'),
    path('api/get_routine_interview/<int:pk>/', SingleRoutineFormView.as_view(), name='get-routine'),
    path('api/guidance_class_evaluation/', GuidanceClassEvalView.as_view(), name='guidance'),
    path('api/get_guidance_class_evaluation/<int:pk>/', SingleGuidanceFormView.as_view(), name='get-guidance'),
    path('api/ms_impactevaluation/', MsImpactFormView.as_view(), name='impact'),
    path('api/get_ms_impactevaluation/<int:pk>/', SingleMsImpactFormView.as_view(), name='get-impact'),
    path('api/command/', RunCommandView.as_view(), name='get-impact'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
