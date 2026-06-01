# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1467
- Title: Homebuyers Privacy Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1467
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-01T16:08:51Z
- Update date including text: 2026-04-01T16:08:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-06-12 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S3395-3396)
- 2025-06-12 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent. (text: CR S3395-3396)
- 2025-06-12 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2025-06-12 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent. (consideration: CR S3395-3396)
- 2025-06-17 11:02:14 - Floor: Received in the House.
- 2025-06-17 11:02:25 - Floor: Held at the desk.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-06-12 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S3395-3396)
- 2025-06-12 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent. (text: CR S3395-3396)
- 2025-06-12 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2025-06-12 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent. (consideration: CR S3395-3396)
- 2025-06-17 11:02:14 - Floor: Received in the House.
- 2025-06-17 11:02:25 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1467",
    "number": "1467",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Homebuyers Privacy Protection Act",
    "type": "S",
    "updateDate": "2026-04-01T16:08:51Z",
    "updateDateIncludingText": "2026-04-01T16:08:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-06-17",
      "actionTime": "11:02:25",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-06-17",
      "actionTime": "11:02:14",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (text: CR S3395-3396)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent. (text: CR S3395-3396)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent. (consideration: CR S3395-3396)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
        "item": [
          {
            "date": "2025-06-12T22:37:55Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-04-10T19:32:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MD"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ND"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MD"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "SD"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WV"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ID"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MS"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "RI"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ID"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-10",
      "state": "ME"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "WI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NM"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MS"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "OH"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "LA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "ME"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "ND"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "AK"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1467is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1467\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Reed (for himself, Mr. Hagerty , Mr. Van Hollen , Mr. Tillis , Ms. Cortez Masto , Mr. Cramer , Ms. Smith , Mrs. Britt , Mr. Gallego , Mr. Ricketts , Ms. Alsobrooks , Mr. Rounds , Mrs. Capito , Mr. Wyden , Mr. Crapo , Mrs. Hyde-Smith , Mr. Whitehouse , Mr. Risch , Mr. King , Mr. Tuberville , Mr. Fetterman , Ms. Klobuchar , Mr. Kaine , Ms. Rosen , Mrs. Shaheen , Mr. Blumenthal , Ms. Baldwin , Mr. Welch , Mr. Hickenlooper , Mr. Peters , Mr. Bennet , Mr. Markey , Mr. Schatz , Mr. Merkley , Mr. Kelly , and Mrs. Fischer ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Fair Credit Reporting Act to prevent consumer reporting agencies from furnishing consumer reports under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homebuyers Privacy Protection Act .\n#### 2. Treatment of prescreening report requests\nSection 604(c) of the Fair Credit Reporting Act ( 15 U.S.C. 1681b(c) ) is amended by adding at the end the following:\n(4) Treatment of prescreening report requests (A) Definitions In this paragraph: (i) Credit union The term credit union means a Federal credit union or a State credit union, as those terms are defined in section 101 of the Federal Credit Union Act (12 U.S.C 1752). (ii) Insured depository institution The term insured depository institution has the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813(c) ). (iii) Residential mortgage loan The term residential mortgage loan has the meaning given the term in section 1503 of the S.A.F.E. Mortgage Licensing Act of 2008 ( 12 U.S.C. 5102 ). (iv) Servicer The term servicer has the meaning given the term in section 6(i) of the Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2605(i) ). (B) Limitation If a person requests a consumer report from a consumer reporting agency in connection with a credit transaction involving a residential mortgage loan, that agency may not, based in whole or in part on that request, furnish a consumer report to another person under this subsection unless\u2014 (i) the transaction consists of a firm offer of credit or insurance; and (ii) that other person\u2014 (I) has submitted documentation to that agency certifying that such other person has, pursuant to paragraph (1)(A), the authorization of the consumer to whom the consumer report relates; or (II) (aa) has originated a current residential mortgage loan of the consumer to whom the consumer report relates; (bb) is the servicer of a current residential mortgage loan of the consumer to whom the consumer report relates; or (cc) (AA) is an insured depository institution or credit union; and (BB) holds a current account for the consumer to whom the consumer report relates. .\n#### 3. Effective date\nThis Act, and the amendments made by this Act, shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1467es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1467\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Fair Credit Reporting Act to prevent consumer reporting agencies from furnishing consumer reports under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homebuyers Privacy Protection Act .\n#### 2. Treatment of prescreening report requests\nSection 604(c) of the Fair Credit Reporting Act ( 15 U.S.C. 1681b(c) ) is amended by adding at the end the following:\n(4) Treatment of prescreening report requests (A) Definitions In this paragraph: (i) Credit union The term credit union means a Federal credit union or a State credit union, as those terms are defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ). (ii) Insured depository institution The term insured depository institution has the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813(c) ). (iii) Residential mortgage loan The term residential mortgage loan has the meaning given the term in section 1503 of the S.A.F.E. Mortgage Licensing Act of 2008 ( 12 U.S.C. 5102 ). (iv) Servicer The term servicer has the meaning given the term in section 6(i) of the Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2605(i) ). (B) Limitation If a person requests a consumer report from a consumer reporting agency in connection with a credit transaction involving a residential mortgage loan, that agency may not, based in whole or in part on that request, furnish a consumer report to another person under this subsection unless\u2014 (i) the transaction consists of a firm offer of credit or insurance; and (ii) that other person\u2014 (I) has submitted documentation to that agency certifying that such other person has, pursuant to paragraph (1)(A), the authorization of the consumer to whom the consumer report relates; or (II) (aa) has originated a current residential mortgage loan of the consumer to whom the consumer report relates; (bb) is the servicer of a current residential mortgage loan of the consumer to whom the consumer report relates; or (cc) (AA) is an insured depository institution or credit union; and (BB) holds a current account for the consumer to whom the consumer report relates. .\n#### 3. Effective date\nThis Act, and the amendments made by this Act, shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-09-05",
        "text": "Became Public Law No: 119-36."
      },
      "number": "2808",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Homebuyers Privacy Protection Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Consumer credit",
            "updateDate": "2025-06-16T17:11:50Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-06-16T17:11:50Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-06-16T17:11:50Z"
          },
          {
            "name": "Real estate business",
            "updateDate": "2025-06-16T17:11:50Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-06-16T17:11:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-20T13:19:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1467",
          "measure-number": "1467",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1467v55",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-06-12",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Homebuyers Privacy Protection Act</strong></p><p>This bill limits the circumstances in which credit reporting agencies may provide consumer credit reports to third parties in connection with residential mortgage transactions.\u00a0</p><p>Specifically, the bill prohibits a credit reporting agency from providing a consumer's credit report to a third party in connection with a residential mortgage transaction unless the transaction consists of a firm offer of credit or insurance and\u00a0(1) the third party provides documentation certifying that it has the consumer's consent; or (2) the third party has originated a mortgage on behalf of the consumer, is a current mortgage loan\u00a0servicer to the consumer, or has a current specified banking relationship with the consumer.</p><p>These provisions take effect 180 days after the bill's enactment.</p>"
        },
        "title": "Homebuyers Privacy Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1467.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Homebuyers Privacy Protection Act</strong></p><p>This bill limits the circumstances in which credit reporting agencies may provide consumer credit reports to third parties in connection with residential mortgage transactions.\u00a0</p><p>Specifically, the bill prohibits a credit reporting agency from providing a consumer's credit report to a third party in connection with a residential mortgage transaction unless the transaction consists of a firm offer of credit or insurance and\u00a0(1) the third party provides documentation certifying that it has the consumer's consent; or (2) the third party has originated a mortgage on behalf of the consumer, is a current mortgage loan\u00a0servicer to the consumer, or has a current specified banking relationship with the consumer.</p><p>These provisions take effect 180 days after the bill's enactment.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s1467"
    },
    "title": "Homebuyers Privacy Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Homebuyers Privacy Protection Act</strong></p><p>This bill limits the circumstances in which credit reporting agencies may provide consumer credit reports to third parties in connection with residential mortgage transactions.\u00a0</p><p>Specifically, the bill prohibits a credit reporting agency from providing a consumer's credit report to a third party in connection with a residential mortgage transaction unless the transaction consists of a firm offer of credit or insurance and\u00a0(1) the third party provides documentation certifying that it has the consumer's consent; or (2) the third party has originated a mortgage on behalf of the consumer, is a current mortgage loan\u00a0servicer to the consumer, or has a current specified banking relationship with the consumer.</p><p>These provisions take effect 180 days after the bill's enactment.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s1467"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1467is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1467es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Homebuyers Privacy Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T11:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Homebuyers Privacy Protection Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-06-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Homebuyers Privacy Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Credit Reporting Act to prevent consumer reporting agencies from furnishing consumer reports under certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:22Z"
    }
  ]
}
```
