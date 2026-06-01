# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/862?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/862
- Title: HBOT Access Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 862
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-05-14T11:03:26Z
- Update date including text: 2026-05-14T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/862",
    "number": "862",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "HBOT Access Act of 2025",
    "type": "S",
    "updateDate": "2026-05-14T11:03:26Z",
    "updateDateIncludingText": "2026-05-14T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
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
            "date": "2025-03-05T17:51:25Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-05T17:51:25Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ND"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ND"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "ID"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s862is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 862\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Tuberville (for himself, Mr. Hoeven , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to furnish hyperbaric oxygen therapy to certain veterans with traumatic brain injury or post-traumatic stress disorder.\n#### 1. Short title\nThis Act may be cited as the HBOT Access Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe suicide rate among veterans is 18 per day.\n**(2)**\nVeterans are at a higher risk of suicide than the general population of the United States and Congress must provide continued support at the Federal, State, and local levels to combat the pandemic of veteran suicide.\n**(3)**\nVeterans deserve every opportunity to enjoy the freedom that they fought for overseas.\n**(4)**\nThe Department of Veterans Affairs should consider and establish alternate treatments for traumatic brain injury and post-traumatic stress disorder that do not require prescription drugs, opioids, or invasive procedures.\n**(5)**\nHyperbaric oxygen therapy is a proven treatment for symptoms of traumatic brain injury and post-traumatic stress disorder and should be accessible to veterans who are at a high-risk of suicide or self-harm.\n#### 3. Hyperbaric oxygen therapy for veterans with traumatic brain injury or post-traumatic stress disorder\n##### (a) In general\nSubchapter II of chapter 17 of title 38, United States Code, is amended by inserting after section 1710E the following new section:\n1710F. Traumatic brain injury and post-traumatic stress disorder: hyperbaric oxygen therapy (a) Authority The Secretary shall furnish hyperbaric oxygen therapy to a veteran who\u2014 (1) has a condition specified in subsection (b); and (2) has used not fewer than two evidence-based treatment options for such condition. (b) Covered conditions The conditions specified in this subsection are the following: (1) Traumatic brain injury. (2) Post-traumatic stress disorder. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1710E the following new item:\n1710F. Traumatic brain injury and post-traumatic stress disorder: hyperbaric oxygen therapy. .",
      "versionDate": "2025-03-05",
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
        "updateDate": "2025-05-08T13:39:44Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s862is.xml"
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
      "title": "HBOT Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HBOT Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to furnish hyperbaric oxygen therapy to certain veterans with traumatic brain injury or post-traumatic stress disorder.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:57Z"
    }
  ]
}
```
