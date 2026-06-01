# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3868?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3868
- Title: Count the Crimes to Cut Act
- Congress: 119
- Bill type: S
- Bill number: 3868
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3868",
    "number": "3868",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Count the Crimes to Cut Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T19:27:15Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "SC"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3868is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3868\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Lee (for himself, Mr. Coons , Mr. Cruz , Mr. Booker , Mr. Wicker , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to submit to the Congress a report on Federal criminal offenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Count the Crimes to Cut Act .\n#### 2. Report on Federal criminal offenses\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term criminal regulatory offense means a Federal regulation that is enforceable by a criminal penalty; and\n**(2)**\nthe term criminal statutory offense means a criminal offense under a Federal statute.\n##### (b) Report on criminal statutory offenses\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report, which shall include\u2014\n**(1)**\na list of all criminal statutory offenses, including a list of the elements for each criminal statutory offense; and\n**(2)**\nfor each criminal statutory offense listed under paragraph (1)\u2014\n**(A)**\nthe potential criminal penalty for the criminal statutory offense;\n**(B)**\nthe number of prosecutions for the criminal statutory offense brought by the Department of Justice each year for the 15-year period preceding the date of enactment of this Act; and\n**(C)**\nthe mens rea requirement for the criminal statutory offense.\n##### (c) Report on criminal regulatory offenses\n**(1) Reports**\nNot later than 1 year after the date of enactment of this Act, the head of each Federal agency described in paragraph (2) shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report, which shall include\u2014\n**(A)**\na list of all criminal regulatory offenses enforceable by the agency; and\n**(B)**\nfor each criminal regulatory offense listed under subparagraph (A)\u2014\n**(i)**\nthe potential criminal penalty for a violation of the criminal regulatory offense;\n**(ii)**\nthe number of violations of the criminal regulatory offense referred to the Department of Justice for prosecution in each of the years during the 15-year period preceding the date of enactment of this Act; and\n**(iii)**\nthe mens rea requirement for the criminal regulatory offense.\n**(2) Agencies described**\nThe Federal agencies described in this paragraph are the Department of Agriculture, the Department of Commerce, the Department of Education, the Department of Energy, the Department of Health and Human Services, the Department of Homeland Security, the Department of Housing and Urban Development, the Department of the Interior, the Department of Labor, the Department of Transportation, the Department of the Treasury, the Commodity Futures Trading Commission, the Consumer Product Safety Commission, the Equal Employment Opportunity Commission, the Export-Import Bank of the United States, the Farm Credit Administration, the Federal Communications Commission, the Federal Deposit Insurance Corporation, the Federal Election Commission, the Federal Labor Relations Authority, the Federal Maritime Commission, the Federal Mine Safety and Health Review Commission, the Federal Trade Commission, the National Labor Relations Board, the National Transportation Safety Board, the Nuclear Regulatory Commission, the Occupational Safety and Health Review Commission, the Office of Congressional Workplace Rights, the Postal Regulatory Commission, the Securities and Exchange Commission, the Securities Investor Protection Corporation, the Environmental Protection Agency, the Small Business Administration, the Federal Housing Finance Agency, and the Office of Government Ethics.\n##### (d) Index\nNot later than 2 years after the date of enactment of this Act\u2014\n**(1)**\nthe Attorney General shall establish a publically accessible index of each criminal statutory offense listed in the report required under subsection (b) and make the index available and freely accessible on the website of the Department of Justice; and\n**(2)**\nthe head of each agency described in subsection (c)(2) shall establish a publically accessible index of each criminal regulatory offense listed in the report required under subsection (c)(1) and make the index available and freely accessible on the website of the agency.\n##### (e) Rule of construction\nNothing in this section shall be construed to require or authorize appropriations.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-04-14",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 370."
      },
      "number": "2159",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Count the Crimes to Cut Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-02",
        "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S733-734)"
      },
      "number": "3959",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Smarter Sentencing Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-26T18:08:22Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3868is.xml"
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
      "title": "Count the Crimes to Cut Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Count the Crimes to Cut Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Attorney General to submit to the Congress a report on Federal criminal offenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:19Z"
    }
  ]
}
```
