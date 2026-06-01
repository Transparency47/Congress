# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4533
- Title: Coast Guard Personnel Equipment Act
- Congress: 119
- Bill type: S
- Bill number: 4533
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-28T22:29:14Z
- Update date including text: 2026-05-28T22:29:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4533",
    "number": "4533",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Coast Guard Personnel Equipment Act",
    "type": "S",
    "updateDate": "2026-05-28T22:29:14Z",
    "updateDateIncludingText": "2026-05-28T22:29:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T16:57:18Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4533is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4533\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mr. Graham introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 10, United States Code, to include the Coast Guard in the requirement to buy certain articles from American sources.\n#### 1. Short title\nThis Act may be cited as the Coast Guard Personnel Equipment Act .\n#### 2. Requirement for Coast Guard to buy certain articles from American sources\nSection 4862 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking Department of Defense and inserting Department of Defense or any branch of the Armed Forces ;\n**(2)**\nin subsection (c), by striking the Secretary of the military department concerned and inserting the Secretary concerned ;\n**(3)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1), by striking Department of Defense and inserting Department of Defense or any branch of the Armed Forces ; and\n**(B)**\nin paragraph (2)(B), by striking The Secretary of Defense and inserting The Secretary of Defense or, with respect to the Coast Guard when it is not operating as a service in the Navy, the Secretary of Homeland Security ;\n**(4)**\nin subsection (h)\u2014\n**(A)**\nin paragraph (2)(B), by striking Secretary of Defense and inserting Secretary of Defense or, with respect to the Coast Guard when it is not operating as a service in the Navy, the Secretary of Homeland Security ; and\n**(B)**\nin paragraph (3), by striking Secretary of Defense and inserting Secretary of Defense, in consultation with the Secretary of Homeland Security, ; and\n**(5)**\nin subsection (k), by striking or of the military department concerned and inserting or the Secretary concerned .",
      "versionDate": "2026-05-14",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-28T22:29:14Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4533is.xml"
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
      "title": "Coast Guard Personnel Equipment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Coast Guard Personnel Equipment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to include the Coast Guard in the requirement to buy certain articles from American sources.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:45Z"
    }
  ]
}
```
