# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1607
- Title: INSPECT Act
- Congress: 119
- Bill type: S
- Bill number: 1607
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-05-27T14:22:30Z
- Update date including text: 2025-05-27T14:22:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1607",
    "number": "1607",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "INSPECT Act",
    "type": "S",
    "updateDate": "2025-05-27T14:22:30Z",
    "updateDateIncludingText": "2025-05-27T14:22:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T16:13:34Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1607is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1607\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish an Inspector General of the National Institutes of Health, an Inspector General of the Centers for Disease Control and Prevention, and an Inspector General for the Food and Drug Administration.\n#### 1. Short title\nThis Act may be cited as the Improving National Safety, Public health, Ethics, and Clinical Trials Act or the INSPECT Act .\n#### 2. Establishment of Inspectors General of the National Institutes of Health, the Centers for Disease Control and Prevention, and the Food and Drug Administration\n##### (a) Definitions\nSection 401 of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking or the National Reconnaissance Office, and inserting the National Reconnaissance Office, the National Institutes of Health, the Centers for Disease Control and Prevention, or the Food and Drug Administration, ; and\n**(2)**\nin paragraph (3), by striking or the Director of the National Reconnaissance Office; and inserting the Director of the National Reconnaissance Office; the Director of the National Institutes of Health; the Director for the Centers for Disease Control and Prevention; or the Commissioner of Food and Drugs, .\n##### (b) Appointment of Inspectors General\nNot later than 1 year after the date of enactment of this Act, the President shall, in accordance with section 403(a) of title 5, United States Code\u2014\n**(1)**\nappoint an individual to serve as the Inspector General of the National Institutes of Health;\n**(2)**\nappoint an individual to serve as the Inspector General of the Centers for Disease Control and Prevention; and\n**(3)**\nappoint an individual to serve as the Inspector General of the Food and Drug Administration.\n#### 3. Compliance with CUTGO\nThis Act and the amendments made by this Act shall be carried out using amounts otherwise appropriated to the Office of the Inspector General of the Department of Health and Human Services, and no additional amounts are authorized to be appropriated to carry out this Act or the amendments made by this Act.",
      "versionDate": "2025-05-06",
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
        "name": "Health",
        "updateDate": "2025-05-27T14:22:30Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1607is.xml"
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
      "title": "INSPECT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INSPECT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving National Safety, Public health, Ethics, and Clinical Trials Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an Inspector General of the National Institutes of Health, an Inspector General of the Centers for Disease Control and Prevention, and an Inspector General for the Food and Drug Administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:19Z"
    }
  ]
}
```
