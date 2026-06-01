# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/1?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/1
- Title: A joint resolution proposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve.
- Congress: 119
- Bill type: SJRES
- Bill number: 1
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2025-12-05T21:25:37Z
- Update date including text: 2025-12-05T21:25:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in Senate
- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-07: Introduced in Senate

## Actions

- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/1",
    "number": "1",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A joint resolution proposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve.",
    "type": "SJRES",
    "updateDate": "2025-12-05T21:25:37Z",
    "updateDateIncludingText": "2025-12-05T21:25:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:14:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "UT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "MO"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "KY"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "IN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "MT"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "WY"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "AL"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "KS"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "IN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "OH"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "MT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "NC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "LA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "SC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres1is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 1\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Cruz (for himself, Mr. Lee , Mr. Scott of Florida , Mr. Schmitt , Mr. Paul , Mr. Young , Mr. Daines , Mr. Hagerty , Ms. Lummis , Mrs. Britt , Mr. Marshall , and Mr. Banks ) introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission by the Congress:\n\u2014 1. No person who has served 3 terms as a Representative shall be eligible for election to the House of Representatives. For purposes of this section, the election of a person to fill a vacancy in the House of Representatives shall be included as 1 term in determining the number of terms that such person has served as a Representative if the person fills the vacancy for more than 1 year. 2. No person who has served 2 terms as a Senator shall be eligible for election or appointment to the Senate. For purposes of this section, the election or appointment of a person to fill a vacancy in the Senate shall be included as 1 term in determining the number of terms that such person has served as a Senator if the person fills the vacancy for more than 3 years. 3. No term beginning before the date of the ratification of this article shall be taken into account in determining eligibility for election or appointment under this article. .",
      "versionDate": "2025-01-07",
      "versionType": "IS"
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
        "actionDate": "2025-01-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "12",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
      "type": "HJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-08",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution proposing amendments to the Constitution of the United States relative to the line item veto, a limitation on the number of terms that a Member of Congress may serve, and requiring a vote of two-thirds of the membership of both Houses of Congress on any legislation raising or imposing new taxes or fees.",
      "type": "SJRES"
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
            "name": "Congressional elections",
            "updateDate": "2025-01-15T18:44:06Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:44:06Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:44:06Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-15T18:44:06Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-15T18:44:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-13T13:02:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119sjres1",
          "measure-number": "1",
          "measure-type": "sjres",
          "orig-publish-date": "2025-01-07",
          "originChamber": "SENATE",
          "update-date": "2025-01-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres1v00",
            "update-date": "2025-01-31"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution proposes an amendment to the Constitution establishing term limits for individuals serving in the Senate and the House of Representatives.</p><p>The proposed amendment makes an individual who has served two terms in the Senate ineligible for appointment or election to the Senate and an individual who has served three terms as a Member of the House of Representatives ineligible for election to the House of Representatives.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>"
        },
        "title": "A joint resolution proposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres1.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution proposes an amendment to the Constitution establishing term limits for individuals serving in the Senate and the House of Representatives.</p><p>The proposed amendment makes an individual who has served two terms in the Senate ineligible for appointment or election to the Senate and an individual who has served three terms as a Member of the House of Representatives ineligible for election to the House of Representatives.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-31",
      "versionCode": "id119sjres1"
    },
    "title": "A joint resolution proposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution proposes an amendment to the Constitution establishing term limits for individuals serving in the Senate and the House of Representatives.</p><p>The proposed amendment makes an individual who has served two terms in the Senate ineligible for appointment or election to the Senate and an individual who has served three terms as a Member of the House of Representatives ineligible for election to the House of Representatives.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-31",
      "versionCode": "id119sjres1"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres1is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution proposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-09T03:03:34Z"
    },
    {
      "title": "A joint resolution proposing an amendment to the Constitution of the United States relative to limiting the number of terms that a Member of Congress may serve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T11:56:14Z"
    }
  ]
}
```
