# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/832?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/832
- Title: EPIC Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 832
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2026-02-13T20:59:51Z
- Update date including text: 2026-02-13T20:59:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/832",
    "number": "832",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "EPIC Act of 2025",
    "type": "S",
    "updateDate": "2026-02-13T20:59:51Z",
    "updateDateIncludingText": "2026-02-13T20:59:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T17:23:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "MT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "OK"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "UT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "KS"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s832is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 832\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Tillis (for himself, Mr. Budd , Mrs. Blackburn , Mr. Daines , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to equalize the negotiation period between small-molecule and biologic candidates under the Drug Price Negotiation Program.\n#### 1. Short title\nThis Act may be cited as the Ensuring Pathways to Innovative Cures Act of 2025 or the EPIC Act of 2025 .\n#### 2. Equalizing the negotiation period between small-molecule and biologic candidates under the Drug Price Negotiation Program\nSection 1192(e)(1)(A)(ii) of the Social Security Act ( 42 U.S.C. 1320f\u20131(e)(1)(A)(ii) ) is amended\u2014\n**(1)**\nby striking year, at least 7 and inserting \u201cyear\u2014\n(I) for initial price applicability years 2026 and 2027, at least 7 ; and\n**(2)**\nby adding at the end the following:\n(II) for initial price applicability year 2028 and each subsequent initial price applicability year, at least 11 years will have elapsed since the date of such approval; and .",
      "versionDate": "2025-03-04",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-27T13:58:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119s832",
          "measure-number": "832",
          "measure-type": "s",
          "orig-publish-date": "2025-03-04",
          "originChamber": "SENATE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s832v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ensuring Pathways to Innovative Cures Act of 2025 or the EPIC Act of 2025</strong></p><p>This bill lengthens the amount of time for which drug products must have market approval in order for the products to qualify for negotiation under the Medicare Drug Price Negotiation Program.</p><p>The Medicare Drug Price Negotiation Program requires the Centers for Medicare & Medicaid Services to negotiate the prices of certain prescription drugs under Medicare beginning in 2026. Among other requirements, drugs must have had market approval for at least 7 years (for drug products) or 11 years (for biologics) to qualify for negotiation.\u00a0</p><p>The bill modifies these provisions so as to require drug products to also have had at least 11 years of market approval in order to qualify for negotiation beginning in 2028.</p>"
        },
        "title": "EPIC Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s832.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Pathways to Innovative Cures Act of 2025 or the EPIC Act of 2025</strong></p><p>This bill lengthens the amount of time for which drug products must have market approval in order for the products to qualify for negotiation under the Medicare Drug Price Negotiation Program.</p><p>The Medicare Drug Price Negotiation Program requires the Centers for Medicare & Medicaid Services to negotiate the prices of certain prescription drugs under Medicare beginning in 2026. Among other requirements, drugs must have had market approval for at least 7 years (for drug products) or 11 years (for biologics) to qualify for negotiation.\u00a0</p><p>The bill modifies these provisions so as to require drug products to also have had at least 11 years of market approval in order to qualify for negotiation beginning in 2028.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119s832"
    },
    "title": "EPIC Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Pathways to Innovative Cures Act of 2025 or the EPIC Act of 2025</strong></p><p>This bill lengthens the amount of time for which drug products must have market approval in order for the products to qualify for negotiation under the Medicare Drug Price Negotiation Program.</p><p>The Medicare Drug Price Negotiation Program requires the Centers for Medicare & Medicaid Services to negotiate the prices of certain prescription drugs under Medicare beginning in 2026. Among other requirements, drugs must have had market approval for at least 7 years (for drug products) or 11 years (for biologics) to qualify for negotiation.\u00a0</p><p>The bill modifies these provisions so as to require drug products to also have had at least 11 years of market approval in order to qualify for negotiation beginning in 2028.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119s832"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s832is.xml"
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
      "title": "EPIC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T11:48:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EPIC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Pathways to Innovative Cures Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to equalize the negotiation period between small-molecule and biologic candidates under the Drug Price Negotiation Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:33Z"
    }
  ]
}
```
