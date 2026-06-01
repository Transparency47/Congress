# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6454
- Title: VA Zero Suicide Demonstration Project Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6454
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-04-15T08:05:56Z
- Update date including text: 2026-04-15T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6454",
    "number": "6454",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "VA Zero Suicide Demonstration Project Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:56Z",
    "updateDateIncludingText": "2026-04-15T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": {
          "date": "2025-12-04T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:10:12Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CO"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TN"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "KS"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6454ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6454\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. Lee of Nevada (for herself, Mr. Tony Gonzales of Texas , Ms. Pettersen , Mr. Fleischmann , Mr. Keating , Mr. Davis of North Carolina , and Mr. Mann ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish the Zero Suicide Initiative pilot program of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the VA Zero Suicide Demonstration Project Act of 2025 .\n#### 2. Zero Suicide Initiative pilot program\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a pilot program called the Zero Suicide Initiative (referred to in this section as the program ).\n##### (b) Curriculum\nThe program shall implement the curriculum of the Zero Suicide Institute of the Education Development Center (referred to in this section as the Institute ) to improve safety and suicide care for veterans, thereby significantly reducing rates of suicide.\n##### (c) Development\n**(1) In general**\nThe first year of the program shall be dedicated to program development, including planning and site selection.\n**(2) Consultation**\nIn developing the program, the Secretary shall consult with\u2014\n**(A)**\nthe Secretary of Health and Human Services;\n**(B)**\nthe National Institutes of Health;\n**(C)**\npublic and private institutions of higher education;\n**(D)**\neducators;\n**(E)**\nexperts in suicide assessment, treatment, and management;\n**(F)**\nveterans service organizations; and\n**(G)**\nprofessional associations the Secretary of Veterans Affairs determines relevant to the purposes of the program.\n##### (d) Staff leaders; program elements\nThe program shall consist of not less than ten weeks of education regarding suicide care, beginning with the selection of five to ten staff leaders from each site selected under subsection (e) who shall carry out the following program elements:\n**(1)**\nComplete the organizational self-study of the Institute as a team.\n**(2)**\nAttend the two-day Zero Suicide Academy of the Institute.\n**(3)**\nFormulate a plan to collect data to support evaluation and quality improvement using the data elements worksheet of the Institute.\n**(4)**\nCommunicate to staff at the respective site the adoption of a specific suicide care approach.\n**(5)**\nAdminister the workforce survey of the Institute to all staff at the respective site to learn more about perceived comfort with and competence in caring for patients at risk of suicide.\n**(6)**\nReview, develop, and implement training on processes and policies regarding patients at risk of suicide, including\u2014\n**(A)**\nscreening;\n**(B)**\nassessment;\n**(C)**\nuse of electronic health records;\n**(D)**\nrisk formulation;\n**(E)**\ntreatment; and\n**(F)**\ncare transition.\n##### (e) Sites\n**(1) Number**\nThe Secretary shall carry out the program at five medical centers of the Department of Veterans Affairs, one of which primarily serves veterans who live in rural and remote areas as determined by the Secretary.\n**(2) Timeline**\nThe Secretary shall select\u2014\n**(A)**\n15 candidate sites for the program not later than 180 days after the date of the enactment of this Act; and\n**(B)**\nthe final five sites not later than 270 days after the date of the enactment of this Act.\n**(3) Consultation**\nIn selecting sites at which to carry out the program, the Secretary shall consult with experts including officials of\u2014\n**(A)**\nthe National Institute of Mental Health;\n**(B)**\nthe Substance Abuse and Mental Health Services Administration of the Department of Health and Human Services;\n**(C)**\nthe Office of Mental Health and Suicide Prevention of the Department of Veterans Affairs;\n**(D)**\nthe Health Services Research Division of the Department of Veterans Affairs;\n**(E)**\nthe Office of Health Care Transformation of the Department of Veterans Affairs; and\n**(F)**\nthe Zero Suicide Institute.\n**(4) Factors**\nIn selecting sites for the program, the Secretary shall consider the following factors:\n**(A)**\nInterest in, and capacity of, the staff of the medical centers to implement the program.\n**(B)**\nGeographic variation.\n**(C)**\nVariations in size of medical centers.\n**(D)**\nRegional suicide rates of veterans.\n**(E)**\nDemographic and health characteristics of populations served by each medical center.\n##### (f) Annual progress report\n**(1) In general**\nNot later than two years after the date on which the Secretary establishes the program, and annually thereafter until termination of the program, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the program.\n**(2) Elements**\nEach report under paragraph (1) shall include the following:\n**(A)**\nProgress of staff leaders at each site in carrying out tasks under paragraphs (1) through (5) of subsection (d).\n**(B)**\nThe percentage of staff at each site trained under paragraph (6) of subsection (d).\n**(C)**\nAn assessment of whether policies and procedures implemented at each site align with standards of the Institute with regard to\u2014\n**(i)**\nsuicide screening;\n**(ii)**\nlethal means counseling;\n**(iii)**\nreferrals for comprehensive assessment of suicidality;\n**(iv)**\nsafety planning for patients receiving referrals under clause (iii);\n**(v)**\nrisk management during care transitions; and\n**(vi)**\noutreach to high-risk patients.\n**(D)**\nA comparison of the suicide-related outcomes at program sites and those of other medical centers of the Department of Veterans Affairs, including\u2014\n**(i)**\nthe percentage of patients screened for suicide risk;\n**(ii)**\nthe percentage of patients counseled in lethal means safety;\n**(iii)**\nthe percentage of patients screened for suicide risk referred for comprehensive assessment of suicidality;\n**(iv)**\nthe percentage of patients referred for comprehensive assessment who complete safety planning;\n**(v)**\nemergency department utilization;\n**(vi)**\ninpatient psychiatric hospitalizations;\n**(vii)**\nthe number of suicide attempts among all patients and among patients referred for comprehensive assessment of suicidality; and\n**(viii)**\nthe number of suicide deaths among all patients and among patients referred for comprehensive assessment of suicidality.\n##### (g) Final report\n**(1) In general**\nNot later than one year after the termination of the program, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a final report.\n**(2) Elements**\nThe report under paragraph (1) shall include the following:\n**(A)**\nA detailed analysis of information in the annual reports under subsection (f).\n**(B)**\nAn evaluation of the effectiveness and outcomes of the program, including an evaluation of all data collected during the program.\n**(C)**\nThe determination of the Secretary whether it is feasible to continue the program.\n**(D)**\nThe recommendations of the Secretary whether to expand the program to additional sites, extend the program, or make the program permanent.\n##### (h) Termination; extension\n**(1) In general**\nSubject to paragraph (2), the program shall terminate on the date that is five years after the date on which the Secretary establishes the program under subsection (a).\n**(2) Authority to extend**\nThe Secretary may extend the program for not more than two years if the Secretary notifies Congress in writing of such extension not less than 180 days before the termination date under paragraph (1).",
      "versionDate": "2025-12-04",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-06",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3139",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "VA Zero Suicide Demonstration Project Act of 2025",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-07T23:19:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-04",
    "originChamber": "House",
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
          "measure-id": "id119hr6454",
          "measure-number": "6454",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6454v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-12-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>VA Zero Suicide Demonstration Project Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Zero Suicide Initiative pilot program for the purpose of improving safety and suicide care for veterans. The program must be implemented at five VA medical centers, including one that serves veterans in rural and remote areas.</p>"
        },
        "title": "VA Zero Suicide Demonstration Project Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6454.xml",
    "summary": {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>VA Zero Suicide Demonstration Project Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Zero Suicide Initiative pilot program for the purpose of improving safety and suicide care for veterans. The program must be implemented at five VA medical centers, including one that serves veterans in rural and remote areas.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6454"
    },
    "title": "VA Zero Suicide Demonstration Project Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>VA Zero Suicide Demonstration Project Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Zero Suicide Initiative pilot program for the purpose of improving safety and suicide care for veterans. The program must be implemented at five VA medical centers, including one that serves veterans in rural and remote areas.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6454"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6454ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "VA Zero Suicide Demonstration Project Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Zero Suicide Demonstration Project Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish the Zero Suicide Initiative pilot program of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:31Z"
    }
  ]
}
```
