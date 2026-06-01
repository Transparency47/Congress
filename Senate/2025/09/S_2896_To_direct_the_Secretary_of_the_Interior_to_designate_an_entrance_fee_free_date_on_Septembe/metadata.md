# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2896
- Title: STARS Act
- Congress: 119
- Bill type: S
- Bill number: 2896
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-04-08T11:53:26Z
- Update date including text: 2026-04-08T11:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2896",
    "number": "2896",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001236",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Boozman, John [R-AR]",
        "lastName": "Boozman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "STARS Act",
    "type": "S",
    "updateDate": "2026-04-08T11:53:26Z",
    "updateDateIncludingText": "2026-04-08T11:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T20:42:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2896is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2896\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Boozman (for himself, Mr. Padilla , Mr. Daines , Mr. Hickenlooper , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of the Interior to designate an entrance-fee-free date on September 17, 2026, at units of the National Park System to celebrate the 250th anniversary of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Semiquincentennial Tourism and Access to Recreation Sites Act or the STARS Act .\n#### 2. Waived fees at public recreational sites in honor of the 250th anniversary of the United States\n##### (a) Definitions\nIn this section:\n**(1) Entrance fee**\nThe term entrance fee has the meaning given the term in section 802 of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6801 ).\n**(2) Standard amenity recreation fee**\nThe term standard amenity recreation fee has the meaning given the term in section 802 of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6801 ).\n##### (b) Waiver of fees\nIn honor of the semiquincentennial of the United States\u2014\n**(1)**\nthe Secretary of the Interior shall\u2014\n**(A)**\ndesignate September 17, 2026, as an entrance-fee-free date on which admission is free to all visitors with respect to each unit of the National Park System or unit of the National Wildlife Refuge System that charges an entrance fee; and\n**(B)**\nwaive standard amenity recreation fees on September 17, 2026, for each visitor to each site managed by the Bureau of Land Management or the Bureau of Reclamation that charges a standard amenity recreation fee; and\n**(2)**\nthe Secretary of Agriculture shall waive standard amenity recreation fees for September 17, 2026, for each visitor to each site managed by the Forest Service that charges a standard amenity recreation fee.",
      "versionDate": "2025-09-18",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T16:38:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119s2896",
          "measure-number": "2896",
          "measure-type": "s",
          "orig-publish-date": "2025-09-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2896v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Semiquincentennial Tourism and Access to Recreation Sites Act or the STARS Act</strong></p><p>This bill directs the Department of the Interior and the Forest Service to designate September 17, 2026, as an entrance-fee free date in honor of the 250th anniversary of the United States of America. On that date, Interior must waive (1) the entrance fees for all visitors of National Park Service or\u00a0National Wildlife Refuge System sites; and (2) the standard amenity recreation fees for all visitors to each site managed by the Bureau of Land Management or the Bureau of Reclamation. The Forest Service must waive the standard amenity recreation fees on that date for all visitors to sites it manages.</p>"
        },
        "title": "STARS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2896.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Semiquincentennial Tourism and Access to Recreation Sites Act or the STARS Act</strong></p><p>This bill directs the Department of the Interior and the Forest Service to designate September 17, 2026, as an entrance-fee free date in honor of the 250th anniversary of the United States of America. On that date, Interior must waive (1) the entrance fees for all visitors of National Park Service or\u00a0National Wildlife Refuge System sites; and (2) the standard amenity recreation fees for all visitors to each site managed by the Bureau of Land Management or the Bureau of Reclamation. The Forest Service must waive the standard amenity recreation fees on that date for all visitors to sites it manages.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2896"
    },
    "title": "STARS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Semiquincentennial Tourism and Access to Recreation Sites Act or the STARS Act</strong></p><p>This bill directs the Department of the Interior and the Forest Service to designate September 17, 2026, as an entrance-fee free date in honor of the 250th anniversary of the United States of America. On that date, Interior must waive (1) the entrance fees for all visitors of National Park Service or\u00a0National Wildlife Refuge System sites; and (2) the standard amenity recreation fees for all visitors to each site managed by the Bureau of Land Management or the Bureau of Reclamation. The Forest Service must waive the standard amenity recreation fees on that date for all visitors to sites it manages.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2896"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2896is.xml"
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
      "title": "STARS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STARS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Semiquincentennial Tourism and Access to Recreation Sites Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior to designate an entrance-fee-free date on September 17, 2026, at units of the National Park System to celebrate the 250th anniversary of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:22Z"
    }
  ]
}
```
