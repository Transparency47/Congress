# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3303?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3303
- Title: LINC VA Act
- Congress: 119
- Bill type: S
- Bill number: 3303
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-03-26T18:52:56Z
- Update date including text: 2026-03-26T18:52:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3303",
    "number": "3303",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "LINC VA Act",
    "type": "S",
    "updateDate": "2026-03-26T18:52:56Z",
    "updateDateIncludingText": "2026-03-26T18:52:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
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
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
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
            "date": "2026-03-18T20:00:34Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:40Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-02T17:55:49Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3303is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3303\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mr. Sullivan (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to carry out a pilot program to establish or enhance a community integration platform for services for veterans, to require the collection from veterans of information related to social determinants of health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leveraging Integrated Networks in Communities for Veterans Act or the LINC VA Act .\n#### 2. Pilot program on establishment or enhancement of community integration platform for veterans\n##### (a) In general\nBeginning not later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, acting through the Center for Innovation for Care and Payment of the Department of Veterans Affairs, shall carry out a pilot program under which the Secretary shall establish a new, or enhance an existing, interoperable community integration platform to coordinate local support services for veterans through other governmental and nongovernmental organizations (in this section referred to as the pilot program ).\n##### (b) Community integration platform\nThe community integration platform established or enhanced pursuant to the pilot program shall be accessible to veterans, employees of the Department of Veterans Affairs, and others participating in the pilot program as determined appropriate by the Secretary and shall\u2014\n**(1)**\nenable the coordination of services such as\u2014\n**(A)**\nnutritional assistance;\n**(B)**\nhousing;\n**(C)**\nhealth care, including preventive health intervention, chronic disease management, and behavioral health care;\n**(D)**\ntransportation;\n**(E)**\njob training;\n**(F)**\nchild development or care;\n**(G)**\ncaregiving and respite care;\n**(H)**\ndisability assistance;\n**(I)**\nsuicide prevention;\n**(J)**\nsexual assault services;\n**(K)**\nlegal aid;\n**(L)**\ntransition programs of the Department of Defense; and\n**(M)**\nother services, as determined by the Secretary;\n**(2)**\nprioritize connectivity with appropriate existing technology networks developed by public or private organizations that comply with, as applicable, standards adopted by the Secretary of Health and Human Services under section 3004 of the Public Health Service Act ( 42 U.S.C. 300jj\u201314 ), for the purposes described in paragraph (1);\n**(3)**\nensure that\u2014\n**(A)**\nreasonable measures are taken to promote connectivity and interoperable exchange among covered entities; and\n**(B)**\nappropriate privacy and security protections are in place, in accordance with applicable Federal and State privacy laws;\n**(4)**\nconnect covered entities for purposes of communication, service coordination and consumer assistance, referral and capacity management, outcome tracking and reporting, and related services;\n**(5)**\nprovide technical assistance and support covered entities in connecting and participating in the community integration platform;\n**(6)**\ncollect information from veterans served under the pilot program regarding social determinants of health using a standardized risk assessment or screening tool, which shall include standardized definitions for identifying social determinants of health needs identified in the ICD\u201310 diagnostic codes Z55 through Z63 and Z75 (as in effect on the date of the enactment of this Act) that incorporate measures for quantifying the relative severity of any such social determinant of health need identified in a veteran;\n**(7)**\nincorporate screenings used to collect information under paragraph (6) into routine care provided to veterans under the laws administered by the Secretary; and\n**(8)**\nbe accessible via a web-based platform for all veterans and via a non-web-based alternative platform or process for veterans who are unable to easily and reliably access the web-based platform.\n##### (c) Locations\n**(1) In general**\nThe Secretary of Veterans Affairs shall carry out the pilot program at not fewer than five medical facilities of the Department of Veterans Affairs.\n**(2) Variety of facilities**\nIn selecting facilities under paragraph (1), the Secretary shall ensure the selection of a variety of different types of facilities, including\u2014\n**(A)**\nfrontier facilities;\n**(B)**\nunder-resourced facilities; and\n**(C)**\nfacilities at which there are existing efforts to coordinate with community resources.\n##### (d) Coordination and integration of programs\n**(1) Coordination with existing networks**\nIn carrying out the pilot program, the Secretary of Veterans Affairs shall coordinate with existing community networks.\n**(2) Coordination and integration with State medicaid programs**\nThe Secretary of Health and Human Services, in consultation with the Secretary of Veterans Affairs, shall issue guidance to States that includes options for State Medicaid programs to coordinate and integrate medical assistance provided under a State plan or waiver under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) with services for veterans provided under the pilot program, as well as a template for States to use to request or modify Medicaid waiver authority under section 1115 of the Social Security Act ( 42 U.S.C. 1315 ) for such purpose.\n##### (e) Tracking of referrals\n**(1) In general**\nThe Secretary of Veterans Affairs shall track\u2014\n**(A)**\nthe accuracy of referrals of veterans to community networks under the pilot program;\n**(B)**\nthe response time of providers to which such veterans are referred; and\n**(C)**\nthe outcome of the initial meeting by a veteran and the provider to which the veteran is referred.\n**(2) Form**\nThe Secretary may track the information required under paragraph (1) in any medium determined appropriate by the Secretary.\n##### (f) Report\nNot later than three years after amounts are first appropriated to carry out the pilot program, the Secretary of Veterans Affairs shall submit to Congress a report indicating the social service needs of veterans reflected by the use of services under the community integration platform established or enhanced under the pilot program, including an assessment of\u2014\n**(1)**\nthe need for services that is being met through such platform; and\n**(2)**\nthe need for services that is not being met through such platform.\n##### (g) Comptroller General evaluation, report, and recommendations\n**(1) Evaluation**\nThe Comptroller General of the United States shall conduct an evaluation that measures the overall impact of the community integration platform established or enhanced under the pilot program with respect to\u2014\n**(A)**\nchanges in individual and population health outcomes among veterans;\n**(B)**\nchanges in access to health care or social services among veterans; and\n**(C)**\nsuch other factors as the Comptroller General considers appropriate.\n**(2) Report and recommendations**\n**(A) In general**\nNot later than four years after the date of the enactment of this Act, the Comptroller General shall\u2014\n**(i)**\nsubmit to Congress a report on the evaluation conducted under paragraph (1);\n**(ii)**\nmake such report publicly available; and\n**(iii)**\nbased on such evaluation, make recommendations to the Secretary of Veterans Affairs on how to improve and sustain the community integration platform established or enhanced under the pilot program.\n**(B) Elements of report**\nThe report under subparagraph (A)(i) shall include data on\u2014\n**(i)**\nwhat resources under the pilot program are being utilized the most;\n**(ii)**\nwhat requests for services under the pilot program cannot be met; and\n**(iii)**\nthe impact of the provision of services under the pilot program on health outcomes of veterans.\n##### (h) Definitions\nIn this section:\n**(1) Community integration platform**\nThe term community integration platform means an interoperable platform used to enable the coordination, alignment, and connection of covered entities at the local level for purposes of communication, service coordination, and referral management of services, with respect to services specified in subsection (b)(1).\n**(2) Covered entity**\nThe term covered entity means any\u2014\n**(A)**\ncommunity-based organization that\u2014\n**(i)**\naccepts referrals from health care organizations; and\n**(ii)**\nprovides services specified in subsection (b)(1).\n**(B)**\npublic or private health care provider organization;\n**(C)**\npublic or private funded payor of health care services, including home- or community-based services;\n**(D)**\nState, local, territorial, or Tribal health and social services agency;\n**(E)**\nState public housing authority or housing finance agency;\n**(F)**\npublic health information exchange or public health information network, as defined by the Secretary of Veterans Affairs; or\n**(G)**\nother similar entity, as determined by the Secretary.\n**(3) State**\nThe term State means a State, territory of the United States, or the District of Columbia.\n#### 3. Collection of information from veterans related to social determinants of health\n##### (a) In general\nThe Secretary of Veterans Affairs shall collect from veterans enrolled in the system of annual patient enrollment of the Department of Veterans Affairs established and operated under section 1705(a) of title 38, United States Code, as part of routine screenings of such veterans under the laws administered by the Secretary, information related to social determinants that may factor into the health of such veterans.\n##### (b) Social determinants of health\n**(1) In general**\nThe information collected under subsection (a) shall include standardized definitions for identifying social determinants of health needs identified in the ICD\u201310 diagnostic codes Z55 through Z63 and Z75 (as in effect on the date of enactment of this Act).\n**(2) Incorporation of measures**\nDefinitions included under paragraph (1) with respect to identifying social determinants of health needs shall incorporate measures for quantifying the relative severity of any such social determinant of health need identified in an individual.",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in Senate"
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
            "name": "Community life and organization",
            "updateDate": "2026-03-26T18:50:55Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-26T18:52:13Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-26T18:52:43Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-26T18:52:50Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-03-26T18:51:14Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2026-03-26T18:52:56Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-03-26T18:52:07Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-03-26T18:52:24Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-03-26T18:52:46Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-03-26T18:51:08Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2026-03-26T18:51:02Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-03-26T18:50:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-07T23:18:36Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3303is.xml"
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
      "title": "LINC VA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LINC VA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leveraging Integrated Networks in Communities for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to carry out a pilot program to establish or enhance a community integration platform for services for veterans, to require the collection from veterans of information related to social determinants of health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T03:48:20Z"
    }
  ]
}
```
