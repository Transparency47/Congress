# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2977?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2977
- Title: FAST Justice Act
- Congress: 119
- Bill type: S
- Bill number: 2977
- Origin chamber: Senate
- Introduced date: 2025-10-07
- Update date: 2025-12-08T21:49:56Z
- Update date including text: 2025-12-08T21:49:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-07: Introduced in Senate
- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-10-07: Introduced in Senate

## Actions

- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-07",
    "latestAction": {
      "actionDate": "2025-10-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2977",
    "number": "2977",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "FAST Justice Act",
    "type": "S",
    "updateDate": "2025-12-08T21:49:56Z",
    "updateDateIncludingText": "2025-12-08T21:49:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-07",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-07",
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
          "date": "2025-10-07T16:02:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "MD"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
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
      "sponsorshipDate": "2025-10-07",
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
      "sponsorshipDate": "2025-10-07",
      "state": "VA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "MI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "IL"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2977is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2977\nIN THE SENATE OF THE UNITED STATES\nOctober 7, 2025 Mr. Blumenthal (for himself, Ms. Alsobrooks , Mr. Van Hollen , Mr. Kaine , Mr. Warner , Mr. Peters , Mr. Kim , Ms. Duckworth , Mr. Reed , Mr. Schatz , Mr. Padilla , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend chapter 77 of title 5, United States Code, to ensure timely rulings by the Merit Systems Protection Board on appeals by Federal employees and applicants for employment.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Swift and Timely Justice Act or the FAST Justice Act .\n#### 2. Timeliness of MSPB appeals\n##### (a) In general\nSection 7701 of title 5, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (k) as subsection (l); and\n**(2)**\nby inserting after subsection (j) the following:\n(k) Untimely action by MSPB (1) In general On and after the date that is 120 days after the date on which an employee or applicant for employment files an appeal under this section, other than an appeal of a case that is subject to section 7702, if the Merit Systems Protection Board has not taken an action with respect to the appeal that is subject to judicial review, the employee or applicant shall be entitled to file a civil action with respect to the personnel action that is the subject of the appeal. (2) Filing (A) In general An employee or applicant may bring a civil action under paragraph (1) in a district court of the United States for\u2014 (i) any judicial district in which a personnel action that is a subject of the civil action is alleged to have occurred; or (ii) the judicial district in which the employee or applicant would have been employed, but for a personnel action that is a subject of the civil action. (B) Where principal office is located If the respondent for a civil action under paragraph (1) is not subject to personal jurisdiction in any judicial district described in subparagraph (A), the civil action may be brought in a district court of the United States for the judicial district in which the principal office of the respondent is located. (3) Standards for judicial review In a civil action under paragraph (1), the court\u2014 (A) shall apply the standard of review under section 7703(c) only with respect to an order or decision of the Merit Systems Protection Board; and (B) in making any other determination, shall apply the same standard of review that would have applied to the review of the personnel action at issue by the Merit Systems Protection Board. (4) Appeal of district court determination An appeal from an order or decision of the district court in a civil action under paragraph (1) shall, in accordance with section 1291 of title 28, be filed with the court of appeals of the United States for the judicial district in which the district court is located. (5) Stay If an employee or applicant for employment brings a civil action in accordance with paragraph (1) with respect to a personnel action, the Merit Systems Protection Board\u2014 (A) shall stay the appeal relating to the personnel action upon the filing of the civil action; and (B) if the civil action is dismissed for lack of jurisdiction, shall resume processing the appeal. .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to limit the ability of an employee or applicant for employment to obtain judicial review of an order or decision of the Merit Systems Protection Board in accordance with section 7703 of title 5, United States Code.",
      "versionDate": "2025-10-07",
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
        "actionDate": "2025-10-08",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5724",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAST Justice Act",
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
        "updateDate": "2025-12-08T21:26:11Z"
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
      "date": "2025-10-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2977is.xml"
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
      "title": "FAST Justice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAST Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Access to Swift and Timely Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 77 of title 5, United States Code, to ensure timely rulings by the Merit Systems Protection Board on appeals by Federal employees and applicants for employment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:03:17Z"
    }
  ]
}
```
