# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4249
- Title: FARM Stability Act
- Congress: 119
- Bill type: S
- Bill number: 4249
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-17T14:18:23Z
- Update date including text: 2026-04-17T14:18:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4249",
    "number": "4249",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "FARM Stability Act",
    "type": "S",
    "updateDate": "2026-04-17T14:18:23Z",
    "updateDateIncludingText": "2026-04-17T14:18:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T20:16:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "SC"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MS"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AR"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "ID"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MS"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4249is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4249\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Budd (for himself, Mr. Scott of South Carolina , Mrs. Hyde-Smith , Mr. Boozman , Mr. Crapo , Mr. Ricketts , Mr. Tillis , Ms. Lummis , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize, if applicable, the Secretary of Labor to annually establish a 2-tiered wage rate for H\u20132A workers that distinguishes between entry-level and experience-level workers and to annually establish a compensation adjustment factor to account for the value of housing provided to H\u20132A workers.\n#### 1. Short titles\nThis Act may be cited as the Farmworker Access and Retention Modernization Stability Act or the FARM Stability Act .\n#### 2. Annual wage rates and adjustments for H\u20132A workers\nSection 218(a) of the Immigration and Nationality Act ( 8 U.S.C. 1188(a) ) is amended by adding at the end the following:\n(3) If the Secretary of Labor determines a minimum wage rate other than the Federal or State minimum wage rate applicable to agricultural employment is required to be paid to H\u20132A workers, the Secretary shall\u2014 (A) annually establish a 2-tiered wage rate based on the skill level required for H\u20132A occupations that\u2014 (i) classifies positions requiring entry-level workers as Skill Level I; (ii) classifies positions requiring experience-level workers with formal education, training certificates, or significant experience in agricultural operations as Skill Level II; and (iii) sets the wage rate for Skill Level II H\u20132 A workers higher than the wage rate for Skill Level I H\u20132A workers; and (B) account for the value of housing provided to H\u20132A workers by\u2014 (i) annually establishing a compensation adjustment factor to the wage rate established for each State pursuant to subparagraph (A); (ii) computing such compensation adjustment factor as an equivalent hourly rate based on the weighted statewide average of fair market rents for a 4-bedroom housing unit available from the Department of Housing and Urban Development; and (iii) keeping such compensation adjustment factor at or below 30 percent of the relevant wage rate established pursuant to subparagraph (A). .",
      "versionDate": "2026-03-26",
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
        "name": "Labor and Employment",
        "updateDate": "2026-04-14T15:24:42Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4249is.xml"
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
      "title": "FARM Stability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:18:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FARM Stability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farmworker Access and Retention Modernization Stability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize, if applicable, the Secretary of Labor to annually establish a 2-tiered wage rate for H-2A workers that distinguishes between entry-level and experience-level workers and to annually establish a compensation adjustment factor to account for the value of housing provided to H-2A workers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:18:24Z"
    }
  ]
}
```
