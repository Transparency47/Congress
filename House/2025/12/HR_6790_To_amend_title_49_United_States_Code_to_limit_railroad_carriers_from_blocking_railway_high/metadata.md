# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6790?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6790
- Title: D-BLOC Act
- Congress: 119
- Bill type: HR
- Bill number: 6790
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-02-03T09:05:31Z
- Update date including text: 2026-02-03T09:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6790",
    "number": "6790",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000587",
        "district": "29",
        "firstName": "Sylvia",
        "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
        "lastName": "Garcia",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "D-BLOC Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:31Z",
    "updateDateIncludingText": "2026-02-03T09:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:07:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:42:28Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "DC"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6790ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6790\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Garcia of Texas (for herself, Mr. Mrvan , Ms. Norton , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to limit railroad carriers from blocking railway-highway crossings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Don\u2019t BLock Our Communities Act or the D-BLOC Act .\n#### 2. Establishment of 10-minute time limit for blocking public highway-rail grade crossings\n##### (a) In general\nSubchapter II of chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Time limit for blocking public highway-rail grade crossing (a) Time limit A railroad carrier may not cause a blocked crossing incident that is longer than 10 minutes in duration, unless the blocked crossing incident is caused by\u2014 (1) a casualty or serious injury; (2) an accident; (3) a track obstruction; (4) actions necessary to comply with Federal rail safety laws, regulations, or orders issued thereunder unless the action to comply could reasonably occur at a different time or location; (5) actions necessary to adhere to section 24308; (6) a train fully contained within rail yard limits or fully contained in a rail siding; (7) an act of God; or (8) a derailment or a safety appliance equipment failure that prevents the train from advancing. (b) Investigation of frequently blocked crossings For any public highway-rail grade crossing that has had 3 or more blocked crossing incidents that exceed the time limit set forth in subsection (a) and are reported to the blocked crossing portal, and such incidents have occurred on at least 3 calendar days within a 30-day period, the Secretary shall\u2014 (1) provide an electronic notice of the number of reported blocked crossing incidents to the railroad carrier that owns the public highway-rail grade crossing; (2) investigate the causes of the blocked crossing incidents; and (3) investigate possible measures to reduce the frequency and duration of blocked crossing incidents at such grade crossing. (c) Recordkeeping (1) In general A railroad carrier shall, upon receiving a notice under subsection (b), maintain train location data records for the public highway-rail grade crossing that was the subject of the notice. (2) Contents of records The train location data records required under paragraph (1) shall include\u2014 (A) a list of all blocked crossing incidents at the public highway-rail grade crossing that is the subject of the report exceeding 10 minutes; (B) the cause of the blocked crossing incident (to the extent available); (C) train length; and (D) the estimated duration of each blocked crossing incident. (3) Consultation Beginning on the date on which a railroad carrier receives a notice under subsection (b), the Secretary may consult with the carrier for a period of 60 days to address concerns with blocked crossing incidents at the public highway-rail grade crossing that is the subject of the notice. (4) Expiration of data collection The requirement to maintain records under paragraph (1) shall cease with respect to a public highway-rail grade crossing noticed under subsection (b)(2) if there are no reports submitted to the blocked crossing portal for blocked crossing incidents reported to occur at such grade crossing during the previous 365 consecutive calendar days. (d) Civil penalties (1) In general The Secretary may issue civil penalties in accordance with section 21301 to railroad carriers for violations of subsection (a) occurring 60 days after the date of submission of a notice under subsection (b). (2) Release of records Upon the request of, and under requirements set by, the Secretary, railroad carriers shall provide the records maintained pursuant to subsection (c)(1) to the Administrator of the Federal Railroad Administration. (3) Alternate route exemption Civil penalties may not be issued for violations of subsection (a) that occur at a public highway-rail grade crossing if no alternate route created by a public highway-rail grade separation exists within a half mile by road of such public highway-rail grade crossing. (4) Grade separation project Civil penalties may not be issued for violations of subsection (a) if the violation occurs at a public highway-rail grade crossing for which there is a proposed grade separation project\u2014 (A) that has received written agreement from the relevant local authorities; and (B) for which rail carrier and project funding from all parties has been budgeted. (5) Considerations In determining civil penalties under this section, the Secretary shall consider increased penalties in a case in which a pattern of the blocked crossing incidents continue to cause delays to State or local emergency services. (e) Application to Amtrak and commuter railroads This section shall not apply to Amtrak or commuter authorities, including Amtrak and commuter authorities\u2019 operations run or dispatched by a Class I railroad. (f) Definitions In this section: (1) Blocked crossing portal The term blocked crossing portal means the national blocked crossing portal initiated by the Federal Railroad Administration in 2019 and required by section 22404 of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 22907 note). (2) Blocked crossing incident The term blocked crossing incident means a circumstance in which a train, locomotive, rail car, or other rail equipment is stopped in a manner that obstructs travel at a public highway-rail grade crossing. (3) Public highway-rail grade crossing The term public highway-rail grade crossing means a location within a State in which a public highway, road, or street, including associated sidewalks and pathways, crosses 1 or more railroad tracks at grade. .\n##### (b) Clerical amendment\nThe analysis for subchapter II of chapter 201 of title 49, United States Code, is amended by adding at the end the following new item:\n20172. Time limit for blocking public highway-rail grade crossing. .\n#### 3. Blocked crossing portal\n##### (a) Blocked crossing portal\nSection 22404 of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 22907 note) is amended\u2014\n**(1)**\nin subsection (a), by striking 3-year ;\n**(2)**\nby striking subsection (h);\n**(3)**\nby redesignating subsection (i) as subsection (h); and\n**(4)**\nby striking subsections (j) and (k) and inserting the following:\n(i) Rule of construction Nothing in this section may be construed to invalidate any authority of the Secretary with respect to blocked highway-rail grade crossings. .\n##### (b) Publication of blocked crossing information\nNot later than 60 days after the date of enactment of the D-BLOC Act, each Class I railroad carrier shall publish on the home page of the publicly-available website of the railroad carrier an active link to the blocked crossing portal initiated by the Federal Railroad Administration in 2019 and required by section 22404 of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 22907 note).\n#### 4. Railroad point of contact for blocked crossing matters\nSection 20152 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (C), by striking or at the end;\n**(ii)**\nby redesignating subparagraph (D) as subparagraph (E); and\n**(iii)**\nby inserting the following after subparagraph (C):\n(D) blocked crossing incident, as defined in section 20172; or ;\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nby striking paragraph (1)(C) or (D) and inserting subparagraph (C), (D), or (E) of paragraph (1) ; and\n**(ii)**\nby striking and at the end;\n**(C)**\nin paragraph (5), by striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(6) upon receiving a report of a blocked crossing pursuant to paragraph (1)(D), the railroad carrier shall, within 14 days of receipt of the report\u2014 (A) verify that the public highway-rail grade crossing, as defined in section 20172, was blocked for a period of at least 10 minutes; and (B) upon positive verification of the report, enter the report into the blocked crossing portal initiated by the Federal Railroad Administration in 2019 and required by section 22404 of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 22907 note); and (7) promptly inform the Secretary of any update to the number maintained under paragraph (1). ; and\n**(2)**\nby adding at the end the following:\n(c) Publication of telephone numbers The Secretary shall make any telephone number established under subsection (a) publicly available on the website of the Department of Transportation. .",
      "versionDate": "2025-12-17",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-22T15:16:08Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6790ih.xml"
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
      "title": "D-BLOC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "D-BLOC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t BLock Our Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to limit railroad carriers from blocking railway-highway crossings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:38Z"
    }
  ]
}
```
