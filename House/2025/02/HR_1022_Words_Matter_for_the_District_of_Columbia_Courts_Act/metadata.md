# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1022?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1022
- Title: Words Matter for the District of Columbia Courts Act
- Congress: 119
- Bill type: HR
- Bill number: 1022
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-12-05T21:54:36Z
- Update date including text: 2025-12-05T21:54:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-05 - IntroReferral: Sponsor introductory remarks on measure. (CR E99)
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-05 - IntroReferral: Sponsor introductory remarks on measure. (CR E99)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1022",
    "number": "1022",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Words Matter for the District of Columbia Courts Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:54:36Z",
    "updateDateIncludingText": "2025-12-05T21:54:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E99)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1022ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1022\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 11, District of Columbia Official Code, to revise references in such title to individuals with intellectual disabilities.\n#### 1. Short title\nThis Act may be cited as the Words Matter for the District of Columbia Courts Act .\n#### 2. References to individuals with intellectual disabilities\n##### (a) Jurisdiction of United States District Court\nSection 11\u2013501(2)(D), District of Columbia Official Code, is amended by striking substantially retarded persons and inserting persons with moderate intellectual disabilities .\n##### (b) Jurisdiction of Superior Court\nSection 11\u2013921(a)(4)(D), District of Columbia Official Code, is amended by striking substantially retarded persons and inserting persons with moderate intellectual disabilities .\n##### (c) Jurisdiction of Family Court\nSection 11\u20131101(a)(15), District of Columbia Official Code, is amended by striking the at least moderately mentally retarded and inserting persons with moderate intellectual disabilities .",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "402",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Words Matter for the District of Columbia Courts Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-06-18T14:13:02Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-06-18T14:13:02Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-06-18T14:13:02Z"
          },
          {
            "name": "Specialized courts",
            "updateDate": "2025-06-18T14:13:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-05-06T12:51:43Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1022ih.xml"
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
      "title": "Words Matter for the District of Columbia Courts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Words Matter for the District of Columbia Courts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 11, District of Columbia Official Code, to revise references in such title to individuals with intellectual disabilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:28Z"
    }
  ]
}
```
