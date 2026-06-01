# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1984
- Title: Striking and Locked Out Workers Healthcare Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1984
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2025-12-05T21:44:55Z
- Update date including text: 2025-12-05T21:44:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1984",
    "number": "1984",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Striking and Locked Out Workers Healthcare Protection Act",
    "type": "S",
    "updateDate": "2025-12-05T21:44:55Z",
    "updateDateIncludingText": "2025-12-05T21:44:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T18:50:26Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-05",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "RI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MD"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "AZ"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1984is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1984\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Ms. Baldwin (for herself, Mr. Blumenthal , Mr. Padilla , Mr. Fetterman , Mr. Durbin , Ms. Smith , Mr. Sanders , Ms. Warren , Mr. Whitehouse , Mr. Markey , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit an employer from terminating the coverage of an employee under a group health plan while the employer is engaged in a lock-out or while the employee is engaged in a lawful strike, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Striking and Locked Out Workers Healthcare Protection Act .\n#### 2. Continuation of coverage under a group health plan during a lock-out or a lawful strike\n##### (a) Lock-Out\nSection 8(a) of the National Labor Relations Act ( 29 U.S.C. 158(a) ) is amended\u2014\n**(1)**\nin paragraph (5), by striking the period and inserting a semicolon; and\n**(2)**\nby adding at the end the following:\n(6) to terminate or alter the coverage of an employee under a group health plan during the period that such employer is taking action to lock-out, suspend, or otherwise withhold employment from the employee in order to influence the position of such employee or the representative of such employee in collective bargaining prior to a strike; and .\n##### (b) Strike\nSection 8(a) of such Act ( 29 U.S.C. 158(a) ), as so amended, is further amended by adding at the end the following:\n(7) to terminate or alter the coverage of an employee under a group health plan during the period that such employee is engaged in a lawful strike. .\n##### (c) Definition of group health plan\nSection 2 of the National Labor Relations Act ( 29 U.S.C. 152 ) is amended by adding at the end the following:\n(15) The term group health plan has the meaning given the term under section 607(1) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1167(1) ). .\n#### 3. Penalties\nSection 12 of the National Labor Relations Act ( 29 U.S.C. 162 ) is amended\u2014\n**(1)**\nby striking Sec. 12. Any person and inserting the following:\n12. Penalties (a) Violations for interference with the board Any person ; and\n**(2)**\nby adding at the end the following:\n(b) Civil penalties for unfair labor practices related to coverage under a group health plan during a lock-Out Any employer who commits an unfair labor practice within the meaning of section 8(a)(6) shall be subject to a civil penalty in an amount not to exceed $75,000 for each violation, except that, with respect to such an unfair labor practice that coincides with the discharge of an employee or that results in other serious economic harm to an employee, the Board shall double the amount of such penalty, to an amount not to exceed $150,000, in any case where the employer has within the preceding 5 years committed another violation of section 8(a)(6). A civil penalty under this subsection shall be in addition to any other remedy ordered by the Board. (c) Civil penalties for unfair labor practices related to coverage under a group health plan during a lawful strike Any employer who commits an unfair labor practice within the meaning of section 8(a)(7) shall be subject to a civil penalty in an amount not to exceed $50,000 for each violation, except that, with respect to such an unfair labor practice that coincides with the discharge of an employee or that results in other serious economic harm to an employee, the Board shall double the amount of such penalty, to an amount not to exceed $100,000, in any case where the employer has within the preceding 5 years committed another violation of section 8(a)(7). A civil penalty under this subsection shall be in addition to any other remedy ordered by the Board. (d) Director and officer liability If the Board determines, based on the particular facts and circumstances presented, that a director or officer\u2019s personal liability is warranted, a civil penalty for a violation described in subsection (b) or (c) may also be assessed against any director or officer of the employer who directed or committed the violation, or had actual or constructive knowledge of and the authority to prevent the violation and failed to prevent the violation. (e) Considerations In determining the amount of any civil penalty under subsection (b), (c), or (d), the Board shall consider\u2014 (1) the gravity of the actions of the employer resulting in the penalty, including the impact of such actions on the charging party or on other persons seeking to exercise rights guaranteed by this Act; (2) the size of the employer; (3) the history of previous unfair labor practices or other actions by the employer resulting in a penalty; and (4) the public interest. .",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "3532",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Striking and Locked Out Workers Healthcare Protection Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-07-02T13:27:55Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1984is.xml"
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
      "title": "Striking and Locked Out Workers Healthcare Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Striking and Locked Out Workers Healthcare Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit an employer from terminating the coverage of an employee under a group health plan while the employer is engaged in a lock-out or while the employee is engaged in a lawful strike, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:18Z"
    }
  ]
}
```
