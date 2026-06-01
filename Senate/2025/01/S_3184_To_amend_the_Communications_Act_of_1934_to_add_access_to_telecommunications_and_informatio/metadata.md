# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3184?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3184
- Title: Tribal Internet Expansion Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3184
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2025-12-06T13:21:01Z
- Update date including text: 2025-12-06T13:21:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3184",
    "number": "3184",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Tribal Internet Expansion Act of 2025",
    "type": "S",
    "updateDate": "2025-12-06T13:21:01Z",
    "updateDateIncludingText": "2025-12-06T13:21:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T21:57:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3184is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3184\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Communications Act of 1934 to add access to telecommunications and information services in Indian country and areas with high populations of Indian people to the universal service principle relating to access to those services in rural, insular, and high cost areas.\n#### 1. Short title\nThis Act may be cited as the Tribal Internet Expansion Act of 2025 .\n#### 2. Universal service in Indian country and areas with high populations of Indian people\nSection 254(b)(3) of the Communications Act of 1934 (47 U.S.C. 254(b)(3)) is amended\u2014\n**(1)**\nby striking and those in and inserting , consumers in ; and\n**(2)**\nby inserting , and consumers in Indian country (as defined in section 1151 of title 18, United States Code) and in areas with high populations of Indian (as defined in section 19 of the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 988, chapter 576; 25 U.S.C. 5129)) persons after high cost areas .",
      "versionDate": "",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-06T13:21:01Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3184is.xml"
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
      "title": "Tribal Internet Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tribal Internet Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Communications Act of 1934 to add access to telecommunications and information services in Indian country and areas with high populations of Indian people to the universal service principle relating to access to those services in rural, insular, and high cost areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T04:03:46Z"
    }
  ]
}
```
