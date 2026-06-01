# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2134
- Title: Veterans Full-Service Care and Access Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2134
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-12-05T21:46:40Z
- Update date including text: 2025-12-05T21:46:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2134",
    "number": "2134",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Veterans Full-Service Care and Access Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:46:40Z",
    "updateDateIncludingText": "2025-12-05T21:46:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T19:27:57Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2134is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2134\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mrs. Shaheen introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to ensure that veterans in each of the 48 contiguous States are able to receive services in at least one full-service hospital of the Veterans Health Administration in the State or receive comparable services provided by contract in the State.\n#### 1. Short title\nThis Act may be cited as the Veterans Full-Service Care and Access Act of 2025 .\n#### 2. Availability of full-service hospital of the Veterans Health Administration in certain States or provision of comparable services through contract with other health care providers in the State\n##### (a) In general\nChapter 17 of title 38, United States Code, is amended by inserting after section 1716 the following new section:\n1716A. Access to full-service hospitals in certain States or comparable services through contract (a) Requirement With respect to each of the 48 contiguous States, the Secretary shall ensure that veterans in the State eligible for hospital care and medical services under section 1710 of this title may receive such hospital care and medical services at not fewer than one full-service hospital of the Veterans Health Administration located within the geographic boundaries of the State. (b) Rule of construction Nothing in subsection (a) shall be construed to restrict the ability of the Secretary to provide enhanced care to an eligible veteran who resides in one State in a hospital of the Veterans Health Administration in another State. .\n##### (b) Conforming amendments to Veterans Community Care Program\nSection 1703(d)(1) of such title is amended in subparagraph (B) by inserting as of the date of the enactment of the Veterans Full-Service Care and Access Act of 2025 before the semicolon at the end.\n##### (c) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1716 the following new item:\n1716A. Access to full-service hospitals in certain States or comparable services through contract. .\n##### (d) Report on implementation\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report describing the extent to which the Secretary has complied with the requirement imposed by section 1716A of title 38, United States Code, as added by subsection (a), including the effect of such requirement on improving the quality and standards of care provided to veterans.",
      "versionDate": "2025-06-18",
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
        "actionDate": "2025-06-20",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "4063",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans Full-Service Care and Access Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-09T15:26:38Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2134is.xml"
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
      "title": "Veterans Full-Service Care and Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-03T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Full-Service Care and Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to ensure that veterans in each of the 48 contiguous States are able to receive services in at least one full-service hospital of the Veterans Health Administration in the State or receive comparable services provided by contract in the State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-03T04:18:19Z"
    }
  ]
}
```
