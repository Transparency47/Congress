# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/701?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/701
- Title: Helping Heroes Act
- Congress: 119
- Bill type: S
- Bill number: 701
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:55:44Z
- Update date including text: 2025-12-05T22:55:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/701",
    "number": "701",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Helping Heroes Act",
    "type": "S",
    "updateDate": "2025-12-05T22:55:44Z",
    "updateDateIncludingText": "2025-12-05T22:55:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
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
        "item": {
          "date": "2025-02-25T15:24:59Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CT"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AK"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-25",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "VT"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NV"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s701is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 701\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mrs. Murray (for herself, Mr. Boozman , Mr. Blumenthal , Ms. Murkowski , Mr. Sanders , Mr. Booker , Mr. Schiff , Mr. Durbin , Mr. Kaine , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish the Veteran Family Resource Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Heroes Act .\n#### 2. Establishment of Veteran Family Resource Program\n##### (a) Establishment\n**(1) In general**\nThe Secretary of Veterans Affairs shall, acting through the Under Secretary for Health and the Office of Patient Care Services and Care Management and Social Work Services of the Veterans Health Administration, establish a program\u2014\n**(A)**\nto enhance the resilience, health, and well-being of veterans by addressing social determinants of health challenges experienced in their family units through person-centered clinical integrations, connections to benefits furnished by the Department of Veterans Affairs, and community resource engagement; and\n**(B)**\nto ensure veterans and their families have access to a continuum of services and resources needed to support wellness within their family units as they define the family units.\n**(2) Designation**\nThe program established pursuant to paragraph (1) shall be known as the Veteran Family Resource Program (in this section referred to as the Program ).\n##### (b) Family coordinators and staffing\n**(1) In general**\nThe Secretary shall carry out the Program by, not later than the date that is five years after the date of the enactment of this Act\u2014\n**(A)**\nappointing at least one family coordinator in each Veterans Integrated Service Network; and\n**(B)**\nensuring adequate staffing and resources to ensure family coordinators are able to carry out their functions and duties under the Program.\n**(2) Functions**\nThe functions of a family coordinator under paragraph (1) are as follows:\n**(A)**\nTo serve at medical centers of the Department as point persons who understand and have a good working knowledge of\u2014\n**(i)**\nall resources that families, caregivers, and survivors may be eligible for under provisions of law administered by the Secretary; and\n**(ii)**\ncommunity resources available to such families, caregivers, and survivors when they have needs that are not met by the resources described in clause (i).\n**(B)**\nTo help veterans, their families, their caregivers, and their survivors access and navigate the public and private resources described in subparagraph (A).\n**(3) Duties**\nEach family coordinator appointed under paragraph (1) shall, to the extent practicable\u2014\n**(A)**\nassess the needs of veterans and the family members of veterans using evidence-based strategies;\n**(B)**\nbuild positive relationships with veterans and such family members;\n**(C)**\nrefer veterans and such family members to local, State, Federal, and non-Department resources to support the overall health, well-being, and treatment goals of such veterans; and\n**(D)**\ndevelop and maintain a list of\u2014\n**(i)**\nsupportive services offered by the Department; and\n**(ii)**\nsupportive services offered by non-Department providers;\n##### (c) Goals and metrics\n**(1) Goals**\nThe goals of the Program shall be as follows:\n**(A)**\nTo connect veterans to family resources to increase their well-being and resiliency.\n**(B)**\nTo develop internal partnerships to improve health care furnished by the Department.\n**(C)**\nTo capture and maintain data to enhance understanding of process improvement opportunities and impact.\n**(D)**\nTo function as a community liaison to bolster existing partnerships and conduct due diligence to form new partnerships.\n**(2) Metrics**\nThe Secretary shall establish metrics for assessment of the Program, including metrics relating to the following:\n**(A)**\nDepartment referrals into the Program.\n**(B)**\nNon-Department referrals into the Program.\n**(C)**\nHealth factors.\n**(D)**\nVeteran and staff satisfaction.\n##### (d) Expansion of Program\nThe Secretary may expand the Program to additional medical centers of the Department or otherwise expand the Program to carry out the purposes specified in subsection (a)(1) as the Secretary determines appropriate.\n##### (e) Report to Congress\n**(1) In general**\nNot later than two years after the commencement of the Program, the Secretary shall submit to the appropriate committees of Congress a report on the progress of the Program.\n**(2) Contents**\nThe report required by paragraph (1) shall include\u2014\n**(A)**\nthe number of veterans and children who received supportive services under the Program;\n**(B)**\nthe demographic data of veterans and family members in receipt of supportive services under the Program, including\u2014\n**(i)**\nthe relationship to the veteran;\n**(ii)**\nage;\n**(iii)**\nrace;\n**(iv)**\nethnicity;\n**(v)**\ngender;\n**(vi)**\ndisability; and\n**(vii)**\nEnglish proficiency and whether a language other than English is spoken at home;\n**(C)**\na summary of the supportive services carried out under the Program and the costs to the Department of such supportive services; and\n**(D)**\nan assessment, measured by a survey of participants, of whether, and how, participation in the Program\u2014\n**(i)**\nresulted in positive outcomes for veterans and children; and\n**(ii)**\ncontributed to the overall health, well-being, and treatment goals of the veteran.\n**(3) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Veterans\u2019 Affairs and the Subcommittee on Military Construction, Veterans Affairs, and Related Agencies of the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Veterans\u2019 Affairs and the Subcommittee on Military Construction, Veterans Affairs, and Related Agencies of the Committee on Appropriations of the House of Representatives.\n##### (f) Supportive services defined\nIn this section, the term supportive services means services that address the social, emotional, and mental health, career-readiness, and other needs of children, including\u2014\n**(1)**\nwellness services, including mental, emotional, behavioral, and physical health;\n**(2)**\npeer-support programs for children; and\n**(3)**\nany other services or activities the Secretary considers appropriate to support the needs of children.\n#### 3. Survey of disabled veterans and their families\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, and not less frequently than once every five years thereafter as the Secretary of Veterans Affairs determines appropriate, the Secretary shall conduct a survey of disabled veterans and their families to identify and better understand the needs of such disabled veterans and their families.\n##### (b) Content\nThe survey required under subsection (a) shall include questions with respect to\u2014\n**(1)**\nthe types and quality of support disabled veterans receive for their children; and\n**(2)**\nthe unmet needs of such children.\n#### 4. Nondiscrimination\nThe following provisions of law shall apply to any program or activity that receives funds provided under this Act:\n**(1)**\nTitle IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ).\n**(2)**\nTitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n**(3)**\nSection 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ).\n**(4)**\nThe Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(5)**\nThe Age Discrimination Act of 1975 ( 42 U.S.C. 6101 et seq. ).\n**(6)**\nAny other Federal law prohibiting discrimination under an applicable program or activity receiving Federal financial assistance.",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "2077",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping Heroes Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-24T14:23:48Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-07-24T14:23:32Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-07-24T14:23:21Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-07-24T14:23:13Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-24T14:23:37Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-24T14:23:26Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-24T14:23:52Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-07-24T14:23:43Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-07-24T14:23:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T19:51:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119s701",
          "measure-number": "701",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s701v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Helping Heroes Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Veteran Family Resource Program to address social determinants of health challenges experienced in veterans\u2019 family units and ensure veterans and their families have access to services and resources to support wellness within the family units.</p><p>In implementing the program, the VA must (1) appoint at least one family coordinator in each Veterans Integrated Service Network (regional VA health care administrative areas), and (2) ensure adequate staffing and resources to ensure family coordinators are able to carry out their duties and functions. Under the bill, a family coordinator\u2019s function is generally to serve at a VA medical center as a point person regarding VA and community resources for veterans, their families, and caregivers and survivors of veterans.</p><p>The VA may expand the program to additional medical centers as appropriate.</p><p>Not later than one year after the date of enactment of this bill, and not less frequently than once every five years after, the VA must survey disabled veterans and their families to identify and better understand their needs.</p>"
        },
        "title": "Helping Heroes Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s701.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Helping Heroes Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Veteran Family Resource Program to address social determinants of health challenges experienced in veterans\u2019 family units and ensure veterans and their families have access to services and resources to support wellness within the family units.</p><p>In implementing the program, the VA must (1) appoint at least one family coordinator in each Veterans Integrated Service Network (regional VA health care administrative areas), and (2) ensure adequate staffing and resources to ensure family coordinators are able to carry out their duties and functions. Under the bill, a family coordinator\u2019s function is generally to serve at a VA medical center as a point person regarding VA and community resources for veterans, their families, and caregivers and survivors of veterans.</p><p>The VA may expand the program to additional medical centers as appropriate.</p><p>Not later than one year after the date of enactment of this bill, and not less frequently than once every five years after, the VA must survey disabled veterans and their families to identify and better understand their needs.</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s701"
    },
    "title": "Helping Heroes Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Helping Heroes Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish the Veteran Family Resource Program to address social determinants of health challenges experienced in veterans\u2019 family units and ensure veterans and their families have access to services and resources to support wellness within the family units.</p><p>In implementing the program, the VA must (1) appoint at least one family coordinator in each Veterans Integrated Service Network (regional VA health care administrative areas), and (2) ensure adequate staffing and resources to ensure family coordinators are able to carry out their duties and functions. Under the bill, a family coordinator\u2019s function is generally to serve at a VA medical center as a point person regarding VA and community resources for veterans, their families, and caregivers and survivors of veterans.</p><p>The VA may expand the program to additional medical centers as appropriate.</p><p>Not later than one year after the date of enactment of this bill, and not less frequently than once every five years after, the VA must survey disabled veterans and their families to identify and better understand their needs.</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s701"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s701is.xml"
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
      "title": "Helping Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T11:03:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to establish the Veteran Family Resource Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:09Z"
    }
  ]
}
```
