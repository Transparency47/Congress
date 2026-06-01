# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/25?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/25
- Title: A concurrent resolution recognizing the 15th anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors and victims, including former Congresswoman Gabby Giffords, a gun violence survivor and one of the most influential voices of courage in the United States in the fight to end gun violence.
- Congress: 119
- Bill type: SCONRES
- Bill number: 25
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-02-14T09:06:07Z
- Update date including text: 2026-02-14T09:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-02-05 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-02-05 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S516; text: CR 1/8/2026 S118-119)
- 2026-02-05 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-02-05 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-02-12 - Floor: Message on Senate action sent to the House.
- 2026-02-13 10:02:45 - Floor: Received in the House.
- 2026-02-13 10:03:01 - Floor: Held at the desk.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-02-05 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-02-05 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S516; text: CR 1/8/2026 S118-119)
- 2026-02-05 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-02-05 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-02-12 - Floor: Message on Senate action sent to the House.
- 2026-02-13 10:02:45 - Floor: Received in the House.
- 2026-02-13 10:03:01 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/25",
    "number": "25",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "A concurrent resolution recognizing the 15th anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors and victims, including former Congresswoman Gabby Giffords, a gun violence survivor and one of the most influential voices of courage in the United States in the fight to end gun violence.",
    "type": "SCONRES",
    "updateDate": "2026-02-14T09:06:07Z",
    "updateDateIncludingText": "2026-02-14T09:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-02-13",
      "actionTime": "10:03:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-02-13",
      "actionTime": "10:02:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S516; text: CR 1/8/2026 S118-119)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
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
            "date": "2026-02-05T19:27:44Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-01-08T20:38:59Z",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MD"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "AZ"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MD"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "AZ"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NH"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NJ"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "RI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "VA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "RI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NM"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "DE"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "WA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NV"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NM"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "OR"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "WA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MN"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NH"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "HI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NV"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-01-08",
      "state": "VT"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "VA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CO"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "AR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres25is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. CON. RES. 25\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mrs. Gillibrand (for herself, Ms. Alsobrooks , Mr. Kelly , Mr. Murphy , Ms. Hirono , Mr. Blumenthal , Mr. Schumer , Mr. Van Hollen , Mr. Gallego , Mrs. Shaheen , Ms. Duckworth , Mr. Kim , Mr. Whitehouse , Mr. Kaine , Mr. Reed , Mr. Luj\u00e1n , Ms. Slotkin , Mr. Peters , Mr. Coons , Mr. Fetterman , Mrs. Murray , Mr. Merkley , Ms. Rosen , Mr. Heinrich , Mr. Wyden , Mr. Bennet , Mr. Booker , Ms. Cantwell , Ms. Klobuchar , Ms. Hassan , Mr. Schatz , Ms. Cortez Masto , Mr. Welch , Mr. Schiff , Mr. Sanders , Mr. Warner , and Mr. Markey ) submitted the following concurrent resolution; which was referred to the Committee on the Judiciary\nCONCURRENT RESOLUTION\nRecognizing the 15th anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors and victims, including former Congresswoman Gabby Giffords, a gun violence survivor and one of the most influential voices of courage in the United States in the fight to end gun violence.\nThat Congress\u2014\n**(1)**\nhonors the memory of the 6 individuals whose lives were lost on January 8, 2011, and expresses continued support for all survivors and families affected by the tragedy;\n**(2)**\nrecognizes the courage and leadership of former Congresswoman Gabby Giffords and her ongoing work to promote civility, bipartisanship, and solutions to prevent gun violence;\n**(3)**\ncommends the people of Tucson and first responders for their strength, compassion, and heroism in responding to the attack; and\n**(4)**\nreaffirms its dedication to promoting a respectful dialogue, condemning political violence and hate, and maintaining the core principles of peaceful self-governance.",
      "versionDate": "2026-01-08",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres25es.xml",
      "text": "119th CONGRESS\n2d Session\nS. CON. RES. 25\nIN THE SENATE OF THE UNITED STATES\nCONCURRENT RESOLUTION\nRecognizing the 15th anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors and victims, including former Congresswoman Gabby Giffords, a gun violence survivor and one of the most influential voices of courage in the United States in the fight to end gun violence.\nThat Congress\u2014\n**(1)**\nhonors the memory of the 6 individuals whose lives were lost on January 8, 2011, and expresses continued support for all survivors and families affected by the tragedy;\n**(2)**\nrecognizes the courage and leadership of former Congresswoman Gabby Giffords and her ongoing work to promote civility, bipartisanship, and solutions to prevent gun violence;\n**(3)**\ncommends the people of Tucson and first responders for their strength, compassion, and heroism in responding to the attack; and\n**(4)**\nreaffirms its dedication to promoting a respectful dialogue, condemning political violence and hate, and maintaining the core principles of peaceful self-governance.",
      "versionDate": "",
      "versionType": "ES"
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
        "actionDate": "2026-01-08",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "69",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the 15th Anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors, victims, and former Congresswoman Gabby Giffords, a gun violence survivor, and one of the Nation's most influential voices of courage in the fight to end gun violence.",
      "type": "HCONRES"
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
            "name": "Arizona",
            "updateDate": "2026-02-06T17:36:43Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-02-06T17:38:24Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2026-02-06T17:38:04Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-02-06T17:38:18Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-02-06T17:38:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-14T15:37:41Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres25is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sconres/BILLS-119sconres25es.xml"
        }
      ],
      "type": "ES"
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
      "title": "A concurrent resolution recognizing the 15th anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors and victims, including former Congresswoman Gabby Giffords, a gun violence survivor and one of the most influential voices of courage in the United States in the fight to end gun violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:18:17Z"
    },
    {
      "title": "A concurrent resolution recognizing the 15th anniversary of the January 8, 2011, Tucson, Arizona, shooting and honoring the survivors and victims, including former Congresswoman Gabby Giffords, a gun violence survivor and one of the most influential voices of courage in the United States in the fight to end gun violence.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T11:56:18Z"
    }
  ]
}
```
