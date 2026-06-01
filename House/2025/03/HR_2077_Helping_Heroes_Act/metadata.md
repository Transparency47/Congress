# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2077?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2077
- Title: Helping Heroes Act
- Congress: 119
- Bill type: HR
- Bill number: 2077
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-12-05T22:55:59Z
- Update date including text: 2025-12-05T22:55:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-31 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-31 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2077",
    "number": "2077",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Helping Heroes Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:55:59Z",
    "updateDateIncludingText": "2025-12-05T22:55:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-31T18:06:34Z",
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
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "MI"
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
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "GA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2077ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2077\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Ms. Perez (for herself and Mr. James ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish the Veteran Family Resource Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Heroes Act .\n#### 2. Establishment of Veteran Family Resource Program\n##### (a) Establishment\n**(1) In general**\nThe Secretary of Veterans Affairs shall, acting through the Under Secretary for Health and the Office of Patient Care Services and Care Management and Social Work Services of the Veterans Health Administration, establish a program\u2014\n**(A)**\nto enhance the resilience, health, and well-being of veterans by addressing social determinants of health challenges experienced in their family units through person-centered clinical integrations, connections to benefits furnished by the Department of Veterans Affairs, and community resource engagement; and\n**(B)**\nto ensure veterans and their families have access to a continuum of services and resources needed to support wellness within their family units as they define the family units.\n**(2) Designation**\nThe program established pursuant to paragraph (1) shall be known as the Veteran Family Resource Program (in this section referred to as the Program ).\n##### (b) Family coordinators and staffing\n**(1) In general**\nThe Secretary shall carry out the Program by, not later than the date that is five years after the date of the enactment of this Act\u2014\n**(A)**\nappointing at least one family coordinator in each Veterans Integrated Service Network; and\n**(B)**\nensuring adequate staffing and resources to ensure family coordinators are able to carry out their functions and duties under the Program.\n**(2) Functions**\nThe functions of a family coordinator under paragraph (1) are as follows:\n**(A)**\nTo serve at medical centers of the Department as point persons who understand and have a good working knowledge of\u2014\n**(i)**\nall resources that families, caregivers, and survivors may be eligible for under provisions of law administered by the Secretary; and\n**(ii)**\ncommunity resources available to such families, caregivers, and survivors when they have needs that are not met by the resources described in clause (i).\n**(B)**\nTo help veterans, their families, their caregivers, and their survivors access and navigate the public and private resources described in subparagraph (A).\n**(3) Duties**\nEach family coordinator appointed under paragraph (1) shall, to the extent practicable\u2014\n**(A)**\nassess the needs of veterans and the family members of veterans using evidence-based strategies;\n**(B)**\nbuild positive relationships with veterans and such family members;\n**(C)**\nrefer veterans and such family members to local, State, Federal, and non-Department resources to support the overall health, well-being, and treatment goals of such veterans; and\n**(D)**\ndevelop and maintain a list of\u2014\n**(i)**\nsupportive services offered by the Department; and\n**(ii)**\nsupportive services offered by non-Department providers;\n##### (c) Goals and metrics\n**(1) Goals**\nThe goals of the Program shall be as follows:\n**(A)**\nTo connect veterans to family resources to increase their well-being and resiliency.\n**(B)**\nTo develop internal partnerships to improve health care furnished by the Department.\n**(C)**\nTo capture and maintain data to enhance understanding of process improvement opportunities and impact.\n**(D)**\nTo function as a community liaison to bolster existing partnerships and conduct due diligence to form new partnerships.\n**(2) Metrics**\nThe Secretary shall establish metrics for assessment of the Program, including metrics relating to the following:\n**(A)**\nDepartment referrals into the Program.\n**(B)**\nNon-Department referrals into the Program.\n**(C)**\nHealth factors.\n**(D)**\nVeteran and staff satisfaction.\n##### (d) Expansion of Program\nThe Secretary may expand the Program to additional medical centers of the Department or otherwise expand the Program to carry out the purposes specified in subsection (a)(1) as the Secretary determines appropriate.\n##### (e) Report to Congress\n**(1) In general**\nNot later than two years after the commencement of the Program, the Secretary shall submit to the appropriate committees of Congress a report on the progress of the Program.\n**(2) Contents**\nThe report required by paragraph (1) shall include\u2014\n**(A)**\nthe number of veterans and children who received supportive services under the Program;\n**(B)**\nthe demographic data of veterans and family members in receipt of supportive services under the Program, including\u2014\n**(i)**\nthe relationship to the veteran;\n**(ii)**\nage;\n**(iii)**\nrace;\n**(iv)**\nethnicity;\n**(v)**\ngender;\n**(vi)**\ndisability; and\n**(vii)**\nEnglish proficiency and whether a language other than English is spoken at home;\n**(C)**\na summary of the supportive services carried out under the Program and the costs to the Department of such supportive services; and\n**(D)**\nan assessment, measured by a survey of participants, of whether, and how, participation in the Program\u2014\n**(i)**\nresulted in positive outcomes for veterans and children; and\n**(ii)**\ncontributed to the overall health, well-being, and treatment goals of the veteran.\n**(3) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Veterans\u2019 Affairs and the Subcommittee on Military Construction, Veterans Affairs, and Related Agencies of the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Veterans\u2019 Affairs and the Subcommittee on Military Construction, Veterans Affairs, and Related Agencies of the Committee on Appropriations of the House of Representatives.\n##### (f) Supportive services defined\nIn this section, the term supportive services means services that address the social, emotional, and mental health, career-readiness, and other needs of children, including\u2014\n**(1)**\nwellness services, including mental, emotional, behavioral, and physical health;\n**(2)**\npeer-support programs for children; and\n**(3)**\nany other services or activities the Secretary considers appropriate to support the needs of children.\n#### 3. Survey of disabled veterans and their families\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, and not less frequently than once every five years thereafter as the Secretary of Veterans Affairs determines appropriate, the Secretary shall conduct a survey of disabled veterans and their families to identify and better understand the needs of such disabled veterans and their families.\n##### (b) Content\nThe survey required under subsection (a) shall include questions with respect to\u2014\n**(1)**\nthe types and quality of support disabled veterans receive for their children; and\n**(2)**\nthe unmet needs of such children.\n#### 4. Nondiscrimination\nThe following provisions of law shall apply to any program or activity that receives funds provided under this Act:\n**(1)**\nTitle IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ).\n**(2)**\nTitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n**(3)**\nSection 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ).\n**(4)**\nThe Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(5)**\nThe Age Discrimination Act of 1975 ( 42 U.S.C. 6101 et seq. ).\n**(6)**\nAny other Federal law prohibiting discrimination under an applicable program or activity receiving Federal financial assistance.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "701",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping Heroes Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-07-24T14:24:03Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-07-24T14:24:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:47:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2077",
          "measure-number": "2077",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2077v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Helping Heroes Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Veteran Family Resource Program to address social determinants of health challenges experienced in veterans\u2019 family units and ensure veterans and their families have access to services and resources to support wellness within the family units.</p><p>In implementing the program, the VA must (1) appoint at least one family coordinator in each Veterans Integrated Service Network (regional VA health care administrative areas), and (2) ensure adequate staffing and resources to ensure family coordinators are able to carry out their duties and functions. Under the bill, a family coordinator\u2019s function is generally to serve at a VA medical center as a point person regarding VA and community resources for veterans, their families, and caregivers and survivors of veterans.</p><p>The VA may expand the program to additional medical centers as appropriate.</p><p>Not later than one year after the date of enactment of this bill, and not less frequently than once every five years after, the VA must survey disabled veterans and their families to identify and better understand their needs.</p>"
        },
        "title": "Helping Heroes Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2077.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Heroes Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Veteran Family Resource Program to address social determinants of health challenges experienced in veterans\u2019 family units and ensure veterans and their families have access to services and resources to support wellness within the family units.</p><p>In implementing the program, the VA must (1) appoint at least one family coordinator in each Veterans Integrated Service Network (regional VA health care administrative areas), and (2) ensure adequate staffing and resources to ensure family coordinators are able to carry out their duties and functions. Under the bill, a family coordinator\u2019s function is generally to serve at a VA medical center as a point person regarding VA and community resources for veterans, their families, and caregivers and survivors of veterans.</p><p>The VA may expand the program to additional medical centers as appropriate.</p><p>Not later than one year after the date of enactment of this bill, and not less frequently than once every five years after, the VA must survey disabled veterans and their families to identify and better understand their needs.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr2077"
    },
    "title": "Helping Heroes Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Heroes Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Veteran Family Resource Program to address social determinants of health challenges experienced in veterans\u2019 family units and ensure veterans and their families have access to services and resources to support wellness within the family units.</p><p>In implementing the program, the VA must (1) appoint at least one family coordinator in each Veterans Integrated Service Network (regional VA health care administrative areas), and (2) ensure adequate staffing and resources to ensure family coordinators are able to carry out their duties and functions. Under the bill, a family coordinator\u2019s function is generally to serve at a VA medical center as a point person regarding VA and community resources for veterans, their families, and caregivers and survivors of veterans.</p><p>The VA may expand the program to additional medical centers as appropriate.</p><p>Not later than one year after the date of enactment of this bill, and not less frequently than once every five years after, the VA must survey disabled veterans and their families to identify and better understand their needs.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr2077"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2077ih.xml"
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
      "title": "Helping Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to establish the Veteran Family Resource Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:54Z"
    }
  ]
}
```
