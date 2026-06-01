# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/785?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/785
- Title: Expressing support for designation of the week of October 4, 2025, through October 10, 2025, as "World Space Week".
- Congress: 119
- Bill type: HRES
- Bill number: 785
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2026-03-31T15:44:32Z
- Update date including text: 2026-03-31T15:44:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Submitted in House
- 2025-10-03 - IntroReferral: Submitted in House
- Latest action: 2025-10-03: Submitted in House

## Actions

- 2025-10-03 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Submitted in House
- 2025-10-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/785",
    "number": "785",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Expressing support for designation of the week of October 4, 2025, through October 10, 2025, as \"World Space Week\".",
    "type": "HRES",
    "updateDate": "2026-03-31T15:44:32Z",
    "updateDateIncludingText": "2026-03-31T15:44:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-10-03T19:31:25Z",
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
          "date": "2025-10-03T19:31:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres785ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 785\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mrs. Dingell (for herself, Mr. Smith of Washington , Mr. Whitesides , Mr. Bacon , and Ms. Houlahan ) submitted the following resolution; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for designation of the week of October 4, 2025, through October 10, 2025, as World Space Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of World Space Week ;\n**(2)**\nexpresses strong support for the goals and ideals of World Space Week and its aims to increase understanding of, and interest in, space sciences and technology at the local, State, national, and international levels;\n**(3)**\nrecognizes the importance of international cooperation in space missions and outreach and education in furthering knowledge and discovery of new worlds and development of sustainable living solutions for space;\n**(4)**\nrecognizes the importance of education and public outreach efforts to ensure that the United States public gains a better understanding and appreciation for the impact of the space science and technology on their daily lives;\n**(5)**\nencourages K\u201312 students to participate in local, State, and national events in connection with World Space Week and to get involved in the celebration by exploring academic applications of and opportunities in space science and technology; and\n**(6)**\nencourages the people of the United States to observe World Space Week with appropriate activities to gain a better understanding and appreciation for the space sciences and technology and their contributions to society.",
      "versionDate": "2025-10-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-15T16:52:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119hres785",
          "measure-number": "785",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres785v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of World Space Week.</p>"
        },
        "title": "Expressing support for designation of the week of October 4, 2025, through October 10, 2025, as \"World Space Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres785.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of World Space Week.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hres785"
    },
    "title": "Expressing support for designation of the week of October 4, 2025, through October 10, 2025, as \"World Space Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of World Space Week.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hres785"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres785ih.xml"
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
      "title": "Expressing support for designation of the week of October 4, 2025, through October 10, 2025, as \"World Space Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:24Z"
    },
    {
      "title": "Expressing support for designation of the week of October 4, 2025, through October 10, 2025, as \"World Space Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T08:05:25Z"
    }
  ]
}
```
