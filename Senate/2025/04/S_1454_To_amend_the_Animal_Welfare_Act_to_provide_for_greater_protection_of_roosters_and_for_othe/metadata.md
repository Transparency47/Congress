# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1454
- Title: FIGHT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1454
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-28T11:03:21Z
- Update date including text: 2026-04-28T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1454",
    "number": "1454",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "FIGHT Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T11:03:21Z",
    "updateDateIncludingText": "2026-04-28T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
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
            "date": "2025-04-10T18:39:32Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-10T18:39:32Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sponsorshipDate": "2025-04-10",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "VT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "TX"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "OR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "AL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "ME"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "DE"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "PA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "LA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
      "state": "PA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "MO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "IL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1454is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1454\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Kennedy (for himself and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Animal Welfare Act to provide for greater protection of roosters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Inhumane Gambling and High-risk Trafficking Act of 2025 or the FIGHT Act of 2025 .\n#### 2. Animal fighting\n##### (a) Definition of rooster\nSection 2 of the Animal Welfare Act ( 7 U.S.C. 2132 ) is amended by adding at the end the following:\n(p) The term rooster means any male member of Gallus Domesticus species that is older than 6 months. .\n##### (b) Gambling on animal fighting ventures prohibited\nSection 26 of the Animal Welfare Act ( 7 U.S.C. 2156 ) is amended\u2014\n**(1)**\nby striking the section designation and header and all that follows through It shall be unlawful in subsection (a)(2) and inserting the following:\n26. Sponsoring or exhibiting an animal in, attending, causing an individual who has not attained the age of 16 to attend, or gambling on, an animal fighting venture (a) Sponsoring or exhibiting (1) In general It shall be unlawful for any person to knowingly sponsor or exhibit an animal in an animal fighting venture. (2) Attending or causing an individual who has not attained the age of 16 to attend It shall be unlawful ; and\n**(2)**\nin subsection (a), by adding at the end the following:\n(3) Animal venture gambling It shall be unlawful for any person to gamble on an animal fighting venture, including an in-person or broadcast event. .\n##### (c) Use of Postal Service or other interstate instrumentality To transport roosters\nSection 26(c) of the Animal Welfare Act ( 7 U.S.C. 2156(c) ) is amended\u2014\n**(1)**\nin the subsection heading, by inserting or to transport roosters after venture ;\n**(2)**\nby striking speech for purposes of advertising and inserting the following:\nspeech\u2014 (1) for purposes of advertising ;\n**(3)**\nin paragraph (1) (as so designated), by striking the period at the end and inserting ; or ; and\n**(4)**\nby adding at the end the following:\n(2) to transport a rooster. .\n##### (d) Civil citizen suits; seizure\nSection 26(e) of the Animal Welfare Act ( 7 U.S.C. 2156(e) ) is amended\u2014\n**(1)**\nby striking the subsection designation and heading and all that follows through The Secretary or any other person authorized by him in the first sentence and inserting the following:\n(e) Investigations; civil citizen suits (1) Investigation of violations by Secretary; assistance by other federal agencies; issuance of search warrant; forfeiture; cost recoverable in forfeiture or civil action The Secretary, or any other person authorized by the Secretary, ; and\n**(2)**\nby adding at the end the following:\n(2) Civil citizen suits (A) In general Any person may commence a civil suit in a district court of the United States on their own behalf to enjoin any person who is alleged to be in violation of any provision of this section. (B) Amount of fine For any person found to have violated a provision of this section in any suit brought under subparagraph (A), the district court may issue a fine in an amount not greater than $5,000 for each violation. (C) Requirement A person seeking to commence a civil suit under subparagraph (A) shall, at least 60 days before commencing the suit, submit to the Secretary and local law enforcement notice of the alleged violation of a provision of this section. (D) Limitation No action may be commenced under subparagraph (A)\u2014 (i) if the Secretary has commenced an action against the same person to impose a penalty pursuant to paragraph (1) for the same alleged violation; or (ii) if the United States has commenced, and is diligently prosecuting, a criminal action against the same person in a State or Federal court to redress the same alleged violation. (E) Jurisdiction A suit under this paragraph may be brought in the judicial district in which the alleged violation occurred. (F) Intervention The Attorney General, at the request of the Secretary, may intervene on behalf of the United States as a matter of right in any civil suit brought under subparagraph (A). (G) Attorney\u2019s fees The court, in issuing any final order in any suit brought under subparagraph (A), may award costs of litigation (including reasonable attorney and expert witness fees) to any party, whenever the court determines such an award is appropriate. (3) Seizure Whoever is found, pursuant to an investigation under paragraph (1), to have violated subsection (a)(1) shall, in addition to the penalties applicable under paragraph (1), be subject to seizure of all real property, including any right, title, and interest (including any leasehold interest) in the whole of any lot or tract of land and any appurtenances or improvements, that is used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of, a violation of subsection (a)(1). .\n##### (e) Technical corrections\n**(1)**\nSection 26(h) of the Animal Welfare Act ( 7 U.S.C. 2156(h) ) is amended to read as follows:\n(h) Conflict with State law The provisions of this Act shall not supersede or otherwise invalidate any such State, local, or municipal legislation or ordinance relating to animal fighting ventures except in case of a direct and irreconcilable conflict between any requirements thereunder and this Act or any rule, regulation, or standard hereunder. .\n**(2)**\nSection 3001(a) of title 39, United States Code, is amended by inserting ( 7 U.S.C. 2156 ), before is nonmailable .",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-06-12",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3946",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FIGHT Act of 2025",
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
        "updateDate": "2025-05-20T12:14:53Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1454is.xml"
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
      "title": "FIGHT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FIGHT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fighting Inhumane Gambling and High-risk Trafficking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Animal Welfare Act to provide for greater protection of roosters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:24Z"
    }
  ]
}
```
