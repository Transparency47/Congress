# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7210?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7210
- Title: Fuel the Force Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7210
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-04-14T08:05:41Z
- Update date including text: 2026-04-14T08:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7210",
    "number": "7210",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Fuel the Force Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:41Z",
    "updateDateIncludingText": "2026-04-14T08:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:05:45Z",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7210ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7210\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Fitzpatrick (for himself and Ms. Perez ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude certain income of law enforcement officers from gross income.\n#### 1. Short title\nThis Act may be cited as the Fuel the Force Act of 2026 .\n#### 2. Exclusion of certain income from gross income of law enforcement officers\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139L the following new section:\n139M. Certain income of law enforcement officers (a) In general In the case of a qualified taxpayer, gross income does not include qualified income. (b) Qualified taxpayer For purposes of this section, the term qualified taxpayer means, with respect to a taxable year, an individual that\u2014 (1) worked full-time during such taxable year as a law enforcement officer, and (2) has worked full-time as a law enforcement officer for periods aggregating not less than 5 years (determined as of the beginning of such taxable year). (c) Qualified income For purposes of this section, the term qualified income means, with respect to any taxable year, the first $100,000 of ordinary income earned by the taxpayer during such taxable year. (d) Law enforcement officer For purposes of this section, the term law enforcement officer means\u2014 (1) an individual serving a Federal, State, or local law enforcement or corrections agency who is involved in crime and juvenile delinquency control or reduction, or enforcement of the criminal laws (including juvenile delinquency), including police, corrections, probation, parole, and judicial officers, and sheriffs and their deputies, and (2) any school resource officer (as defined in section 1709 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10389 )). .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Certain income of law enforcement officers. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this section.",
      "versionDate": "2026-01-22",
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
        "updateDate": "2026-02-19T19:00:57Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7210ih.xml"
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
      "title": "Fuel the Force Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fuel the Force Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude certain income of law enforcement officers from gross income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:37Z"
    }
  ]
}
```
