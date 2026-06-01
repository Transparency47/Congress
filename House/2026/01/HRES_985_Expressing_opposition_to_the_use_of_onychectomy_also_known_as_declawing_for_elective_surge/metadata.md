# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/985
- Title: Expressing opposition to the use of onychectomy, also known as declawing, for elective surgery in cats.
- Congress: 119
- Bill type: HRES
- Bill number: 985
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-05-16T08:07:14Z
- Update date including text: 2026-05-16T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-09 - IntroReferral: Submitted in House
- 2026-01-09 - IntroReferral: Submitted in House
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2026-01-09: Submitted in House

## Actions

- 2026-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-09 - IntroReferral: Submitted in House
- 2026-01-09 - IntroReferral: Submitted in House
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/985",
    "number": "985",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "N000002",
        "district": "12",
        "firstName": "Jerrold",
        "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
        "lastName": "Nadler",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Expressing opposition to the use of onychectomy, also known as declawing, for elective surgery in cats.",
    "type": "HRES",
    "updateDate": "2026-05-16T08:07:14Z",
    "updateDateIncludingText": "2026-05-16T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-01-09T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:49:39Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "IN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "MO"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "OR"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NV"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres985ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 985\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mr. Nadler (for himself, Mr. Carson , Mr. Cleaver , Ms. Dean of Pennsylvania , Ms. Dexter , Ms. Jayapal , Mr. Johnson of Georgia , Mr. Krishnamoorthi , Mr. Lieu , Ms. Lofgren , Ms. Norton , Mr. Quigley , Ms. Rivas , Ms. Simon , Mr. Soto , Ms. Titus , Ms. Tlaib , and Mr. Vindman ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nExpressing opposition to the use of onychectomy, also known as declawing, for elective surgery in cats.\nThat the House of Representatives\u2014\n**(1)**\nopposes declawing, as defined in this resolution, when performed for cosmetic or aesthetic purposes, or for reasons of convenience in keeping or handling a cat, and encourages veterinary professionals to discourage the practice with vigor;\n**(2)**\nrecognizes that these practices should only be performed when medically necessary for a therapeutic purpose for the physical health of the cat, meaning a medically necessary procedure to address an existing or recurring anatomical pathology issue such as infection, disease, injury, or abnormal condition in the claws, nail bed, or toe bone that jeopardizes the cat\u2019s health, and not for the purpose of convenience, property protection, or behavioral modification;\n**(3)**\nurges State legislatures that have not yet banned onychectomy (declawing) and tendonectomy for elective reasons to consider this on the grounds of animal welfare and public health; and\n**(4)**\naffirms the commitment of the United States to advancing the cause of animal protection and animal welfare.",
      "versionDate": "2026-01-09",
      "versionType": "IH"
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
        "name": "Animals",
        "updateDate": "2026-01-13T13:21:39Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres985ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing opposition to the use of onychectomy, also known as declawing, for elective surgery in cats.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:18:25Z"
    },
    {
      "title": "Expressing opposition to the use of onychectomy, also known as declawing, for elective surgery in cats.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-10T09:06:24Z"
    }
  ]
}
```
