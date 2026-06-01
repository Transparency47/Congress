# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1594
- Title: Captive Primate Safety Act
- Congress: 119
- Bill type: S
- Bill number: 1594
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2026-02-24T12:03:19Z
- Update date including text: 2026-02-24T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1594",
    "number": "1594",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
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
    "title": "Captive Primate Safety Act",
    "type": "S",
    "updateDate": "2026-02-24T12:03:19Z",
    "updateDateIncludingText": "2026-02-24T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-05",
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
            "date": "2025-05-05T22:31:18Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-05T22:31:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MD"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1594is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1594\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Blumenthal (for himself, Mr. Booker , Mrs. Gillibrand , Mr. Schiff , Ms. Smith , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Lacey Act Amendments of 1981 to prohibit certain activities involving prohibited primate species, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Captive Primate Safety Act .\n#### 2. Prohibition of certain activities involving prohibited primate species\n##### (a) Definition of prohibited primate species\nSection 2 of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3371 ) is amended\u2014\n**(1)**\nby redesignating subsections (h) through (l) as subsections (i) through (m), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Prohibited primate species The term prohibited primate species means any live species of nonhuman primate, including species of chimpanzee, galago, gibbon, gorilla, lemur, loris, monkey, orangutan, tarsier, or any hybrid of such species. .\n##### (b) Prohibited acts\nSection 3(e) of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3372(e) ) is amended\u2014\n**(1)**\nby striking paragraph (1) and all that follows through the period at the end of the undesignated matter following subparagraph (B) and inserting the following:\n(1) In general Except as provided in paragraph (2), it is unlawful for any person\u2014 (A) to import, export, transport, sell, receive, acquire, or purchase in interstate or foreign commerce, or in a manner substantially affecting interstate or foreign commerce, any prohibited wildlife species or prohibited primate species; or (B) to breed or possess any prohibited wildlife species or prohibited primate species. ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (C), by inserting or prohibited primate species after prohibited wildlife species each place it appears; and\n**(B)**\nby striking subparagraphs (D) and (E) and inserting the following:\n(D) an entity or individual that has custody of any prohibited wildlife species or prohibited primate species for the purpose of expeditiously transporting the prohibited wildlife species or prohibited primate species, as applicable, to an entity or individual described in this paragraph with respect to the species; (E) an entity or individual that is in possession of any prohibited wildlife species or prohibited primate species that was born before the date of the enactment of the Big Cat Public Safety Act, with respect to a prohibited wildlife species, or the Captive Primate Safety Act , with respect to a prohibited primate species, if the entity or individual\u2014 (i) not later than 180 days after the date of enactment of the applicable Act, registers each individual animal of each prohibited wildlife species or prohibited primate species, as applicable, possessed by the entity or individual with the United States Fish and Wildlife Service; (ii) does not breed, acquire, or sell any prohibited wildlife species or prohibited primate species, as applicable, after the date of enactment of the applicable Act; and (iii) does not allow direct contact between the public and any prohibited wildlife species or prohibited primate species, as applicable; or (F) a research facility that conducts research that involves a prohibited primate species that is registered with the Department of Agriculture, if the research facility holds the registration in good standing. .\n##### (c) Regulations\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary of the Interior shall promulgate regulations implementing the amendments made by subsections (a) and (b).\n**(2) Enforceability**\nThe enforceability of the amendments made by subsections (a) and (b) shall not be affected by a failure of the Secretary of the Interior to timely promulgate regulations under paragraph (1).\n##### (d) Technical amendments\n**(1)**\nSection 4 of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3373 ) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin the second sentence, by striking subpenas and inserting subpoenas ; and\n**(ii)**\nin the fourth sentence, by striking subpena issued pursuant to this paragraph and inserting subpoena issued pursuant to this subsection ; and\n**(B)**\nin subsection (e), in the first sentence, by striking Fishery Conservation and Management Act of 1976 and inserting Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ) .\n**(2)**\nSection 6(b) of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3375(b) ) is amended\u2014\n**(A)**\nin the matter preceding the proviso, by striking Attorney General; and inserting Attorney General: ; and\n**(B)**\nin the first sentence of the proviso, by striking subpena and inserting subpoena .\n**(3)**\nSection 8(a) of the Lacey Act Amendments of 1981 ( 16 U.S.C. 3377(a) ) is amended by striking Fishery Conservation and Management Act of 1976 and inserting Magnuson-Stevens Fishery Conservation and Management Act .",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-05-05",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "3199",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Captive Primate Safety Act of 2025",
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
        "name": "Animals",
        "updateDate": "2025-05-22T17:46:48Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1594is.xml"
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
      "title": "Captive Primate Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Captive Primate Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Lacey Act Amendments of 1981 to prohibit certain activities involving prohibited primate species, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:19Z"
    }
  ]
}
```
