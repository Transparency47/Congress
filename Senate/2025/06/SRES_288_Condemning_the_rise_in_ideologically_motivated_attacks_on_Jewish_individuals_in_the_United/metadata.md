# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/288?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/288
- Title: A resolution condemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the commitment of the Senate to combating antisemitism and politically motivated violence.
- Congress: 119
- Bill type: SRES
- Bill number: 288
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-04-14T19:27:06Z
- Update date including text: 2026-04-14T19:27:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-07 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 6/18/2025 S3474)
- 2026-01-07 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-07 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-07 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 6/18/2025 S3474)
- 2026-01-07 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-07 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/288",
    "number": "288",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "A resolution condemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the commitment of the Senate to combating antisemitism and politically motivated violence.",
    "type": "SRES",
    "updateDate": "2026-04-14T19:27:06Z",
    "updateDateIncludingText": "2026-04-14T19:27:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 6/18/2025 S3474)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
            "date": "2026-01-07T22:36:36Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-18T18:14:57Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "PA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "IA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CO"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "UT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CO"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "OK"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NV"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "WV"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NY"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
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
      "sponsorshipDate": "2025-06-18",
      "state": "ME"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ID"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NH"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ND"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "TN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "OH"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "NC"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "MT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "MT"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "IN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "SC"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "IA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "WV"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ME"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "SC"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ND"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "LA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "LA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "AL"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "NE"
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "MO"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres288is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 288\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. McCormick (for himself, Mr. Fetterman , Mr. Grassley , Mr. Bennet , Mr. Lee , Mr. Hickenlooper , Mr. Lankford , Ms. Rosen , Mrs. Capito , Mrs. Gillibrand , Mr. Risch , Mr. King , Mr. Crapo , Ms. Hassan , Mr. Hoeven , Mr. Blumenthal , Mrs. Blackburn , Ms. Duckworth , Mr. Moreno , Mrs. Hyde-Smith , Mr. Budd , Mr. Tillis , Mr. Scott of Florida , Mr. Sheehy , Mr. Daines , Mr. Young , Mr. Graham , Ms. Ernst , Mr. Justice , Ms. Collins , Mr. Scott of South Carolina , Mr. Cramer , Mr. Kennedy , Mr. Cassidy , Mrs. Britt , and Mrs. Fischer ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the commitment of the Senate to combating antisemitism and politically motivated violence.\nThat the Senate\u2014\n**(1)**\ncondemns in the strongest possible terms the June 1, 2025, targeted act of terror in Boulder, Colorado, as a cowardly act of ideologically motivated violence;\n**(2)**\nrecognizes this attack as part of a disturbing pattern of targeted aggression against Jewish individuals in the United States;\n**(3)**\nreaffirms its commitment to protecting the rights of all individuals in the United States to assemble peacefully and practice their faith without fear of violence;\n**(4)**\ncalls on Federal, State, and local law enforcement agencies to ensure thorough investigation and prosecution of all such incidents; and\n**(5)**\nurges elected officials, community leaders, and civil society to speak out against antisemitism and politically motivated violence in all forms.",
      "versionDate": "2025-06-18",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres288ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 288\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. McCormick (for himself, Mr. Fetterman , Mr. Grassley , Mr. Bennet , Mr. Lee , Mr. Hickenlooper , Mr. Lankford , Ms. Rosen , Mrs. Capito , Mrs. Gillibrand , Mr. Risch , Mr. King , Mr. Crapo , Ms. Hassan , Mr. Hoeven , Mr. Blumenthal , Mrs. Blackburn , Ms. Duckworth , Mr. Moreno , Mrs. Hyde-Smith , Mr. Budd , Mr. Tillis , Mr. Scott of Florida , Mr. Sheehy , Mr. Daines , Mr. Young , Mr. Graham , Ms. Ernst , Mr. Justice , Ms. Collins , Mr. Scott of South Carolina , Mr. Cramer , Mr. Kennedy , Mr. Cassidy , Mrs. Britt , Mrs. Fischer , Mr. Gallego , Mr. Hawley , Mr. Schumer , Mr. Murphy , and Mr. Cruz ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJanuary 7, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nCondemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the commitment of the Senate to combating antisemitism and politically motivated violence.\nThat the Senate\u2014\n**(1)**\ncondemns in the strongest possible terms the June 1, 2025, targeted act of terror in Boulder, Colorado, as a cowardly act of ideologically motivated violence;\n**(2)**\nrecognizes this attack as part of a disturbing pattern of targeted aggression against Jewish individuals in the United States;\n**(3)**\nreaffirms its commitment to protecting the rights of all individuals in the United States to assemble peacefully and practice their faith without fear of violence;\n**(4)**\ncalls on Federal, State, and local law enforcement agencies to ensure thorough investigation and prosecution of all such incidents; and\n**(5)**\nurges elected officials, community leaders, and civil society to speak out against antisemitism and politically motivated violence in all forms.",
      "versionDate": "2026-01-07",
      "versionType": "ATS"
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
        "actionDate": "2025-06-09",
        "actionTime": "19:10:09",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "481",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Condemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the House of Representatives commitment to combating antisemitism and politically motivated violence.",
      "type": "HRES"
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
            "name": "Colorado",
            "updateDate": "2026-01-08T20:11:37Z"
          },
          {
            "name": "First Amendment rights",
            "updateDate": "2026-01-08T20:11:37Z"
          },
          {
            "name": "Religion",
            "updateDate": "2026-01-08T20:11:37Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-01-08T20:11:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-07-21T15:02:33Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres288is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres288ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution condemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the commitment of the Senate to combating antisemitism and politically motivated violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T04:18:19Z"
    },
    {
      "title": "A resolution condemning the rise in ideologically motivated attacks on Jewish individuals in the United States, including the recent violent assault in Boulder, Colorado, and reaffirming the commitment of the Senate to combating antisemitism and politically motivated violence.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T10:56:22Z"
    }
  ]
}
```
