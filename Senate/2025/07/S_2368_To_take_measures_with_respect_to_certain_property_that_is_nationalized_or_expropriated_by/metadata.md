# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2368?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2368
- Title: Defending American Property Abroad Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2368
- Origin chamber: Senate
- Introduced date: 2025-07-21
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in Senate
- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-21: Introduced in Senate

## Actions

- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2368",
    "number": "2368",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Defending American Property Abroad Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-21",
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
            "date": "2025-07-21T22:43:43Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-21T22:43:43Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "VA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "AL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "AL"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "TN"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MD"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "WY"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "OK"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NC"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2368is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2368\nIN THE SENATE OF THE UNITED STATES\nJuly 21, 2025 Mr. Hagerty (for himself, Mr. Kaine , Mrs. Britt , Mr. Tuberville , Mr. Wicker , Mrs. Blackburn , Ms. Alsobrooks , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo take measures with respect to certain property that is nationalized or expropriated by foreign governments, to amend section 301 of the Trade Act of 1974 to include expropriation of the assets of United States persons in acts, policies, and practices of foreign countries that are unreasonable or discriminatory, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defending American Property Abroad Act of 2025 .\n#### 2. Identification and prohibitions with respect to property nationalized or expropriated by foreign governments\n##### (a) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs, the Committee on Foreign Relations, the Committee on Finance, and the Select Committee on Intelligence of the Senate; and\n**(B)**\nthe Committee on Homeland Security, the Committee on Foreign Affairs, the Committee on Ways and Means, and the Permanent Select Committee on Intelligence of the House of Representatives.\n**(2) Covered foreign trade partner**\nThe term covered foreign trade partner means a country in the Western Hemisphere that has in effect a free trade agreement with the United States.\n**(3) Passenger vessel**\nThe term passenger vessel means a vessel that\u2014\n**(A)**\nis authorized to carry 149 or more passengers;\n**(B)**\nhas onboard sleeping facilities for each passenger;\n**(C)**\nis on a voyage that embarks or disembarks passengers; and\n**(D)**\nis not engaged in a coastwise voyage subject to chapter 105 of title 46, United States Code.\n**(4) Prohibited property**\nThe term prohibited property means any port, harbor, or marine terminal, including any relevant port infrastructure\u2014\n**(A)**\nthat is located within the territory of a covered foreign trade partner;\n**(B)**\nthat is accessible only through land that is owned, held, or controlled, directly or indirectly, by a United States person; and\n**(C)**\nif an agency or official of the government of the covered foreign trade partner has, on or after January 1, 2024\u2014\n**(i)**\nnationalized, forcibly limited, or expropriated the land described in subparagraph (B);\n**(ii)**\nrepudiated or nullified any contract, permit, concession, easement, or similar authorization with a United States person related to that land; or\n**(iii)**\ntaken any other action that has the effect of seizing ownership or control of that land.\n**(5) Relevant port infrastructure**\nThe term relevant port infrastructure means the following infrastructure at a port or harbor:\n**(A)**\nConveyors and other equipment used to load or unload freight or passenger vessels.\n**(B)**\nRoads and pathways used to load or unload freight or passenger vessels.\n**(C)**\nDocks and piers used to load or unload freight or passenger vessels.\n**(D)**\nMoorings, dolphins, or other structures used for anchoring freight or passenger vessels.\n**(E)**\nSilos, domes, or other structures used for the storage of any good, ware, article, merchandise, or other freight.\n**(F)**\nOffices, facilities, and other buildings used for the administration and security of the port or harbor.\n**(6) United States**\nThe term United States includes the 50 States, the District of Columbia, and any territory or possession of the United States.\n**(7) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity not less than 50 percent of the ownership interest in which is owned by United States citizens.\n##### (b) Designation of prohibited property\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Homeland Security, in consultation with and with the concurrence of the Secretary of the Treasury and the Secretary of State, shall\u2014\n**(1)**\nidentify and designate all prohibited property;\n**(2)**\nprovide a list of all prohibited property designated under paragraph (1) to\u2014\n**(A)**\nthe agencies and officials within the Department of Homeland Security, the Department of the Treasury, and the Department of State responsible for the implementation of subsection (c); and\n**(B)**\nthe appropriate congressional committees; and\n**(3)**\npublish the list required under paragraph (2) in the Federal Register.\n##### (c) Prohibitions on use of prohibited property\nThe President shall prohibit any vessel loaded or previously held at a port, harbor, or marine terminal that is designated as prohibited property under subsection (b)(1) from\u2014\n**(1)**\nimporting into the United States any good;\n**(2)**\nreleasing into the United States any good;\n**(3)**\ndocking any passenger vessel in the United States;\n**(4)**\nreleasing into the United States any passenger from a passenger vessel; or\n**(5)**\ndry docking, completing repair work, refurbishing, victualing, refueling, or conducting any other servicing or maintenance-related activities.\n#### 3. Expansion of acts, policies, and practices that are unreasonable or discriminatory under title III of the Trade Act of 1974\nSection 301(d)(3)(B) of the Trade Act of 1974 ( 19 U.S.C. 2411(d)(3)(B) ) is amended\u2014\n**(1)**\nin clause (iii)(V), by striking , or and inserting a comma;\n**(2)**\nby moving clause (iv) 2 ems to the left;\n**(3)**\nin clause (iv), by striking the period at the end and inserting , or ; and\n**(4)**\nby adding at the end the following:\n(v) constitutes, with respect to the assets of a United States person\u2014 (I) direct or indirect expropriation or nationalization, (II) arbitrary or capricious treatment, (III) denial of due process, or (IV) discrimination on the basis of nationality. .",
      "versionDate": "2025-07-21",
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
        "actionDate": "2025-07-21",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4577",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Defending American Property Abroad Act of 2025",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T16:42:33Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2368is.xml"
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
      "title": "Defending American Property Abroad Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defending American Property Abroad Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to take measures with respect to certain property that is nationalized or expropriated by foreign governments, to amend section 301 of the Trade Act of 1974 to include expropriation of the assets of United States Persons in acts, policies, and practices of foreign countries that are unreasonable or discriminatory, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:53Z"
    }
  ]
}
```
