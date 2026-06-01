# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/19?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/19
- Title: To acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home.
- Congress: 119
- Bill type: HJRES
- Bill number: 19
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-02-27T23:41:17Z
- Update date including text: 2026-02-27T23:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/19",
    "number": "19",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home.",
    "type": "HJRES",
    "updateDate": "2026-02-27T23:41:17Z",
    "updateDateIncludingText": "2026-02-27T23:41:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-15T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MT"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "AZ"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "OH"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001195",
      "district": "8",
      "firstName": "Jason",
      "fullName": "Rep. Smith, Jason [R-MO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MO"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres19ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 19\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Crenshaw (for himself, Mr. Zinke , Mr. Fitzpatrick , Mr. Valadao , Mrs. Cammack , Mr. Newhouse , Mr. Moolenaar , Mr. Ciscomani , Ms. De La Cruz , Mr. Carey , and Mr. Babin ) submitted the following joint resolution; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nJOINT RESOLUTION\nTo acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home.\nThat the United States, acting through Congress\u2014\n**(1)**\nrecognizes the extraordinary sacrifice of veterans of the Vietnam war and commends them for their unwavering and courageous sacrifice to our Nation;\n**(2)**\nurges the President of the United States to formally acknowledge the widespread mistreatment of veterans of the Vietnam war as part of the ongoing Vietnam War Commemoration;\n**(3)**\non behalf of the American people, issues the long-overdue formal apology to veterans of the Vietnam war and their families for the mistreatment they endured during and after the war; and\n**(4)**\nexpresses urgent support for increased education in our Nation\u2019s schools to better reflect the courage and sacrifice of veterans of the Vietnam war and the lack of support back home.",
      "versionDate": "2025-01-15",
      "versionType": "IH"
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
            "name": "Asia",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-01-22T14:49:12Z"
          },
          {
            "name": "Vietnam",
            "updateDate": "2025-01-22T14:49:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-01-21T12:43:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hjres19",
          "measure-number": "19",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres19v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution recognizes the sacrifice of veterans of the Vietnam War and commends them for their sacrifice to the United States. The joint resolution also urges the President to formally acknowledge the widespread mistreatment of such veterans as part of the ongoing Vietnam War Commemoration and issue a formal apology to the veterans and their families. Additionally, the joint resolution expresses urgent support for increased education to better reflect the sacrifice and treatment of Vietnam veterans.</p>"
        },
        "title": "To acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres19.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution recognizes the sacrifice of veterans of the Vietnam War and commends them for their sacrifice to the United States. The joint resolution also urges the President to formally acknowledge the widespread mistreatment of such veterans as part of the ongoing Vietnam War Commemoration and issue a formal apology to the veterans and their families. Additionally, the joint resolution expresses urgent support for increased education to better reflect the sacrifice and treatment of Vietnam veterans.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hjres19"
    },
    "title": "To acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home."
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution recognizes the sacrifice of veterans of the Vietnam War and commends them for their sacrifice to the United States. The joint resolution also urges the President to formally acknowledge the widespread mistreatment of such veterans as part of the ongoing Vietnam War Commemoration and issue a formal apology to the veterans and their families. Additionally, the joint resolution expresses urgent support for increased education to better reflect the sacrifice and treatment of Vietnam veterans.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hjres19"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres19ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-16T09:18:15Z"
    },
    {
      "title": "To acknowledge the courage and sacrifice of veterans of the Vietnam war and formally apologize for the treatment they received upon returning home.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-16T09:05:18Z"
    }
  ]
}
```
