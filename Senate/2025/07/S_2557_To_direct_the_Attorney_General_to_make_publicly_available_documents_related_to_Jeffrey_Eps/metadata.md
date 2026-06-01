# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2557?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2557
- Title: Epstein Files Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 2557
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-03-23T16:50:03Z
- Update date including text: 2026-03-23T16:50:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2557",
    "number": "2557",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Epstein Files Transparency Act",
    "type": "S",
    "updateDate": "2026-03-23T16:50:03Z",
    "updateDateIncludingText": "2026-03-23T16:50:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
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
      "actionDate": "2025-07-30",
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
          "date": "2025-07-31T00:05:35Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NM"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "IL"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MD"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NJ"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
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
      "sponsorshipDate": "2025-07-30",
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
      "sponsorshipDate": "2025-07-30",
      "state": "RI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "DE"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "OR"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "HI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-30",
      "state": "VT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CO"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "WI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NV"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "AK"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2557is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2557\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Merkley (for himself, Mr. Luj\u00e1n , Mr. Durbin , Mr. Schumer , Mr. Booker , Mr. Schiff , Mr. Heinrich , Mr. Hickenlooper , Mr. Blumenthal , Mr. Van Hollen , Mr. Gallego , Mr. Kim , Mr. Kelly , Ms. Alsobrooks , Mr. Welch , Mr. Warner , Mr. Reed , Mrs. Shaheen , Mr. Coons , Mr. Wyden , Ms. Hirono , Mr. Sanders , Ms. Duckworth , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to make publicly available documents related to Jeffrey Epstein, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Epstein Files Transparency Act .\n#### 2. Release of documents relating to Jeffrey Epstein\n##### (a) In general\nSubject to subsection (c), not later than 30 days after the date of enactment of this Act, the Attorney General shall make publicly available in a searchable and downloadable format all unclassified records, documents, communications, and investigative materials in the possession of the Department of Justice, including the Federal Bureau of Investigation and each United States Attorney's Office, that relate to\u2014\n**(1)**\nJeffrey Epstein, including all investigations, prosecutions, or custodial matters;\n**(2)**\nGhislaine Maxwell;\n**(3)**\nany flight logs or travel records, including manifests, itineraries, pilot records, and customs or immigration documentation, for any aircraft, vessel, or vehicle owned, operated, or used by Jeffrey Epstein or any related entity;\n**(4)**\nany individuals, including government officials, named or referenced in connection with the criminal activities, civil settlements, immunity or plea agreements, or investigatory proceedings of Jeffrey Epstein;\n**(5)**\nany corporate, nonprofit, academic, or governmental entities with known or alleged ties to the trafficking or financial networks of Jeffrey Epstein;\n**(6)**\nany immunity deals, non-prosecution agreements, plea bargains, or sealed settlements involving Jeffrey Epstein or his associates;\n**(7)**\nany internal Department of Justice communications, including emails, memoranda, and meeting notes, concerning decisions to charge, not charge, investigate, or decline to investigate Jeffrey Epstein or his associates;\n**(8)**\nany communications, memoranda, directives, logs, or metadata concerning the destruction, deletion, alteration, misplacement, or concealment of documents, recordings, or electronic data related to Jeffrey Epstein, his associates, his detention and death, or any investigative files; or\n**(9)**\nany documentation of the detention or death of Jeffrey Epstein, including incident reports, witness interviews, medical examiner files, autopsy reports, and written records detailing the circumstances and cause of death.\n##### (b) Prohibited grounds for withholding\nIn carrying out subsection (a), the Attorney General may not withhold from publication, delay the publication of, or redact any record, document, communication, or investigative material on the basis of embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary.\n##### (c) Permitted withholdings\n**(1) In general**\nIn carrying out subsection (a), the Attorney General may withhold from publication any record, document, communication, or investigative material, or redact any segregable portion of any record, document, communication, or investigative material, that\u2014\n**(A)**\ncontains personally identifiable information from the personal or medical file of a victim or child witness, including information the publication of which would constitute a clearly unwarranted invasion of personal privacy;\n**(B)**\ndepicts or contains child pornography, as defined in section 2256 of title 18, United States Code;\n**(C)**\nwould jeopardize an active Federal investigation or ongoing Federal prosecution, if the withholding or redaction is narrowly tailored and temporary;\n**(D)**\ndepicts or contains any image of the death, physical abuse, or injury of any person; or\n**(E)**\ncontains information that is specifically authorized under criteria established by an Executive order to be kept secret in the interest of national defense or foreign policy and is properly classified pursuant to that Executive order.\n**(2) Redactions**\nThe Attorney General shall publish in the Federal Register and submit to Congress a written justification for each redaction under paragraph (1).\n**(3) Declassification to the maximum extent possible**\n**(A) In general**\nThe Attorney General shall declassify, to the maximum extent possible, any information that the Attorney General would otherwise withhold or redact as classified information under this section.\n**(B) Unclassified summary**\nIf the Attorney General determines that information described in subparagraph (A) may not be declassified and made available in a manner that protects the national security of the United States, including methods or sources related to national security, the Attorney General shall make publicly available an unclassified summary of the information.\n**(4) Classification of covered information**\nThe Attorney General shall publish in the Federal Register and submit to Congress each decision made after July 1, 2025, to classify any information that would otherwise be required to be made publicly available under subsection (a), including the date of classification, the identity of the classifying authority, and an unclassified summary of the justification for classification.\n#### 3. Report to Congress\nNot later than 15 days after making publicly available all records, documents, communications, and investigative materials under section 2(a), the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report containing\u2014\n**(1)**\na list of each category of records, documents, communications, and investigative materials made publicly available or withheld;\n**(2)**\na summary of the redactions made, including the legal basis upon which the redactions were made; and\n**(3)**\na list of each government official, public figure, or foreign dignitary named or referenced in the records, documents, communications, and investigative materials made publicly available, without redaction in accordance with section 2(b).",
      "versionDate": "2025-07-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-18T18:16:17Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2557is.xml"
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
      "title": "Epstein Files Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Epstein Files Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Attorney General to make publicly available documents related to Jeffrey Epstein, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:51Z"
    }
  ]
}
```
