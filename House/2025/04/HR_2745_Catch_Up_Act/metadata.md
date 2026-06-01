# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2745
- Title: Catch Up Act
- Congress: 119
- Bill type: HR
- Bill number: 2745
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-05-30T23:52:06Z
- Update date including text: 2025-05-30T23:52:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2745",
    "number": "2745",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Catch Up Act",
    "type": "HR",
    "updateDate": "2025-05-30T23:52:06Z",
    "updateDateIncludingText": "2025-05-30T23:52:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2745ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2745\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Steube (for himself and Mr. Hill of Arkansas ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow both spouses to make catch-up contributions to the same health savings account.\n#### 1. Short title\nThis Act may be cited as the Catch Up Act .\n#### 2. Allow both spouses to make catch-up contributions to the same health savings account\n##### (a) In general\nSection 223(b)(5) of the Internal Revenue Code of 1986 is amended to read as follows:\n(5) Special rule for married individuals with family coverage (A) In general In the case of individuals who are married to each other, if both spouses are eligible individuals and either spouse has family coverage under a high deductible health plan as of the first day of any month\u2014 (i) the limitation under paragraph (1) shall be applied by not taking into account any other high deductible health plan coverage of either spouse (and if such spouses both have family coverage under separate high deductible health plans, only one such coverage shall be taken into account), (ii) such limitation (after application of clause (i)) shall be reduced by the aggregate amount paid to Archer MSAs of such spouses for the taxable year, and (iii) such limitation (after application of clauses (i) and (ii)) shall be divided equally between such spouses unless they agree on a different division. (B) Treatment of additional contribution amounts If both spouses referred to in subparagraph (A) have attained age 55 before the close of the taxable year, the limitation referred to in subparagraph (A)(iii) which is subject to division between the spouses shall include the additional contribution amounts determined under paragraph (3) for both spouses. In any other case, any additional contribution amount determined under paragraph (3) shall not be taken into account under subparagraph (A)(iii) and shall not be subject to division between the spouses. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "548",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HSA Modernization Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-22",
        "actionTime": "06:56:39",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T17:40:36Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2745ih.xml"
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
      "title": "Catch Up Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Catch Up Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow both spouses to make catch-up contributions to the same health savings account.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T05:18:22Z"
    }
  ]
}
```
