# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7660
- Title: HBCU Empowerment and Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 7660
- Origin chamber: House
- Introduced date: 2026-02-24
- Update date: 2026-03-12T18:52:55Z
- Update date including text: 2026-03-12T18:52:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-24: Introduced in House

## Actions

- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7660",
    "number": "7660",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "HBCU Empowerment and Reform Act",
    "type": "HR",
    "updateDate": "2026-03-12T18:52:55Z",
    "updateDateIncludingText": "2026-03-12T18:52:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-02-24T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7660ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7660\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2026 Mr. McCormick introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to expand the definition of a historically Black college or university to include schools established prior to November 8, 1965, so long as such schools meet all other required criteria, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the HBCU Empowerment and Reform Act .\n#### 2. Definition of a historically Black college or university\nSection 322(2) of the Higher Education Act of 1965 ( 20 U.S.C. 1061(2) ) is amended by striking 1964 and inserting November 8, 1965 .",
      "versionDate": "2026-02-24",
      "versionType": "Introduced in House"
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
        "name": "Education",
        "updateDate": "2026-03-12T18:52:55Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7660ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "HBCU Empowerment and Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T03:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HBCU Empowerment and Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-11T03:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to expand the definition of a historically Black college or university to include schools established prior to November 8, 1965, so long as such schools meet all other required criteria, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-11T03:33:31Z"
    }
  ]
}
```
