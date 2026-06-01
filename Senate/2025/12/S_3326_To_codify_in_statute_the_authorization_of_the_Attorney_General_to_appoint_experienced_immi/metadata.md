# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3326?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3326
- Title: Temporary Immigration Judge Integrity Act
- Congress: 119
- Bill type: S
- Bill number: 3326
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-01-12T21:40:41Z
- Update date including text: 2026-01-12T21:40:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3326",
    "number": "3326",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Temporary Immigration Judge Integrity Act",
    "type": "S",
    "updateDate": "2026-01-12T21:40:41Z",
    "updateDateIncludingText": "2026-01-12T21:40:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
            "date": "2025-12-03T19:56:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-03T19:56:58Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "HI"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-03",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3326is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3326\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Schiff (for himself, Mr. Durbin , Mr. Bennet , Mr. Booker , Ms. Duckworth , Ms. Hirono , Mr. Kelly , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Sanders , Mr. Van Hollen , Ms. Warren , Mr. Welch , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo codify in statute the authorization of the Attorney General to appoint experienced immigration law experts as temporary immigration judges to reduce the number of pending cases in immigration courts.\n#### 1. Short title\nThis Act may be cited as the Temporary Immigration Judge Integrity Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe purpose of temporary immigration judges is not to replace permanent immigration judges or to serve in lieu of appointing permanent immigration judges; and\n**(2)**\ndue to the complex nature and high-stakes consequences of the adjudication of immigration cases, immigration judges must have extensive knowledge and application of United States immigration laws.\n#### 3. Temporary immigration judges\nSection 240(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(1) ) is amended\u2014\n**(1)**\nby striking The immigration judge shall administer and inserting the following:\n(A) In general The immigration judge shall administer ; and\n**(2)**\nby inserting after subparagraph (A), as redesignated, the following:\n(B) Temporary immigration judges (i) Appointment The Attorney General is authorized to appoint, as temporary immigration judges for a renewable term not to exceed 6 months\u2014 (I) former members of the Board of Immigration Appeals or appellate immigration judges; (II) former immigration judges; (III) administrative law judges who are employed within, or have retired from, the Executive Office for Immigration Review; (IV) administrative law judges at another Federal agency who have at least ten years of experience, after being admitted to a State bar, in the field of immigration law, subject to the written consent of the head of such agency; and (V) attorneys at the Department of Justice who have at least 10 years of legal experience, after being admitted to a State bar, in the field of immigration law. (ii) Scope of authority Subject to clause (iii), each temporary immigration judge appointed pursuant to clause (i) shall have the same authority as an immigration judge to adjudicate assigned cases and administer immigration court matters, in accordance with the immigration laws. (iii) Oversight; training (I) In general The Attorney General, in collaboration with the Chief Immigration Judge and Regional Chief Immigration Judges, shall establish management and training procedures that\u2014 (aa) assign caseloads to, and oversee the performance of, temporary immigration judges; (bb) evaluate the work product produced by such judges; and (cc) except as provided in subclause (II), ensure that temporary immigration judges receive\u2014 (AA) a minimum of 8 weeks of initial training; and (BB) ongoing training for at least 1 day during every 2 weeks of their temporary service. (II) Exemption Individuals described in subclause (I) or (II) of clause (i) shall be exempted from the training described in subclause (I)(cc) if their service as a temporary immigration judge begins not later than 2 years after the last day of their service as an immigration judge, an immigration appellate judge, or a member of the Board of Immigration Appeals. (iv) Length of service (I) In general Temporary immigration judges may serve for up to 4 consecutive 6-month terms. (II) Additional service Temporary immigration judges who have reached the 2-year service limit described in subclause (I) shall not be reappointed to this temporary position until at least 3 years after the conclusion of their temporary service. .",
      "versionDate": "2025-12-03",
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
        "actionDate": "2025-12-05",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6497",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Temporary Immigration Judge Integrity Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-07T17:30:32Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3326is.xml"
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
      "title": "Temporary Immigration Judge Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to codify in statute the authorization of the Attorney General to appoint experienced immigration law experts as temporary immigration judges to reduce the number of pending cases in immigration courts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T11:56:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Temporary Immigration Judge Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    }
  ]
}
```
