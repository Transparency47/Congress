# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/236
- Title: A bill to amend the Act of August 9, 1955 (commonly known as the "Long-Term Leasing Act"), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 236
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-05-21T10:56:46Z
- Update date including text: 2026-05-21T10:56:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2025-12-17 - Committee: Committee on Indian Affairs. Hearings held.
- 2026-05-20 - Committee: Committee on Indian Affairs. Ordered to be reported without amendment favorably.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2025-12-17 - Committee: Committee on Indian Affairs. Hearings held.
- 2026-05-20 - Committee: Committee on Indian Affairs. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/236",
    "number": "236",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A bill to amend the Act of August 9, 1955 (commonly known as the \"Long-Term Leasing Act\"), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-21T10:56:46Z",
    "updateDateIncludingText": "2026-05-21T10:56:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
            "date": "2026-05-20T18:30:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-17T20:25:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-23T23:01:51Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s236is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 236\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Markey (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo amend the Act of August 9, 1955 (commonly known as the Long-Term Leasing Act ), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes.\n#### 1. Mashpee Wampanoag Tribe and Wampanoag Tribe of Gay Head (Aquinnah) leasing authority\nSubsection (a) of the first section of the Act of August 9, 1955 (69 Stat. 539, chapter 615; 25 U.S.C. 415(a) ) (commonly known as the Long-Term Leasing Act ), is amended, in the second sentence, by inserting , the Mashpee Wampanoag Tribe Reservation, land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah) after Confederated Tribes of the Chehalis Reservation .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2026-05-20",
        "text": "Committee on Indian Affairs. Ordered to be reported without amendment favorably."
      },
      "number": "681",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Act of August 9, 1955 (commonly known as the \u201cLong-Term Leasing Act\u201d), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes",
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
            "name": "Federal-Indian relations",
            "updateDate": "2025-03-25T17:18:31Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-03-25T17:18:31Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-25T17:18:31Z"
          },
          {
            "name": "Massachusetts",
            "updateDate": "2025-03-25T17:18:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-04-09T20:29:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s236",
          "measure-number": "236",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s236v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill authorizes the Mashpee Wampanoag Tribe and the Wampanoag Tribe of Gay Head (Aquinnah)\u00a0to lease their land held in trust for a term of up to 99 years. Both tribes are located in Massachusetts.</p>"
        },
        "title": "A bill to amend the Act of August 9, 1955 (commonly known as the \"Long-Term Leasing Act\"), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s236.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill authorizes the Mashpee Wampanoag Tribe and the Wampanoag Tribe of Gay Head (Aquinnah)\u00a0to lease their land held in trust for a term of up to 99 years. Both tribes are located in Massachusetts.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s236"
    },
    "title": "A bill to amend the Act of August 9, 1955 (commonly known as the \"Long-Term Leasing Act\"), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill authorizes the Mashpee Wampanoag Tribe and the Wampanoag Tribe of Gay Head (Aquinnah)\u00a0to lease their land held in trust for a term of up to 99 years. Both tribes are located in Massachusetts.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s236"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s236is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Act of August 9, 1955 (commonly known as the \"Long-Term Leasing Act\"), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:19Z"
    },
    {
      "title": "A bill to amend the Act of August 9, 1955 (commonly known as the \"Long-Term Leasing Act\"), to authorize leases of up to 99 years for land in the Mashpee Wampanoag Tribe Reservation and land held in trust for the Wampanoag Tribe of Gay Head (Aquinnah), and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T11:56:17Z"
    }
  ]
}
```
