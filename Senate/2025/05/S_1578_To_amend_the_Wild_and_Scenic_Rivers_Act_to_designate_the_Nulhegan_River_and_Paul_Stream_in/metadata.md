# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1578?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1578
- Title: Nulhegan River and Paul Stream Wild and Scenic River Study Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1578
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1578",
    "number": "1578",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Nulhegan River and Paul Stream Wild and Scenic River Study Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T17:52:38Z",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-01",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1578is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1578\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Welch (for himself and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Wild and Scenic Rivers Act to designate the Nulhegan River and Paul Stream in the State of Vermont for potential addition to the national wild and scenic rivers system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nulhegan River and Paul Stream Wild and Scenic River Study Act of 2025 .\n#### 2. Amendments to the Wild and Scenic Rivers Act\n##### (a) Designation for study\nSection 5(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1276(a) ) is amended by adding at the end the following:\n(147) Nulhegan River and Paul Stream, Vermont The following segments: (A) The approximately 22-mile segment of the main stem of the Nulhegan River from the headwaters near Nulhegan Pond to the confluence with the Connecticut River, and any associated tributaries (including the North, Yellow, Black, and East Branches). (B) The approximately 18-mile segment of Paul Stream from the headwaters on West Mountain to the confluence with the Connecticut River, and any associated tributaries. .\n##### (b) Study and report\nSection 5(b) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1276(b) ) is amended by adding at the end the following:\n(24) Nulhegan River and Paul Stream, Vermont Not later than 3 years after the date on which funds are made available to carry out this paragraph, the Secretary of the Interior shall\u2014 (A) complete the study of the Nulhegan River and Paul Stream segments in Vermont described in subsection (a)(147); and (B) submit to the appropriate committees of Congress a report describing the results of such study. .",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-05-05",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "3181",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nulhegan River and Paul Stream Wild and Scenic River Study Act of 2025",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-04T15:10:33Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1578is.xml"
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
      "title": "A bill to amend the Wild and Scenic Rivers Act to designate the Nulhegan River and Paul Stream in the State of Vermont for potential addition to the national wild and scenic rivers system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:31Z"
    },
    {
      "title": "Nulhegan River and Paul Stream Wild and Scenic River Study Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:38Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nulhegan River and Paul Stream Wild and Scenic River Study Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:25Z"
    }
  ]
}
```
