# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/473
- Title: SHOW UP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 473
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-07-21T15:48:21Z
- Update date including text: 2025-07-21T15:48:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/473",
    "number": "473",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001108",
        "district": "1",
        "firstName": "James",
        "fullName": "Rep. Comer, James [R-KY-1]",
        "lastName": "Comer",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "SHOW UP Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T15:48:21Z",
    "updateDateIncludingText": "2025-07-21T15:48:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SC"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "VA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "CO"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr473ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 473\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Comer (for himself, Mr. Higgins of Louisiana , Mr. Timmons , Mr. Biggs of Arizona , Mr. Cloud , Ms. Foxx , Mr. Langworthy , Mr. Crane , Mr. Palmer , Mr. McGuire , Mr. Grothman , Mr. Fallon , Mr. Burlison , Mr. Sessions , Mr. Jack , Mr. Burchett , Ms. Boebert , Mr. Perry , and Ms. Greene of Georgia ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo restore in-person work at Federal agencies to not less than pre-pandemic levels, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Home Office Work\u2019s Unproductive Problems Act of 2025 or the SHOW UP Act of 2025 .\n#### 2. Reinstatement of pre-pandemic telework policies, practices, and levels for Executive agencies\nNot later than 30 days after the date of enactment of this Act, each agency shall adopt and apply telework policies, practices, and levels at the agency that are equivalent to, or otherwise permit no additional levels of telework than, those which were in effect on December 31, 2019, and may not expand any such policy, practice, or level until the date that an agency plan is submitted to Congress with a certification by the Director of the Office of Personnel Management under section 3.\n#### 3. Study, plan, and certification regarding Executive agency telework policies, practices, and levels for Executive agencies\n##### (a) In general\nNot later than 6 months after the date of enactment of this Act, the head of each agency, in consultation with the Director, shall submit to Congress\u2014\n**(1)**\na study on the impacts on the agency and its mission of expanding telework by its employees during the SARS\u2013CoV\u20132 pandemic that commenced in 2019 and maintaining such expanded telework thereafter, including an analysis of\u2014\n**(A)**\nany adverse impacts of that expansion on the agency\u2019s performance of its mission, including the performance of customer service by the agency;\n**(B)**\nany costs to the agency during that expansion attributable to\u2014\n**(i)**\nowning, leasing, or maintaining underutilized real property; or\n**(ii)**\npaying higher rates of locality pay to teleworking employees as a result of incorrectly classifying such employees as teleworkers rather than remote workers;\n**(C)**\nany degree to which the agency failed during that expansion to provide teleworking employees with secure network capacity, communications tools, necessary and secure access to appropriate agency data assets and Federal records, and equipment sufficient to enable each such employee to be fully productive;\n**(D)**\nany degree to which that expansion facilitated dispersal of the agency workforce around the Nation; and\n**(E)**\nany other impacts of that expansion that the agency or the Director considers appropriate;\n**(2)**\nany agency plan to expand telework policies, practices, or levels beyond those in place as a result of section 2; and\n**(3)**\na certification by the Director that such plan will\u2014\n**(A)**\nhave a substantial positive effect on\u2014\n**(i)**\nthe performance of the agency\u2019s mission, including the performance of customer service;\n**(ii)**\nincreasing the level of dispersal of agency personnel throughout the Nation; and\n**(iii)**\nthe reversal of any adverse impact set forth pursuant to paragraph (1)(D);\n**(B)**\nsubstantially lower the agency\u2019s costs of owning, leasing, or maintaining real property;\n**(C)**\nsubstantially lower the agency\u2019s costs attributable to paying locality pay to agency personnel working from locations outside the pay locality of their position\u2019s official worksite; and\n**(D)**\nensure that teleworking employees will be provided with secure network capacity, communications tools, necessary and secure access to appropriate agency data assets and Federal records, and equipment sufficient to enable each such employee to be fully productive, without substantially increasing the agency\u2019s overall costs for secure network capacity, communications tools, and equipment.\n##### (b) Limitation\n**(1) In general**\nAn agency may not implement the plan submitted under subsection (a)(2) unless a certification by the Director was issued under subsection (a)(3).\n**(2) Subsequent plans**\nIn the event an initial agency plan submitted under subsection (a)(2) fails to receive such certification, the agency may submit to the Director subsequent plans until such certification is received, and submit such plan and certification to Congress.\n##### (c) Definitions\nIn this Act\u2014\n**(1)**\nthe term agency has the meaning given the term Executive agency in section 105 of title 5, United States Code, except that such term does not include the Government Accountability Office;\n**(2)**\nthe term Director means the Director of the Office of Personnel Management;\n**(3)**\nthe term locality pay means locality pay provided for under section 5304 or 5304a of such title; and\n**(4)**\nthe terms telework and teleworking have the meaning given those terms in section 6501 of such title, and include remote work.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in House"
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Commuting",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-07T15:21:42Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-07T15:21:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:09:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr473",
          "measure-number": "473",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr473v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stopping Home Office Work's Unproductive Problems Act of 2025 or the SHOW UP Act of 2025</strong></p><p>This bill requires each executive agency (other than the Government Accountability Office) to establish as its current policies the telework policies that were in place on December 31, 2019. Agencies may not implement expanded telework policies unless the Office of Personnel Management certifies that such policies, among other requirements, will have a positive effect on the agency's mission and operational costs.</p>"
        },
        "title": "SHOW UP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr473.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Home Office Work's Unproductive Problems Act of 2025 or the SHOW UP Act of 2025</strong></p><p>This bill requires each executive agency (other than the Government Accountability Office) to establish as its current policies the telework policies that were in place on December 31, 2019. Agencies may not implement expanded telework policies unless the Office of Personnel Management certifies that such policies, among other requirements, will have a positive effect on the agency's mission and operational costs.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr473"
    },
    "title": "SHOW UP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Home Office Work's Unproductive Problems Act of 2025 or the SHOW UP Act of 2025</strong></p><p>This bill requires each executive agency (other than the Government Accountability Office) to establish as its current policies the telework policies that were in place on December 31, 2019. Agencies may not implement expanded telework policies unless the Office of Personnel Management certifies that such policies, among other requirements, will have a positive effect on the agency's mission and operational costs.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr473"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr473ih.xml"
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
      "title": "SHOW UP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHOW UP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Home Office Work\u2019s Unproductive Problems Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restore in-person work at Federal agencies to not less than pre-pandemic levels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T11:03:23Z"
    }
  ]
}
```
