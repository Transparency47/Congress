# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8242?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8242
- Title: Health Coverage Tax Credit Reauthorization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8242
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-16T08:07:09Z
- Update date including text: 2026-04-16T08:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8242",
    "number": "8242",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Health Coverage Tax Credit Reauthorization Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-16T08:07:09Z",
    "updateDateIncludingText": "2026-04-16T08:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:30:35Z",
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
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8242ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8242\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Turner of Ohio (for himself, Ms. McDonald Rivet , Ms. Tenney , and Ms. Stevens ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the health coverage tax credit.\n#### 1. Short title\nThis Act may be cited as the Health Coverage Tax Credit Reauthorization Act of 2026 .\n#### 2. Extension of health coverage tax credit\n##### (a) In general\nSection 35(b)(1)(B) of the Internal Revenue Code of 1986 is amended by striking before January 1, 2022 and inserting before January 1, 2030 .\n##### (b) Effective date\nThe amendments made by this section shall apply to months beginning after December 31, 2021.",
      "versionDate": "2026-04-09",
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
        "updateDate": "2026-04-15T01:38:10Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8242ih.xml"
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
      "title": "Health Coverage Tax Credit Reauthorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Coverage Tax Credit Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the health coverage tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:25Z"
    }
  ]
}
```
