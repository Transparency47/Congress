# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2670?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2670
- Title: FIGHTER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2670
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-04-09 - IntroReferral: Sponsor introductory remarks on measure. (CR H1553)
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-04-09 - IntroReferral: Sponsor introductory remarks on measure. (CR H1553)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2670",
    "number": "2670",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001325",
        "district": "3",
        "firstName": "Sheri",
        "fullName": "Rep. Biggs, Sheri [R-SC-3]",
        "lastName": "Biggs",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "FIGHTER Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1553)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:01:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2670ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2670\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mrs. Biggs of South Carolina introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide that regular compensation received for active service by a member of the Armed Forces shall not be subject to income taxes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fortifying Income by Giving our Heroes Their Earned-Tax Relief Act of 2025 or the FIGHTER Act of 2025 .\n#### 2. Exclusion from gross income of regular compensation received by members of the Armed Forces\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Regular compensation received by members of the Armed Forces (a) In general Gross income shall not include regular compensation received by an individual for active service as a member of the Armed Forces. (b) Exception This section shall not apply to any compensation if the individual receiving such compensation served as a Member of Congress at any time during the 10-year period ending on the date that such individual received such compensation. (c) Definitions For purposes of this section\u2014 (1) Active service The term active service has the meaning given that term under section 101 of title 37, United States Code. (2) Member of Congress The term Member of Congress means a Senator or Representative in, or Delegate or Resident Commissioner to, the Congress. (3) Regular compensation The term regular compensation has the meaning given that term under section 101 of title 37, United States Code. (d) Regulations The Secretary shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Withholding\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall modify the tables and procedures prescribed under section 3402(a) of the Internal Revenue Code of 1986 to take into account amounts excludable from gross income under section 139J of such Code (as added by this Act).\n##### (c) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Regular compensation received by members of the Armed Forces. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 3. Government Efficiency Savings and Expenditure Reductions\nThe United States DOGE Service (commonly referred to as the Department of Government Efficiency or DOGE ) shall implement cost-saving initiatives that reduce Federal expenditures by an amount that is at least equal to the reduction in Federal revenues that occurs by reason of the amendments made by section 2.",
      "versionDate": "2025-04-07",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T17:53:58Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2670ih.xml"
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
      "title": "FIGHTER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIGHTER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fortifying Income by Giving our Heroes Their Earned-Tax Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide that regular compensation received for active service by a member of the Armed Forces shall not be subject to income taxes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T05:18:35Z"
    }
  ]
}
```
