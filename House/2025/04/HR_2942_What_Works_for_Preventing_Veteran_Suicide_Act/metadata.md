# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2942?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2942
- Title: What Works for Preventing Veteran Suicide Act
- Congress: 119
- Bill type: HR
- Bill number: 2942
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-12-12T09:07:33Z
- Update date including text: 2025-12-12T09:07:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2942",
    "number": "2942",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000601",
        "district": "1",
        "firstName": "Greg",
        "fullName": "Rep. Landsman, Greg [D-OH-1]",
        "lastName": "Landsman",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "What Works for Preventing Veteran Suicide Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:33Z",
    "updateDateIncludingText": "2025-12-12T09:07:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
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
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:34:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-12T15:36:28Z",
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
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "WI"
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
      "sponsorshipDate": "2025-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2942ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2942\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Landsman (for himself, Mr. Luttrell , Mr. Deluzio , and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish standard practices for a grant or pilot program administered by the Secretary of Veterans Affairs through the Veterans Health Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the What Works for Preventing Veteran Suicide Act .\n#### 2. Establishment of standard practices for a grant or pilot program administered by the Secretary of Veterans Affairs through the Veterans Health Administration\n##### (a) Establishment\nSection 527 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by inserting (1) before The Secretary, ;\n**(2)**\nby redesignating subsections (b) and (c) as paragraphs (2) and (3), respectively; and\n**(3)**\nby adding at the end the following new subsection (b):\n(b) The Secretary shall prescribe regulations that establish standard practices that, unless otherwise prohibited by law, shall apply to a grant program or pilot program relating to suicide prevention or mental health carried out through the Veterans Health Administration. Such practices shall include the following: (1) The establishment of clear and measurable objectives. (2) The development of a methodology and plan to\u2014 (A) determine information necessary to evaluate the program; (B) identify sources, methods, timing, and frequency for collecting of such information; (C) determine how such information will be analyzed to evaluate the program\u2019s implementation and performance and to identify lessons learned; and (D) identify criteria or standards for informing decisions about whether the program should be expanded, extended, or made permanent. (3) The communication of program objectives, assessment methodology, and evaluation plan with entities determined relevant to the program by the Secretary\u2014 (A) during the development of the program; (B) at least 30 days prior to the beginning of the program; and (C) throughout the term of the program. (4) At the conclusion of the program, the performance of an evaluation of the program\u2014 (A) to validate lessons learned; and (B) to assess the generalizability of the program. (5) The sharing of program results and best practices with entities determined relevant to the program by the Secretary. .\n##### (b) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall prescribe regulations under section 527(b) of such title, as amended by subsection (a).\n##### (c) Applicability\nThe standard practices prescribed in such regulations shall apply to a grant or pilot program without regard to when such program was established.",
      "versionDate": "2025-04-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T20:12:33Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2942ih.xml"
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
      "title": "What Works for Preventing Veteran Suicide Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "What Works for Preventing Veteran Suicide Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to establish standard practices for a grant or pilot program administered by the Secretary of Veterans Affairs through the Veterans Health Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:31Z"
    }
  ]
}
```
