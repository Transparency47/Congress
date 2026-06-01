# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3015?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3015
- Title: AWRC Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3015
- Origin chamber: Senate
- Introduced date: 2025-10-16
- Update date: 2026-04-13T21:27:34Z
- Update date including text: 2026-04-13T21:27:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-16: Introduced in Senate
- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-10-16: Introduced in Senate

## Actions

- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-16",
    "latestAction": {
      "actionDate": "2025-10-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3015",
    "number": "3015",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
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
    "title": "AWRC Act of 2025",
    "type": "S",
    "updateDate": "2026-04-13T21:27:34Z",
    "updateDateIncludingText": "2026-04-13T21:27:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-16",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-16",
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
          "date": "2025-10-16T18:34:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "MS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "NH"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3015is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3015\nIN THE SENATE OF THE UNITED STATES\nOctober 16, 2025 Mr. Boozman (for himself, Mr. Kelly , Mrs. Hyde-Smith , Mrs. Shaheen , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Water Resources Research Act of 1984 to reauthorize the water resources research and technology institutes program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Water Research and Collaboration Act of 2025 or the AWRC Act of 2025 .\n#### 2. Congressional declaration of purpose\nSection 103(4) of the Water Resources Research Act of 1984 ( 42 U.S.C. 10302(4) ) is amended by inserting , including the growing artificial intelligence industry, after private industry .\n#### 3. Water resources research and technology institutes\nSection 104 of the Water Resources Research Act of 1984 ( 42 U.S.C. 10303 ) is amended\u2014\n**(1)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (2), by striking subsection 104(g) of this Act and inserting subsection (g) ; and\n**(B)**\nby striking the subsection designation and all that follows through Any sums in paragraph (2) and inserting the following:\n(f) General authorization of appropriations (1) In general Except as provided in paragraph (2) and subject to subsection (g)(1), there is authorized to be appropriated to carry out this section $16,000,000 for each of fiscal years 2026 through 2029. (2) Failure to obligate Any amounts ; and\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (2), by striking (2) Research funds and inserting the following:\n(4) Competitive grants ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin the third sentence, by striking Funds made and inserting the following:\n(3) Availability of funds Funds made ; and\n**(ii)**\nby striking by institutes which focuses in the first sentence and all that follows through Such funds when appropriated in the second sentence and inserting the following:\nby institutes with respect to any of the following: (A) Research that focuses on water problems and issues of a regional or interstate nature beyond those of concern only to a single State. (B) Research that relates to specific program priorities identified jointly by the Secretary and the institutes. (C) Research that relates to water problems identified by Congress as being of an interstate nature. (2) Federal cost-share Funds made available under this subsection ; and\n**(C)**\nby striking the subsection designation and all that follows through 2025 in the first sentence of paragraph (1) and inserting the following:\n(g) Additional funds for research focused on water problems of interstate nature (1) In general Of the amounts made available under subsection (f)(1) for each of fiscal years 2026 through 2029, 20 percent shall be used .",
      "versionDate": "2025-10-16",
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
        "actionDate": "2026-03-26",
        "text": "Subcommittee Hearings Held"
      },
      "number": "7889",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AWRC Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-12-02T21:30:16Z"
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
      "date": "2025-10-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3015is.xml"
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
      "title": "AWRC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AWRC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Water Research and Collaboration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Water Resources Research Act of 1984 to reauthorize the water resources research and technology institutes program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:19Z"
    }
  ]
}
```
