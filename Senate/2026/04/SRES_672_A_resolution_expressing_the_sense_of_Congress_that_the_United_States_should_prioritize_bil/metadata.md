# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/672?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/672
- Title: A resolution expressing the sense of Congress that the United States should prioritize bilateral security partnerships over multilateral security partnerships and institutions.
- Congress: 119
- Bill type: SRES
- Bill number: 672
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-04-21T01:36:43Z
- Update date including text: 2026-04-21T01:36:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1787-1788)
- 2026-04-15 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-15: Submitted in Senate

## Actions

- 2026-04-15 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1787-1788)
- 2026-04-15 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/672",
    "number": "672",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A resolution expressing the sense of Congress that the United States should prioritize bilateral security partnerships over multilateral security partnerships and institutions.",
    "type": "SRES",
    "updateDate": "2026-04-21T01:36:43Z",
    "updateDateIncludingText": "2026-04-21T01:36:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1787-1788)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-04-15T21:26:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres672is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 672\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. Lee submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of Congress that the United States should prioritize bilateral security partnerships over multilateral security partnerships and institutions.\nThat the Senate\u2014\n**(1)**\nexpresses that the United States must use its power, influence, and resources to encourage small and medium states to choose the United States as its great power partner and ally of choice;\n**(2)**\nrecognizes that the United States should prioritize bilateral security agreements over multilateral security agreements and institutions; and\n**(3)**\ndetermines that the United States should withdraw support for multilateral security agreements or institutions that undermine United States interests.",
      "versionDate": "2026-04-15",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2026-04-21T01:36:43Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres672is.xml"
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
      "title": "A resolution expressing the sense of Congress that the United States should prioritize bilateral security partnerships over multilateral security partnerships and institutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:38Z"
    },
    {
      "title": "A resolution expressing the sense of Congress that the United States should prioritize bilateral security partnerships over multilateral security partnerships and institutions.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T10:56:23Z"
    }
  ]
}
```
