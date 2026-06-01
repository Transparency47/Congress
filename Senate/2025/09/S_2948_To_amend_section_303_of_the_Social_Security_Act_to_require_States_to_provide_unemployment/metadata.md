# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2948
- Title: Help FEDS Act
- Congress: 119
- Bill type: S
- Bill number: 2948
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-03-30T18:47:25Z
- Update date including text: 2026-03-30T18:47:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2948",
    "number": "2948",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Help FEDS Act",
    "type": "S",
    "updateDate": "2026-03-30T18:47:25Z",
    "updateDateIncludingText": "2026-03-30T18:47:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T18:59:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IL"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2948is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2948\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Alsobrooks (for herself, Mr. Van Hollen , Mr. Kaine , Mr. Warner , Ms. Duckworth , Mr. Schatz , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend section 303 of the Social Security Act to require States to provide unemployment compensation benefits to Federal employees during a government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Help Federal Employees During Shutdowns Act or the Help FEDS Act .\n#### 2. Regular compensation required for Federal employees during a shutdown\nSection 303 of the Social Security Act ( 42 U.S.C. 503 ) is amended by adding at the end the following:\n(n) (1) For purposes of subsection (a), the unemployment compensation law of a State must\u2014 (A) allow for excepted Federal employees to apply for and receive unemployment compensation for any week in which such employee is performing emergency work (as such term is defined by the Office of Personnel Management) during a lapse in appropriations during fiscal year 2026 or 2027; (B) in the case that an excepted Federal employee receives pay under section 1341(c)(2) of title 31, United States Code, for any period in which such employee received compensation pursuant to subparagraph (A), require such an excepted Federal employee to repay such compensation to the State; (C) treat as an overpayment any such compensation not repaid to the State and allow for the recovery of such compensation in the same manner the State recovers any overpayment paid pursuant to the unemployment compensation law of the State; and (D) deposit all money repaid or recovered pursuant to subparagraphs (B) and (C) in the unemployment fund of such State. (2) (A) The Secretary of Treasury shall pay to each State, for the purpose of providing unemployment compensation to excepted Federal employees pursuant to paragraph (1)(A), the amount described in subparagraph (B). The Secretary of Labor shall, from time to time, certify to the Secretary of the Treasury the amount to be paid under this paragraph. (B) There shall be paid to each State an amount equal to 100 percent of\u2014 (i) the total amount of unemployment compensation provided to excepted Federal employees by the State pursuant to paragraph (1)(A); and (ii) any additional administrative expenses incurred by the State in relation to such compensation. (C) Funds in the Unemployment Trust Fund (as established by section 904(a)) shall be used to make payments to States pursuant to subparagraph (A). (3) In this section, the term excepted Federal employee means, with respect to a lapse in appropriations, a Federal employee who\u2014 (A) is an excepted employee, as defined in section 1341(c)(1) of title 31, United States Code; and (B) is not being paid due to the lapse in appropriations. .",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-09-26",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5572",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Help FEDS Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-10-20T12:44:41Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2948is.xml"
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
      "title": "Help FEDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Help FEDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Help Federal Employees During Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 303 of the Social Security Act to require States to provide unemployment compensation benefits to Federal employees during a government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:21Z"
    }
  ]
}
```
