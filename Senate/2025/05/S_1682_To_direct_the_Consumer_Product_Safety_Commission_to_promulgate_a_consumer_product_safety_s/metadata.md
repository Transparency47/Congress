# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1682?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1682
- Title: Alex Gate Safety Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1682
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-04-16T13:38:23Z
- Update date including text: 2026-04-16T13:38:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1682",
    "number": "1682",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Alex Gate Safety Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T13:38:23Z",
    "updateDateIncludingText": "2026-04-16T13:38:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
            "date": "2026-04-14T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-08T17:03:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1682is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1682\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Curtis (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Consumer Product Safety Commission to promulgate a consumer product safety standard for certain gates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Alex Gate Safety Act of 2025 .\n#### 2. Consumer product safety standard for covered gates\n##### (a) Standard required\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Commission shall promulgate, in accordance with section 553 of title 5, United States Code, a final consumer product safety standard for covered gates that includes the requirements described in paragraph (2).\n**(2) Requirements described**\nThe requirements described in this paragraph for a covered gate are the following:\n**(A)**\nThe covered gate meets the safety-related standards of ASTM F900\u201325, ASTM F1184\u201323e1, or ASTM F2200\u201324, as applicable to the relevant category of covered gate as of January 1, 2025, or any successor standard.\n**(B)**\nIf the covered gate has an operator or similar system, the gate meets the safety-related standards of ANSI/CAN/UL 325 as of January 1, 2025, or any successor standard.\n##### (b) CPSC determination of scope\nIn promulgating a consumer product safety standard under subsection (a), the Commission shall determine the types of covered gates that are subject to the standard and ensure that such covered gates are within the jurisdiction of the Commission.\n##### (c) Revision of voluntary standards\n**(1) Notice to the commission**\nIf an organization revises a voluntary standard that has been adopted, in whole or in part, as a consumer product safety standard under this section, the organization shall notify the Commission of the revision.\n**(2) Treatment of revision**\nThe revised voluntary standard shall be considered to be adopted by the Commission, effective on the date that is 180 days after the date on which the organization notifies the Commission of the revision (or such later date specified by the Commission in the Federal Register) unless, not later than 90 days after the date on which the organization notifies the Commission of the revision, the Commission notifies the organization that the Commission has determined that the revision does not improve the safety of the covered gates to which the standard applies and that the Commission is retaining the existing consumer product safety standard. Not later than 90 days before the date on which a revised voluntary standard is considered to be adopted by the Commission under this subsection, the Commission shall publish in the Federal Register notice that such revised voluntary standard will be considered to be so adopted on such date.\n##### (d) Future rulemaking\nAt any time after the promulgation of a consumer product safety standard under subsection (a), the Commission may initiate a rulemaking, in accordance with section 553 of title 5, United States Code, to modify such standard, if the Commission determines that a modification would further reduce the risk of injury associated with covered gates.\n##### (e) Treatment of standards\nAny consumer product safety standard promulgated under subsection (a) (including any modification of such standard under subsection (c)) or revised voluntary standard considered to be adopted by the Commission under subsection (c) shall be treated as a consumer product safety rule promulgated under section 9 of the Consumer Product Safety Act ( 15 U.S.C. 2058 ).\n#### 3. Education and awareness campaign\n##### (a) In general\nNot later than 2 years after the date of the enactment of this Act, the Commission shall undertake a national campaign to promote awareness and educate the public about the dangers associated with covered gates, including the dangers of detached or falling covered gates, and methods (including low-cost methods) to prevent covered gates from causing death or injury, including safety standards relating to covered gates and best practices for design, installation, inspection, maintenance, and improvement of covered gates.\n##### (b) Requirements\nIn carrying out the campaign required by subsection (a), the Commission shall employ, at a minimum, the following:\n**(1)**\nEducational materials designed for covered gate manufacturers, contractors, retailers, and service companies.\n**(2)**\nEducational materials designed for consumers, owners, and operators of covered gates.\n**(3)**\nEducational materials designed for building officials and local educational agencies to support the updating and enforcement of building codes for new and existing buildings with respect to the safety of covered gates.\n##### (c) Report to Congress\nNot later than 3 years after the date of the enactment of this Act, the Commission shall submit to Congress a report that contains a summary of actions taken by the Commission in the campaign required by subsection (a).\n#### 4. Definitions\nIn this Act:\n**(1) Building official**\nThe term building official means any State, Tribal, territorial, or local official who is responsible for proposing modifications to building codes, participating in adopting building codes, interpreting building code requirements, overseeing building code enforcement activities, or otherwise administering building codes.\n**(2) Commission**\nThe term Commission means the Consumer Product Safety Commission.\n**(3) Covered gate**\nThe term covered gate means\u2014\n**(A)**\nan automatic vehicular gate;\n**(B)**\na manual vehicular gate; and\n**(C)**\nany other gate that is more than 48 inches wide or 84 inches or greater in height.\n**(4) Local educational agency**\nThe term local educational agency has the meaning given such term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(5) Manufacturer**\nThe term manufacturer has the meaning given such term in section 3(a) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a) ).\n**(6) Positive stops**\nThe term positive stops means an immovable component that, by the placement of the component, physically impedes the motion of a covered gate.\n**(7) State**\nThe term State has the meaning given such term in section 3(a) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a) ).",
      "versionDate": "2025-05-08",
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
            "name": "Building construction",
            "updateDate": "2026-04-16T13:37:42Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-04-16T13:37:24Z"
          },
          {
            "name": "Housing industry and standards",
            "updateDate": "2026-04-16T13:38:23Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-04-16T13:37:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-06-09T14:44:03Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1682is.xml"
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
      "title": "Alex Gate Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Alex Gate Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Consumer Product Safety Commission to promulgate a consumer product safety standard for certain gates, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-22T02:18:32Z"
    }
  ]
}
```
