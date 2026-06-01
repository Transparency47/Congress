# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3154?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3154
- Title: Service Academies District of Columbia Equality Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3154
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2025-11-25T20:42:54Z
- Update date including text: 2025-11-25T20:42:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3154",
    "number": "3154",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Service Academies District of Columbia Equality Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T20:42:54Z",
    "updateDateIncludingText": "2025-11-25T20:42:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T18:22:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3154is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3154\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Mr. Kaine introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to increase the number of individuals from the District of Columbia who may be appointed to military service academies.\n#### 1. Short title\nThis Act may be cited as the Service Academies District of Columbia Equality Act of 2025 .\n#### 2. Increased number of individuals from the District of Columbia who may be appointed to military service academies\n##### (a) United States Military Academy\nSection 7442(a)(5) of title 10, United States Code, is amended by striking Five and inserting Fifteen .\n##### (b) United States Naval Academy\nSection 8454(a)(5) of title 10, United States Code, is amended by striking Five and inserting Fifteen .\n##### (c) United States Air Force Academy\nSection 9442(a)(5) of title 10, United States Code, is amended by striking Five and inserting Fifteen .",
      "versionDate": "2025-11-07",
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
        "actionDate": "2025-11-07",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "5971",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Service Academies District of Columbia Equality Act",
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
        "updateDate": "2025-11-25T19:07:12Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3154is.xml"
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
      "title": "Service Academies District of Columbia Equality Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Service Academies District of Columbia Equality Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to increase the number of individuals from the District of Columbia who may be appointed to military service academies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:31Z"
    }
  ]
}
```
