# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2336?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2336
- Title: Halting the Epidemic of Addiction and Loss Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2336
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-04-03T19:55:35Z
- Update date including text: 2026-04-03T19:55:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2336",
    "number": "2336",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Halting the Epidemic of Addiction and Loss Act of 2025",
    "type": "S",
    "updateDate": "2026-04-03T19:55:35Z",
    "updateDateIncludingText": "2026-04-03T19:55:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T17:29:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2336is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2336\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Cornyn (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ensure references to opioid overdose reversal agents in certain grant programs of the Department of Health and Human Services are not limited to naloxone.\n#### 1. Short title\nThis Act may be cited as the Halting the Epidemic of Addiction and Loss Act of 2025 .\n#### 2. References to opioid overdose reversal agents in HHS grant programs\n##### (a) In general\nThe Secretary of Health and Human Services shall ensure that, as appropriate, whenever the Department of Health and Human Services issues a regulation or guidance for any grant program addressing opioid misuse and use disorders, any reference to an opioid overdose reversal drug (such as a reference to naloxone) is inclusive of any opioid overdose reversal drug that has been approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) for emergency treatment of a known or suspected opioid overdose.\n##### (b) Existing references\n**(1) Update**\nNot later than one year after the date of enactment of this Act, the Secretary of Health and Human Services shall update all references described in paragraph (2) to be inclusive of any opioid overdose reversal drug that has been approved or otherwise authorized for use by the Food and Drug Administration.\n**(2) References**\nA reference described in this paragraph is any reference to an opioid overdose reversal drug (such as naloxone) in any regulation or guidance of the Department of Health and Human Services that\u2014\n**(A)**\nwas issued before the date of enactment of this Act; and\n**(B)**\nis included in\u2014\n**(i)**\nthe grant program for State and Tribal response to opioid use disorders under section 1003 of the 21st Century Cures Act ( 42 U.S.C. 290ee\u20133a ) (commonly referred to as State Opioid Response Grants and Tribal Opioid Response Grants ); or\n**(ii)**\nthe grant program for priority substance use disorder prevention needs of regional and national significance under section 516 of the Public Health Service Act ( 42 U.S.C. 290bb\u201322 ).",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-12-01",
        "text": "Became Public Law No: 119-44."
      },
      "number": "2483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-09-05T15:47:18Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2336is.xml"
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
      "title": "Halting the Epidemic of Addiction and Loss Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Halting the Epidemic of Addiction and Loss Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure references to opioid overdose reversal agents in certain grant programs of the Department of Health and Human Services are not limited to naloxone.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:23Z"
    }
  ]
}
```
