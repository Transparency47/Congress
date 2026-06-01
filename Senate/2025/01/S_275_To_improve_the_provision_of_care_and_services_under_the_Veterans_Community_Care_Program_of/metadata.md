# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/275?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/275
- Title: Veterans’ Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 275
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-05-13T11:03:31Z
- Update date including text: 2026-05-13T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/275",
    "number": "275",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:31Z",
    "updateDateIncludingText": "2026-05-13T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2025-07-30T20:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-30T20:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-11T14:30:04Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-28T19:38:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IN"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "AL"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SD"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "MT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "FL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "NE"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "WV"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IA"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "UT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "AK"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s275is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 275\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Moran introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo improve the provision of care and services under the Veterans Community Care Program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Improvement of Veterans Community Care Program\nSec. 101. Codification of requirements for eligibility standards for access to community care from Department of Veterans Affairs.\nSec. 102. Requirement that Secretary notify veterans of eligibility for care under Veterans Community Care Program.\nSec. 103. Consideration under Veterans Community Care Program of veteran preference for care, continuity of care, and need for caregiver or attendant.\nSec. 104. Notification of denial of request for care under Veterans Community Care Program.\nSec. 105. Discussion of telehealth options under Veterans Community Care Program.\nSec. 106. Extension of deadline for submittal of claims by health care entities and providers under prompt payment standard.\nTITLE II\u2014Mental health treatment programs\nSec. 201. Definitions.\nSec. 202. Standardized process to determine eligibility of covered veterans for participation in certain mental health treatment programs.\nSec. 203. Improvements to Department of Veterans Affairs Mental Health Residential Rehabilitation Treatment Program.\nTITLE III\u2014Other health care matters\nSec. 301. Plan on establishment of interactive, online self-service module for care.\nSec. 302. Modification of requirements for Center for Innovation for Care and Payment of the Department of Veterans Affairs and requirement for pilot program.\nSec. 303. Reports.\nI\nImprovement of Veterans Community Care Program\n#### 101. Codification of requirements for eligibility standards for access to community care from Department of Veterans Affairs\n##### (a) Eligibility access standards\nSection 1703B of title 38, United States Code, is amended\u2014\n**(1)**\nby striking subsections (a) through (e) and inserting the following:\n(a) Eligibility standards for access to community care (1) A covered veteran shall be eligible to elect to receive non-Department hospital care, medical services, or extended care services, excluding nursing home care, through the Veterans Community Care Program under section 1703 of this title pursuant to subsection (d)(1)(D) of such section using the following eligibility access standards: (A) With respect to primary care, mental health care, or extended care services, excluding nursing home care, if the Department cannot schedule an appointment for the covered veteran with a health care provider of the Department who can provide the needed service\u2014 (i) within 30 minutes average driving time (or such shorter average driving time as the Secretary may prescribe) from the residence of the veteran unless a longer average driving time has been agreed to by the veteran in consultation with a health care provider of the veteran; and (ii) within 20 days (or such shorter period as the Secretary may prescribe) of the date of request for such an appointment unless a later date has been agreed to by the veteran in consultation with a health care provider of the veteran. (B) With respect to specialty care, if the Department cannot schedule an appointment for the covered veteran with a health care provider of the Department who can provide the needed service\u2014 (i) within 60 minutes average driving time (or such shorter average driving time as the Secretary may prescribe) from the residence of the veteran unless a longer average driving time has been agreed to by the veteran in consultation with a health care provider of the veteran; and (ii) within 28 days (or such shorter period as the Secretary may prescribe) of the date of request for such an appointment unless a later date has been agreed to by the veteran in consultation with a health care provider of the veteran. (2) For the purposes of determining the eligibility of a covered veteran for care or services under paragraph (1), the Secretary shall not take into consideration the availability of telehealth appointments from the Department when determining whether the Department is able to furnish such care or services in a manner that complies with the eligibility access standards under such paragraph. (3) In the case of a covered veteran who has had an appointment with a health care provider of the Department canceled by the Department for a reason other than the request of the veteran, in calculating a wait time for a subsequent appointment under paragraph (1), the Secretary shall calculate such wait time from the date of the request for the original, canceled appointment. (4) If a veteran agrees to a longer average drive time or a later date under subparagraph (A) or (B) of paragraph (1), the Secretary shall document the agreement to such longer average drive time or later date in the electronic health record of the veteran and provide the veteran a copy of such documentation. Such copy may be provided electronically. (b) Application The Secretary shall ensure that the eligibility access standards established under subsection (a) apply\u2014 (1) to all care and services within the medical benefits package of the Department to which a covered veteran is eligible under section 1703 of this title, excluding nursing home care; and (2) to all covered veterans, regardless of whether a veteran is a new or established patient. (c) Periodic review of access standards Not later than three years after the date of the enactment of the Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025 , and not less frequently than once every three years thereafter, the Secretary shall\u2014 (1) conduct a review of the eligibility access standards under subsection (a) in consultation with\u2014 (A) such Federal entities as the Secretary considers appropriate, including the Department of Defense, the Department of Health and Human Services, and the Centers for Medicare & Medicaid Services; (B) entities and individuals in the private sector, including\u2014 (i) veteran patients; (ii) veterans service organizations; and (iii) health care providers participating in the Veterans Community Care Program under section 1703 of this title; and (C) other entities that are not part of the Federal Government; and (2) submit to the appropriate committees of Congress a report on\u2014 (A) the findings of the Secretary with respect to the review conducted under paragraph (1); and (B) such recommendations as the Secretary may have with respect to the eligibility access standards under subsection (a). ;\n**(2)**\nby striking subsection (g);\n**(3)**\nby redesignating subsections (f), (h), and (i) as subsections (d), (e), and (f), respectively;\n**(4)**\nin subsection (d), as redesignated by paragraph (3)\u2014\n**(A)**\nby striking established each place it appears; and\n**(B)**\nin paragraph (1), by striking (1) Subject to and inserting Compliance by community care providers with access standards .\u2014(1) Subject to ;\n**(5)**\nin subsection (e), as so redesignated\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking (1) Consistent with and inserting Determination regarding eligibility .\u2014(1) Consistent with ; and\n**(ii)**\nby striking designated access standards established under this section and inserting eligibility access standards under subsection (a) ; and\n**(B)**\nin paragraph (2)(B), by striking designated access standards established under this section and inserting eligibility access standards under subsection (a) ; and\n**(6)**\nin subsection (f), as redesignated by paragraph (2)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking In this section and inserting Definitions .\u2014In this section ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking covered veterans and inserting covered veteran ; and\n**(ii)**\nby striking veterans described and inserting a veteran described .\n##### (b) Conforming amendments\nSection 1703(d) of such title is amended\u2014\n**(1)**\nin paragraph (1)(D), by striking designated access standards developed by the Secretary under section 1703B of this title and inserting eligibility access standards under section 1703B(a) of this title ; and\n**(2)**\nin paragraph (3), by striking designated access standards developed by the Secretary under section 1703B of this title and inserting eligibility access standards under section 1703B(a) of this title .\n#### 102. Requirement that Secretary notify veterans of eligibility for care under Veterans Community Care Program\nSection 1703(a) of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(5) (A) The Secretary shall notify each covered veteran in writing of the eligibility of such veteran for care or services under this section as soon as possible, but not later than two business days, after the date on which the Secretary is aware that the veteran is seeking care or services and is eligible for such care or services under this section. (B) With respect to each covered veteran eligible for care or services under subsection (d), the Secretary shall provide such veteran periodic reminders, as the Secretary determines appropriate, of their ongoing eligibility under such subsection. (C) Any notification or reminder under this paragraph may be provided electronically. .\n#### 103. Consideration under Veterans Community Care Program of veteran preference for care, continuity of care, and need for caregiver or attendant\nSection 1703(d)(2) of title 38, United States Code, is amended by adding at the end the following new subparagraphs:\n(F) The preference of the covered veteran for where, when, and how to seek hospital care, medical services, or extended care services. (G) Continuity of care. (H) Whether the covered veteran requests or requires the assistance of a caregiver or attendant when seeking hospital care, medical services, or extended care services. .\n#### 104. Notification of denial of request for care under Veterans Community Care Program\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (o) as subsection (p); and\n**(2)**\nby inserting after subsection (n) the following new subsection (o):\n(o) Notification of denial of request for care and how To appeal (1) If a request by a veteran for care or services under this section is denied, the Secretary shall notify the veteran in writing as soon as possible, but not later than two business days, after the denial is made\u2014 (A) of the reason for the denial; and (B) with instructions on how to appeal such denial using the clinical appeals process of the Veterans Health Administration. (2) If a denial under paragraph (1) is due to not meeting the eligibility access standards under section 1703B(a) of this title, notice under such paragraph shall include an explanation for why the Secretary does not consider the veteran to have met such standards. (3) Any notification under this subsection may be provided electronically. .\n#### 105. Discussion of telehealth options under Veterans Community Care Program\nSection 1703 of title 38, United States Code, as amended by section 104, is further amended\u2014\n**(1)**\nby redesignating subsection (p) as subsection (q); and\n**(2)**\nby inserting after subsection (o) the following new subsection (p):\n(p) Discussion of options for telehealth When discussing options for care or services for a covered veteran under this section, the Secretary shall ensure that the veteran is informed of the ability of the veteran to seek care or services via telehealth, either through a medical facility of the Department or under this section, if telehealth\u2014 (1) is available to the veteran; (2) is appropriate for the type of care or services the veteran is seeking, as determined by the Secretary; and (3) is acceptable to the veteran. .\n#### 106. Extension of deadline for submittal of claims by health care entities and providers under prompt payment standard\nSection 1703D(b) of title 38, United States Code, is amended by striking 180 days and inserting one year .\nII\nMental health treatment programs\n#### 201. Definitions\nIn this title:\n**(1) Covered treatment program**\nThe term covered treatment program \u2014\n**(A)**\nmeans\u2014\n**(i)**\na mental health residential rehabilitation treatment program of the Department of Veterans Affairs; or\n**(ii)**\na program of the Department for residential care for mental health and substance abuse disorders;\n**(B)**\nincludes\u2014\n**(i)**\nthe programs designated as of the date of the enactment of this Act as domiciliary residential rehabilitation treatment programs; and\n**(ii)**\nany programs designated as domiciliary residential rehabilitation treatment programs on or after such date of enactment; and\n**(C)**\ndoes not include Compensated Work Therapy Transition Residence programs of the Department.\n**(2) Covered veteran**\nThe term covered veteran means a veteran described in section 1703(b) of title 38, United States Code.\n**(3) Social support systems**\nThe term social support systems , with respect to a covered veteran\u2014\n**(A)**\nmeans\u2014\n**(i)**\na member of the family of the covered veteran, including a parent, spouse, child, step-family member, or extended family member; or\n**(ii)**\nan individual who lives with the veteran but is not a member of the family of the veteran; and\n**(B)**\ndoes not include a facility-organized peer support program.\n**(4) Treatment track**\nThe term treatment track means a specialized treatment program that is provided to a subset of covered veterans in a covered treatment program who receive the same or similar intensive treatment and rehabilitative services.\n#### 202. Standardized process to determine eligibility of covered veterans for participation in certain mental health treatment programs\n##### (a) Standardized screening process\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a standardized screening process to determine, based on clinical need, whether a covered veteran satisfies criteria for priority or routine admission to a covered treatment program.\n##### (b) Eligibility criteria for priority admission\n**(1) In general**\nUnder the standardized screening process required by subsection (a), a covered veteran shall be eligible for priority admission to a covered treatment program if the covered veteran meets criteria established by the Secretary that include any of the following:\n**(A)**\nSymptoms that\u2014\n**(i)**\nsignificantly affect activities of daily life; and\n**(ii)**\nincrease the risk of such veteran for adverse outcomes.\n**(B)**\nAn unsafe living situation.\n**(C)**\nA high-risk flag for suicide.\n**(D)**\nA determination of being a high risk for suicide.\n**(E)**\nRisk factors for overdose.\n**(F)**\nNon-responsive, relapsed, or unable to find recovery from one other course of treatment, such as outpatient or intensive outpatient treatment.\n**(G)**\nSuch other criteria as the Secretary determines appropriate.\n**(2) Consideration**\nIn making a determination that a covered veteran meets criteria established by the Secretary under paragraph (1) for priority admission to a covered treatment program, the Secretary shall consider any referral of a health care provider of a covered veteran.\n##### (c) Time for screening and admission\nUnder the standardized screening process required by subsection (a), the Secretary shall ensure a covered veteran\u2014\n**(1)**\nis screened not later than 48 hours after the date on which the covered veteran, or a relevant health care provider, makes a request for the covered veteran to be admitted to a covered treatment program;\n**(2)**\nif determined eligible for priority admission to a covered treatment program, is admitted to such covered treatment program not later than 48 hours after the date of such determination; and\n**(3)**\nis screened at an appropriate time for potential mild, moderate, or severe traumatic brain injury.\n##### (d) Considerations\nIn making placement decisions in a covered treatment program for veterans who meet criteria for priority admission, the Secretary shall\u2014\n**(1)**\nconsider the input of the covered veteran with respect to the\u2014\n**(A)**\nprogram specialty, subtype, and treatment track offered to the covered veteran; and\n**(B)**\ngeographic placement of the covered veteran; and\n**(2)**\nmaximize the proximity of the covered veteran to social support systems.\n##### (e) Conditions under which care shall be furnished through non-Department providers\n**(1) Priority admission**\nIf the Secretary determines a covered veteran is eligible for priority admission to a covered treatment program pursuant to the standardized screening process required by subsection (a) and the Secretary is unable to admit such covered veteran to a covered treatment program at a facility of the Department of Veterans Affairs in a manner that complies with the requirements under subsections (c) and (d), the Secretary shall offer the covered veteran the option to receive care at a non-Department facility that\u2014\n**(A)**\ncan admit the covered veteran within the period required by subsection (c);\n**(B)**\nis party to a contract or agreement with the Department or enters into such a contract or agreement under which the Department furnishes a program that is equivalent to a covered treatment program to a veteran through such non-Department facility;\n**(C)**\nis licensed by a State; and\n**(D)**\nis accredited by the Commission on Accreditation of Rehabilitation Facilities or the Joint Commission.\n**(2) Routine admission**\nIf the Secretary determines a covered veteran is eligible for routine admission to a covered treatment program pursuant to the standardized screening process required by subsection (a) and the Secretary is unable to admit such covered veteran to a covered treatment program at a facility of the Department of Veterans Affairs in a manner that complies with the access standards for mental health care established pursuant to section 1703B of title 38, United States Code, the Secretary shall offer the covered veteran the option to receive care at a non-Department facility that\u2014\n**(A)**\nis party to a contract or agreement with the Department or enters into such a contract or agreement under which the Department furnishes a program that is equivalent to a covered treatment program to a veteran through such non-Department facility;\n**(B)**\nis licensed by a State; and\n**(C)**\nis accredited by the Commission on Accreditation of Rehabilitation Facilities or the Joint Commission.\n**(3) Rule of construction**\nThis subsection shall not be construed to affect a covered veteran in a covered treatment program pursuant to a determination made on or before the date of the enactment of this Act.\n#### 203. Improvements to Department of Veterans Affairs Mental Health Residential Rehabilitation Treatment Program\n##### (a) Performance metrics\n**(1) In general**\nThe Secretary of Veterans Affairs shall develop metrics to track, and shall subsequently track, the performance of medical facilities and Veterans Integrated Service Networks of the Department of Veterans Affairs in meeting the requirements for\u2014\n**(A)**\nscreening, under section 202, for a covered treatment program; and\n**(B)**\ntimely admission to a covered treatment program under such screening.\n**(2) Elements**\nThe metrics developed under paragraph (1) shall include metrics for tracking the performance of medical facilities and Veterans Integrated Service Networks with respect to routine and priority admission under a covered treatment program.\n##### (b) Oversight\n**(1) In general**\nThe Secretary shall develop a process for systematically assessing the quality of care delivered by Department and non-Department providers treating covered veterans under this section, which shall include assessments of\u2014\n**(A)**\nthe extent to which the provider is delivering evidence-based treatments to covered veterans;\n**(B)**\nclinical outcomes for covered veterans;\n**(C)**\nthe ratio of licensed independent practitioners per resident;\n**(D)**\nthe rate of completion of training on military cultural competence by licensed independent practitioners; and\n**(E)**\npotentially wasteful, fraudulent, or inappropriate referral or billing practices.\n##### (c) Placement; transportation\n**(1) Locations**\nIf the Secretary determines that a covered veteran is in need of residential care under a covered treatment program, the Secretary shall provide to the covered veteran a list of locations at which such covered veteran can receive such residential care that meets\u2014\n**(A)**\nthe standards for screening under section 202; and\n**(B)**\nthe care needs of the covered veteran, including applicable treatment tracks.\n**(2) Transportation coverage**\nThe Secretary shall provide transportation or pay for or reimburse the costs of transportation for any covered veteran who is admitted into a covered treatment program and needs transportation assistance\u2014\n**(A)**\nfrom the residence of the covered veteran or a facility of the Department or authorized non-Department facility that does not provide such care to another such facility that provides residential care covered under a covered treatment program; and\n**(B)**\nback to the residence of the covered veteran after the conclusion of a covered treatment program, if applicable.\n##### (d) Appeals\n**(1) In general**\nThe Secretary shall develop a national policy and associated procedures under which a covered veteran, a representative of a covered veteran, or a provider who requests a covered veteran be admitted to a covered treatment program, including a provider of the Department or a non-Department provider, may file a clinical appeal pursuant to this subsection if the covered veteran is\u2014\n**(A)**\ndenied admission into a covered treatment program; or\n**(B)**\naccepted into a covered treatment program but is not offered bed placement in a timely manner.\n**(2) Timeliness standards for review**\n**(A) In general**\nThe national policy and procedures developed under paragraph (1) for appeals described in such paragraph shall include timeliness standards for the Department to review and make a decision on such an appeal.\n**(B) Decision**\nThe Secretary shall review and respond to any appeal under paragraph (1) not later than 72 hours after the Secretary receives such appeal.\n**(3) Public guidance**\nThe Secretary shall develop, and make available to the public, guidance on how a covered veteran, a representative of the covered veteran, or a provider of the covered veteran can file a clinical appeal pursuant to this subsection\u2014\n**(A)**\nif the covered veteran is denied admission into a covered treatment program;\n**(B)**\nif the first date on which the covered veteran may enter a covered treatment program does not comply with the standards established by the Department under section 1703B of title 38, United States Code, for purposes of determining eligibility for mental health care under subsections (d) and (e) of section 1703 of such title; or\n**(C)**\nwith respect to such other factors as the Secretary may specify.\n**(4) Rule of construction**\nNothing in this subsection may be construed as granting a covered veteran the right to appeal a decision of the Secretary with respect to admission to a covered treatment program to the Board of Veterans\u2019 Appeals under chapter 71 of title 38, United States Code.\n##### (e) Tracking of availability and wait times\n**(1) In general**\nThe Secretary shall, to the extent practicable, create a method for tracking availability and wait times under a covered treatment program across all facilities of the Department, Veterans Integrated Service Networks of the Department, and non-Department providers throughout the United States.\n**(2) Availability of information**\nThe Secretary shall, to the extent practicable, make the information tracked under paragraph (1) available in real time to\u2014\n**(A)**\nthe mental health treatment coordinators at each facility of the Department;\n**(B)**\nthe leadership of each medical center of the Department;\n**(C)**\nthe leadership of each Veterans Integrated Service Network; and\n**(D)**\nthe Office of the Under Secretary for Health of the Department.\n##### (f) Training and oversight\n**(1) Training**\n**(A) In general**\nThe Secretary shall update and implement training for staff of the Department directly involved in a covered treatment program regarding referrals, screening, admission, placement decisions, and appeals for such program, including all changes to processes and guidance under such program required by this section and section 202.\n**(B) Covered veterans awaiting admission**\nThe training under subparagraph (A) shall include procedures for the care of covered veterans awaiting admission into a covered treatment program and communication with such covered veterans and the providers of such covered veterans.\n**(C) Timing of training**\n**(i) In general**\nThe Secretary shall require the training under subparagraph (A) to be completed by staff required to complete such training\u2014\n**(I)**\nnot later than 60 days after beginning employment at the Department in a position that includes work directly involving a covered treatment program; and\n**(II)**\nnot less frequently than annually.\n**(ii) Tracking**\nThe Secretary shall track completion of training required under clause (i) by staff required to complete such training.\n**(2) Oversight standards**\nThe Secretary shall review and revise oversight standards for the leadership of the Veterans Integrated Service Networks and the Veterans Health Administration to ensure that facilities and staff of the Department are adhering to the policy on access to care of each covered treatment program.\n##### (g) Care coordination and follow-Up care\n**(1) Continuity of care**\nThe Secretary shall ensure each covered veteran who is screened for admission to a covered treatment program is offered, and provided if agreed upon, care options during the period between screening of the covered veteran and admission of the covered veteran to such program to ensure the covered veteran does not experience any lapse in care.\n**(2) Care coordination for substance use disorder**\nFor a covered veteran being treated for substance use disorder, the Secretary shall\u2014\n**(A)**\nensure there is a care plan in place during the period between any detoxification services or inpatient care received by the covered veteran and admission of the covered veteran to a covered treatment program; and\n**(B)**\ncommunicate that care plan to the covered veteran, the primary care provider of the covered veteran, and the facility where the covered veteran is or will be residing under such program.\n**(3) Care planning prior to discharge**\n**(A) In general**\nThe Secretary, in consultation with the covered veteran and the treating providers of the covered veteran in a covered treatment program, shall ensure the completion of a care plan prior to the covered veteran being discharged from such program.\n**(B) Matters to be included**\nThe care plan required under subparagraph (A) for a covered veteran shall include details on the course of treatment for the covered veteran following completion of treatment under the covered treatment program, including any necessary follow-up care.\n**(C) Sharing of care plan**\nThe care plan required under subparagraph (A) shall be shared with the covered veteran, the primary care provider of the covered veteran, and any other providers with which the covered veteran consents to sharing the plan.\n**(D) Discharge from non-department facility**\nUpon discharge of a covered veteran under a covered treatment program from a non-Department facility, the facility shall share with the Department all care records maintained by the facility with respect to the covered veteran and shall work in consultation with the Department on the care plan of the covered veteran required under subparagraph (A).\n##### (h) Reports to Congress\n**(1) Report on modifications to programs**\n**(A) In general**\nNot later than two years after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on modifications made to the guidance, operation, and oversight of covered treatment programs to fulfill the requirements of this section.\n**(B) Elements**\nThe report required by subparagraph (A) shall include\u2014\n**(i)**\nan assessment of whether costs of covered treatment programs, including for residential care provided through facilities of the Department and non-Department facilities, serve as a disincentive to placement in the such a program;\n**(ii)**\na description of actions taken by the Department to address the findings and recommendations by the Secretary contained in the report under section 503(c) of the STRONG Veterans Act of 2022 (division V of Public Law 117\u2013328 ; 136 Stat. 5515), including\u2014\n**(I)**\nsuch actions with respect to\u2014\n**(aa)**\nany new locations added for covered treatment programs;\n**(bb)**\nany beds added at existing facilities of such programs; and\n**(cc)**\nany additional treatment tracks or sex-specific programs created or added at facilities of the Department; and\n**(II)**\na breakdown of the number and percentage of covered veterans who are determined eligible for priority placement into a covered treatment program and the number and percentage of covered veterans who are determined eligible for routine placement into a covered treatment program; and\n**(iii)**\nsuch recommendations as the Secretary may have for legislative or administrative action to address any funding constraints or disincentives for use of a covered treatment program.\n**(2) Annual report on operation of programs**\n**(A) In general**\nNot later than one year after the submission of the report under paragraph (1), and not less frequently than annually thereafter during the period in which a covered treatment program is carried out, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the operation of such programs.\n**(B) Elements**\nSubject to subparagraph (C), each report required by subparagraph (A) shall include the following:\n**(i)**\nThe number of covered veterans served by a covered treatment program, disaggregated by\u2014\n**(I)**\nVeterans Integrated Service Network in which the covered veteran receives care;\n**(II)**\nfacility, including facilities of the Department and non-Department facilities, at which the covered veteran receives care;\n**(III)**\ntype of residential rehabilitation treatment care received by the covered veteran under such program;\n**(IV)**\nsex of the covered veteran; and\n**(V)**\nrace or ethnicity of the covered veteran.\n**(ii)**\nWait times under a covered treatment program for the most recent year data is available, disaggregated by\u2014\n**(I)**\ntreatment track or specificity of residential rehabilitation treatment care sought by the covered veteran;\n**(II)**\nsex of the covered veteran;\n**(III)**\nState or territory in which the covered veteran is located;\n**(IV)**\nVeterans Integrated Service Network in which the covered veteran is located; and\n**(V)**\nfacility of the Department at which the covered veteran seeks care.\n**(iii)**\nA list of all locations of a covered treatment program and number of bed spaces at each such location, disaggregated by residential rehabilitation treatment care or treatment track provided under such program at such location.\n**(iv)**\nA list of any new locations of covered treatment programs added or removed and any bed spaces added or removed during the one-year period preceding the date of the report.\n**(v)**\nAverage cost of a stay under a covered treatment program, including total stay average and daily average, at facilities of the Department compared to non-Department facilities.\n**(vi)**\nA review of staffing needs and gaps with respect to covered treatment programs.\n**(vii)**\nAny recommendations for changes to the operation of covered treatment programs, including any policy changes, guidance changes, training changes, or other changes.\n**(C) Anonymity**\nTo ensure that the data provided under this paragraph, or some portion of that data, will not undermine the anonymity of a veteran, the Secretary shall provide such data pursuant to applicable Federal law and in a manner that is wholly consistent with applicable Federal privacy and confidentiality laws, including\u2014\n**(i)**\nsection 552a of title 5, United States Code (commonly known as the Privacy Act of 1974 );\n**(ii)**\nthe Health Insurance Portability and Accountability Act of 1996 ( Public Law 104\u2013191 );\n**(iii)**\nparts 160 and 164 of title 45, Code of Federal Regulations, or successor regulations; and\n**(iv)**\nsections 5701, 5705, and 7332 of title 38, United States Code.\n##### (i) Revision of guidance\nThe Secretary shall update the guidance of the Department on the operation of covered treatment programs to reflect each of the requirements under subsections (b) through (h).\n##### (j) Deadline\nThe Secretary shall carry out each requirement under this section by not later than one year after the date of the enactment of this Act, unless otherwise specified.\n##### (k) Comptroller General review\n**(1) In general**\nNot later than two years after the date of the enactment of this Act, the Comptroller General of the United States shall review access to care under a covered treatment program for covered veterans in need of residential mental health care and substance use disorder care.\n**(2) Elements**\nThe review required by paragraph (1) shall include the following:\n**(A)**\nA review of wait times under a covered treatment program, disaggregated by\u2014\n**(i)**\ntreatment track or specificity of residential rehabilitation treatment care needed;\n**(ii)**\nsex of the covered veteran;\n**(iii)**\nhome State of the covered veteran;\n**(iv)**\nhome Veterans Integrated Service Network of the covered veteran; and\n**(v)**\nwait times for\u2014\n**(I)**\nfacilities of the Department; and\n**(II)**\nnon-Department facilities.\n**(B)**\nA review of policy and training of the Department on screening, admission, and placement under a covered treatment program.\n**(C)**\nA review of the rights of covered veterans and providers to appeal admission decisions under a covered treatment program and how the Department adjudicates appeals.\n**(D)**\nWhen determining the facility at which a covered veteran admitted to a covered treatment program will be placed in such program, a review of how the input of the covered veteran is taken into consideration with respect to\u2014\n**(i)**\nprogram specialty, subtype, or treatment track offered to the covered veteran; and\n**(ii)**\nthe geographic placement of the covered veteran, including family- or occupation-related preferences or circumstances.\n**(E)**\nA review of staffing and staffing needs and gaps of covered treatment programs, including with respect to\u2014\n**(i)**\nmental health providers and coordinators at the facility level;\n**(ii)**\nstaff of facilities of such programs;\n**(iii)**\nstaff of Veterans Integrated Service Networks; and\n**(iv)**\noverall administration of such programs at the national level.\n**(F)**\nRecommendations for improvement of access by covered veterans to care under a covered treatment program, including with respect to\u2014\n**(i)**\nany new sites or types of programs needed or in development;\n**(ii)**\nchanges in training or policy;\n**(iii)**\nchanges in communications with covered veterans; and\n**(iv)**\noversight of covered treatment programs by the Department.\nIII\nOther health care matters\n#### 301. Plan on establishment of interactive, online self-service module for care\n##### (a) In general\nThe Secretary of Veterans Affairs, working with Third Party Administrators and acting through the Center for Innovation for Care and Payment of the Department of Veterans Affairs under section 1703E of title 38, United States Code, shall develop and implement a plan to establish an interactive, online self-service module\u2014\n**(1)**\nto allow veterans to request appointments, track referrals for health care under the laws administered by the Secretary, whether at a facility of the Department or through a non-Department provider, and receive appointment reminders;\n**(2)**\nto allow veterans to appeal and track decisions relating to\u2014\n**(A)**\ndenials of requests for care or services under section 1703 of title 38, United States Code; or\n**(B)**\ndenials of requests for care or services at facilities of the Department, including under section 1710 of such title; and\n**(3)**\nto implement such other matters as determined appropriate by the Secretary in consultation with Third Party Administrators.\n##### (b) Submittal of plan\n**(1) Initial plan**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives the plan developed under subsection (a).\n**(2) Quarterly update**\nNot less frequently than quarterly following the submittal of the plan under paragraph (1) and for two years thereafter, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report containing any updates on the implementation of such plan.\n##### (c) Rule of construction\nThis section shall not be construed to be a pilot program subject to the requirements of section 1703E of title 38, United States Code.\n##### (d) Third Party Administrator defined\nIn this section, the term Third Party Administrator means an entity that manages a provider network and performs administrative services related to such network under section 1703 of title 38, United States Code.\n#### 302. Modification of requirements for Center for Innovation for Care and Payment of the Department of Veterans Affairs and requirement for pilot program\n##### (a) In general\nSection 1703E of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking within the Department and inserting within the Office of the Secretary ;\n**(B)**\nin paragraph (2), by striking may and inserting shall ; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(C) increase productivity, efficiency, and modernization throughout the Department. ;\n**(2)**\nby striking subsection (d) and inserting the following new subsection (d):\n(d) Budgetary line item The Secretary shall include in the budget justification materials submitted to Congress in support of the budget of the Department of Veterans Affairs for a fiscal year (as submitted with the budget of the President under section 1105(a) of title 31) specific identification, as a budgetary line item, of the amounts required to carry out this section. ;\n**(3)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1), by striking in subchapters I, II, and III of this chapter and inserting of this title, of title 38, Code of Federal Regulations, and of any handbooks, directives, or policy documents of the Department ; and\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by striking waiving any authority and inserting waiving any provision of this title ;\n**(4)**\nin subsection (g)(1), by inserting fewer than three or before more than 10 ;\n**(5)**\nin subsection (i)\u2014\n**(A)**\nin paragraph (1), by striking the Under Secretary for Health and the Special Medical Advisory Group established pursuant to section 7312 of this title and inserting the Under Secretary for Health, the Special Medical Advisory Group established pursuant to section 7312 of this title, the Office of Integrated Veteran Care (or successor office), the Office of Finance (or successor office), the Veteran Experience Office (or successor office), the Office of Enterprise Integration (or successor office), and the Office of Information and Technology (or successor office) ; and\n**(B)**\nin paragraph (2), by striking representatives of relevant Federal agencies, and clinical and analytical experts with expertise in medicine and health care management and inserting representatives of relevant Federal agencies, nonprofit organizations, and other public and private sector entities, including those with clinical and analytical experts with expertise in medicine and health care management ; and\n**(6)**\nby adding at the end the following new subsection:\n(k) Report on activities of Center for Innovation for Care and Payment Not less frequently than annually, the Secretary shall submit to Congress a report that contains, for the one-year period preceding the date of the report\u2014 (1) a full accounting of the activities, staff, budget, and other resources and efforts of the Center; and (2) an assessment of the outcomes of the efforts of the Center. .\n##### (b) Comptroller General Report\nNot later than 18 months after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report\u2014\n**(1)**\non the efforts of the Center for Innovation for Care and Payment of the Department of Veterans Affairs in fulfilling the objectives and requirements under section 1703E of title 38, United States Code, as amended by subsection (a); and\n**(2)**\ncontaining such recommendations as the Comptroller General considers appropriate.\n##### (c) Pilot program\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Center for Innovation for Care and Payment of the Department of Veterans Affairs under section 1703E of title 38, United States Code, shall establish a three-year pilot program in not fewer than five locations to allow veterans enrolled in the system of annual patient enrollment of the Department established and operated under section 1705(a) of such title to access outpatient mental health and substance use services through health care providers specified under section 1703(c) of such title without referral or pre-authorization.\n**(2) Priority**\nIn selecting sites for the pilot program under paragraph (1), the Secretary shall prioritize sites in the following areas:\n**(A)**\nAreas with varying degrees of urbanization, including urban, rural, and highly rural areas.\n**(B)**\nAreas with high rates of suicide among veterans.\n**(C)**\nAreas with high rates of overdose deaths among veterans.\n**(D)**\nAreas with high rates of calls to the Veterans Crisis Line.\n**(E)**\nAreas with long wait times for mental health and substance use services at facilities of the Department.\n**(F)**\nAreas with outpatient mental health and substance use programs that utilize a value-based care model, to the extent practicable.\n**(3) Elements**\nThe Secretary, in implementing the pilot program under paragraph (1), shall ensure the Department has a care coordination system in place that includes\u2014\n**(A)**\nknowledge sharing, including the timely exchange of medical documentation;\n**(B)**\nassistance with transitions of care, including the potential need for inpatient or residential psychiatric services, substance use detoxification services, post-detoxification step-down services, and residential rehabilitation programs;\n**(C)**\ncontinuous assessment of patient needs and goals; and\n**(D)**\ncreating personalized, proactive care plans.\n**(4) Oversight and outcomes**\nThe Secretary shall develop appropriate metrics and measures\u2014\n**(A)**\nto track and oversee sites at which the pilot program under paragraph (1) is carried out;\n**(B)**\nto monitor patient safety and outcomes under the pilot program; and\n**(C)**\nto assess and mitigate any barriers to extending the pilot program across the entire Veterans Health Administration.\n**(5) Annual report**\n**(A) In general**\nNot later than one year after the commencement of the pilot program under paragraph (1), and not less frequently than annually thereafter during the duration of the pilot program, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and Committee on Veterans\u2019 Affairs of the House of Representatives a report on the pilot program, which shall include the following:\n**(i)**\nThe number of unique veterans who participated in the pilot program.\n**(ii)**\nThe number of health care providers who participated in the pilot program.\n**(iii)**\nAn assessment of the effectiveness of the pilot program in increasing access to, and improving outcomes for, mental health and substance use treatment services.\n**(iv)**\nThe cost of the pilot program.\n**(v)**\nSuch other matters as the Secretary considers appropriate.\n**(B) Final report**\nThe Secretary shall include in the final report submitted under subparagraph (A), in addition to the requirements under such subparagraph, the assessment by the Secretary of the feasibility and advisability of extending the pilot program across the entire Veterans Health Administration, including a plan, timeline, and required resources for such an extension.\n**(6) Veterans crisis line defined**\nIn this subsection, the term Veterans Crisis Line means the toll-free hotline for veterans established under section 1720F(h) of title 38, United States Code.\n#### 303. Reports\n##### (a) Report on improvements to clinical appeals process\nNot later than one year after the date of the enactment of this Act, and not less frequently than once every three years thereafter, the Secretary of Veterans Affairs, in consultation with veterans service organizations, veterans, caregivers of veterans, employees of the Department of Veterans Affairs, and other stakeholders as determined by the Secretary, shall submit to the Committee on Veterans\u2019 Affairs of the Senate and Committee on Veterans\u2019 Affairs of the House of Representatives a report containing recommendations for legislative or administrative action to improve the clinical appeals process of the Department with respect to timeliness, transparency, objectivity, consistency, and fairness.\n##### (b) Report on required care and services under community care program\nNot later than one year after the date of the enactment of this Act, and not less frequently than annually thereafter, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and Committee on Veterans\u2019 Affairs of the House of Representatives a report that contains, for the one-year period preceding the date of the report, the following:\n**(1)**\nThe number of veterans eligible for care or services under section 1703 of title 38, United States Code, and the reasons for such eligibility, including multiple such reasons for veterans eligible under more than one eligibility criteria.\n**(2)**\nThe number of veterans who opt to seek care or services under such section.\n**(3)**\nThe number of veterans who do not opt to seek care or services under such section.\n**(4)**\nAn assessment of the timeliness of referrals for care or services under such section.\n**(5)**\nThe number of times a veteran did not show for an appointment for care or services under such section.\n**(6)**\nThe number of requests for an appeal of a denial of care or services under such section using the clinical appeals process of the Veterans Health Administration.\n**(7)**\nThe timeliness of each such appeal.\n**(8)**\nThe outcome of each such appeal.\n##### (c) Veterans service organization defined\nIn this section, the term veterans service organization means any organization recognized by the Secretary under section 5902 of title 38, United States Code.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-23",
        "text": "Ordered to be Reported (Amended) by Voice Vote."
      },
      "number": "740",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans\u2019 ACCESS Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-19T17:29:02Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T17:28:13Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-03-19T17:29:16Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-03-19T17:29:09Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-19T17:28:02Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-19T17:27:38Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-19T17:29:21Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-19T17:28:20Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-19T17:27:43Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-19T17:27:53Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-03-19T17:28:37Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-03-19T17:27:48Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-19T17:28:27Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-03-19T17:28:42Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-19T17:27:33Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-03-19T17:29:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T17:42:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s275",
          "measure-number": "275",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-12-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s275v00",
            "update-date": "2025-12-31"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans' Assuring Critical Care Expansions to Support\u00a0Servicemembers (ACCESS) Act of 2025</strong></p><p>This bill addresses the administration of the Veterans Community Care Program (VCCP) and other Department of Veterans Affairs (VA) health care matters.</p><p>Among other provisions regarding the VCCP, the bill</p><ul><li>establishes in statute access standards that determine when a veteran is eligible to receive non-VA care through the VCCP,</li><li>requires the VA to notify veterans regarding their eligibility for care within two business days after the VA is aware the veteran is seeking care, and</li><li>extends the deadline for the submittal of claims under the\u00a0VCCP by health care entities and providers.</li></ul><p>The VA must address its mental health treatment programs by</p><ul><li>establishing a standardized screening process to determine whether a veteran satisfies criteria for priority or routine admission to a mental health residential rehabilitation treatment program or a program for residential care for mental health and substance abuse disorders,</li><li>tracking the performance of medical facilities and Veterans Integrated Service Networks in meeting the requirements for mental health treatment screenings and timely admission to treatment programs under such screenings, and</li><li>establishing an appeal process for when a veteran is denied admission to a covered treatment program or is accepted into a program but not offered bed placement in a timely manner.</li></ul><p>Additionally, the VA must establish an online self-service module for veterans to request and manage appointments, track referrals, and appeal and track decisions related to requests for care.</p>"
        },
        "title": "Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s275.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans' Assuring Critical Care Expansions to Support\u00a0Servicemembers (ACCESS) Act of 2025</strong></p><p>This bill addresses the administration of the Veterans Community Care Program (VCCP) and other Department of Veterans Affairs (VA) health care matters.</p><p>Among other provisions regarding the VCCP, the bill</p><ul><li>establishes in statute access standards that determine when a veteran is eligible to receive non-VA care through the VCCP,</li><li>requires the VA to notify veterans regarding their eligibility for care within two business days after the VA is aware the veteran is seeking care, and</li><li>extends the deadline for the submittal of claims under the\u00a0VCCP by health care entities and providers.</li></ul><p>The VA must address its mental health treatment programs by</p><ul><li>establishing a standardized screening process to determine whether a veteran satisfies criteria for priority or routine admission to a mental health residential rehabilitation treatment program or a program for residential care for mental health and substance abuse disorders,</li><li>tracking the performance of medical facilities and Veterans Integrated Service Networks in meeting the requirements for mental health treatment screenings and timely admission to treatment programs under such screenings, and</li><li>establishing an appeal process for when a veteran is denied admission to a covered treatment program or is accepted into a program but not offered bed placement in a timely manner.</li></ul><p>Additionally, the VA must establish an online self-service module for veterans to request and manage appointments, track referrals, and appeal and track decisions related to requests for care.</p>",
      "updateDate": "2025-12-31",
      "versionCode": "id119s275"
    },
    "title": "Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans' Assuring Critical Care Expansions to Support\u00a0Servicemembers (ACCESS) Act of 2025</strong></p><p>This bill addresses the administration of the Veterans Community Care Program (VCCP) and other Department of Veterans Affairs (VA) health care matters.</p><p>Among other provisions regarding the VCCP, the bill</p><ul><li>establishes in statute access standards that determine when a veteran is eligible to receive non-VA care through the VCCP,</li><li>requires the VA to notify veterans regarding their eligibility for care within two business days after the VA is aware the veteran is seeking care, and</li><li>extends the deadline for the submittal of claims under the\u00a0VCCP by health care entities and providers.</li></ul><p>The VA must address its mental health treatment programs by</p><ul><li>establishing a standardized screening process to determine whether a veteran satisfies criteria for priority or routine admission to a mental health residential rehabilitation treatment program or a program for residential care for mental health and substance abuse disorders,</li><li>tracking the performance of medical facilities and Veterans Integrated Service Networks in meeting the requirements for mental health treatment screenings and timely admission to treatment programs under such screenings, and</li><li>establishing an appeal process for when a veteran is denied admission to a covered treatment program or is accepted into a program but not offered bed placement in a timely manner.</li></ul><p>Additionally, the VA must establish an online self-service module for veterans to request and manage appointments, track referrals, and appeal and track decisions related to requests for care.</p>",
      "updateDate": "2025-12-31",
      "versionCode": "id119s275"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s275is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans\u2019 Assuring Critical Care Expansions to Support Servicemembers (ACCESS) Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the provision of care and services under the Veterans Community Care Program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:39Z"
    }
  ]
}
```
