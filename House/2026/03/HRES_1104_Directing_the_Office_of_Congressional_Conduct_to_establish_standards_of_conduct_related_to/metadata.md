# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1104
- Title: Directing the Office of Congressional Conduct to establish standards of conduct related to mental capacity of members of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 1104
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-03-09T15:00:13Z
- Update date including text: 2026-03-09T15:00:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-03-04 - IntroReferral: Submitted in House
- 2026-03-04 - IntroReferral: Submitted in House
- Latest action: 2026-03-04: Submitted in House

## Actions

- 2026-03-04 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-03-04 - IntroReferral: Submitted in House
- 2026-03-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1104",
    "number": "1104",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Directing the Office of Congressional Conduct to establish standards of conduct related to mental capacity of members of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2026-03-09T15:00:13Z",
    "updateDateIncludingText": "2026-03-09T15:00:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-04T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1104ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1104\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Ms. Perez submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nDirecting the Office of Congressional Conduct to establish standards of conduct related to mental capacity of members of the House of Representatives.\n#### 1. Standards of conduct and whistleblower portal relating to mental capacity of Members of the House of Representatives\n##### (a) Office of Congressional Conduct; standard of conduct relating to cognitive impairment\n**(1) In general**\nNot later than 180 days after the date of the adoption of this resolution, the Office of Congressional Conduct shall\u2014\n**(A)**\ndevelop a standard for what constitutes conduct, relating to a Member who is unable to behave at all times in a manner that reflects creditably on the House, as required under clause 1 of rule XXIII of the Rules of the House of Representatives, because the Member suffers from a significant and irreversible cognitive impairment; and\n**(B)**\nsubmit a report on such standard to the Committee on Ethics.\n**(2) Application**\nIn carrying out paragraph (1)\u2014\n**(A)**\nthe Office of Congressional Conduct may consult with relevant offices of Congress and outside experts in developing such standard; and\n**(B)**\nnot later than 90 days after receiving the report under paragraph (1)(B), the Committee on Ethics shall develop and issue a standard described under paragraph (1)(A) or issue the standard contained in such report.\n##### (b) Committee on Ethics; guidance on mental capacity\nThe Committee on Ethics shall draft and make publicly available specific guidance for employees of the House to safely and confidentially make disclosures to relevant committees and legislative branch offices on the mental capacity of Members.",
      "versionDate": "2026-03-04",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2026-03-09T15:00:13Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1104ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Directing the Office of Congressional Conduct to establish standards of conduct related to mental capacity of members of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T09:18:25Z"
    },
    {
      "title": "Directing the Office of Congressional Conduct to establish standards of conduct related to mental capacity of members of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:07:09Z"
    }
  ]
}
```
