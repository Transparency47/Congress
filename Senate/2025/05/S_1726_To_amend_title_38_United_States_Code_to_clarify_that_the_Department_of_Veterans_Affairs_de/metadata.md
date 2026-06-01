# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1726?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1726
- Title: ASSIST Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1726
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1726",
    "number": "1726",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "ASSIST Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
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
      "actionDate": "2025-05-13",
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
      "actionDate": "2025-05-13",
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
            "date": "2026-03-18T20:00:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-13T16:35:44Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-13T16:35:44Z",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NH"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "SD"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1726is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1726\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Tuberville introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to clarify that the Department of Veterans Affairs definition of medical services includes medically necessary automobile adaptations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Automotive Support Services to Improve Safe Transportation Act of 2025 or the ASSIST Act of 2025 .\n#### 2. Clarification regarding inclusion of medically necessary automobile adaptations in Department of Veterans Affairs definition of medical services\nSection 1701(6)(I) of title 38, United States Code, is amended to read as follows:\n(I) The provision of any medically necessary automobile adaptations for driver or passenger use, including\u2014 (i) ramp and kneeling systems; (ii) raised doors or lowered floors; (iii) raised roofs; (iv) air conditioning; (v) occupied and unoccupied mobility lifts; (vi) ingress or egress accessibility modifications; (vii) wheelchair tiedowns; and (viii) adapted seating. .\n#### 3. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking November 30, 2031 and inserting September 30, 2032 .",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-05-20",
        "text": "Received in the Senate and Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "1364",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Automotive Support Services to Improve Safe Transportation Act of 2025",
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
            "name": "Disability and health-based discrimination",
            "updateDate": "2026-04-06T19:39:20Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-04-06T19:39:25Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-04-06T19:39:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:50:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
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
          "measure-id": "id119s1726",
          "measure-number": "1726",
          "measure-type": "s",
          "orig-publish-date": "2025-05-13",
          "originChamber": "SENATE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1726v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Automotive Support Services to Improve Safe Transportation Act of 2025 or the ASSIST Act of 2025</strong></p><p>This bill expands the definition of <em>medical services</em> for purposes of veterans\u2019 benefits to include additional medically necessary automobile\u00a0adaptations. Under the bill, the Department of Veterans Affairs may provide funding for the following medically necessary automobile adaptations for driver or passenger use:\u00a0ramp and kneeling systems, lowered floors, occupied and unoccupied mobility lifts, ingress or egress accessibility modifications, and adapted seating.\u00a0</p><p>The bill also extends the limitation on pension amounts for certain hospitalized or institutionalized veterans through September 30, 2032.</p>"
        },
        "title": "ASSIST Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1726.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Automotive Support Services to Improve Safe Transportation Act of 2025 or the ASSIST Act of 2025</strong></p><p>This bill expands the definition of <em>medical services</em> for purposes of veterans\u2019 benefits to include additional medically necessary automobile\u00a0adaptations. Under the bill, the Department of Veterans Affairs may provide funding for the following medically necessary automobile adaptations for driver or passenger use:\u00a0ramp and kneeling systems, lowered floors, occupied and unoccupied mobility lifts, ingress or egress accessibility modifications, and adapted seating.\u00a0</p><p>The bill also extends the limitation on pension amounts for certain hospitalized or institutionalized veterans through September 30, 2032.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119s1726"
    },
    "title": "ASSIST Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Automotive Support Services to Improve Safe Transportation Act of 2025 or the ASSIST Act of 2025</strong></p><p>This bill expands the definition of <em>medical services</em> for purposes of veterans\u2019 benefits to include additional medically necessary automobile\u00a0adaptations. Under the bill, the Department of Veterans Affairs may provide funding for the following medically necessary automobile adaptations for driver or passenger use:\u00a0ramp and kneeling systems, lowered floors, occupied and unoccupied mobility lifts, ingress or egress accessibility modifications, and adapted seating.\u00a0</p><p>The bill also extends the limitation on pension amounts for certain hospitalized or institutionalized veterans through September 30, 2032.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119s1726"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1726is.xml"
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
      "title": "ASSIST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ASSIST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Automotive Support Services to Improve Safe Transportation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to clarify that the Department of Veterans Affairs definition of \"medical services\" includes medically necessary automobile adaptations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:18:29Z"
    }
  ]
}
```
